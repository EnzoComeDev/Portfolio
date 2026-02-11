#include "expressionBinaire.hh"

ExpressionBinaire::ExpressionBinaire(ExpressionPtr gauche, ExpressionPtr droite, OperateurBinaire op):
    _gauche(gauche), _droite(droite), _op(op) {}

double ExpressionBinaire::calculer(const Contexte& contexte) const {
    double gauche = _gauche->calculer(contexte), droite = _droite->calculer(contexte);
    switch (_op) {
        case OperateurBinaire::plus: return gauche + droite;
        case OperateurBinaire::moins: return gauche - droite;
        case OperateurBinaire::divise: return gauche / droite;
        case OperateurBinaire::multiplie: return gauche * droite;
        default: return 0;
    }
}

std::string ExpressionBinaire::toString() const {
    std::string op;
    switch (_op) {
        case OperateurBinaire::plus: op = "+"; break;
        case OperateurBinaire::moins: op = "-"; break;
        case OperateurBinaire::multiplie: op = "*"; break;
        case OperateurBinaire::divise: op = "/"; break;
    }
    return "(" + _gauche->toString() + " " + op + " " + _droite->toString() + ")";
}
