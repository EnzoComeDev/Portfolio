#include "variable.hh"

Variable::Variable(const std::string& nom) : _nom(nom) {}

double Variable::calculer(const Contexte & contexte) const {
    return contexte[_nom];
}

std::string Variable::toString() const {
    return _nom;
}
