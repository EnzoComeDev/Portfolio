%{

#include <string>
#include "scanner.hh"


#undef YY_DECL
#define YY_DECL int Scanner::yylex(yy::Parser::semantic_type * const lval, yy::Parser::location_type *loc)

using token = yy::Parser::token;

/* update location on matching */
#define YY_USER_ACTION loc->step(); loc->columns(yyleng);
%}

%option c++
%option yyclass="Scanner"
%option noyywrap

%%

%{
    yylval = lval;
%}

[ \t]+          { /* ignore whitespace */ }

"--"[^\n]*      { /* ignore comments until end of line */ }

\n              { loc->lines(); return token::NL; }

"avance"        { return token::AVANCE; }
"recule"        { return token::RECULE; }
"saute"         { return token::SAUTE; }
"sauter"        { return token::SAUTE; }
"tourne"        { return token::TOURNE; }

"si"            { return token::SI; }
"sinon"         { return token::SINON; }
"fin"[ \t]+"si" { return token::FIN_SI; }

"tant"[ \t]+"que" { return token::TANT_QUE; }
"fin"[ \t]+"tant"[ \t]+"que" { return token::FIN_TANT_QUE; }

"repete"        { return token::REPETE; }
"fin"[ \t]+"repete" { return token::FIN_REPETE; }

"fonction"      { return token::FONCTION; }
"fin"[ \t]+"fonction" { return token::FIN_FONCTION; }

"pas"[ \t]+"de" { return token::PAS_DE; }

"mur"           { return token::MUR; }
"vide"          { return token::VIDE; }

"couleur"       { return token::COULEUR; }
"tortues"       { return token::TORTUES; }
"dessiner"      { return token::DESSINER; }

"a"[ \t]+"gauche"|"à"[ \t]+"gauche" { return token::A_GAUCHE; }
"a"[ \t]+"droite"|"à"[ \t]+"droite" { return token::A_DROITE; }
"devant"        { return token::DEVANT; }
"derriere"|"derrière" { return token::DERRIERE; }

"jardin"        { return token::JARDIN; }
"end"           { return token::END; }

"fois"          { return token::FOIS; }

"#"[0-9A-Fa-f]{6} { yylval->build<std::string>(yytext); return token::COULEUR_HEX; }

\"[^\"]*\"|'[^']*'      {
    std::string str(yytext + 1, yyleng - 2);
    yylval->build<std::string>(str);
    return token::CHAINE;
}

[0-9]+          { yylval->build<int>(std::stoi(yytext)); return token::ENTIER; }

"@"             { return token::AROBASE; }
"$"             { return token::DOLLAR; }
":"             { return token::DEUX_POINTS; }
"("             { return token::PAR_OUV; }
")"             { return token::PAR_FERM; }
"+"             { return token::PLUS; }
"*"             { return token::MUL; }
"/"             { return token::DIV; }
"-"             { return token::MOINS; }

[a-zA-Z_][a-zA-Z0-9_]* { yylval->build<std::string>(yytext); return token::IDENTIFIANT; }

<<EOF>>         { return token::END_OF_FILE; }

.               { std::cerr << "Caractère inconnu : " << yytext << std::endl; }

%%
