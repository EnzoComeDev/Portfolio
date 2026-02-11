#include "constante.hh"
#include <string>

Constante::Constante(double valeur) : _valeur(valeur) {}

double Constante::calculer(const Contexte & contexte) const {
    return _valeur;
}

std::string Constante::toString() const {
    return std::to_string(_valeur);
}
