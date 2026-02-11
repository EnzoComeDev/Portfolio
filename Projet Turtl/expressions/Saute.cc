#include "Saute.hh"
#include "jardinHandler.hh"
#include <cmath>

Saute::Saute(ExpressionPtr distance, int fois, int tortueId)
    : _distance(std::move(distance)), _fois(fois), _tortueId(tortueId) {}

void Saute::executer(JardinHandler& jardin, Contexte& ctx) const {
    int nb = static_cast<int>(std::round(_distance->evaluer(ctx)));

    // sauter = avancer de 2*nb cases
    for (int i = 0; i < _fois; ++i) {
        if (_tortueId == 0) {
            jardin.avancerToutes(nb * 2);
        } else {
            jardin.avancer(_tortueId - 1, nb * 2);
        }
    }
}

std::string Saute::toString(int indent) const {
    std::string s(indent, ' ');
    s += "Saute " + _distance->toString();
    if (_fois != 1) s += " " + std::to_string(_fois) + " fois";
    if (_tortueId > 0) s += " @" + std::to_string(_tortueId);
    return s;
}
