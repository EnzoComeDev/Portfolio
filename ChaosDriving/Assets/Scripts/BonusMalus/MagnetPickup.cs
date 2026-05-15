using UnityEngine;

public class MagnetPickup : MonoBehaviour
{
    void OnTriggerEnter(Collider other)
    {
        if (!other.CompareTag("Player")) return;
        MagnetAttractor attractor = other.GetComponentInParent<MagnetAttractor>();

        if (attractor == null)
        {
            attractor = FindObjectOfType<MagnetAttractor>();
        }

        if (attractor != null)
        {
            attractor.ActivatePickupBonus();
        }
        Destroy(gameObject);
    }
}