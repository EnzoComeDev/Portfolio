#include "Recule.hh"
#include "jardinHandler.hh"
#include <cmath>

Recule::Recule(ExpressionPtr distance, int fois, int tortueId)
    : _distance(std::move(distance)), _fois(fois), _tortueId(tortueId) {}

void Recule::executer(JardinHandler& jardin, Contexte& ctx) const {
    int nb = _distance->evaluer(ctx);

    for (int i = 0; i < _fois; ++i) {
        if (_tortueId == 0) {
            jardin.avancerToutes(-nb);
        } else {
            jardin.avancer(_tortueId - 1, -nb);
        }
    }
}

std::string Recule::toString(int indent) const {
    std::string s(indent, ' ');
    s += "Recule " + _distance->toString();
    if (_fois != 1) s += " " + std::to_string(_fois) + " fois";
    if (_tortueId > 0) s += " @" + std::to_string(_tortueId);
    return s;
}
