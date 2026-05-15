using UnityEngine;
using UnityEngine.InputSystem;

public class CarController : MonoBehaviour
{
    public static CarController Instance { get; private set; }
    private Rigidbody rb;
    public LayerMask roadLayer;
    public float BaseSpeed { get; set; } = 520f;
    public float CurrentSpeed { get; private set; }
    private int currentRoadNumber = 0;
    private float _raycastTimer = 0f;
    public int CurrentRoadNumber => currentRoadNumber;
    public bool _boosting = false;
    private bool _isSliding = false;
    private float _slideTimer = 0f;
    private float _slideForce = 0f;
    private float _boostMultiplier = 1.1f;

    void Awake()
    {
        Instance = this;
    }

    void Start()
    {
        foreach (Transform child in transform)
        {
            if (child.gameObject.activeSelf)
            {
                rb = GetComponentInChildren<Rigidbody>();
                break;
            }
        }

        int carIndex = DataManager.Instance.SelectedCarIndex;
        CarData carData = CarSelector.Instance.cars[carIndex];

        // Vitesse
        UpgradeData speedData = UpgradeDatabase.Instance.Get(UpgradeType.Speed);
        int speedLevel = DataManager.Instance.GetUpgradeLevel(carIndex, UpgradeType.Speed);
        float speedBonus = speedData != null ? speedLevel * speedData.valuePerLevel : 0f;
        BaseSpeed = carData.baseSpeed + speedBonus;
        CurrentSpeed = BaseSpeed;

        // Vies
        UpgradeData healthData = UpgradeDatabase.Instance.Get(UpgradeType.Health);
        int healthLevel = DataManager.Instance.GetUpgradeLevel(carIndex, UpgradeType.Health);
        float healthBonus = healthData != null ? healthLevel * healthData.valuePerLevel : 0f;
        int totalLives = carData.baseHealth + Mathf.FloorToInt(healthBonus);
        GameManager.Instance.SetLives(totalLives);

        // Nitro  x1.1 + 0.05 par niveau
        UpgradeData nitroData = UpgradeDatabase.Instance.Get(UpgradeType.Nitro);
        int nitroLevel = DataManager.Instance.GetUpgradeLevel(carIndex, UpgradeType.Nitro);
        float nitroBonus = nitroData != null ? nitroLevel * nitroData.valuePerLevel : 0f;
        _boostMultiplier = 1.1f + nitroBonus;
    }

    void FixedUpdate()
    {
        if (GameManager.Instance.CurrentState != GameManager.GameState.Playing) return;
        if (_isSliding)
        {
            _slideTimer -= Time.fixedDeltaTime;
            rb.linearVelocity = new Vector3(_slideForce, rb.linearVelocity.y, -2 * BaseSpeed);
            if (_slideTimer <= 0f)
            {
                _isSliding = false;
                _slideForce = 0f;
            }
            return;
        }

        float moveZ = 0;
        float moveX = 0;
        float targetSpeed = BaseSpeed;

        if (Keyboard.current.wKey.isPressed || Keyboard.current.zKey.isPressed || Keyboard.current.upArrowKey.isPressed)
            moveX = 1;
        if (Keyboard.current.sKey.isPressed || Keyboard.current.downArrowKey.isPressed)
            moveX = -1;

        moveZ = -2;

        if (Keyboard.current.aKey.isPressed || Keyboard.current.qKey.isPressed || Keyboard.current.leftArrowKey.isPressed)
            targetSpeed = BaseSpeed * 0.7f;

        if (Keyboard.current.spaceKey.isPressed || Keyboard.current.dKey.isPressed || Keyboard.current.rightArrowKey.isPressed)
        {
            targetSpeed = BaseSpeed * _boostMultiplier;
            _boosting = true;
        }
        else
        {
            _boosting = false;
        }

        CurrentSpeed = targetSpeed;

        Vector3 movement = new Vector3(moveX, 0, moveZ) * CurrentSpeed;
        rb.linearVelocity = new Vector3(movement.x, rb.linearVelocity.y, movement.z);

        _raycastTimer += Time.fixedDeltaTime;
        if (_raycastTimer >= 0.1f)
        {
            DetectCurrentRoad();
            _raycastTimer = 0f;
        }
    }

    void DetectCurrentRoad()
    {
        if (Physics.Raycast(transform.position + Vector3.up * 1f, Vector3.down, out RaycastHit hit, 5f, roadLayer))
        {
            RoadStraight road = hit.collider.GetComponent<RoadStraight>();
            if (road != null && road.RoadNumber != currentRoadNumber)
                currentRoadNumber = road.RoadNumber;
        }
    }

    public void TriggerOilSlide(float duration = 2f, float forceMagnitude = 5f)
    {
        if (_isSliding) return; 
        _isSliding = true;
        _slideTimer = duration;
        float direction = Random.value > 0.5f ? 1f : -1f;
        _slideForce = direction * forceMagnitude;
    }

}