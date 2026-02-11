#include "Avance.hh"
#include "jardinHandler.hh"

Avance::Avance(ExpressionPtr distance, int fois, int tortueId)
    : _distance(std::move(distance)), _fois(fois), _tortueId(tortueId) {}

void Avance::executer(JardinHandler& jardin, Contexte& ctx) const {
    int nbPas = _distance->evaluer(ctx);

    for (int f = 0; f < _fois; f++) {
        if (_tortueId == 0) {
            jardin.avancerToutes(nbPas);
        } else {
            jardin.avancer(_tortueId - 1, nbPas);
        }
    }
}

std::string Avance::toString(int indent) const {
    std::string s(indent, ' ');
    s += "Avance " + _distance->toString();
    if (_fois != 1) s += " " + std::to_string(_fois) + " fois";
    if (_tortueId > 0) s += " @" + std::to_string(_tortueId);
    return s;
}

