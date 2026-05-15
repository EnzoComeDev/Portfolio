using System;
using System.Collections.Generic;

[Serializable]
public class PlayerData
{    
    public int money;
    public float bestDistance;
    public int selectedCarIndex;
    public float totalDistance;
    public int gamesPlayed;
    public float averageDistance;
    public List<int> unlockedCars = new List<int>();
    public List<CarUpgradeData> carUpgrades = new List<CarUpgradeData>();
}

[Serializable]
public class CarUpgradeData
{
    public int carIndex;
    public int healthLevel;
    public int speedLevel;
    public int magnetLevel;
    public int nitroLevel;
}