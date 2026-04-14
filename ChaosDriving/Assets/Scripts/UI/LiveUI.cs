using UnityEngine;
using TMPro;
using System;

public class HUDManager : MonoBehaviour
{
    [SerializeField] private TextMeshProUGUI livesText;

    void Update()
    {
        if (GameManager.Instance == null) return;
        livesText.text = GameManager.Instance.Lives.ToString();
    }
}