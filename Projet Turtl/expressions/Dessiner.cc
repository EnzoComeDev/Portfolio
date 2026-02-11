#include "Dessiner.hh"
#include "jardinHandler.hh"

void Dessiner::executer(JardinHandler& jardin, Contexte& ctx) const {
    jardin.dessiner();
}

std::string Dessiner::toString(int indent) const {
    return std::string(indent, ' ') + "Dessiner";
}
