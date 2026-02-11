#include "Repete.hh"
#include "jardinHandler.hh"
#include <cmath>

Repete::Repete(ExpressionPtr nombre, Bloc bloc)
    : _nombre(nombre), _bloc(bloc) {}

void Repete::executer(JardinHandler& jardin, Contexte& ctx) const {
    int n = static_cast<int>(std::round(_nombre->calculer(ctx)));

    for (int i = 0; i < n; ++i) {
        for (const auto& inst : _bloc) {
            inst->executer(jardin, ctx);
        }
    }
}

std::string Repete::toString(int indent) const {
    std::string s(indent, ' ');
    s += "Repete " + _nombre->toString() + " fois:\n";

    for (const auto& inst : _bloc) {
        s += inst->toString(indent + 2) + "\n";
    }

    s += std::string(indent, ' ') + "Fin Repete";
    return s;
}
