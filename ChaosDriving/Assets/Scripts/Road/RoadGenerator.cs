using UnityEngine;
using System.Collections.Generic;

public class RoadGenerator : MonoBehaviour
{
    public int segmentsBehind = 3;
    public int segmentsAhead = 5;
    public GameObject roadPrefab;
    public float segmentSpacing = -12f;
    public Vector3 startPos = Vector3.zero;

    private Queue<GameObject> pool = new Queue<GameObject>();
    private Queue<(GameObject obj, int roadNumber)> activeSegments = new Queue<(GameObject, int)>();

    private int _nextRoadNumber = 1;
    private int _lastCarRoadNumber = -1;

    int TotalSegments => segmentsBehind + segmentsAhead + 1;

    void Start()
    {
        for (int i = 0; i < TotalSegments; i++)
        {
            GameObject seg = Instantiate(roadPrefab);
            seg.SetActive(false);
            pool.Enqueue(seg);
        }

        for (int i = 0; i < TotalSegments; i++)
            SpawnNext();

        Debug.Log($"[RoadGenerator] Initialisé : {activeSegments.Count} segments actifs.");
    }

    void Update()
    {
        if (CarController.Instance == null) return;

        int carRoad = CarController.Instance.CurrentRoadNumber;
        if (carRoad <= 0) return;
        if (carRoad == _lastCarRoadNumber) return;
        _lastCarRoadNumber = carRoad;

        while (activeSegments.Count > 0 && activeSegments.Peek().roadNumber < carRoad - segmentsBehind)
        {
            var seg = activeSegments.Dequeue();
            Debug.Log($"[RoadGenerator] Despawn segment {seg.roadNumber}");
            Recycle(seg.obj);
        }

        int safetyLimit = segmentsAhead + segmentsBehind + 2;
        int spawned = 0;
        while (_nextRoadNumber <= carRoad + segmentsAhead)
        {
            if (spawned >= safetyLimit) break;
            SpawnNext();
            spawned++;
        }
    }

    void SpawnNext()
    {
        Vector3 pos = startPos + new Vector3(0, 0, segmentSpacing * (_nextRoadNumber - 1));

        GameObject seg = pool.Count > 0 ? pool.Dequeue() : Instantiate(roadPrefab);
        seg.transform.position = pos;
        seg.SetActive(true);

        seg.GetComponent<RoadStraight>().RoadNumber = _nextRoadNumber;
        activeSegments.Enqueue((seg, _nextRoadNumber));

        //Debug.Log($"[RoadGenerator] Spawn segment {_nextRoadNumber}");
        _nextRoadNumber++;
    }

    void Recycle(GameObject seg)
    {
        seg.SetActive(false);
        pool.Enqueue(seg);
    }
}