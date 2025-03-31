from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

# The quiz question dictionary
quiz_questions = {
    "What does CPU stand for?": {
        "A": "Central Processing Unit",
        "B": "Computer Processing Unit",
        "C": " Central Performance Unit",
        "D": "Computer Performance Unit",
        "Answer": "A"
    },
    "Which of the following operating systems is developed by Microsoft?": {
        "A": "macOS",
        "B": "Linux",
        "C": "Chrome OS",
        "D": "Windows",
        "Answer": "D"
    },
    "Which of the following types of computer networks is used to connect devices over a large geographic area?": {
        "A": "LAN (Local Area Network)",
        "B": "WAN (Wide Area Network)",
        "C": "MAN (Metropolitan Area Network)",
        "D": "WLAN (Wireless Local Area Network)",
        "Answer": "B"
    },
    "What is the term for a program that is used to protect a computer from viruses and other malicious software?":{
        "A":"Firewall",
        "B":"Antivirus software",
        "C" :"Malware",
        "D":"Spyware",
        "Answer":"B"
    },
    "What is a motherboard?":{
       "A":"Power supply",
       "B":"CPU",
       "C":"Main circuit board",
       "D":"RAM",
       "Answer":"C"
    },
    "Which software is used for video editing?":{
        "A":"Adobe Photoshop",
        "B":"Adobe Premiere Pro",
        "C":"Microsoft Word",
        "D":"Google Docs",
        "Answer": "B"
    },
    "What is a firewall?":{
        "A":"Antivirus software",
        "B":"Malware removal tool",
        "C":"Network security system",
        "D":"Operating system",
        "Answer":"C" 
    },
    "Which browser is developed by Mozilla?":{
       "A":"Google Chrome",
       "B":"Mozilla Firefox",
       "C":"Safari",
       "D":"Edge",
       "Answer":"B"
    },
    "What does GPU stand for?":{
        "A":"Graphics Processing Unit",
        "B":"General Processing Unit",
        "C":"Gaming Processing Unit",
        "D":"Graphical Processing Unit",
        "Answer": "A" 
    },
    "Which of the following programming languages is used for developing web applications?":{
       "A":"Java",
       "B":"Python",
       "C":"JavaScript",
       "D":"All of the above",
       "Answer":"D" 
    }
}

class QuizApp(App):
    def build(self):
        self.score = 0
        self.current_question_index = 0
        self.quiz_questions_list = list(quiz_questions.items())

        # Layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title Label
        self.title_label = Label(text="Quiz Application", font_size=24, size_hint_y=None, height=50)
        self.layout.add_widget(self.title_label)

        # Question Label
        self.question_label = Label(text="", font_size=20, size_hint_y=None, height=50)
        self.layout.add_widget(self.question_label)

        # Answer Buttons
        self.button_a = Button(text="A", on_press=self.check_answer, size_hint_y=None, height=50)
        self.layout.add_widget(self.button_a)
        self.button_b = Button(text="B", on_press=self.check_answer, size_hint_y=None, height=50)
        self.layout.add_widget(self.button_b)
        self.button_c = Button(text="C", on_press=self.check_answer, size_hint_y=None, height=50)
        self.layout.add_widget(self.button_c)
        self.button_d = Button(text="D", on_press=self.check_answer, size_hint_y=None, height=50)
        self.layout.add_widget(self.button_d)

        # Feedback Label (to display correct/incorrect messages)
        self.feedback_label = Label(text="", font_size=16, size_hint_y=None, height=50)
        self.layout.add_widget(self.feedback_label)

        # Display the first question
        self.display_question()

        return self.layout

    def display_question(self):
        # Get the current question and its options
        question, options = self.quiz_questions_list[self.current_question_index]
        self.question_label.text = question
        self.button_a.text = f"A: {options['A']}"
        self.button_b.text = f"B: {options['B']}"
        self.button_c.text = f"C: {options['C']}"
        self.button_d.text = f"D: {options['D']}"

    def check_answer(self, instance):
        # Get the selected answer
        question, options = self.quiz_questions_list[self.current_question_index]
        selected_answer = instance.text[0]

        if selected_answer == options["Answer"]:
            self.feedback_label.text = "Congratulations! You answered correctly."
            self.score += 1
        else:
            self.feedback_label.text = f"Incorrect! The correct answer is {options['Answer']}."

        # Automatically move to the next question after a brief delay
        self.next_question(None)

    def next_question(self, instance):
        # Move to the next question
        if self.current_question_index + 1 < len(self.quiz_questions_list):
            self.current_question_index += 1
            self.display_question()
            self.feedback_label.text = ""  # Clear feedback for next question
        else:
            self.disable_buttons()  # Disable buttons after all questions are answered
            self.show_score()

    def disable_buttons(self):
        # Disable all the answer buttons after the quiz is finished
        self.button_a.disabled = True
        self.button_b.disabled = True
        self.button_c.disabled = True
        self.button_d.disabled = True
        self.feedback_label.text = "The quiz is finished. No further answers allowed."

    def show_score(self):
        # Show the final score in a popup
        score_popup = Popup(title="Quiz Finished",
                            content=Label(text=f"Your final score is {self.score} out of {len(quiz_questions)}."),
                            size_hint=(0.6, 0.4))
        score_popup.open()

if __name__ == '__main__':
    QuizApp().run()
