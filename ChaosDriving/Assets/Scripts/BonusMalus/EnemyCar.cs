using UnityEngine;

public class EnemyCar : MonoBehaviour
{
    public float speed = 300f;
    private bool _hasHit = false;

    void FixedUpdate()
    {
        if (GameManager.Instance.CurrentState != GameManager.GameState.Playing) return;
        transform.position += Vector3.forward * speed * Time.fixedDeltaTime;
    }

    void OnTriggerEnter(Collider other)
    {
        if (_hasHit) return;
        if (other.CompareTag("Player") ||
            (other.transform.parent != null && other.transform.parent.CompareTag("Player")))
        {
            _hasHit = true;
            GameManager.Instance.PlayerDied();
            Destroy(gameObject);
        }
    }

    void Update()
    {
        if (CarController.Instance == null) return;
        if (transform.position.z > CarController.Instance.transform.position.z + 20f)
            Destroy(gameObject);
    }
}