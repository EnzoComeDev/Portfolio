using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    public Transform playerCar;
    public float baseFOV = 60f;
    public float maxFOV = 80f;
    public float fovSmoothSpeed = 3f;
    public float offsetX = -10f;
    public float offsetY = 13f;
    public float baseOffsetZ = -15f;
    public float maxOffsetZ = -23f;
    public float smoothTime = 0.1f;
    private Transform target;
    private Camera _cam;
    private Vector3 _velocity = Vector3.zero;

    void Start()
    {
        foreach (Transform child in playerCar)
        {
            if (child.gameObject.activeSelf)
            {
                target = child;
                break;
            }
        }

        _cam = GetComponent<Camera>();
        if (target != null)
            transform.position = target.position + new Vector3(offsetX, offsetY, baseOffsetZ);
    }

    void LateUpdate()
    {
        if (target == null) return;

        float speedRatio = CarController.Instance.CurrentSpeed / CarController.Instance.BaseSpeed;

        float currentOffsetZ = Mathf.Clamp(
            Mathf.Lerp(baseOffsetZ, maxOffsetZ, speedRatio - 1f),
            maxOffsetZ, baseOffsetZ
        );

        Vector3 desiredPos = target.position + new Vector3(offsetX, offsetY, currentOffsetZ);
        transform.position = Vector3.SmoothDamp(transform.position, desiredPos, ref _velocity, smoothTime);

        float targetFOV = Mathf.Lerp(baseFOV, maxFOV, (speedRatio - 1f) * 0.3f);
        _cam.fieldOfView = Mathf.Lerp(_cam.fieldOfView, targetFOV, fovSmoothSpeed * Time.deltaTime);
    }
}