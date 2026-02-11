/*#include "jardinHandler.hh"
#include <fstream>

JardinHandler::JardinHandler(JardinRendering * J, QObject *parent)
    : QThread(parent)
{
    restart = false;
    abort = false;
    driver = new Driver(this); 
    scanner = new Scanner(&std::cin, &std::cout);
    parser = new yy::Parser(*scanner, *driver);
    jardin = J;
}

JardinHandler::~JardinHandler()
{
    mutex.lock();
    abort = true;
    condition.wakeOne();
    mutex.unlock();

    wait();

    delete driver;
    delete scanner;
    delete parser;
}

void JardinHandler::parsingJardin()
{
    QMutexLocker locker(&mutex);

    if (!isRunning()) {
        start(LowPriority);
    } else {
        restart = true;
        condition.wakeOne();
    }
}

void JardinHandler::dessiner(){
    first = true;
}

void JardinHandler::run()
{
    if (first) {
        first = false;
        mutex.lock();
	
        parser->parse();

        mutex.unlock();
        emit parse();
        //emit parsingFinish();
    }
}

void JardinHandler::avancer(unsigned int id, int nbPas) {
    for (int i = 0; i < nbPas; ++i) {
        tortues[id].avancer();  
    }
}


void JardinHandler::avancerToutes(int nbPas) {
    for (unsigned int id = 0; id < tortues.size(); ++id) {
        avancer(id, nbPas);
    }
}

void JardinHandler::avancer(unsigned int id, int nbPas) {
    (void)id; (void)nbPas;
}
void JardinHandler::avancerToutes(int nbPas) {
    (void)nbPas;
}

*/
#include "jardinHandler.hh"
#include <fstream>

JardinHandler::JardinHandler(JardinRendering * J, QObject *parent)
    : QThread(parent)
{
    restart = false;
    abort = false;
    driver = new Driver(this);
    scanner = new Scanner(&std::cin, &std::cout); 
    parser = new yy::Parser(*scanner, *driver);
    jardin = J;
}

JardinHandler::~JardinHandler()
{
    mutex.lock();
    abort = true;
    condition.wakeOne();
    mutex.unlock();

    wait();

    delete driver;
    delete scanner;
    delete parser;
}

void JardinHandler::parsingJardin()
{
    QMutexLocker locker(&mutex);

    if (!isRunning()) {
        start(LowPriority);
    } else {
        restart = true;
        condition.wakeOne();
    }
}

void JardinHandler::dessiner(){
    first = true;
}

void JardinHandler::run()
{
    if (first) {
        first = false;
        mutex.lock();

        parser->parse();

        mutex.unlock();
        emit parse();
    }
}

void JardinHandler::avancer(unsigned int id, int nbPas) {
    (void)id;
    (void)nbPas;
}

void JardinHandler::avancerToutes(int nbPas) {
    (void)nbPas;
}
