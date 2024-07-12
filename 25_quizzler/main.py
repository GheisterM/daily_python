# from data import question_data
import urllib.parse
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests
import urllib

# Call to trivia DB for dynamic question generation.
parameters = {
    "amount": 12,
    "type": "boolean",
    "encode": "url3986",
}
api_url = "https://opentdb.com/api.php"
api_call = requests.get(api_url, params=parameters)
api_data = api_call.json()
api_questions = api_data['results']

question_bank = []
for question in api_questions:
    text = urllib.parse.unquote(question['question'])
    question_bank.append(Question(text, question["correct_answer"]))

q_brain = QuizBrain(question_bank)

interface = QuizInterface(q_brain)
