using UnityEngine;

public class MagnetAttractor : MonoBehaviour
{
    public float baseRadius = 1.74f;
    public float attractSpeed = 10f;

    [Header("Pickup Bonus")]
    public float pickupRadiusMultiplier = 2.5f;
    public float pickupDuration = 5f; 

    private float _baseComputedRadius;
    private float _radius;
    private Transform _carTransform;

    private bool _pickupActive = false;
    private float _pickupTimer = 0f;

    void Start()
    {
        foreach (Transform child in transform)
        {
            if (child.gameObject.activeSelf)
            {
                _carTransform = child;
                break;
            }
        }

        if (_carTransform == null) return;

        _baseComputedRadius = ComputeRadius();
        _radius = _baseComputedRadius;
    }

    float ComputeRadius()
    {
        int carIndex = DataManager.Instance.SelectedCarIndex;
        UpgradeData magnetData = UpgradeDatabase.Instance.Get(UpgradeType.Magnet);
        int level = DataManager.Instance.GetUpgradeLevel(carIndex, UpgradeType.Magnet);

        float levelBonus = magnetData != null ? level * magnetData.valuePerLevel : 0f;
        float maxBonus = (magnetData != null && level >= magnetData.maxLevel) ? 0.15f : 0f;

        float multiplier = 1f + levelBonus + maxBonus;
        return baseRadius * multiplier;
    }

    public void ActivatePickupBonus()
    {
        _pickupActive = true;
        _pickupTimer = pickupDuration;
        _radius = _baseComputedRadius * pickupRadiusMultiplier;
        Debug.Log($"[Magnet] Bonus activé ! Rayon : {_radius:F2} pendant {pickupDuration}s");
    }

    void Update()
    {
        if (!_pickupActive) return;

        _pickupTimer -= Time.deltaTime;
        if (_pickupTimer <= 0f)
        {
            _pickupActive = false;
            _radius = _baseComputedRadius;
        }
    }

    void FixedUpdate()
    {
        if (GameManager.Instance.CurrentState != GameManager.GameState.Playing) return;
        if (_carTransform == null) return;

        Collider[] hits = Physics.OverlapSphere(_carTransform.position, _radius);
        foreach (Collider hit in hits)
        {
            bool isMoney = hit.CompareTag("Money") ||
                           (hit.transform.parent != null && hit.transform.parent.CompareTag("Money"));

            if (isMoney)
            {
                Transform moneyRoot = hit.CompareTag("Money") ? hit.transform : hit.transform.parent;
                Vector3 dir = _carTransform.position - moneyRoot.position;
                moneyRoot.position += dir.normalized * attractSpeed * Time.fixedDeltaTime;
            }
        }
    }

    void OnDrawGizmos()
    {
        Transform target = _carTransform != null ? _carTransform : transform;

        if (!Application.isPlaying)
        {
            foreach (Transform child in transform)
            {
                if (child.gameObject.activeSelf) { target = child; break; }
            }
        }

        float gizmoRadius = baseRadius;
        if (Application.isPlaying && DataManager.Instance != null && UpgradeDatabase.Instance != null)
        {
            gizmoRadius = _radius;
        }

        Gizmos.color = Color.yellow;
        Gizmos.DrawWireSphere(target.position, _pickupActive ? _baseComputedRadius : gizmoRadius);

        if (_pickupActive)
        {
            Gizmos.color = Color.cyan;
            Gizmos.DrawWireSphere(target.position, gizmoRadius);
        }
    }
}