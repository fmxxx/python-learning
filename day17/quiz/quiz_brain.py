from question_model import Question
import random


class QuizBrain:
    def __init__(self, question_bank) -> None:
        self.score = 0
        self.asked_questions = 0
        self.question_bank = question_bank
        self.current_question = Question("", "")

    def print_question(self) -> None:
        print(f"{self.asked_questions}. {self.current_question.text}")
        print('Answer with "True" or "False". Type "exit" to close the program')

    def new_random_question(self) -> None:
        self.current_question = self.question_bank[
            random.randint(0, len(self.question_bank) - 1)
        ]

    def get_user_answer(self) -> None:
        is_valid = False
        answer = input(">").title()

        while is_valid == False:
            if answer in ["True", "False", "Exit"]:
                is_valid = True

            else:
                print("Invalid answer.")
                print("")
                self.print_question()
                answer = input(">").title()

        if answer == "Exit":
            exit()
        elif answer == self.current_question.answer:
            self.score += 1
            print(f"CORRECT! ({self.score}/{self.asked_questions})")
        else:
            print(f"Incorrect :( ({self.score}/{self.asked_questions})")

    def play_quiz(self) -> None:
        is_game_on = True

        while is_game_on:
            self.asked_questions += 1

            self.new_random_question()
            self.print_question()
            self.get_user_answer()

            print("")
