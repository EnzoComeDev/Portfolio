%skeleton "lalr1.cc"
%require "3.0"

%defines
%define api.parser.class { Parser }
%define api.value.type variant
%define parse.assert

%locations

%code requires {
    #include "Avance.hh"
    #include "Recule.hh"
    #include "Saute.hh"
    #include "Tourne.hh"
    #include "Couleur.hh"
    #include "Dessiner.hh"
    #include "Si.hh"
    #include "TantQue.hh"
    #include "Repete.hh"
    #include "Condition.hh"
    #include "contexte.hh"
    #include "expressionBinaire.hh"
    #include "expressionUnaire.hh"
    #include "constante.hh"
    #include "variable.hh"
    #include "Instruction.hh"
    #include <vector>

    using ExpressionPtr = std::shared_ptr<Expression>;
    using InstructionPtr = std::shared_ptr<Instruction>;

    class Scanner;
    class Driver;
}

%parse-param { Scanner &scanner }
%parse-param { Driver &driver }

%code{
    #include <iostream>
    #include <string>

    #include "scanner.hh"
    #include "driver.hh"

    #undef  yylex
    #define yylex scanner.yylex
}

%token                  NL
%token                  END
%token                  END_OF_FILE
%token                  DIRECTION
%token                  JARDIN
%token <std::string>    CHAINE
%token                  AVANCE
%token                  TOURNE
%token                  RECULE
%token                  SAUTE
%token                  SI SINON FIN_SI
%token                  TANT_QUE FIN_TANT_QUE
%token                  REPETE FIN_REPETE
%token                  FONCTION FIN_FONCTION
%token                  MUR VIDE PAS_DE
%token                  FOIS
%token                  COULEUR TORTUES DESSINER
%token                  A_GAUCHE A_DROITE DEVANT DERRIERE
%token                  AROBASE DOLLAR DEUX_POINTS
%token                  PAR_OUV PAR_FERM PLUS MOINS MUL DIV
%token <std::string>    COULEUR_HEX IDENTIFIANT
%token <int>            ENTIER

%type <InstructionPtr>  instruction
%type <ExpressionPtr>   expression expression_opt
%type <int>             fois_opt at_opt
%type <std::string>     direction
%type <ConditionPtr>    condition
%type <Bloc>            bloc_instructions
%type <TypeCondition>   type_condition
%type <bool>            negation_opt
%type <std::vector<ExpressionPtr>> liste_args

%left PLUS MOINS
%left MUL DIV

%%

programme:
    /* vide */
    | programme instruction NL {
          driver.ajouterInstruction($2);
      }
    | programme NL {
          /* ligne vide ou commentaire*/
      }
    | programme JARDIN CHAINE NL {
          driver.nouveauJardin($3);
      }
    | programme FONCTION IDENTIFIANT DEUX_POINTS NL bloc_instructions FIN_FONCTION NL {
          driver.definirFonction($3, $6);
      }
    | programme END NL {
          std::cout << "Fin de programme rencontrée" << std::endl;
          driver.executerProgramme();
          driver.dessiner();
          YYACCEPT;
      }
    | programme END_OF_FILE {
          std::cout << "Fin de fichier rencontrée" << std::endl;
          driver.executerProgramme();
          YYACCEPT;
      }
    ;

instruction
    : AVANCE expression_opt fois_opt at_opt {
          ExpressionPtr expr = $2 ? $2 : std::make_shared<Constante>(1);
          $$ = std::make_shared<Avance>(expr, $3, $4);
      }
    | RECULE expression_opt fois_opt at_opt {
          ExpressionPtr expr = $2 ? $2 : std::make_shared<Constante>(1);
          $$ = std::make_shared<Recule>(expr, $3, $4);
      }
    | SAUTE expression_opt fois_opt at_opt {
          ExpressionPtr expr = $2 ? $2 : std::make_shared<Constante>(1);
          $$ = std::make_shared<Saute>(expr, $3, $4);
      }
    | TOURNE direction fois_opt at_opt {
          $$ = std::make_shared<Tourne>($2, $3, $4);
      }
    | COULEUR COULEUR_HEX at_opt {
          $$ = std::make_shared<Couleur>($2, $3);
      }
    | TORTUES ENTIER {
          driver.setNombreTortues($2);
          $$ = nullptr;
      }
    | DESSINER {
          $$ = std::make_shared<Dessiner>();
      }
    | SI condition DEUX_POINTS NL bloc_instructions FIN_SI {
          $$ = std::make_shared<Si>($2, $5);
      }
    | SI condition DEUX_POINTS NL bloc_instructions SINON DEUX_POINTS NL bloc_instructions FIN_SI {
          $$ = std::make_shared<Si>($2, $5, $9);
      }
    | TANT_QUE condition DEUX_POINTS NL bloc_instructions FIN_TANT_QUE {
          $$ = std::make_shared<TantQue>($2, $5);
      }
    | REPETE expression fois_opt DEUX_POINTS NL bloc_instructions FIN_REPETE {
          ExpressionPtr nb = std::make_shared<ExpressionBinaire>(
              $2,
              std::make_shared<Constante>($3),
              OperateurBinaire::multiplie
          );
          $$ = std::make_shared<Repete>(nb, $6);
      }
    | IDENTIFIANT liste_args {
          $$ = driver.appelFonction($1, $2);
      }
    ;

bloc_instructions:
    /* rien */ {
        $$ = Bloc();
    }
    | bloc_instructions instruction NL {
        $$ = $1;
        if ($2 != nullptr) {
            $$.push_back($2);
        }
    }
    | bloc_instructions NL {
        $$ = $1;
    }
    ;

liste_args:
    /* vide */ {
        $$ = std::vector<ExpressionPtr>();
    }
    | liste_args expression {
        $$ = $1;
        $$.push_back($2);
    }
    ;

condition:
    negation_opt type_condition at_opt {
        $$ = std::make_shared<Condition>($2, $1, $3);
    }
    ;

negation_opt:
    /* vide */ { $$ = false; }
    | PAS_DE { $$ = true; }
    ;

type_condition:
    MUR DEVANT { $$ = TypeCondition::MUR_DEVANT; }
    | MUR DERRIERE { $$ = TypeCondition::MUR_DERRIERE; }
    | MUR A_GAUCHE { $$ = TypeCondition::MUR_GAUCHE; }
    | MUR A_DROITE { $$ = TypeCondition::MUR_DROITE; }
    | VIDE DEVANT { $$ = TypeCondition::VIDE_DEVANT; }
    | VIDE DERRIERE { $$ = TypeCondition::VIDE_DERRIERE; }
    | VIDE A_GAUCHE { $$ = TypeCondition::VIDE_GAUCHE; }
    | VIDE A_DROITE { $$ = TypeCondition::VIDE_DROITE; }
    ;

direction:
    A_GAUCHE    { $$ = "gauche"; }
    | A_DROITE  { $$ = "droite"; }
    | DEVANT    { $$ = "devant"; }
    | DERRIERE  { $$ = "derriere"; }
    ;

expression_opt:
    /* vide */ { $$ = nullptr; }
    | expression { $$ = $1; }
    ;

fois_opt:
    /* vide */     { $$ = 1; }
    | ENTIER FOIS  { $$ = $1; }
    | ENTIER       { $$ = $1; }
    | FOIS         { $$ = 1; }
    ;

at_opt:
    /* vide */     { $$ = 0; }
    | AROBASE ENTIER { $$ = $2; }
    ;

expression:
    ENTIER                        { $$ = std::make_shared<Constante>($1); }
    | DOLLAR ENTIER               { $$ = driver.getArgument($2); }
    | PAR_OUV expression PAR_FERM { $$ = $2; }
    | expression PLUS expression  { $$ = std::make_shared<ExpressionBinaire>($1, $3, OperateurBinaire::plus); }
    | expression MOINS expression { $$ = std::make_shared<ExpressionBinaire>($1, $3, OperateurBinaire::moins); }
    | expression MUL expression   { $$ = std::make_shared<ExpressionBinaire>($1, $3, OperateurBinaire::multiplie); }
    | expression DIV expression   { $$ = std::make_shared<ExpressionBinaire>($1, $3, OperateurBinaire::divise); }
    | MOINS expression %prec MOINS { $$ = std::make_shared<ExpressionUnaire>($2, OperateurUnaire::neg); }
    ;

%%

void yy::Parser::error(const location_type &l, const std::string & err_msg) {
    std::cerr << "Erreur : " << l << ", " << err_msg << std::endl;
}
