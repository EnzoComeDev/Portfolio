using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }
    public enum GameState { Menu, Playing, Dead, GameOver, Win }
    public GameState CurrentState { get; private set; } = GameState.Menu;
    public float Distance { get; private set; }
    public int Score { get; private set; }
    public int Lives { get; private set; } = 3;
    public bool IsPaused { get; private set; }
    private int startLives = 3;
    private string gameScene = "Game";
    private string menuScene = "Menu";
    public int GameMoney { get; private set; } = 0;

    void Awake()
    {
        bool isFullscreen = Screen.fullScreen;
        Screen.SetResolution(1920, 1080, isFullscreen);
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

    void Start()
    {
        if (SceneManager.GetActiveScene().name == gameScene)
            StartGame();
    }


    public void StartGame()
    {
        Distance = 0;
        Score = 0;
        Lives = startLives;
        GameMoney = 0; 
        IsPaused = false;
        Time.timeScale = 1f; 
        ChangeState(GameState.Playing);
        SceneManager.LoadScene(gameScene); 
    }

    public void ReturnToMenu()
    {
        ChangeState(GameState.Menu);
        SceneManager.LoadScene(menuScene);
    }

    public void AddDistance(float delta)
    {
        if (CurrentState != GameState.Playing) return;
        Distance += delta;
    }

    public void AddScore(int pts)
    {
        if (CurrentState != GameState.Playing) return;
        Score += pts;
    }
    public void AddCash(int cash)
    {
        if (cash > 0)
        {
            GameMoney += cash;
        }
    }
    public void PlayerDied()
    {
        if (CurrentState != GameState.Playing) return;
        Lives--;
        if (Lives <= 0)
            ChangeState(GameState.GameOver);
    }

    public void TogglePause()
    {
        IsPaused = !IsPaused;
        Time.timeScale = IsPaused ? 0f : 1f;
    }

    public void ChangeState(GameState newState)
    {
        CurrentState = newState;
    }
    
    public int GetDistanceMeters(float positionZ)
    {
        return Mathf.FloorToInt(positionZ / 10f);
    }

    public void SetLives(int amount)
    {
        startLives = amount;
        Lives = amount;
    }

    public void SetDistance(float distance)
    {
        Distance = distance;
    }
}