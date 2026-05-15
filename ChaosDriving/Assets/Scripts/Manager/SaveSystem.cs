using UnityEngine;

public static class SaveSystem
{
    public static PlayerData Data;

    public static void Load()
    {
        PlayerPrefs.DeleteAll();
        if (PlayerPrefs.HasKey("SAVE"))
        {
            Data = JsonUtility.FromJson<PlayerData>(
                PlayerPrefs.GetString("SAVE")
            );
        }
        else
        {
            Data = new PlayerData();
            Data.money = 45000;
            Data.selectedCarIndex = 0;
            Data.carUpgrades = new System.Collections.Generic.List<CarUpgradeData>();
            Data.unlockedCars = new System.Collections.Generic.List<int>();
            Data.unlockedCars.Add(0);

            Save();
        }
    }

    public static void Save()
    {
        PlayerPrefs.SetString("SAVE", JsonUtility.ToJson(Data));
        PlayerPrefs.Save();
    }
}