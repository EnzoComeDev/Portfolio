#include "Tourne.hh"
#include "jardinHandler.hh"
#include <iostream>

Tourne::Tourne(const std::string& direction, int fois, int tortueId)
    : _direction(direction), _fois(fois), _tortueId(tortueId) {}

void Tourne::executer(JardinHandler& jardin, Contexte& ctx) const {
    float angle = 0;
    if (_direction == "gauche" || _direction == "à gauche") {
        angle = 90.0f;
    } else if (_direction == "droite" || _direction == "à droite") {
        angle = -90.0f;
    } else if (_direction == "derriere" || _direction == "derrière") {
        angle = 180.0f;
    }

    for (int i = 0; i < _fois; ++i) {
        if (_tortueId == 0) {
            int nbTortues = jardin.getJardin()->nombreTortues();
            for (int t = 0; t < nbTortues; ++t) {
                float orientationActuelle = jardin.getJardin()->orientation(t);
                jardin.getJardin()->changeOrientation(t, orientationActuelle + angle);
            }
        } else {
            float orientationActuelle = jardin.getJardin()->orientation(_tortueId - 1);
            jardin.getJardin()->changeOrientation(_tortueId - 1, orientationActuelle + angle);
        }
    }
}

std::string Tourne::toString(int indent) const {
    std::string s(indent, ' ');
    s += "Tourne " + _direction;
    if (_fois != 1) s += " " + std::to_string(_fois) + " fois";
    if (_tortueId > 0) s += " @" + std::to_string(_tortueId);
    return s;
}
