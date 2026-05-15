using UnityEngine;
using TMPro;

public class HUDManager : MonoBehaviour
{
    [SerializeField] private TextMeshProUGUI livesText;
    [SerializeField] private TextMeshProUGUI cashText;
    [SerializeField] private TextMeshProUGUI distanceText;
    [SerializeField] private Transform playerCar; 

    private Transform playerTransform;
    private int _lastCash = -1;
    private int _lastDistance = -1;

    void Start()
    {
        foreach (Transform child in playerCar)
        {
            if (child.gameObject.activeSelf)
            {
                playerTransform = child;
                break;
            }
        }
    }

    void Update()
    {
        if (GameManager.Instance == null) return;
        if (playerTransform == null) return;

        int cash = GameManager.Instance.GameMoney;
        if (cash != _lastCash)
        {
            _lastCash = cash;
            cashText.text = cash.ToString("N0");
        }

        int meters = Mathf.FloorToInt(playerTransform.position.z / 10f) * -1;
        if (meters != _lastDistance)
        {
            _lastDistance = meters;
            distanceText.text = meters + "m";
            GameManager.Instance.SetDistance(meters);
        }

        livesText.text = GameManager.Instance.Lives.ToString();
    }
}