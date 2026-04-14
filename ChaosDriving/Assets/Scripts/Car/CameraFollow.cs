using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    public Transform target;
    public float baseFOV = 60f;
    public float maxFOV = 80f;
    public float smoothSpeed = 8f;
    public Vector3 offset = new Vector3(-10, 13, -4);

    private Camera _cam;

    void Start()
    {
        _cam = GetComponent<Camera>();
    }

    void Update()
    {
        if (target == null) return;

        Vector3 desiredPos = target.position + offset;
        transform.position = Vector3.Lerp(transform.position, desiredPos, smoothSpeed * Time.deltaTime);

        float speedRatio = CarController.Instance.CurrentSpeed / CarController.Instance.BaseSpeed;
        float targetFOV = Mathf.Lerp(baseFOV, maxFOV, (speedRatio - 1f) * 0.3f);
        _cam.fieldOfView = Mathf.Lerp(_cam.fieldOfView, targetFOV, smoothSpeed * Time.deltaTime);
    }

}