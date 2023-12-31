import tkinter as tk
from tkinter import messagebox

questions = [
    "Question 1: Is plastic pollution a significant threat to marine ecosystems?",
    "Question 2: Plastic pollution is mainly caused by human activities.",
    "Question 3: Biodegradable plastics do not contribute to plastic pollution.",
    "Question 4: Plastic pollution in the ocean originates from land-based sources only.",
    "Question 5: Plastic pollution is a problem only in coastal areas.",
]

answers = [
    ["A. Yes", "B. No", "C. Maybe", "D. I'm not sure"],
    ["A. True", "B. False", "C. Not sure", "D. N/A"],
    ["A. False", "B. True", "C. It depends", "D. Not applicable"],
    ["A. False", "B. True", "C. Mostly true", "D. Mostly false"],
    ["A. False", "B. True", "C. Sometimes true", "D. Sometimes false"],
]

correct_answers = [
    0,  # Question 1: Correct answer is A (Yes)
    1,  # Question 2: Correct answer is B (False)
    1,  # Question 3: Correct answer is B (True)
    1,  # Question 4: Correct answer is B (True)
    0,  # Question 5: Correct answer is A (False)
]

class PlasticPollutionQuiz:
    def __init__(self, root):
        self.root = root
        self.current_question = 0
        self.score = 0

        self.root.title("Plastic Pollution Quiz")
        self.root.configure(bg="#D4E4F7")  # Set light blue background color

        self.question_label = tk.Label(root, text="", wraplength=400, bg="#D4E4F7")
        self.question_label.pack(pady=20)

        self.answer_buttons = []

        for i in range(4):
            button = tk.Button(root, text="", command=lambda idx=i: self.check_answer(idx), bg="#90EE90")
            self.answer_buttons.append(button)
            button.pack(pady=5)

        self.score_label = tk.Label(root, text="Score: 0", bg="#D4E4F7")
        self.score_label.pack(pady=5)

        self.show_next_question()

    def show_next_question(self):
        if self.current_question < len(questions):
            question_text = questions[self.current_question]
            answers_options = answers[self.current_question]

            self.question_label.config(text=question_text)

            for i in range(4):
                self.answer_buttons[i].config(text=answers_options[i])

        else:
            self.show_quiz_finished_message()

    def check_answer(self, user_answer_index):
        correct_answer_index = correct_answers[self.current_question]
        if user_answer_index == correct_answer_index:
            self.score += 1
            messagebox.showinfo("Correct!", "You are correct!")
        elif answers[self.current_question][user_answer_index] == "C. Maybe":
            self.score += 0.5
            messagebox.showinfo("Half Correct!", "You are half correct!")
        else:
            messagebox.showerror("Incorrect!", "Oops! That's incorrect.")

        self.current_question += 1
        self.update_score_label()
        self.show_next_question()

    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.score}")

    def show_quiz_finished_message(self):
        messagebox.showinfo("Quiz Finished", f"Congratulations! You have completed the quiz. Your score is: {self.score}")

        # Ask if the user wants to retake the quiz
        if messagebox.askyesno("Retake Quiz", "Do you want to retake the quiz?"):
            self.current_question = 0
            self.score = 0
            self.show_next_question()
        else:
            self.root.destroy()




# Create and run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    quiz = PlasticPollutionQuiz(root)
    root.mainloop()
