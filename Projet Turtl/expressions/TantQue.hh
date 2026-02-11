#pragma once
#include "Instruction.hh"
#include "Condition.hh"
#include <vector>

class TantQue : public Instruction {
public:
    TantQue(ConditionPtr condition, Bloc bloc);

    void executer(JardinHandler& jardin, Contexte& ctx) const override;
    std::string toString(int indent = 0) const override;

private:
    ConditionPtr _condition;
    Bloc _bloc;
};
