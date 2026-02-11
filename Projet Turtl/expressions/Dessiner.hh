#pragma once
#include "Instruction.hh"

class Dessiner : public Instruction {
public:
    Dessiner() = default;
    void executer(JardinHandler& jardin, Contexte& ctx) const override;
    std::string toString(int indent = 0) const override;
};
