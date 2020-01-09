# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
import matplotlib.pyplot as plt
import networkx as nx
import pickle
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.

class EnquestesVisitor(ParseTreeVisitor):

    def isQuestionId(self, id):
        return id in self.ids and self.ids[id]["type"] == "question"

    def isAnswerId(self, id):
        return id in self.ids and self.ids[id]["type"] == "answer"

    def isItemId(self, id):
        return id in self.ids and self.ids[id]["type"] == "item"


    def setup(self):
        self.G = nx.DiGraph()
        self.questions = {}
        self.ids = {}
        try:
            self.questions = pickle.load(
                open("./data/questions.p", "rb"))
        except FileNotFoundError:
            self.questions = {}
            pickle.dump(self.questions, open(
                "./data/questions.p", "wb"))
        try:
            self.G = pickle.load(open("./data/graph.p", "rb"))
        except FileNotFoundError:
            self.G = nx.DiGraph()
            pickle.dump(self.G, open("./data/graph.p", "wb"))

        nodes = self.G.nodes
        edges = self.G.edges

        for nodeId in nodes:
            nodeInformation = self.G.nodes[nodeId]
            nodeType = nodeInformation["type"]
            if nodeType == 'question':
                self.ids[nodeId] = {"type": nodeType}
            elif nodeType == 'answer':
                self.ids[nodeId] = {"type": nodeType}
            elif nodeType == 'quiz':
                self.ids[nodeId] = {"type": nodeType}

        for edge in edges:
            edgeInformation = self.G.edges[edge]
            edgeType = edgeInformation["type"]
            if edgeType == "alternative":
                alternativeId = edgeInformation["alternativeId"]
                self.ids[alternativeId] = {"type": edgeType}
            elif edgeType == "item":
                itemId = edgeInformation["label"]
                questionId, answerId = edge
                self.ids[itemId] = {"type": edgeType,
                                    "question": questionId, "answer": answerId}


    def finish(self):
        pos = nx.spring_layout(self.G)
        E = self.G.edges()
        Ecolors = []
        Elabels = {}
        for u, v in E:
            type = self.G[u][v]["type"]
            Elabels[(u, v)] = self.G[u][v]["label"]
            if type == "item":
                Ecolors.append("#0000ff")
            elif type == "alternative":
                Ecolors.append("#00ff00")
            elif type == "quiz" or type == "end":
                Ecolors.append("#000000")
                Elabels[(u, v)] = ""

        nx.draw(self.G, pos, edge_color=Ecolors, with_labels=True)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=Elabels)
        plt.savefig("./data/quiz_graph.png")
        plt.show()

        pickle.dump(self.G, open("./data/graph.p", "wb"))
        pickle.dump(self.questions, open("./data/questions.p", "wb"))



    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        self.setup()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#pregunta.
    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
        identifier = self.visit(ctx.identifier())
        if not identifier in self.ids:
            self.ids[identifier] = {"type": "question"}
            questionText = self.visit(ctx.text())
            self.G.add_node(identifier, type="question",
                            question=questionText, quizzes={})
            self.questions[identifier] = {}
        return


    # Visit a parse tree produced by EnquestesParser#resposta.
    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        identifier = self.visit(ctx.identifier())
        if identifier not in self.ids:
            self.ids[identifier] = {
                "type": "answer"
            }
            answers = {}
            children = ctx.getChildren()
            n = ctx.getChildCount()
            tokens = [next(children) for i in range(n)]
            for i in range(len(tokens))[3:]:
                answerNum, optionText = self.visit(tokens[i])
                answers[answerNum] = optionText
                self.G.add_node(identifier, type="answer", answers=answers)
        return


    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        itemId = self.visit(ctx.identifier())
        questionId, answerId = self.visit(ctx.itemLink())
        if self.isQuestionId(questionId) and self.isAnswerId(answerId) and itemId not in self.ids:
            self.ids[itemId] = {
                "type": "item",
                "question": questionId,
                "answer": answerId
            }
            self.G.add_edge(questionId, answerId, label=itemId, type="item")
            answer = self.G.nodes[answerId]["answers"]
            for option in answer:
                self.questions[questionId][option] = 0
        else:
            # missatge derror
            pass


    # Visit a parse tree produced by EnquestesParser#alternativa.
    def visitAlternativa(self, ctx:EnquestesParser.AlternativaContext):
        children = ctx.getChildren()
        tokens = [next(children) for i in range(ctx.getChildCount())]

        identifier = self.visit(tokens[0])

        if identifier not in self.ids:
            self.ids[identifier] = {"type": "alternative"}

            sourceItemId = self.visit(tokens[3])

            if self.isItemId(sourceItemId):
                sourceQuestionId = self.ids[sourceItemId]["question"]
                alternatives = self.visit(tokens[4])

                if isinstance(alternatives, list):
                    for alternative in alternatives:
                        answerNum = alternative["answerNum"]
                        itemId = alternative["itemId"]
                        if self.isItemId(itemId):
                            questionId = self.ids[itemId]["question"]
                            answerId = self.ids[itemId]["answer"]
                            self.G.add_edge(sourceQuestionId, questionId, label=answerNum,
                                            type="alternative", alternativeId=identifier, answerId=answerId)
                else:
                    answerNum, itemId = alternatives
                    if self.isItemId(itemId):
                        questionId = self.ids[itemId]["question"]
                        answerId = self.ids[itemId]["answer"]
                        self.G.add_edge(sourceQuestionId, questionId, label=answerNum,
                                        type="alternative", alternativeId=identifier, answerId=answerId)
            else:
                # error message
                pass
        return


    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx:EnquestesParser.EnquestaContext):
        children = ctx.getChildren()
        tokens = [next(children) for i in range(ctx.getChildCount())]
        identifier = self.visit(tokens[0])
        if identifier not in self.ids:
            self.ids[identifier] = {"type": "quiz"}
            items = []
            count = 0
            for i in range(len(tokens))[3:]:
                count += 1
                itemId = self.visit(tokens[i])
                if self.isItemId(itemId):
                    items.append(itemId)
            if count == len(items):
                self.G.add_node(identifier, type="quiz")
                previousQ = identifier
                for itemId in items:
                    question = self.ids[itemId]["question"]
                    self.G.add_edge(previousQ, question, type="quiz",
                                    quizzes={identifier: None}, label=identifier)
                    self.G.nodes[question]["quizzes"][identifier] = self.ids[itemId]["answer"]
                    previousQ = question
                self.G.add_node("END", type="end")
                self.G.add_edge(previousQ, "END", type="quiz", quizzes={
                    identifier: None}, label=identifier)
            else:
                # error message
                pass

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#end.
    def visitEnd(self, ctx:EnquestesParser.EndContext):
        self.finish()



    # Visit a parse tree produced by EnquestesParser#opcioResposta.
    def visitOpcioResposta(self, ctx:EnquestesParser.OpcioRespostaContext):
        answerNum = str(ctx.NUM())
        return (answerNum, self.visit(ctx.text()))


    # Visit a parse tree produced by EnquestesParser#altLinkArray.
    def visitAltLinkArray(self, ctx:EnquestesParser.AltLinkArrayContext):
        children = ctx.getChildren()
        tokens = [next(children) for i in range(ctx.getChildCount())]
        alternatives = []
        for i in range(len(tokens)):
            if i % 2 == 1:
                answerNum, itemId = self.visit(tokens[i])
                alternatives.append({
                    "answerNum": answerNum,
                    "itemId": itemId
                })
        return alternatives


    # Visit a parse tree produced by EnquestesParser#altLink.
    def visitAltLink(self, ctx:EnquestesParser.AltLinkContext):
        children = ctx.getChildren()
        tokens = [next(children) for i in range(ctx.getChildCount())]
        answerNum = str(tokens[1])
        identifier = self.visit(tokens[3])
        return (answerNum, identifier)


    # Visit a parse tree produced by EnquestesParser#itemLink.
    def visitItemLink(self, ctx:EnquestesParser.ItemLinkContext):
        children = ctx.getChildren()
        tokens = [next(children) for i in range(3)]
        return self.visit(tokens[0]), self.visit(tokens[2])


    # Visit a parse tree produced by EnquestesParser#text.
    def visitText(self, ctx:EnquestesParser.TextContext):
        text = ""
        children = ctx.getChildren()
        fst = True
        for i in range(ctx.getChildCount()):
            word = next(children)
            if fst:
                fst = False
                text = str(word)
            else:
                text += f" {word}"
        return text


    # Visit a parse tree produced by EnquestesParser#identifier.
    def visitIdentifier(self, ctx:EnquestesParser.IdentifierContext):
        return ctx.getText()


del EnquestesParser