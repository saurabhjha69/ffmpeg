% Likes facts
likes(mary, wine).
likes(bob, beer).
likes(vini, apple).
likes(charlie, wine).

% Rule: John likes whatever X likes if X likes wine
likes(john, X) :- likes(X, wine).

% Female and male facts
female(pammi).
female(lizza).
female(patty).
female(anny).

male(jimmy).
male(bobby).
male(tomy).
male(pitter).

% Parent relationships
parent(pammi, bobby).
parent(tomy, bobby).
parent(bobby, anny).
parent(patty, pitter).
parent(pitter, jimmy).

% Rules for family relationships
mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).

% X has at least one child
haschild(X) :- parent(X, _).

% Sister relationship: X and Y share the same parent, and X is female
sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X \== Y.

% Brother relationship: X and Y share the same parent, and X is male
brother(X, Y) :- parent(Z, X), parent(Z, Y), male(X), X \== Y.
