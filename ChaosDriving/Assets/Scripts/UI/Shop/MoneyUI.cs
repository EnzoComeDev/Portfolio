using UnityEngine;
using TMPro;

public class MoneyUI : MonoBehaviour
{
    private TextMeshProUGUI text;

    void Awake()
    {
        text = GetComponent<TextMeshProUGUI>();
    }

    void Update()
    {
        if (DataManager.Instance == null) return;

        text.text = DataManager.Instance.Money + " $";
    }
}