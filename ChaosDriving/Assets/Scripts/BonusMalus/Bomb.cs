using UnityEngine;

public class Bomb : MonoBehaviour
{
    void OnTriggerEnter (Collider other)
    {
        Debug.Log ("Explosion");
        if (!other.CompareTag("Player")) return;

        GameManager.Instance.PlayerDied();
        Destroy(gameObject);
    }
}
