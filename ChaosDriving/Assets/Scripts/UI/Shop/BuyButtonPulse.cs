using UnityEngine;
using UnityEngine.EventSystems;
using TMPro;

public class BuyButtonHover : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler
{
    public float speed = 8f;

    private TextMeshProUGUI _text;
    private Color _colorRest;
    private bool  _hovered;
    private float _t;

    void Awake()
    {
        _text = GetComponentInChildren<TextMeshProUGUI>();
        if (_text != null) _colorRest = _text.color;
    }

    public void OnPointerEnter(PointerEventData e) => _hovered = true;
    public void OnPointerExit(PointerEventData e) => _hovered = false;

    void Update()
    {
        _t = Mathf.MoveTowards(_t, _hovered ? 1f : 0f, Time.deltaTime * speed);
        if (_text != null)
            _text.color = Color.Lerp(_colorRest, new Color(1f, 0.55f, 0f), _t);
    }
}