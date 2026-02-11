// expressions/Instruction.hh
#pragma once

#include <memory>
#include <string>
#include <vector>

#include "contexte.hh"

class JardinHandler;

class Instruction {
public:
    virtual ~Instruction() = default;
    virtual void executer(JardinHandler& jardin, Contexte& ctx) const = 0;
    virtual std::string toString(int indent = 0) const = 0;
};

using InstructionPtr = std::shared_ptr<Instruction>;
using Bloc = std::vector<InstructionPtr>;
