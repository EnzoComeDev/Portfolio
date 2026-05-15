using UnityEngine;

public class DataManager : MonoBehaviour
{
    public static DataManager Instance;

    void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }

        Instance = this;
        DontDestroyOnLoad(gameObject);

        SaveSystem.Load();

        if (SaveSystem.Data.carUpgrades == null) SaveSystem.Data.carUpgrades = new System.Collections.Generic.List<CarUpgradeData>();
        if (SaveSystem.Data.unlockedCars == null)  SaveSystem.Data.unlockedCars = new System.Collections.Generic.List<int>();
    }

    public int Money
    {
        get => SaveSystem.Data.money;
        set => SaveSystem.Data.money = value;
    }

    public int SelectedCarIndex
    {
        get => SaveSystem.Data.selectedCarIndex;
        set => SaveSystem.Data.selectedCarIndex = value;
    }

    public float BestDistance
    {
        get => SaveSystem.Data.bestDistance;
        set => SaveSystem.Data.bestDistance = value;
    }

    CarUpgradeData GetCarData(int index)
    {
        var car = SaveSystem.Data.carUpgrades
            .Find(c => c.carIndex == index);

        if (car == null)
        {
            car = new CarUpgradeData();
            car.carIndex = index;

            SaveSystem.Data.carUpgrades.Add(car);
        }

        return car;
    }

    public int GetUpgradeLevel(int carIndex, UpgradeType type)
    {
        var car = GetCarData(carIndex);

        switch (type)
        {
            case UpgradeType.Health: return car.healthLevel;
            case UpgradeType.Speed: return car.speedLevel;
            case UpgradeType.Magnet: return car.magnetLevel;
            case UpgradeType.Nitro: return car.nitroLevel;
        }

        return 0;
    }

    public bool Upgrade(int carIndex, UpgradeType type, int price, int maxLevel)
    {
        if (Money < price)
            return false;

        var car = GetCarData(carIndex);

        int level = GetUpgradeLevel(carIndex, type);

        if (level >= maxLevel)
            return false;

        Money -= price;

        switch (type)
        {
            case UpgradeType.Health: car.healthLevel++; break;
            case UpgradeType.Speed: car.speedLevel++; break;
            case UpgradeType.Magnet: car.magnetLevel++; break;
            case UpgradeType.Nitro: car.nitroLevel++; break;
        }

        SaveSystem.Save();
        return true;
    }

    public void SelectCar(int index)
    {
        SelectedCarIndex = index;
    }

    public void EndGame(int earnedMoney, float distance)
    {
        Money += earnedMoney;

        if (distance > BestDistance)
            BestDistance = distance;

        SaveSystem.Data.totalDistance += distance;
        SaveSystem.Data.gamesPlayed++;

        SaveSystem.Data.averageDistance =
            SaveSystem.Data.gamesPlayed > 0
            ? SaveSystem.Data.totalDistance / SaveSystem.Data.gamesPlayed
            : 0;

        SaveSystem.Save();
    }

    public bool IsCarUnlocked(int index)
    {
        return SaveSystem.Data.unlockedCars.Contains(index);
    }

    public bool BuyCar(int index, int price)
    {
        if (Money < price) return false;
        if (SaveSystem.Data.unlockedCars.Contains(index)) return false;

        Money -= price;
        SaveSystem.Data.unlockedCars.Add(index);

        SaveSystem.Save();
        return true;
    }
}