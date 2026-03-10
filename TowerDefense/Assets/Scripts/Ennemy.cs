using UnityEngine;

public class Ennemy : MonoBehaviour
{
    public float speed = 10f;
    public float life = 50f;
    private Transform target; //Cible vers laquel l'ennemi avance
    private int waypointIndex = 0;
    void Start()
    {
        target = Waypoints.points[waypointIndex];
    
    }

    private void Update()
    {
        Vector3 direction = target.position - transform.position;
        transform.Translate(direction.normalized * speed * Time.deltaTime);
        if (Vector3.Distance(transform.position, target.position) <= 0.2f)
        {
            GetNextWaypoint();
            //waypointIndex++;
            //target = Waypoints.points[waypointIndex];
        }
    }

    private void GetNextWaypoint()
    {
        if (waypointIndex > Waypoints.points.Length-1)
        {
            Destroy(gameObject);
            return;
        }

        waypointIndex++;
        target = Waypoints.points[waypointIndex];
    }


}