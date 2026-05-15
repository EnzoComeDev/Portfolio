using UnityEngine;

public class CarSelector : MonoBehaviour
{
    public static CarSelector Instance { get; private set; }
    public CarData[] cars;

    public GameObject[] carRoots;

    void Awake()
    {
        Instance = this;
        int selected = DataManager.Instance.SelectedCarIndex;
        for (int i = 0; i < carRoots.Length; i++)
            carRoots[i].SetActive(i == selected);
    }
}