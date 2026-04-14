using UnityEngine;
using UnityEngine.InputSystem;

public class CarController : MonoBehaviour
{
    public static CarController Instance { get; private set; }
    private Rigidbody rb;
    public LayerMask roadLayer;
    public float BaseSpeed { get; private set; } = 13f;
    // private float maxSpeed = 25f;
    // private float acceleration = 0.3f;
    public float CurrentSpeed { get; private set; } 
    private int currentRoadNumber = 0;
    public int CurrentRoadNumber => currentRoadNumber;
    public bool _boosting = false;
    public bool _Shield = false;
    public bool _isFrozen = false;
    public bool Shield => _Shield;
    public bool IsFrozen => _isFrozen;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        Debug.Log("Game start");
        CurrentSpeed = BaseSpeed;
    }

    void Awake()
    {
        Instance = this;
    }

    void Update()
    {

        if (Keyboard.current.escapeKey.isPressed)
        {
            Debug.Log("Pause");
            GameManager.Instance.TogglePause();
        }
        
    }
    void FixedUpdate()
    {
        if (GameManager.Instance.CurrentState != GameManager.GameState.Playing) { Debug.Log("Not Playing");return; }
        if (_isFrozen) { Debug.Log("Frozen") ; return; }
        float moveZ = 0;
        float moveX = 0;



        if (Keyboard.current.wKey.isPressed || Keyboard.current.zKey.isPressed ||Keyboard.current.upArrowKey.isPressed) {
            Debug.Log("up");
            moveX = 1;
        }
        if (Keyboard.current.sKey.isPressed ||Keyboard.current.downArrowKey.isPressed){
            Debug.Log("down");
            moveX = -1;
        }
        if (Keyboard.current.aKey.isPressed || Keyboard.current.qKey.isPressed ||Keyboard.current.leftArrowKey.isPressed){
            Debug.Log("left");
            moveZ = 1;
        }
        if (Keyboard.current.dKey.isPressed ||Keyboard.current.rightArrowKey.isPressed)
            moveZ = -1;


        bool isMoving = moveX != 0 || moveZ != 0;

        if (Keyboard.current.spaceKey.isPressed && isMoving)
        {
            if (!_boosting) {
                CurrentSpeed *= 1.3f;
                _boosting = true;
            }
        }
        else
        {
            if (_boosting)
            {
                CurrentSpeed /= 1.3f;
                _boosting = false;
            }
        }
        Vector3 movement = new Vector3(moveX, 0, moveZ) * CurrentSpeed ;
        rb.MovePosition(rb.position + movement * Time.deltaTime);
        DetectCurrentRoad();
    }

    void DetectCurrentRoad()
    {
        //Debug.Log($"[Raycast] Position voiture: {transform.position}");
        
        if (Physics.Raycast(transform.position + Vector3.up * 1f, Vector3.down, out RaycastHit hit, 5f, roadLayer))
        {
            //Debug.Log($"[Raycast] Touche: {hit.collider.gameObject.name}");
            RoadStraight road = hit.collider.GetComponent<RoadStraight>();
            if (road != null && road.RoadNumber != currentRoadNumber)
            {
                currentRoadNumber = road.RoadNumber;
                //Debug.Log($"[Raycast] Segment détecté: {currentRoadNumber}");
            }
        }
        else
        {
            //Debug.Log("[Raycast] Rien touché !");
        }
    }

    public void Respawn()
    {
        if (GameManager.Instance.CurrentState != GameManager.GameState.Playing) return;
    }
        

}
