using UnityEngine;

public class MainMenu : MonoBehaviour
{
    public void Play()
    {
       UnityEngine.SceneManagement.SceneManager.LoadScene("Game");
       GameManager.Instance.StartGame();
    }

    public void Shop()
    {
        UnityEngine.SceneManagement.SceneManager.LoadScene("Shop");
    }

    public void Quit()
    {
        Application.Quit();
    }

    public void Menu()
    {
        UnityEngine.SceneManagement.SceneManager.LoadScene("Menu");
    }
}
