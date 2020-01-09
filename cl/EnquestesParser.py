# Generated from Enquestes.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\3\2\3\2\6\2\"\n\2\r\2\16\2#\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\6\4\62\n\4\r\4")
        buf.write("\16\4\63\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6A\n\6\3\7\3\7\3\7\3\7\6\7G\n\7\r\7\16\7H\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7\nW\n\n\f\n\16\n")
        buf.write("Z\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\r\6\ri\n\r\r\r\16\rj\3\16\3\16\3\16\2\2\17\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\2\3\3\2\24\26\2k\2!\3")
        buf.write("\2\2\2\4\'\3\2\2\2\6-\3\2\2\2\b\65\3\2\2\2\n:\3\2\2\2")
        buf.write("\fB\3\2\2\2\16J\3\2\2\2\20M\3\2\2\2\22R\3\2\2\2\24]\3")
        buf.write("\2\2\2\26c\3\2\2\2\30h\3\2\2\2\32l\3\2\2\2\34\"\5\4\3")
        buf.write("\2\35\"\5\6\4\2\36\"\5\n\6\2\37\"\5\b\5\2 \"\5\f\7\2!")
        buf.write("\34\3\2\2\2!\35\3\2\2\2!\36\3\2\2\2!\37\3\2\2\2! \3\2")
        buf.write("\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\5\16\b")
        buf.write("\2&\3\3\2\2\2\'(\5\32\16\2()\7\f\2\2)*\7\3\2\2*+\5\30")
        buf.write("\r\2+,\7\13\2\2,\5\3\2\2\2-.\5\32\16\2./\7\f\2\2/\61\7")
        buf.write("\4\2\2\60\62\5\20\t\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64\7\3\2\2\2\65\66\5\32\16\2\66")
        buf.write("\67\7\f\2\2\678\7\5\2\289\5\26\f\29\t\3\2\2\2:;\5\32\16")
        buf.write("\2;<\7\f\2\2<=\7\6\2\2=@\5\32\16\2>A\5\24\13\2?A\5\22")
        buf.write("\n\2@>\3\2\2\2@?\3\2\2\2A\13\3\2\2\2BC\5\32\16\2CD\7\f")
        buf.write("\2\2DF\7\7\2\2EG\5\32\16\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2")
        buf.write("\2HI\3\2\2\2I\r\3\2\2\2JK\7\b\2\2KL\7\2\2\3L\17\3\2\2")
        buf.write("\2MN\7\25\2\2NO\7\f\2\2OP\5\30\r\2PQ\7\r\2\2Q\21\3\2\2")
        buf.write("\2RS\7\17\2\2SX\5\24\13\2TU\7\16\2\2UW\5\24\13\2VT\3\2")
        buf.write("\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[\3\2\2\2ZX\3\2\2\2")
        buf.write("[\\\7\20\2\2\\\23\3\2\2\2]^\7\21\2\2^_\7\25\2\2_`\7\16")
        buf.write("\2\2`a\5\32\16\2ab\7\22\2\2b\25\3\2\2\2cd\5\32\16\2de")
        buf.write("\7\23\2\2ef\5\32\16\2f\27\3\2\2\2gi\t\2\2\2hg\3\2\2\2")
        buf.write("ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2k\31\3\2\2\2lm\7\24\2\2")
        buf.write("m\33\3\2\2\2\t!#\63@HXj")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PREGUNTA'", "'RESPOSTA'", "'ITEM'", 
                     "'ALTERNATIVA'", "'ENQUESTA'", "'END'", "<INVALID>", 
                     "'//'", "'?'", "':'", "';'", "','", "'['", "']'", "'('", 
                     "')'", "'->'" ]

    symbolicNames = [ "<INVALID>", "PREGUNTA", "RESPOSTA", "ITEM", "ALTERNATIVA", 
                      "ENQUESTA", "END", "COM", "BSL", "QUE", "COL", "SCOL", 
                      "COMMA", "LBR", "RBR", "LPAR", "RPAR", "ARROW", "ID", 
                      "NUM", "WORD", "WS" ]

    RULE_root = 0
    RULE_pregunta = 1
    RULE_resposta = 2
    RULE_item = 3
    RULE_alternativa = 4
    RULE_enquesta = 5
    RULE_end = 6
    RULE_opcioResposta = 7
    RULE_altLinkArray = 8
    RULE_altLink = 9
    RULE_itemLink = 10
    RULE_text = 11
    RULE_identifier = 12

    ruleNames =  [ "root", "pregunta", "resposta", "item", "alternativa", 
                   "enquesta", "end", "opcioResposta", "altLinkArray", "altLink", 
                   "itemLink", "text", "identifier" ]

    EOF = Token.EOF
    PREGUNTA=1
    RESPOSTA=2
    ITEM=3
    ALTERNATIVA=4
    ENQUESTA=5
    END=6
    COM=7
    BSL=8
    QUE=9
    COL=10
    SCOL=11
    COMMA=12
    LBR=13
    RBR=14
    LPAR=15
    RPAR=16
    ARROW=17
    ID=18
    NUM=19
    WORD=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end(self):
            return self.getTypedRuleContext(EnquestesParser.EndContext,0)


        def pregunta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.PreguntaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.PreguntaContext,i)


        def resposta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.RespostaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.RespostaContext,i)


        def alternativa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.AlternativaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.AlternativaContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ItemContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ItemContext,i)


        def enquesta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.EnquestaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.EnquestaContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = EnquestesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 26
                    self.pregunta()
                    pass

                elif la_ == 2:
                    self.state = 27
                    self.resposta()
                    pass

                elif la_ == 3:
                    self.state = 28
                    self.alternativa()
                    pass

                elif la_ == 4:
                    self.state = 29
                    self.item()
                    pass

                elif la_ == 5:
                    self.state = 30
                    self.enquesta()
                    pass


                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.ID):
                    break

            self.state = 35
            self.end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PreguntaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def COL(self):
            return self.getToken(EnquestesParser.COL, 0)

        def PREGUNTA(self):
            return self.getToken(EnquestesParser.PREGUNTA, 0)

        def text(self):
            return self.getTypedRuleContext(EnquestesParser.TextContext,0)


        def QUE(self):
            return self.getToken(EnquestesParser.QUE, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_pregunta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPregunta" ):
                return visitor.visitPregunta(self)
            else:
                return visitor.visitChildren(self)




    def pregunta(self):

        localctx = EnquestesParser.PreguntaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pregunta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.identifier()
            self.state = 38
            self.match(EnquestesParser.COL)
            self.state = 39
            self.match(EnquestesParser.PREGUNTA)
            self.state = 40
            self.text()
            self.state = 41
            self.match(EnquestesParser.QUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RespostaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def COL(self):
            return self.getToken(EnquestesParser.COL, 0)

        def RESPOSTA(self):
            return self.getToken(EnquestesParser.RESPOSTA, 0)

        def opcioResposta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpcioRespostaContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpcioRespostaContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_resposta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResposta" ):
                return visitor.visitResposta(self)
            else:
                return visitor.visitChildren(self)




    def resposta(self):

        localctx = EnquestesParser.RespostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_resposta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.identifier()
            self.state = 44
            self.match(EnquestesParser.COL)
            self.state = 45
            self.match(EnquestesParser.RESPOSTA)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.opcioResposta()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.NUM):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def COL(self):
            return self.getToken(EnquestesParser.COL, 0)

        def ITEM(self):
            return self.getToken(EnquestesParser.ITEM, 0)

        def itemLink(self):
            return self.getTypedRuleContext(EnquestesParser.ItemLinkContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.identifier()
            self.state = 52
            self.match(EnquestesParser.COL)
            self.state = 53
            self.match(EnquestesParser.ITEM)
            self.state = 54
            self.itemLink()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternativaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def COL(self):
            return self.getToken(EnquestesParser.COL, 0)

        def ALTERNATIVA(self):
            return self.getToken(EnquestesParser.ALTERNATIVA, 0)

        def altLink(self):
            return self.getTypedRuleContext(EnquestesParser.AltLinkContext,0)


        def altLinkArray(self):
            return self.getTypedRuleContext(EnquestesParser.AltLinkArrayContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_alternativa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternativa" ):
                return visitor.visitAlternativa(self)
            else:
                return visitor.visitChildren(self)




    def alternativa(self):

        localctx = EnquestesParser.AlternativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_alternativa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.identifier()
            self.state = 57
            self.match(EnquestesParser.COL)
            self.state = 58
            self.match(EnquestesParser.ALTERNATIVA)
            self.state = 59
            self.identifier()
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EnquestesParser.LPAR]:
                self.state = 60
                self.altLink()
                pass
            elif token in [EnquestesParser.LBR]:
                self.state = 61
                self.altLinkArray()
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

    class EnquestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def COL(self):
            return self.getToken(EnquestesParser.COL, 0)

        def ENQUESTA(self):
            return self.getToken(EnquestesParser.ENQUESTA, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_enquesta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnquesta" ):
                return visitor.visitEnquesta(self)
            else:
                return visitor.visitChildren(self)




    def enquesta(self):

        localctx = EnquestesParser.EnquestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_enquesta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.identifier()
            self.state = 65
            self.match(EnquestesParser.COL)
            self.state = 66
            self.match(EnquestesParser.ENQUESTA)
            self.state = 68 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 67
                    self.identifier()

                else:
                    raise NoViableAltException(self)
                self.state = 70 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EndContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(EnquestesParser.END, 0)

        def EOF(self):
            return self.getToken(EnquestesParser.EOF, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_end

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd" ):
                return visitor.visitEnd(self)
            else:
                return visitor.visitChildren(self)




    def end(self):

        localctx = EnquestesParser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(EnquestesParser.END)
            self.state = 73
            self.match(EnquestesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpcioRespostaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def COL(self):
            return self.getToken(EnquestesParser.COL, 0)

        def text(self):
            return self.getTypedRuleContext(EnquestesParser.TextContext,0)


        def SCOL(self):
            return self.getToken(EnquestesParser.SCOL, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_opcioResposta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcioResposta" ):
                return visitor.visitOpcioResposta(self)
            else:
                return visitor.visitChildren(self)




    def opcioResposta(self):

        localctx = EnquestesParser.OpcioRespostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opcioResposta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(EnquestesParser.NUM)
            self.state = 76
            self.match(EnquestesParser.COL)
            self.state = 77
            self.text()
            self.state = 78
            self.match(EnquestesParser.SCOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AltLinkArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBR(self):
            return self.getToken(EnquestesParser.LBR, 0)

        def altLink(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.AltLinkContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.AltLinkContext,i)


        def RBR(self):
            return self.getToken(EnquestesParser.RBR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.COMMA)
            else:
                return self.getToken(EnquestesParser.COMMA, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_altLinkArray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAltLinkArray" ):
                return visitor.visitAltLinkArray(self)
            else:
                return visitor.visitChildren(self)




    def altLinkArray(self):

        localctx = EnquestesParser.AltLinkArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_altLinkArray)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(EnquestesParser.LBR)
            self.state = 81
            self.altLink()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.COMMA:
                self.state = 82
                self.match(EnquestesParser.COMMA)
                self.state = 83
                self.altLink()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(EnquestesParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AltLinkContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(EnquestesParser.LPAR, 0)

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def COMMA(self):
            return self.getToken(EnquestesParser.COMMA, 0)

        def identifier(self):
            return self.getTypedRuleContext(EnquestesParser.IdentifierContext,0)


        def RPAR(self):
            return self.getToken(EnquestesParser.RPAR, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_altLink

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAltLink" ):
                return visitor.visitAltLink(self)
            else:
                return visitor.visitChildren(self)




    def altLink(self):

        localctx = EnquestesParser.AltLinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_altLink)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(EnquestesParser.LPAR)
            self.state = 92
            self.match(EnquestesParser.NUM)
            self.state = 93
            self.match(EnquestesParser.COMMA)
            self.state = 94
            self.identifier()
            self.state = 95
            self.match(EnquestesParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemLinkContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.IdentifierContext,i)


        def ARROW(self):
            return self.getToken(EnquestesParser.ARROW, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_itemLink

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemLink" ):
                return visitor.visitItemLink(self)
            else:
                return visitor.visitChildren(self)




    def itemLink(self):

        localctx = EnquestesParser.ItemLinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_itemLink)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.identifier()
            self.state = 98
            self.match(EnquestesParser.ARROW)
            self.state = 99
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.NUM)
            else:
                return self.getToken(EnquestesParser.NUM, i)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.WORD)
            else:
                return self.getToken(EnquestesParser.WORD, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_text

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = EnquestesParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 101
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EnquestesParser.ID) | (1 << EnquestesParser.NUM) | (1 << EnquestesParser.WORD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 104 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EnquestesParser.ID) | (1 << EnquestesParser.NUM) | (1 << EnquestesParser.WORD))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = EnquestesParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





