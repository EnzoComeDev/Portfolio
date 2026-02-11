#pragma once
#include "Instruction.hh"
#include "Condition.hh"
#include <vector>

class Si : public Instruction {
public:
    Si(ConditionPtr condition, Bloc blocSi, Bloc blocSinon = {});

    void executer(JardinHandler& jardin, Contexte& ctx) const override;
    std::string toString(int indent = 0) const override;

private:
    ConditionPtr _condition;
    Bloc _blocSi;
    Bloc _blocSinon;
};
