#pragma once
#include "Instruction.hh"
#include "expression.hh"

class Avance : public Instruction {
public:
    Avance(ExpressionPtr distance, int fois = 1, int tortueId = 0);

    void executer(JardinHandler& jardin, Contexte& ctx) const override;
    std::string toString(int indent = 0) const override;

private:
    ExpressionPtr _distance;
    int _fois;
    int _tortueId;
};
