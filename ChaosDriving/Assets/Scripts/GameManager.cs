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
    private int GameMoney = 0;

    void Awake()
    {
        if (Instance != null) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

    void Start()
    {
        StartGame();
    }

    public void StartGame()
    {
        Distance = 0;
        Score = 0;
        Lives = startLives;
        IsPaused = false;
        ChangeState(GameState.Playing);
        if (SceneManager.GetActiveScene().name != gameScene)
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

    private void ChangeState(GameState newState)
    {
        CurrentState = newState;
    }
    


}