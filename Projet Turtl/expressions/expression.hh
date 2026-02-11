#pragma once
#include <memory>
#include <string>
#include "contexte.hh"

class Expression {
public:
    virtual ~Expression() = default;
    virtual double calculer(const Contexte & contexte) const = 0;
    virtual std::string toString() const = 0;
};

using ExpressionPtr = std::shared_ptr<Expression>;
