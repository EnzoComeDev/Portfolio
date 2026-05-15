using UnityEngine;

public class OilSlick : MonoBehaviour
{
    [SerializeField] private float slideDuration = 2f;
    [SerializeField] private float slideForce = 5f;
    private void OnTriggerEnter(Collider other)
    {
        if (!other.CompareTag("Player")) return;
        CarController car = CarController.Instance;
        if (car != null)
            car.TriggerOilSlide(slideDuration, slideForce);
    }
}