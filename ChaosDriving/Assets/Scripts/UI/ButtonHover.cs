using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

public class ButtonHover : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler
{
    Vector3 originalScale;
    Image img;
    Color originalColor;

    void Start()
    {
        originalScale = transform.localScale;
        img = GetComponent<Image>();
        originalColor = img.color;
    }

    public void OnPointerEnter(PointerEventData eventData)
    {
        transform.localScale = originalScale * 1.15f;
        Color c = img.color;
        c.a = 1f;
        img.color = c;
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        transform.localScale = originalScale;
        img.color = originalColor;
    }

}