#include "Condition.hh"
#include "jardinHandler.hh"
#include <cmath>
#include <QPoint>

Condition::Condition(TypeCondition type, bool negation, int tortueId)
    : _type(type), _negation(negation), _tortueId(tortueId) {}

bool Condition::evaluerPourTortue(JardinHandler& jardin, int tortueIndex) const {
    QPoint pos = jardin.getJardin()->position(tortueIndex);
    float orientation = jardin.getJardin()->orientation(tortueIndex);

    int dx = 0, dy = 0;
    switch (_type) {
        case TypeCondition::MUR_DEVANT:
        case TypeCondition::VIDE_DEVANT:
            if (std::abs(orientation - 0) < 0.1) { dx = 1; dy = 0; }      // droite
            else if (std::abs(orientation - 90) < 0.1) { dx = 0; dy = -1; }  // haut
            else if (std::abs(orientation - 180) < 0.1) { dx = -1; dy = 0; } // gauche
            else if (std::abs(orientation - 270) < 0.1) { dx = 0; dy = 1; }  // bas
            break;

        case TypeCondition::MUR_DERRIERE:
        case TypeCondition::VIDE_DERRIERE:
            if (std::abs(orientation - 0) < 0.1) { dx = -1; dy = 0; }
            else if (std::abs(orientation - 90) < 0.1) { dx = 0; dy = 1; }
            else if (std::abs(orientation - 180) < 0.1) { dx = 1; dy = 0; }
            else if (std::abs(orientation - 270) < 0.1) { dx = 0; dy = -1; }
            break;

        case TypeCondition::MUR_GAUCHE:
        case TypeCondition::VIDE_GAUCHE:
            // a gauche de l'orientation
            if (std::abs(orientation - 0) < 0.1) { dx = 0; dy = -1; }
            else if (std::abs(orientation - 90) < 0.1) { dx = -1; dy = 0; }
            else if (std::abs(orientation - 180) < 0.1) { dx = 0; dy = 1; }
            else if (std::abs(orientation - 270) < 0.1) { dx = 1; dy = 0; }
            break;

        case TypeCondition::MUR_DROITE:
        case TypeCondition::VIDE_DROITE:
            // a droite 
            if (std::abs(orientation - 0) < 0.1) { dx = 0; dy = 1; }
            else if (std::abs(orientation - 90) < 0.1) { dx = 1; dy = 0; }
            else if (std::abs(orientation - 180) < 0.1) { dx = 0; dy = -1; }
            else if (std::abs(orientation - 270) < 0.1) { dx = -1; dy = 0; }
            break;
    }

    int testX = pos.x() / 40 + dx;
    int testY = pos.y() / 40 + dy;

    bool resultat = false;
    switch (_type) {
        case TypeCondition::MUR_DEVANT:
        case TypeCondition::MUR_DERRIERE:
        case TypeCondition::MUR_GAUCHE:
        case TypeCondition::MUR_DROITE:
            resultat = jardin.getJardin()->estMur(testX, testY);
            break;

        case TypeCondition::VIDE_DEVANT:
        case TypeCondition::VIDE_DERRIERE:
        case TypeCondition::VIDE_GAUCHE:
        case TypeCondition::VIDE_DROITE:
            resultat = jardin.getJardin()->estVide(testX, testY);
            break;
    }

    return _negation ? !resultat : resultat;
}

bool Condition::evaluer(JardinHandler& jardin, Contexte& ctx) const {
    if (_tortueId == 0) {
        int nbTortues = jardin.getJardin()->nombreTortues();
        for (int i = 0; i < nbTortues; ++i) {
            if (!evaluerPourTortue(jardin, i)) {
                return false;
            }
        }
        return true;
    } else {
        return evaluerPourTortue(jardin, _tortueId - 1);
    }
}

std::string Condition::toString() const {
    std::string s;
    if (_negation) s += "pas de ";

    switch (_type) {
        case TypeCondition::MUR_DEVANT: s += "mur devant"; break;
        case TypeCondition::MUR_DERRIERE: s += "mur derriere"; break;
        case TypeCondition::MUR_GAUCHE: s += "mur à gauche"; break;
        case TypeCondition::MUR_DROITE: s += "mur à droite"; break;
        case TypeCondition::VIDE_DEVANT: s += "vide devant"; break;
        case TypeCondition::VIDE_DERRIERE: s += "vide derriere"; break;
        case TypeCondition::VIDE_GAUCHE: s += "vide à gauche"; break;
        case TypeCondition::VIDE_DROITE: s += "vide à droite"; break;
    }

    if (_tortueId > 0) s += " @" + std::to_string(_tortueId);
    return s;
}
