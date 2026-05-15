using UnityEngine;

[CreateAssetMenu(menuName = "Shop/Car")]
public class CarData : ScriptableObject
{
    public string carName;
    public Sprite icon;
    public GameObject prefab;

    public int baseHealth;
    public float baseSpeed;

    public int price;
    public UpgradeData[] upgrades; 
}