# Generated from Regex.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\60\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\3\2\3\2\5\2\24\n\2\3\3\3\3\3\3\3\3\5\3\32\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\5\3\5")
        buf.write("\5\5(\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\2\3\6\b\2\4\6\b")
        buf.write("\n\f\2\2\2-\2\23\3\2\2\2\4\31\3\2\2\2\6\33\3\2\2\2\b\'")
        buf.write("\3\2\2\2\n)\3\2\2\2\f+\3\2\2\2\16\24\5\4\3\2\17\20\5\4")
        buf.write("\3\2\20\21\7\3\2\2\21\22\5\2\2\2\22\24\3\2\2\2\23\16\3")
        buf.write("\2\2\2\23\17\3\2\2\2\24\3\3\2\2\2\25\32\5\6\4\2\26\27")
        buf.write("\5\6\4\2\27\30\5\4\3\2\30\32\3\2\2\2\31\25\3\2\2\2\31")
        buf.write("\26\3\2\2\2\32\5\3\2\2\2\33\34\b\4\1\2\34\35\5\b\5\2\35")
        buf.write("\"\3\2\2\2\36\37\f\3\2\2\37!\7\4\2\2 \36\3\2\2\2!$\3\2")
        buf.write("\2\2\" \3\2\2\2\"#\3\2\2\2#\7\3\2\2\2$\"\3\2\2\2%(\5\n")
        buf.write("\6\2&(\5\f\7\2\'%\3\2\2\2\'&\3\2\2\2(\t\3\2\2\2)*\7\7")
        buf.write("\2\2*\13\3\2\2\2+,\7\5\2\2,-\5\2\2\2-.\7\6\2\2.\r\3\2")
        buf.write("\2\2\6\23\31\"\'")
        return buf.getvalue()


class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "OR", "STAR", "OPEN", "CLOSED", "VAR" ]

    RULE_expr = 0
    RULE_and_expr = 1
    RULE_star_expr = 2
    RULE_atom = 3
    RULE_variable = 4
    RULE_inner_expr = 5

    ruleNames =  [ "expr", "and_expr", "star_expr", "atom", "variable", 
                   "inner_expr" ]

    EOF = Token.EOF
    OR=1
    STAR=2
    OPEN=3
    CLOSED=4
    VAR=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self):
            return self.getTypedRuleContext(RegexParser.And_exprContext,0)


        def OR(self):
            return self.getToken(RegexParser.OR, 0)

        def expr(self):
            return self.getTypedRuleContext(RegexParser.ExprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = RegexParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.and_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.and_expr()
                self.state = 14
                self.match(RegexParser.OR)
                self.state = 15
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star_expr(self):
            return self.getTypedRuleContext(RegexParser.Star_exprContext,0)


        def and_expr(self):
            return self.getTypedRuleContext(RegexParser.And_exprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_and_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expr" ):
                return visitor.visitAnd_expr(self)
            else:
                return visitor.visitChildren(self)




    def and_expr(self):

        localctx = RegexParser.And_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_and_expr)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.star_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.star_expr(0)
                self.state = 21
                self.and_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Star_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(RegexParser.AtomContext,0)


        def star_expr(self):
            return self.getTypedRuleContext(RegexParser.Star_exprContext,0)


        def STAR(self):
            return self.getToken(RegexParser.STAR, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_star_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar_expr" ):
                return visitor.visitStar_expr(self)
            else:
                return visitor.visitChildren(self)



    def star_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegexParser.Star_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_star_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RegexParser.Star_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_star_expr)
                    self.state = 28
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 29
                    self.match(RegexParser.STAR) 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(RegexParser.VariableContext,0)


        def inner_expr(self):
            return self.getTypedRuleContext(RegexParser.Inner_exprContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = RegexParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegexParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.variable()
                pass
            elif token in [RegexParser.OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.inner_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(RegexParser.VAR, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = RegexParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(RegexParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inner_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(RegexParser.OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(RegexParser.ExprContext,0)


        def CLOSED(self):
            return self.getToken(RegexParser.CLOSED, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_inner_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInner_expr" ):
                return visitor.visitInner_expr(self)
            else:
                return visitor.visitChildren(self)




    def inner_expr(self):

        localctx = RegexParser.Inner_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inner_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(RegexParser.OPEN)
            self.state = 42
            self.expr()
            self.state = 43
            self.match(RegexParser.CLOSED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.star_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def star_expr_sempred(self, localctx:Star_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




