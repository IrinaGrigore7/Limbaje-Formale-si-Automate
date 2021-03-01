grammar Regex;


OR: '|';
STAR: '*';
OPEN: '(';
CLOSED: ')';
VAR: ([a-z]);

expr: and_expr | and_expr OR expr;
and_expr: star_expr | star_expr and_expr;
star_expr: atom | star_expr STAR;
atom: variable | inner_expr;
variable: VAR;
inner_expr: OPEN expr CLOSED;