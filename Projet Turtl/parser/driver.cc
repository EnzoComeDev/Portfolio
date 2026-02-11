#include "driver.hh"
#include "jardinHandler.hh"
#include "Instruction.hh"
#include "constante.hh"
#include <iostream>

Driver::Driver(JardinHandler * J) {
    monJardin = J;
}

Driver::~Driver() {
    delete monJardin;
}

const Contexte& Driver::getContexte() const {
    return variables;
}

double Driver::getVariable(const std::string & name) const {
    return variables.get(name);
}

void Driver::setVariable(const std::string & name, double value) {
    variables[name] = value;
}

JardinRendering * Driver::getJardin() {
    return monJardin->getJardin();
}

void Driver::dessiner(){
    monJardin->dessiner();
}

void Driver::changerPositionTortue0(int x, int y) {
    getJardin()->changePosition(0,x,y);
}

float Driver::obtenirOrientationTortue0() {
    return getJardin()->orientation(1);
}

void Driver::nouveauJardin(std::string nomJardin){
    getJardin()->construction(nomJardin);
}

void Driver::setNombreTortues(int n) {
    std::cout << "Nombre de tortues défini à " << n << std::endl;
    for (int i = 0; i < n; i++) {
        getJardin()->nouvelleTortue();
    }
}


void Driver::ajouterInstruction(InstructionPtr inst) {
    if (inst != nullptr) {
        instructions.push_back(inst);
    }
}

void Driver::executerProgramme() {
    std::cout << "Exécution de " << instructions.size() << " instructions..." << std::endl;
    for (const auto& inst : instructions) {
        inst->executer(*monJardin, variables);
    }
}


void Driver::definirFonction(const std::string& nom, const Bloc& corps) {
    fonctions[nom] = corps;
    std::cout << "Fonction '" << nom << "' définie avec " << corps.size() << " instructions" << std::endl;
}

InstructionPtr Driver::appelFonction(const std::string& nom, const std::vector<ExpressionPtr>& args) {
    if (fonctions.find(nom) == fonctions.end()) {
        std::cerr << "Erreur : Fonction '" << nom << "' non définie" << std::endl;
        return nullptr;
    }
    auto anciensArgs = argumentsCourants;
    argumentsCourants = args;

    const Bloc& corps = fonctions[nom];
    for (const auto& inst : corps) {
        if (inst != nullptr) {
            inst->executer(*monJardin, variables);
        }
    }

    argumentsCourants = anciensArgs;
    return nullptr;
}

ExpressionPtr Driver::getArgument(int n) {
    if (n < 1 || n > (int)argumentsCourants.size()) {
        std::cerr << "Erreur : Argument $" << n << " n'existe pas (fonction appelée avec "
                  << argumentsCourants.size() << " arguments)" << std::endl;
        return std::make_shared<Constante>(0);
    }
    return argumentsCourants[n - 1];
}
