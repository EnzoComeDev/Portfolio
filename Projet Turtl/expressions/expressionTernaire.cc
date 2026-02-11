#include "expressionTernaire.hh"

ExpressionTernaire::ExpressionTernaire(ExpressionPtr condition, ExpressionPtr exp1, ExpressionPtr exp2, OperateurTernaire op):
    _condition(condition), _exp1(exp1), _exp2(exp2), _op(op) {}

double ExpressionTernaire::calculer(const Contexte& contexte) const {
    switch (_op) {
        case OperateurTernaire::ifthenelse: {
            bool resultatCondition = _condition->calculer(contexte);
            if (resultatCondition)
                return _exp1->calculer(contexte);
            else
                return _exp2->calculer(contexte);
        }
        default:
            return 0;
    }
}

std::string ExpressionTernaire::toString() const {
    return "(" + _condition->toString() + " ? " +
           _exp1->toString() + " : " + _exp2->toString() + ")";
}
