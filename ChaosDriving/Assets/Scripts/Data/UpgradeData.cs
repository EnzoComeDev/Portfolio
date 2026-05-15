using UnityEngine;

public enum UpgradeType
{
    Health,
    Speed,
    Magnet,
    Nitro
}

[CreateAssetMenu(menuName = "Shop/Upgrade")]
public class UpgradeData : ScriptableObject
{
    [System.Serializable]
    public class CarPriceData
    {
        public int basePrice;
        public int priceMultiplier = 1;
    }

    [Header("Upgrade Settings")]
    public UpgradeType type;
    public int maxLevel = 5;
    public float valuePerLevel;
    public CarPriceData[] cars;
    public int GetPrice(int carIndex, int level)
    {
        if (cars == null || carIndex < 0 || carIndex >= cars.Length)
        {
            return 0;
        }

        CarPriceData data = cars[carIndex];
        return data.basePrice + (level * data.priceMultiplier);
    }
}