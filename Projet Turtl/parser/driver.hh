#ifndef DRIVER_HH
#define DRIVER_HH

#include <string>
#include <vector>
#include <map>
#include <memory>
#include "contexte.hh"
#include "expression.hh"

class JardinHandler;
class JardinRendering;
class Instruction;

using InstructionPtr = std::shared_ptr<Instruction>;
using ExpressionPtr = std::shared_ptr<Expression>;
using Bloc = std::vector<InstructionPtr>;

class Driver {
private:
    JardinHandler* monJardin;
    Contexte variables;
    std::vector<InstructionPtr> instructions;
    std::map<std::string, Bloc> fonctions;
    std::vector<ExpressionPtr> argumentsCourants;

public:
    Driver(JardinHandler* J);
    ~Driver();

    const Contexte& getContexte() const;
    double getVariable(const std::string& name) const;
    void setVariable(const std::string& name, double value);

    JardinRendering* getJardin();
    void dessiner();

    void changerPositionTortue0(int x, int y);
    float obtenirOrientationTortue0();

    void nouveauJardin(std::string nomJardin);
    void setNombreTortues(int n);

    void ajouterInstruction(InstructionPtr inst);
    void executerProgramme();

    void definirFonction(const std::string& nom, const Bloc& corps);
    InstructionPtr appelFonction(const std::string& nom, const std::vector<ExpressionPtr>& args);
    ExpressionPtr getArgument(int n);
};

#endif
