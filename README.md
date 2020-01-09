# QuizBot

This project consists on a custom compiler for a quiz generation language along with a Telegram bot for quering purposes.


### Prerequisites

The following libraries are needed, as specified in the requirements.txt file:

```
antlr4-python3-runtime==4.7.2
networkx==2.4
python-telegram-bot==12.2.0
```

They can be installed using pip or another package manager.
```
$ pip install -r requirements.txt
```


### Testing the project

The whole project can be tested locally running in parallel these two commands:

```
$ python3 ./cl/test.1.py quiz-data/<quizFile>
$ python3 ./bot/bot.py
```

The Telegram bot user is: **@foix_quiz_bot**


## Author

* **Jordi Foix Esteve**


