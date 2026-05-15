using UnityEngine;
using System.Collections.Generic;

public class PickupSpawner : MonoBehaviour
{
    [System.Serializable]
    public class PickupEntry
    {
        public GameObject prefab;
        [Range(0f, 1f)] public float weight;
    }

    public PickupEntry[] pickups;
    public int laneCount = 3;
    public float laneWidth = 3.5f;
    public float roadCenterX = 0f;
    public float segmentLength = 480f;

    private List<GameObject> _spawnedPickups = new List<GameObject>();

    float[] GetLanes()
    {
        float[] lanes = new float[laneCount];
        float totalWidth = (laneCount - 1) * laneWidth;
        for (int i = 0; i < laneCount; i++)
            lanes[i] = roadCenterX - totalWidth / 2f + i * laneWidth;
        return lanes;
    }

    public void SpawnPickups()
    {
        ClearPickups();

        float[] lanes = GetLanes();
        for (float z = -segmentLength / 2f + 5f; z <= segmentLength / 2f - 5f; z += 10f)
        {
            if (Random.Range(0, 3) == 0) continue;

            float laneX = lanes[Random.Range(0, lanes.Length)];

            PickupEntry entry = GetWeightedRandom();
            if (entry == null || entry.prefab == null) continue;

            Vector3 spawnPos = transform.position + new Vector3(laneX, 1.0f, z);
            GameObject pickup = Instantiate(entry.prefab, spawnPos, entry.prefab.transform.rotation);
            _spawnedPickups.Add(pickup);
        }
    }

    public void ClearPickups()
    {
        foreach (var p in _spawnedPickups)
            if (p != null) Destroy(p);
        _spawnedPickups.Clear();
    }

    PickupEntry GetWeightedRandom()
    {
        float total = 0f;
        foreach (var p in pickups)
            if (p != null && p.prefab != null) total += p.weight;

        if (total == 0f) return null;

        float roll = Random.Range(0f, total);
        float cumul = 0f;

        foreach (var p in pickups)
        {
            if (p == null || p.prefab == null) continue;
            cumul += p.weight;
            if (roll <= cumul) return p;
        }

        return null;
    }
}