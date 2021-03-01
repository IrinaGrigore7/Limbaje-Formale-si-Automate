# Generated from Regex.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

from RegexVisitor import RegexVisitor
from typing import List, Tuple, Set, Dict

State = int



# This class defines a complete generic visitor for a parse tree produced by RegexParser.
class NFA:
    def __init__(self, numberOfStates: int, finalState: int,
                 delta: [Tuple[State, chr, State]]):
        self.numberOfStates = numberOfStates
       # self.states = set(range(self.numberOfStates))
        self.initialState = 0
        self.finalState = finalState
        self.delta = delta
    #def concatNFA(self, nfa1, nfa2):

class RegexVisitorEval(RegexVisitor):

    # Visit a parse tree produced by RegexParser#expr.
    def visitExpr(self, ctx:RegexParser.ExprContext):
        expr1 = ctx.and_expr()
        expr2 = ctx.expr()
        if(expr2):
            expr2_1 = self.visit(expr1)
            expr2_2 = self.visit(expr2)
            numberOfStates = expr2_1.numberOfStates + expr2_2.numberOfStates + 2
            finalState = numberOfStates - 1
            finalState1 = expr2_1.numberOfStates
            initialState2 = expr2_1.numberOfStates + 1
            numberOfStates2 = expr2_2.numberOfStates
            deltaAux1 = [(0, "eps", 1)]

            for (state, char, nextState) in expr2_1.delta:
                deltaAux1 = deltaAux1 + [(state + 1, char, nextState + 1)]
            deltaAux2 = []
            for (state, char, nextState) in expr2_2.delta:
                finalState2 = nextState + initialState2
                deltaAux2 = deltaAux2 + [(state + initialState2, char, nextState + initialState2)]

            delta = deltaAux1 + [(0, "eps", initialState2)] + [(finalState1, "eps", finalState)] + deltaAux2 + [(finalState2, "eps", finalState)]
            return NFA(numberOfStates, finalState, delta)
        else:
            return self.visit(expr1)

    # Visit a parse tree produced by RegexParser#and_expr.
    def visitAnd_expr(self, ctx:RegexParser.And_exprContext):
        expr1 = ctx.star_expr()
        expr2 = ctx.and_expr()
        
        if(expr2):
            expr2_1 = self.visit(expr1)
            expr2_2 = self.visit(expr2)
            delta1 = expr2_1.delta
            finalState1 = expr2_1.numberOfStates - 1
            numberOfStates = expr2_1.numberOfStates + expr2_2.numberOfStates - 1
            finalState2 = expr2_2.numberOfStates - 1
            deltaAux = []
            for (state, char, nextState) in expr2_2.delta:
                deltaAux = deltaAux + [(state + finalState1, char, nextState + finalState1)]
            delta = delta1 + deltaAux
            return NFA(numberOfStates, finalState2, delta1 + deltaAux)
        else:
            return self.visit(expr1)

    # Visit a parse tree produced by RegexParser#star_expr.
    def visitStar_expr(self, ctx:RegexParser.Star_exprContext):
        expr1 = ctx.atom()
        expr2 = ctx.star_expr()
        if(expr2):
            expr2_1 = self.visit(expr2)
            numberOfStates = expr2_1.numberOfStates + 2
            finalState = numberOfStates - 1
            delta = [(0, "eps", 1)]
            initialState1 = expr2_1.initialState + 1
            finalState1 = expr2_1.numberOfStates 
            for (state, char, nextState) in expr2_1.delta:
                delta = delta + [(state + 1, char, nextState + 1)] 
            delta = delta + [(finalState1, "eps", initialState1)] + [(finalState1, "eps", finalState1 + 1)] + [(0, "eps", finalState1 + 1)]
            return NFA(numberOfStates, finalState, delta)
        else: 
            return self.visit(expr1)

    # Visit a parse tree produced by RegexParser#atom.
    def visitAtom(self, ctx:RegexParser.AtomContext):
        expr1 = ctx.variable()
        expr2 = ctx.inner_expr()
        if(expr1):
            return self.visit(expr1)
        else:
            return self.visit(expr2)


    # Visit a parse tree produced by RegexParser#variable.
    def visitVariable(self, ctx:RegexParser.VariableContext):
        return NFA(2, 1, [(0, str(ctx.VAR()), 1)])

    # Visit a parse tree produced by RegexParser#inner_expr.
    def visitInner_expr(self, ctx:RegexParser.Inner_exprContext):
        expr = ctx.expr()
        return self.visit(expr)



del RegexParser