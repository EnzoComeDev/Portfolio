#pragma once
#include "Instruction.hh"
#include "expression.hh"

class Saute : public Instruction {
public:
    Saute(ExpressionPtr distance, int fois = 1, int tortueId = 0);
    void executer(JardinHandler& jardin, Contexte& ctx) const override;
    std::string toString(int indent = 0) const override;
private:
    ExpressionPtr _distance;
    int _fois;
    int _tortueId;
};
