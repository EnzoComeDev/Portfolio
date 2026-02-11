#pragma once
#include "Instruction.hh"
#include <string>

class Couleur : public Instruction {
public:
    Couleur(const std::string& hex, int tortueId = 0);
    void executer(JardinHandler& jardin, Contexte& ctx) const override;
    std::string toString(int indent = 0) const override;
private:
    std::string _hex;
    int _tortueId;
};
