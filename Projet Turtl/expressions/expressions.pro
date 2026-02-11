TEMPLATE = lib
CONFIG += staticlib

INCLUDEPATH += ../build
INCLUDEPATH += ../parser
INCLUDEPATH += ../GUI

HEADERS += ./constante.hh \
           ./contexte.hh \
           ./expression.hh \
           ./expressionBinaire.hh \
           ./expressionTernaire.hh \
           ./expressionUnaire.hh \
           ./variable.hh \
           ./Instruction.hh \
           ./Avance.hh \
           ./Recule.hh \
           ./Saute.hh \
           ./Tourne.hh \
           ./Couleur.hh \
           ./Dessiner.hh \
           ./Condition.hh \
           ./Si.hh \
           ./TantQue.hh \
           ./Repete.hh

SOURCES += ./constante.cc \
           ./contexte.cc \
           ./expressionBinaire.cc \
           ./expressionTernaire.cc \
           ./expressionUnaire.cc \
           ./variable.cc \
           ./Avance.cc \
           ./Recule.cc \
           ./Saute.cc \
           ./Tourne.cc \
           ./Couleur.cc \
           ./Dessiner.cc \
           ./Condition.cc \
           ./Si.cc \
           ./TantQue.cc \
           ./Repete.cc

DEFINES += MAKE_TEST_LIB
QT += widgets
