#pragma once
#include <string>
#include <memory>

class JardinHandler;
class Contexte;

enum class TypeCondition {
    MUR_DEVANT,
    MUR_DERRIERE,
    MUR_GAUCHE,
    MUR_DROITE,
    VIDE_DEVANT,
    VIDE_DERRIERE,
    VIDE_GAUCHE,
    VIDE_DROITE
};

class Condition {
public:
    Condition(TypeCondition type, bool negation = false, int tortueId = 0);

    bool evaluer(JardinHandler& jardin, Contexte& ctx) const;
    std::string toString() const;

private:
    TypeCondition _type;
    bool _negation;
    int _tortueId;

    bool evaluerPourTortue(JardinHandler& jardin, int tortueIndex) const;
};

using ConditionPtr = std::shared_ptr<Condition>;
