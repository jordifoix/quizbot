grammar Enquestes;


root : (pregunta | resposta | alternativa | item | enquesta)+ end ;


pregunta : identifier COL PREGUNTA text QUE ;
resposta : identifier COL RESPOSTA opcioResposta+ ;
item : identifier COL ITEM itemLink ;
alternativa : identifier COL ALTERNATIVA identifier (altLink | altLinkArray) ;
enquesta : identifier COL ENQUESTA identifier+ ;
end : END EOF;

opcioResposta : NUM COL text SCOL ;
altLinkArray : LBR altLink (COMMA altLink)* RBR ;
altLink : LPAR NUM COMMA identifier RPAR ;
itemLink : identifier ARROW identifier ;

text : ( NUM | WORD | ID )+ ;
identifier : ID ;

PREGUNTA : 'PREGUNTA' ;
RESPOSTA : 'RESPOSTA' ;
ITEM : 'ITEM' ;
ALTERNATIVA : 'ALTERNATIVA' ;
ENQUESTA : 'ENQUESTA' ;
END : 'END' ;

COM : ('//') ~'\n'* -> channel(HIDDEN);
BSL : '//' ;
QUE   : '?' ;
COL  : ':' ;
SCOL : ';' ;
COMMA : ',' ;
LBR : '[' ;
RBR : ']' ;
LPAR : '(' ;
RPAR : ')' ;
ARROW : '->' ;

ID : [a-zA-Z][a-zA-Z0-9\u0080-\u00FF]* ;
NUM : [0-9]+ ;
WORD : [A-Za-z0-9\u00C0-\u00FF]+ ;

WS: [ \n\t]+ -> skip;
