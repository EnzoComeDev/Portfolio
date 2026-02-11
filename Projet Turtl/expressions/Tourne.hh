#pragma once
#include "Instruction.hh"
#include <string>

class Tourne : public Instruction {
public:
    Tourne(const std::string& direction, int fois = 1, int tortueId = 0);

    void executer(JardinHandler& jardin, Contexte& ctx) const override;
    std::string toString(int indent = 0) const override;

private:
    std::string _direction;
    int _fois;
    int _tortueId;
};
