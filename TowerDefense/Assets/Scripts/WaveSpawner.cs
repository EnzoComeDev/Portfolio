using System.Collections;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
public class WaveSpawner : MonoBehaviour
{
    [SerializeField]
    private Transform EnnemyPrefab;
    
    [SerializeField]
    private Transform spawnPoint;

    [SerializeField]
    private float timeBeetweenWave = 5.5f; //5seconde

    [SerializeField]
    private TextMeshProUGUI WaveTimer;

    private float countdown = 2f; //Temps avant démarrage

    private int WaveNumber = 0;

    void Update()
    {
        if (countdown <= 0f)
        {
            StartCoroutine(SpawnNewWave());  
            countdown = timeBeetweenWave;
        }
        countdown -= Time.deltaTime;
        WaveTimer.text = Mathf.Round(countdown).ToString();
    }

    IEnumerator SpawnNewWave()
    {
        WaveNumber++;
        Debug.Log("Apparition d'une nouvelle vague. Vague n°" + WaveNumber);
        for (int i = 0 ; i < WaveNumber*3; ++i)
        {
            SpawnEnnemy();
            yield return new WaitForSeconds(0.3f);
        }
        
    }

    void SpawnEnnemy()
    {
        Instantiate(EnnemyPrefab,spawnPoint.position,spawnPoint.rotation);
    }
}
