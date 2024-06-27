# from data import question_data
import urllib.parse
from question_model import Question
from quiz_brain import QuizBrain
import requests
import urllib

# Call to trivia DB for dynamic question generation.
api_url = "https://opentdb.com/api.php?amount=12&type=boolean&encode=url3986"
api_call = requests.get(api_url)
api_data = api_call.json()
api_questions = api_data['results']

question_bank = []
for question in api_questions:
    text = urllib.parse.unquote(question['question'])
    question_bank.append(Question(text, question["correct_answer"]))

q_brain = QuizBrain(question_bank)

while q_brain.still_has_questions():
    q_brain.next_question()

print("You completed the quiz!")
print(f"Your final score was: {q_brain.score}/{q_brain.question_number}.")
