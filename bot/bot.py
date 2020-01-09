from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, ConversationHandler, Filters
from telegram import ParseMode
import networkx as nx 
import matplotlib.pyplot as plt
import pickle
from io import BytesIO


QUIZ = 1

onGoingQuizId = None
onGoingQuestion = None
answeredQuestions = {}
alternativeAnswerId = None
alternativeQuestion = None

G = None


# ------------------ auxiliar functions ------------------

def searchDestination(edges):
    alternatives = {}
    nextDestination = None
    for destination in edges:
        d = edges[destination]
        if (d['type'] == 'quiz' and onGoingQuizId in d['quizzes']):
            nextDestination = destination
        elif d['type'] == "alternative":
            alternatives[d['label']] = {
                "questionId": destination,
                "answerId": d['answerId']
            }
    return (alternatives, nextDestination)


def showQuestion(update, context, question, isAlternative, answerId):
    questionText = G.nodes[question]['question']
    if not isAlternative:
        answerId = G.nodes[question]['quizzes'][onGoingQuizId]
    else:
        global alternativeAnswerId
        global alternativeQuestion
        alternativeAnswerId = answerId
        alternativeQuestion = question
    answers = G.nodes[answerId]['answers']
    text = f'{onGoingQuizId}>{questionText}\n'
    for answerNum in answers:
        text += f'{answerNum}: {answers[answerNum]}\n'
    context.bot.send_message(
        chat_id=update.message.chat_id, text=text)


def getAnswers(idQuestion):
    questions = pickle.load(open("./data/questions.p", "rb"))
    labels = []
    values = []
    options = []
    i = 0
    answers = questions[idQuestion]
    for answerNum in answers:
        labels.append(answerNum)
        values.append(answers[answerNum])
        options.append(i)
        i += 1
    return (labels, values, options)



# ------------ Command Handlers -------------

def startHandler(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Hi there! I'm QuizBot. I can help you on answering and reviewing quizes."
        " Here's a list of my commands (more info with /help):\n"
            "  /start\n  /help\n  /author\n  /quiz <quizId>\n"
            "  /bar <QuestionId>\n  /pie <QuestionId>\n  /report"
    )


def helpHandler(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="I can help you interact with quizes in various ways.\n"
            "You can control me by sending these commands:\n\n"

            "Startup\n"
            "/start - start talking with me\n"
            "/help - display a list of all my commands and its usage/purpose\n"
            "/author - do you really wish to unveil my identity?\n\n"

            "Answering a Quiz\n"
            "/quiz <quizId> - Initiate an interpreter to go over the specified quiz interactively."
            " The user will be asked the questions of the quiz in their respective order,"
            " answering each time with the index corresponding to his answer's choice.\n\n"

            "Reports\n"
            "/bar <QuestionId> - show how many times each answer of the "
            "specified question has been chosen, on a bar diagram\n"
            "/pie <QuestionId> - show the percentages for each answer"
            "of the specified question, on a pie diagram\n"
            "/report - show a global report of every already picked answer,"
            " printing a row for each one that has been chosen at least"
            " once as the answer for a question. Each row is composed by "
            "the question's id, the index of the answer and its number of picks"
    )


def authorHandler(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Jordi Foix Esteve\njordi.foix@est.fib.upc.edu\njordifoixesteve@gmail.com"
    )


def barHandler(update, context):
    idQuestion = "".join(context.args[0])
    G = pickle.load(open("./data/graph.p", "rb"))

    if idQuestion in G:
        labels, values, options = getAnswers(idQuestion)

        fig, ax = plt.subplots()
        ax.bar(options, values)
        ax.set_xlabel("Opcions")
        ax.set_ylabel("Número de respostes")
        ax.set_title(f"Dades pregunta {idQuestion}")

        ax.set_xticks(options)
        ax.set_xticklabels(labels)
        buffer = BytesIO()
        fig.savefig(buffer, format='png')
        buffer.seek(0)
        context.bot.send_photo(chat_id=update.message.chat_id, photo=buffer)
    else:
        context.bot.send_message(
            chat_id=update.message.chat_id, text=f"La pregunta amb identificador '{idQuestion}' no existeix.")


def pieHandler(update, context):
    idQuestion = "".join(context.args[0])
    G = pickle.load(open("./data/graph.p", "rb"))

    if idQuestion in G:
        lab, val, options = getAnswers(idQuestion)
        values = []
        labels = []
        for i in range(len(val)):
            if val[i] > 0:
                values.append(val[i])
                labels.append(lab[i])
        fig, ax = plt.subplots()
        ax.set_ylim(bottom=0)
        ax.pie(values, labels=labels, autopct='%1.1f%%',
               shadow=True, startangle=90)

        buffer = BytesIO()
        fig.savefig(buffer, format='png')
        buffer.seek(0)
        context.bot.send_photo(chat_id=update.message.chat_id, photo=buffer)
    else:
        context.bot.send_message(
            chat_id=update.message.chat_id, text=f"La pregunta amb identificador '{idQuestion}' no existeix.")


def reportHandler(update, context):
    spaces = "   "
    text = f"*pregunta*{spaces}*valor*{spaces}*respostes*\n"

    questions = pickle.load(open("./data/questions.p", "rb"))
    for question in questions:
        q = questions[question]
        for answer in q:
            text += f"{question}{spaces}{answer}{spaces}{q[answer]}\n"

    context.bot.send_message(
        chat_id=update.message.chat_id, text=text, parse_mode=ParseMode.MARKDOWN)


# ------------ Conversation Handlers -------------

def quizHandler(update, context):
    quizId = "".join(context.args[0])
    global G
    G = pickle.load(open("./data/graph.p", "rb"))

    if quizId in G:
        global onGoingQuizId
        onGoingQuizId = quizId
        context.bot.send_message(
            chat_id=update.message.chat_id, text=f'Enquesta {onGoingQuizId}:')

        destinations = G[onGoingQuizId]

        global onGoingQuestion
        onGoingQuestion = list(destinations.keys())[0]

        showQuestion(update, context, onGoingQuestion, False, None)

        return QUIZ
    else:
        context.bot.send_message(
            chat_id=update.message.chat_id, text=f"L'enquesta amb identificador '{quizId}' no existeix.")
        return ConversationHandler.END


def quizAnswerHandler(update, context):
    global onGoingQuestion
    global answeredQuestions
    global onGoingQuizId
    global alternativeAnswerId
    global alternativeQuestion
    questionId = None
    answerId = None
    if alternativeAnswerId is None:
        questionId = onGoingQuestion
        answerId = G.nodes[onGoingQuestion]['quizzes'][onGoingQuizId]
    else:
        questionId = alternativeQuestion
        answerId = alternativeAnswerId
    answers = G.nodes[answerId]['answers']
    answer = update.message.text
    if answer not in answers:
        context.bot.send_message(
            chat_id=update.message.chat_id, text=f"Opció {answer} no vàlida")
    else:
        if questionId in answeredQuestions:
            if answer in answeredQuestions[questionId]:
                answeredQuestions[questionId][answer] += 1
            else:
                answeredQuestions[questionId][answer] = 1
        else:
            answeredQuestions[questionId] = {answer: 1}
        alternatives, auxQuestion = searchDestination(G[questionId])
        if not auxQuestion is None:
            onGoingQuestion = auxQuestion
        if len(alternatives.keys()) == 0:
            alternativeAnswerId = None
            if onGoingQuestion != 'END':
                showQuestion(update, context, onGoingQuestion, False, None)
            else:
                questions = pickle.load(
                    open("./data/questions.p", "rb"))

                for question in answeredQuestions:
                    q = answeredQuestions[question]
                    for answeredQuestion in q:
                        questions[question][answeredQuestion] += q[answeredQuestion]
                pickle.dump(questions, open(
                    "./data/questions.p", "wb"))

                context.bot.send_message(
                    chat_id=update.message.chat_id, text=f"{onGoingQuizId}> Gràcies pel teu temps!")

                onGoingQuestion = None
                onGoingQuizId = None
                answeredQuestions = {}

                return ConversationHandler.END
        else:
            if answer in alternatives:
                showQuestion(
                    update, context, alternatives[answer]['questionId'], True, alternatives[answer]['answerId'])


def cancelHandler(update, context):
    onGoingQuizId = None
    onGoingQuestion = None
    answeredQuestions = {}

    context.bot.send_message(
        chat_id=update.message.chat_id, text=f"S'ha cancelat l'enquesta")
    return ConversationHandler.END
    

# -------------------------------------------------------

def main():
    # hack pel Mac
    #matplotlib.use('Agg')

    TOKEN = open('./bot/token.txt').read().strip()
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', startHandler))
    dispatcher.add_handler(CommandHandler('help', helpHandler))
    dispatcher.add_handler(CommandHandler('author', authorHandler))
    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('quiz', quizHandler)],
        states={
            QUIZ: [MessageHandler(Filters.regex('[0-9]+'), quizAnswerHandler)]
        },
        fallbacks=[CommandHandler('cancel', cancelHandler)]
    ))
    dispatcher.add_handler(CommandHandler('bar', barHandler))
    dispatcher.add_handler(CommandHandler('pie', pieHandler))
    dispatcher.add_handler(CommandHandler('report', reportHandler))

    updater.start_polling()


if __name__ == '__main__':
    main()



