#include "TantQue.hh"
#include "jardinHandler.hh"  




TantQue::TantQue(ConditionPtr condition, Bloc bloc)
    : _condition(condition), _bloc(bloc) {}

void TantQue::executer(JardinHandler& jardin, Contexte& ctx) const {
    while (_condition->evaluer(jardin, ctx)) {
        for (const auto& inst : _bloc) {
            inst->executer(jardin, ctx);
        }
    }
}

std::string TantQue::toString(int indent) const {
    std::string s(indent, ' ');
    s += "Tant que " + _condition->toString() + ":\n";

    for (const auto& inst : _bloc) {
        s += inst->toString(indent + 2) + "\n";
    }

    s += std::string(indent, ' ') + "Fin Tant Que";
    return s;
}
