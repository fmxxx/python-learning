from question_model import Question
import random


class QuizBrain:
    def __init__(self, question_bank) -> None:
        self.score = 0
        self.asked_questions = 0
        self.question_bank = question_bank

    def print_question(self) -> None:
        print(f"{self.asked_questions}. {self.current_question.text}")
        print('Answer with "True" or "False". Type "exit" to close the program')

    def new_random_question(self) -> None:
        self.current_question = random.choice(self.question_bank)

    def is_answer_valid(self, answer) -> bool:
        return answer in ["true", "false", "exit"]

    def get_user_answer(self) -> str:
        while True:
            answer = input(">").lower()
            if self.is_answer_valid(answer):
                return answer
            print("Invalid answer.")
            print("")
            self.print_question()

    def play_quiz(self) -> None:
        is_game_on = True
        self.asked_questions += 1
        while is_game_on:
            self.new_random_question()
            self.print_question()
            answer = self.get_user_answer()

            if answer == "exit":
                is_game_on = False
            elif answer == self.current_question.answer.lower():
                self.score += 1
                print(f"CORRECT! ({self.score}/{self.asked_questions})")
            else:
                print(f"Incorrect :( ({self.score}/{self.asked_questions})")

            print("")
            self.asked_questions += 1
