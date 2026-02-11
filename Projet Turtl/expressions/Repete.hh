#pragma once
#include "Instruction.hh"
#include "expression.hh"
#include <vector>

class Repete : public Instruction {
public:
    Repete(ExpressionPtr nombre, Bloc bloc);

    void executer(JardinHandler& jardin, Contexte& ctx) const override;
    std::string toString(int indent = 0) const override;

private:
    ExpressionPtr _nombre;
    Bloc _bloc;
};
