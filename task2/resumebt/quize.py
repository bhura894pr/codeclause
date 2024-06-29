import tkinter as tk
from tkinter import messagebox
import time

# Define the quiz questions and answers
quiz = [
    {
        "question": "Who is known as the 'Missile Man of India'?",
        "choices": ["A) Homi J. Bhabha", "B) Vikram Sarabhai", "C) A.P.J. Abdul Kalam", "D) C.V. Raman"],
        "answer": "C"
    },
    {
        "question": "Which is the largest organ of the human body?",
        "choices": ["A) Heart", "B) Liver", "C) Skin", "D) Lungs"],
        "answer": "C"
    },
    {
        "question": "The term 'DNA' stands for:",
        "choices": ["A) Deoxyribonucleic Acid", "B) Deoxyribonitric Acid", "C) Deoxyribosugar Acid", "D) Deoxyribonitrous Acid"],
        "answer": "A"
    },
    # Add more questions as needed...
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("1000x700")
        self.current_question = 0
        self.answers = [""] * len(quiz)
        self.score = 0
        self.timer = len(quiz) * 60  # z minutes for z questions
        self.start_time = None

        self.create_widgets()
        self.hide_quiz_widgets()

    def create_widgets(self):
        # Start button to initiate the quiz
        self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz, font=("Arial", 14))
        self.start_button.pack(pady=20)

        # Timer label to display remaining time
        self.timer_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        # Score label to display the current score
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(pady=10)

        # Main frame for question and options
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=10, padx=20, fill="both")

        # Question label to display the current question
        self.question_label = tk.Label(self.main_frame, text="", font=("Arial", 16), wraplength=600, justify="left", bg="gray")
        self.question_label.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky="w")

        # Radio buttons for answer choices
        self.var = tk.StringVar()
        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(self.main_frame, text="", variable=self.var, value="", font=("Arial", 14), indicatoron=0, width=20,
                                command=self.select_option, anchor="w")
            rb.grid(row=i + 1, column=0, columnspan=3, padx=20, pady=5, sticky="w")
            self.options.append(rb)

        # Label to display the correct answer
        self.answer_label = tk.Label(self.main_frame, text="", font=("Arial", 14), fg="green")
        self.answer_label.grid(row=5, column=0, columnspan=3, padx=20, pady=5, sticky="w")

        # Right frame for question navigation buttons
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.grid(row=0, column=3, rowspan=5, padx=20, pady=5, sticky="ne")

        # Question navigation buttons
        self.question_buttons = []
        for i in range(len(quiz)):
            btn = tk.Button(self.right_frame, text=str(i + 1), width=3, command=lambda idx=i: self.go_to_question(idx),
                            font=("Arial", 10), bd=0, relief="solid", anchor="center")
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.question_buttons.append(btn)

        # Navigation buttons (Previous, Next)
        self.navigation_frame = tk.Frame(self.root)
        self.navigation_frame.pack(pady=20)

        self.prev_button = tk.Button(self.navigation_frame, text="Previous", command=self.prev_question, font=("Arial", 12))
        self.prev_button.grid(row=0, column=0, padx=20)

        self.next_button = tk.Button(self.navigation_frame, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.grid(row=0, column=1, padx=20)

        # Submit button to manually submit the quiz
        self.submit_button = tk.Button(self.root, text="Submit", command=self.manual_submit_quiz, font=("Arial", 14))
        self.submit_button.pack(pady=20)

    def hide_quiz_widgets(self):
        # Function to hide all quiz-related widgets before starting the quiz
        self.timer_label.pack_forget()
        self.score_label.pack_forget()
        self.main_frame.pack_forget()
        self.navigation_frame.pack_forget()
        self.submit_button.pack_forget()

    def show_quiz_widgets(self):
        # Function to display all quiz-related widgets when starting the quiz
        self.timer_label.pack(pady=10)
        self.score_label.pack(pady=10)
        self.main_frame.pack(pady=10, padx=20, fill="both")
        self.navigation_frame.pack(pady=20)
        self.submit_button.pack(pady=20)

    def start_quiz(self):
        # Start quiz function
        self.start_button.pack_forget()
        self.show_quiz_widgets()
        self.start_time = time.time()
        self.update_question()
        self.update_timer()

    def update_question(self):
        # Update question and answer choices
        question_data = quiz[self.current_question]
        self.question_label.config(text=f"{self.current_question + 1}. {question_data['question']}")

        self.var.set(self.answers[self.current_question])

        for i, choice in enumerate(question_data["choices"]):
            self.options[i].config(text=choice, value=choice.split(")")[0].strip())

        self.update_navigation_buttons()
        self.update_question_buttons()

        # Display the correct answer if already answered
        if self.answers[self.current_question]:
            correct_answer = question_data["choices"][ord(question_data["answer"]) - ord('A')]
            self.answer_label.config(text=f"Correct Answer: {correct_answer}")
        else:
            self.answer_label.config(text="")

    def select_option(self):
        # Function to handle selection of an answer option
        self.answers[self.current_question] = self.var.get()
        self.update_question_buttons()

    def prev_question(self):
        # Function to move to the previous question
        if self.current_question > 0:
            self.current_question -= 1
            self.update_question()

    def next_question(self):
        # Function to move to the next question
        if self.current_question < len(quiz) - 1:
            self.current_question += 1
            self.update_question()

    def go_to_question(self, index):
        # Function to go to a specific question by index
        self.current_question = index
        self.update_question()

    def update_navigation_buttons(self):
        # Function to update navigation buttons (Previous, Next)
        self.prev_button.config(state=tk.NORMAL if self.current_question > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_question < len(quiz) - 1 else tk.DISABLED)

    def update_question_buttons(self):
        # Function to update question navigation buttons
        for i, btn in enumerate(self.question_buttons):
            if self.answers[i]:
                btn.config(bg="light green" if self.answers[i] == quiz[i]["answer"] else "orange")
            else:
                btn.config(bg="orange" if i == self.current_question else "SystemButtonFace")

    def manual_submit_quiz(self):
        # Function to manually submit the quiz with confirmation
        response = messagebox.askyesno("Submit Quiz", "Are you sure you want to submit the quiz?")
        if response:
            self.submit_quiz()

    def submit_quiz(self):
        # Function to submit the quiz, calculate score, and show results
        self.calculate_score()
        self.show_result()

    def calculate_score(self):
        # Function to calculate the score based on answers
        self.score = sum(1 for i, answer in enumerate(self.answers) if answer == quiz[i]["answer"])
        self.score_label.config(text=f"Score: {self.score}")

    def show_result(self):
        # Function to display quiz results
        self.hide_quiz_widgets()
        result_text = "Quiz Results:\n\n"
        for i, question in enumerate(quiz):
            result_text += f"Question {i + 1}: {question['question']}\n"
            result_text += f"Correct Answer: {question['choices'][ord(question['answer']) - ord('A')]}\n"
            result_text += f"Your Answer: {self.answers[i] if self.answers[i] else 'Not answered'}\n\n"

        result_text += f"Final Score: {self.score}/{len(quiz)}"
        messagebox.showinfo("Quiz Result", result_text)
        self.root.quit()

    def update_timer(self):
        # Function to update the quiz timer
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = self.timer - elapsed_time

        if remaining_time <= 0:
            self.submit_quiz()
        else:
            mins, secs = divmod(remaining_time, 60)
            time_str = f"Time remaining: {mins:02}:{secs:02}"
            self.timer_label.config(text=time_str)
            self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
