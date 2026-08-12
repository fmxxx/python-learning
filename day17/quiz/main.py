from quiz_brain import QuizBrain
from question_model import Question
from data import question_data


def load_question_bank(external_question_data) -> list:
    question_bank = []
    for question in external_question_data:
        new_question = Question(q_text=question["text"], q_answer=question["answer"])
        question_bank.append(new_question)

    return question_bank


new_quiz = QuizBrain(load_question_bank(question_data))
new_quiz.play_quiz()
