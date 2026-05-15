using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class UpgradeUI : MonoBehaviour
{
    public UpgradeData upgradeData;

    public TextMeshProUGUI nameText;
    public TextMeshProUGUI priceText;
    public Button buyButton;

    private int _viewedCarIndex = -1;

    void Start()
    {
        UpdateUI();
    }
    public void SetCarIndex(int carIndex)
    {
        _viewedCarIndex = carIndex;
        UpdateUI();
    }

    int GetCarIndex()
    {
        return _viewedCarIndex >= 0 ? _viewedCarIndex : DataManager.Instance.SelectedCarIndex;
    }

    public void OnBuy()
    {
        int carIndex = GetCarIndex();
        if (!DataManager.Instance.IsCarUnlocked(carIndex))
            return;

        int level = DataManager.Instance.GetUpgradeLevel(carIndex, upgradeData.type);
        int price = upgradeData.GetPrice(carIndex, level);

        bool success = DataManager.Instance.Upgrade(
            carIndex,
            upgradeData.type,
            price,
            upgradeData.maxLevel
        );

        if (success)
            UpdateUI();
    }

   void UpdateUI()
    {
        int carIndex = GetCarIndex();
        bool unlocked = DataManager.Instance.IsCarUnlocked(carIndex);
        int level = DataManager.Instance.GetUpgradeLevel(carIndex, upgradeData.type);
        int price = upgradeData.GetPrice(carIndex, level);

        bool isMax = level >= upgradeData.maxLevel;

        nameText.text = upgradeData.type + " (" + level + "/" + upgradeData.maxLevel + ")";

        if (isMax)
            priceText.text = "MAX";
        else
            priceText.text = price + " $";

        buyButton.interactable = unlocked && !isMax;
    }
}