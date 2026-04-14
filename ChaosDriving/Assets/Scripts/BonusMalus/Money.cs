using UnityEngine;

public class Money : MonoBehaviour
{
    void OnTriggerEnter (Collider other)
    {
        Debug.Log ("Money");
        if (!other.CompareTag("Player")) return;

        GameManager.Instance.AddCash(50);
        Destroy(gameObject);
    }
}
