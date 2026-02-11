#include "Si.hh"
#include "jardinHandler.hh"


Si::Si(ConditionPtr condition, Bloc blocSi, Bloc blocSinon)
    : _condition(condition), _blocSi(blocSi), _blocSinon(blocSinon) {}

void Si::executer(JardinHandler& jardin, Contexte& ctx) const {
    if (_condition->evaluer(jardin, ctx)) {
        for (const auto& inst : _blocSi) {
            inst->executer(jardin, ctx);
        }
    } else if (!_blocSinon.empty()) {
        for (const auto& inst : _blocSinon) {
            inst->executer(jardin, ctx);
        }
    }
}

std::string Si::toString(int indent) const {
    std::string s(indent, ' ');
    s += "Si " + _condition->toString() + ":\n";

    for (const auto& inst : _blocSi) {
        s += inst->toString(indent + 2) + "\n";
    }

    if (!_blocSinon.empty()) {
        s += std::string(indent, ' ') + "Sinon:\n";
        for (const auto& inst : _blocSinon) {
            s += inst->toString(indent + 2) + "\n";
        }
    }

    s += std::string(indent, ' ') + "Fin Si";
    return s;
}
