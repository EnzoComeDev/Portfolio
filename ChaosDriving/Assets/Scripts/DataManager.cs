using UnityEngine;

public class DataManager : MonoBehaviour
{
    public static DataManager Instance;
    public int Money;
    public float BestDistance;
    private string CarSelected;
    void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }

        CarSelected = "Beatall";
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

    public void EndGame(int earnedMoney, float distance)
    {
        Money += earnedMoney;
        if (distance > BestDistance)
        {
            BestDistance = distance;
        }
        Debug.Log($"EndGame Money: {Money}, Best: {BestDistance}");
    }
}