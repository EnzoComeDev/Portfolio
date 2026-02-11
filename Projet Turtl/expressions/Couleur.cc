#include "Couleur.hh"
#include "jardinHandler.hh"

Couleur::Couleur(const std::string& hex, int tortueId)
    : _hex(hex), _tortueId(tortueId) {}

void Couleur::executer(JardinHandler& jardin, Contexte& ctx) const {
    int r = std::stoi(_hex.substr(1, 2), nullptr, 16);
    int g = std::stoi(_hex.substr(3, 2), nullptr, 16);
    int b = std::stoi(_hex.substr(5, 2), nullptr, 16);

    if (_tortueId == 0) {
        int nbTortues = jardin.getJardin()->nombreTortues();
        for (int t = 0; t < nbTortues; ++t) {
            jardin.getJardin()->changeCouleur(t, r, g, b);
        }
    } else {
        jardin.getJardin()->changeCouleur(_tortueId - 1, r, g, b);
    }
}

std::string Couleur::toString(int indent) const {
    std::string s(indent, ' ');
    s += "Couleur " + _hex;
    if (_tortueId > 0) s += " @" + std::to_string(_tortueId);
    return s;
}
