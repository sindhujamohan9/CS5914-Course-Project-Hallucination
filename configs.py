import openai

"""
GPT configs
"""

# API parameters
openai.api_key = "sk-"

# GPT-4 parameters
MODE = 'Chat' # Chat, Complete, Insert, Edit
TEMPERATURE = 1.0
MAXIMUM_LENGTH = 1024
TOP_P = 1.0
FREQUENCY_PENALTY = 0.0
PRESENCE_PENALTY = 0.0


"""
Dataset configs
"""

# Define question types
ALL_QUESTION_TYPES = [
    {
        "type": "COUNT",
        "definition": "questions where the answer requires counting",
        "question": "How many astronauts have been elected to Congress?",
        "answer": "4"
    },
    {
        "type": "COMPARATIVE",
        "definition": "questions that compare two objects on a given attribute such as age, height",
        "question": "Is Mont Blanc taller than Mount Rainier?",
        "answer": "Yes"
    },
    {
        "type": "SUPERLATIVE",
        "definition": "questions about the maximums or minimums of a given attribute",
        "question": "Who was the youngest tribute in the Hunger Games?",
        "answer": "Rue"
    },
    {
        "type": "ORDINAL",
        "definition": "questions based on an object’s position in an ordered list",
        "question": "Who was the last Ptolemaic ruler of Egypt?",
        "answer": "Cleopatra"
    },
    {
        "type": "MULTIHOP",
        "definition": "questions that require 2 or more steps (multiple hops) to answer",
        "question": "Who was the quarterback of the team that won Super Bowl 50?",
        "answer": "Peyton Manning"
    },
    {
        "type": "INTERSECTION",
        "definition": "questions that have two or more conditions that the answer must fulfill",
        "question": "Which movie was directed by Denis Villeneuve and stars Timothee Chalamet?",
        "answer": "Dune"
    },
    {
        "type": "DIFFERENCE",
        "definition": "questions with a condition that contains a negation",
        "question": "Which Mario Kart game did Yoshi not appear in?",
        "answer": "Mario Kart Live: Home Circuit"
    },
    {
        "type": "YESNO",
        "definition": "questions where the answer is Yes or No",
        "question": "Has Lady Gaga ever made a song with Ariana Grande?",
        "answer": "Yes"
    },
    {
        "type": "GENERIC",
        "definition": "questions where the worker was only given the topic and no constraints of complexity; tend to be simpler fact lookups",
        "question": "Where was Michael Phelps born?",
        "answer": "Baltimore, Maryland"
    }
]


