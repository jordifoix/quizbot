import networkx as nx 

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

import matplotlib
import matplotlib.pyplot as plt

from EnquestesVisitor import EnquestesVisitor



# ------------ funcions consulta de Telegram ------------

def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hi! I'm QuizBot. I can help you on answering and reviewing quizes."
        " Here's a list of my commands (more info with /help):\n"
            "  /start\n  /help\n  /author\n  /quiz <quizId>\n"
            "  /bar <QuestionId>\n  /pie <QuestionId>\n  /report"
    )

def help(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I can help you interact with quizes in various ways.\n"
            "You can control me by sending these commands:\n\n"

            "Startup\n"
            "/start - start talking with me\n"
            "/help - display a list of all my commands and its usage/purpose\n"
            "/author - do you really wish to unveil my identity?\n"

            "Answering a Quiz\n"
            "/quiz <quizId> - Initiate an interpreter to go over the specified quiz interactively."
            " The user will be asked the questions of the quiz in their respective order,"
            " answering each time with the index corresponding to his answer's choice.\n"

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

def author(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Jordi Foix Esteve\njordi.foix@est.fib.upc.edu\njordifoixesteve@gmail.com"
    )


def quiz(bot, update, args):
    return ""


def bar(bot, update, args):
    return

def pie(bot, update, args):
    return

def report(bot, update):
    return 0


# -------------------------------------------------------



# hack pel Mac
#matplotlib.use('Agg')


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('nodes', start))
dispatcher.add_handler(CommandHandler('edges', start))
dispatcher.add_handler(CommandHandler('components', start))
dispatcher.add_handler(CommandHandler('graph', graph, pass_args=True))
dispatcher.add_handler(CommandHandler('plotpop', plotpop, pass_args=True))

updater.start_polling()

