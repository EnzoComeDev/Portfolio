using UnityEngine;

public class UpgradeDatabase : MonoBehaviour
{
    public static UpgradeDatabase Instance { get; private set; }
    public UpgradeData health;
    public UpgradeData speed;
    public UpgradeData magnet;
    public UpgradeData nitro;
    void Awake() => Instance = this;
    public UpgradeData Get(UpgradeType type)
    {
        switch (type)
        {
            case UpgradeType.Health: return health;
            case UpgradeType.Speed:  return speed;
            case UpgradeType.Magnet: return magnet;
            case UpgradeType.Nitro:  return nitro;
        }
        return null;
    }
}