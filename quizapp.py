
import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        self.geometry("400x300")
        
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": "Blue Whale"},
            {"question": "What is the symbol for potassium?", "options": ["K", "P", "Ka", "Po"], "answer": "K"}
        
        ]
        self.current_question_index = 0
        self.score = 0
        
        self.question_label = tk.Label(self, text="", font=("Arial", 12))
        self.question_label.pack(pady=10)
        
        self.option_var = tk.StringVar()
        self.option_var.set(None)
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self, text="", variable=self.option_var, value="", font=("Arial", 10))
            button.pack()
            self.option_buttons.append(button)
        
        self.next_button = tk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)
        
        self.display_question()
    
    def display_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question["question"])
        options = question["options"]
        for i in range(4):
            self.option_buttons[i].config(text=options[i], value=options[i])
    
    def next_question(self):
        user_answer = self.option_var.get()
        correct_answer = self.questions[self.current_question_index]["answer"]
        if user_answer == correct_answer:
            self.score += 1
        else:
            pass
        
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.finish_quiz()
    
    def finish_quiz(self):
        messagebox.showinfo("Quiz Finished", f"Your score is {self.score}/{len(self.questions)}")
        self.destroy()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
