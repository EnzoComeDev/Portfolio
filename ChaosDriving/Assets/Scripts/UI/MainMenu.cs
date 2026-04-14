using UnityEngine;

public class MainMenu : MonoBehaviour
{
    public void Play()
    {
       Debug.Log("Game Cliqued");
       UnityEngine.SceneManagement.SceneManager.LoadScene("Game");
    }

    public void Shop()
    {
        UnityEngine.SceneManagement.SceneManager.LoadScene("Shop");
    }

    public void Quit()
    {
        Application.Quit();
    }
}
