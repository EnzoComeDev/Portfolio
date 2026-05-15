using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class CarSelectionUI : MonoBehaviour
{
    public CarData[] cars;
    public Image carPreview;
    public TextMeshProUGUI carName;
    public TextMeshProUGUI statHealth;
    public TextMeshProUGUI statSpeed;
    public TextMeshProUGUI statPrice;

    public Button btnBuyCar;
    public TextMeshProUGUI btnBuyCarText;

    public UpgradeUI[] upgradeUIs;

    private int currentIndex = 0;

    void Start()
    {
        UpdateDisplay();
    }

    public void OnBtnNext()
    {
        currentIndex = (currentIndex + 1) % cars.Length;
        UpdateDisplay();
    }

    public void OnBtnPrev()
    {
        currentIndex = (currentIndex - 1 + cars.Length) % cars.Length;
        UpdateDisplay();
    }

    void UpdateDisplay()
    {
        if (cars == null || cars.Length == 0) return;

        CarData car = cars[currentIndex];

        if (carPreview != null) carPreview.sprite = car.icon;
        if (carName != null) carName.text = car.carName;
        if (statHealth != null) statHealth.text = "VIE " + car.baseHealth;
        if (statSpeed != null) statSpeed.text = "VIT " + car.baseSpeed;

        bool unlocked = car.price == 0 || DataManager.Instance.IsCarUnlocked(currentIndex);
        bool isSelected = DataManager.Instance.SelectedCarIndex == currentIndex;

        if (btnBuyCarText != null)
        {
            if (isSelected)
            {
                btnBuyCarText.text = "SELECTED";
                btnBuyCar.interactable = false;
            }
            else if (unlocked)
            {
                btnBuyCarText.text = "SELECT";
                btnBuyCar.interactable = true;
            }
            else
            {
                btnBuyCarText.text = "BUY - " + car.price + "$";
                btnBuyCar.interactable = true;
            }
        }
        if (upgradeUIs != null)
        {
            foreach (var ui in upgradeUIs)
            {
                if (ui != null)
                    ui.SetCarIndex(currentIndex);
            }
        }
    }

    public void OnBtnBuyCar()
    {
        CarData car = cars[currentIndex];

        if (car.price == 0 || DataManager.Instance.IsCarUnlocked(currentIndex))
        {
            DataManager.Instance.SelectedCarIndex = currentIndex;
            SaveSystem.Save();
            UpdateDisplay();
            return;
        }

        bool success = DataManager.Instance.BuyCar(currentIndex, car.price);

        if (success)
        {
            DataManager.Instance.SelectedCarIndex = currentIndex;
            UpdateDisplay();
        }
    }
}