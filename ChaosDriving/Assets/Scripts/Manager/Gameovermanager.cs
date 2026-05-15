using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class GameOverManager : MonoBehaviour
{
    [SerializeField] private GameObject gameOverPanel;
    [SerializeField] private GameObject hudPanel;

    [SerializeField] private TextMeshProUGUI distanceText;
    [SerializeField] private TextMeshProUGUI cashText;

    [SerializeField] private GameObject livesText;
    [SerializeField] private GameObject livesImg;
    [SerializeField] private GameObject cashImg;
    [SerializeField] private GameObject cashTxt;
    [SerializeField] private GameObject distanceHUD;
    
    public GameObject car;

    private bool _hasShown = false;

    void Awake()
    {
        gameOverPanel.SetActive(false);
    }

    void Update()
    {
        if (_hasShown) return;
        if (GameManager.Instance == null) return;

        if (GameManager.Instance.CurrentState == GameManager.GameState.GameOver)
            ShowGameOver();
    }

    private void ShowGameOver()
    {
        CarController cc = car.GetComponent<CarController>();
        if (cc != null) cc.enabled = false;

        Rigidbody rb = car.GetComponent<Rigidbody>();
        if (rb != null)
        {
            rb.linearVelocity = Vector3.zero;
            rb.angularVelocity = Vector3.zero;
        }

        _hasShown = true;

        int earnedMoney = GameManager.Instance.GameMoney;
        float distance = GameManager.Instance.Distance;
        DataManager.Instance.EndGame(earnedMoney, distance);

        int meters = Mathf.FloorToInt(GameManager.Instance.Distance);
        distanceText.text = "Distance : " + meters + "m";
        cashText.text = "Argent : $" + earnedMoney.ToString("N0");

        SetHUDVisible(false);
        gameOverPanel.SetActive(true);
    }

    private void SetHUDVisible(bool visible)
    {
        if (hudPanel != null) hudPanel.SetActive(visible);
        if (livesText != null) livesText.SetActive(visible);
        if (livesImg != null) livesImg.SetActive(visible);
        if (cashImg != null) cashImg.SetActive(visible);
        if (cashTxt != null) cashTxt.SetActive(visible);
        if (distanceHUD != null) distanceHUD.SetActive(visible);
    }
    public void OnPlay()
    {
        GameManager.Instance.StartGame();
    }

    public void OnShop()
    {
        Time.timeScale = 1f;
        GameManager.Instance.ChangeState(GameManager.GameState.Menu);
        UnityEngine.SceneManagement.SceneManager.LoadScene("Shop");
    }

    public void OnMenu()
    {
        GameManager.Instance.ReturnToMenu();
    }

    public void OnQuit()
    {
        Application.Quit();
    }
}