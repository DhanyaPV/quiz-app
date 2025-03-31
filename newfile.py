import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

kivy.require('2.1.0')

class QuizApp(App):
    def build(self):
        self.score = 0
        self.level = ''
        self.questions = []
        self.current_question = 0
        self.answers = []

        # Create a main layout
        self.main_layout = BoxLayout(orientation="vertical")
        
        # Create a welcome screen with options to choose difficulty
        self.welcome_layout = BoxLayout(orientation="vertical", padding=10)
        self.welcome_label = Label(text="Welcome to the Computer Science Quiz!\nSelect your difficulty level:", font_size=20)

        self.beginner_button = Button(text="Beginner", on_press=self.start_beginner_quiz)
        self.intermediate_button = Button(text="Intermediate", on_press=self.start_intermediate_quiz)
        self.high_button = Button(text="High", on_press=self.start_high_quiz)

        self.welcome_layout.add_widget(self.welcome_label)
        self.welcome_layout.add_widget(self.beginner_button)
        self.welcome_layout.add_widget(self.intermediate_button)
        self.welcome_layout.add_widget(self.high_button)

        self.main_layout.add_widget(self.welcome_layout)
        
        return self.main_layout

    def start_beginner_quiz(self, instance):
        self.level = "beginner"
        self.questions = [
            {"question": "Which of these is a programming language?", "options": ["HTML", "Python", "CSS", "SQL"], "correct_answer": "Python"},
            {"question": "What does CPU stand for?", "options": ["Central Processing Unit", "Computer Personal Unit", "Central Processor Unit", "Computer Processing Unit"], "correct_answer": "Central Processing Unit"},
            {"question": "What does 'RAM' stand for?", "options": ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Accessible Memory"], "correct_answer": "Random Access Memory"},
            {"question": "Which of these is a popular version control system?", "options": ["Git", "Python", "Java", "Linux"], "correct_answer": "Git"},
            {"question": "What is the main purpose of the operating system?", "options": ["To manage hardware and software", "To create websites", "To develop applications", "To compile code"], "correct_answer": "To manage hardware and software"},
            {"question": "Which of these is an input device?", "options": ["Monitor", "Keyboard", "Printer", "Speaker"], "correct_answer": "Keyboard"},
            {"question": "What does the 'URL' stand for?", "options": ["Uniform Resource Locator", "Universal Resource Locator", "Uniform Retrieval Locator", "Uniform Retrieval Link"], "correct_answer": "Uniform Resource Locator"},
            {"question": "Which of these is an example of a database?", "options": ["MySQL", "Windows", "Python", "Git"], "correct_answer": "MySQL"},
            {"question": "Which of these is not an example of an operating system?", "options": ["Linux", "Windows", "MacOS", "HTML"], "correct_answer": "HTML"},
            {"question": "Which programming language is known for its simplicity?", "options": ["Python", "Java", "C", "Fortran"], "correct_answer": "Python"}
        ]
        self.current_question = 0
        self.show_question()

    def start_intermediate_quiz(self, instance):
        self.level = "intermediate"
        self.questions = [
            {"question": "Which of the following is an example of a compiled programming language?", "options": ["Python", "JavaScript", "C", "Ruby"], "correct_answer": "C"},
            {"question": "What is the purpose of an 'if' statement in programming?", "options": ["To repeat a block of code", "To define a function", "To check a condition", "To create a loop"], "correct_answer": "To check a condition"},
            {"question": "Which of these is not an operating system?", "options": ["Linux", "Windows", "MacOS", "Visual Studio"], "correct_answer": "Visual Studio"},
            {"question": "Which of these is an example of an interpreted language?", "options": ["C", "Java", "Python", "C++"], "correct_answer": "Python"},
            {"question": "Which type of loop is used to iterate a block of code multiple times until a condition is met?", "options": ["for loop", "while loop", "do-while loop", "foreach loop"], "correct_answer": "while loop"},
            {"question": "What is the main difference between a list and a tuple in Python?", "options": ["Lists are immutable, tuples are mutable", "Lists are mutable, tuples are immutable", "Both are mutable", "Both are immutable"], "correct_answer": "Lists are mutable, tuples are immutable"},
            {"question": "What does the acronym 'HTTP' stand for?", "options": ["HyperText Transfer Protocol", "HyperTransfer Text Protocol", "HomeText Transfer Protocol", "HyperTech Text Protocol"], "correct_answer": "HyperText Transfer Protocol"},
            {"question": "Which of the following is an example of a markup language?", "options": ["HTML", "C", "Java", "Python"], "correct_answer": "HTML"},
            {"question": "What is the purpose of an IDE (Integrated Development Environment)?", "options": ["To compile and execute code", "To run multiple operating systems", "To store code", "To manage databases"], "correct_answer": "To compile and execute code"},
            {"question": "Which of these sorting algorithms has the best average time complexity?", "options": ["Bubble Sort", "Selection Sort", "Quick Sort", "Insertion Sort"], "correct_answer": "Quick Sort"}
        ]
        self.current_question = 0
        self.show_question()

    def start_high_quiz(self, instance):
        self.level = "high"
        self.questions = [
            {"question": "What is the time complexity of merge sort?", "options": ["O(n)", "O(n log n)", "O(log n)", "O(n^2)"], "correct_answer": "O(n log n)"},
            {"question": "Which of these algorithms is used for searching an element in a sorted list?", "options": ["Binary Search", "Bubble Sort", "Insertion Sort", "Quick Sort"], "correct_answer": "Binary Search"},
            {"question": "What does the acronym API stand for?", "options": ["Application Process Interface", "Application Programming Interface", "Automated Programming Interface", "Application Protocol Interface"], "correct_answer": "Application Programming Interface"},
            {"question": "What is the primary function of a hash table?", "options": ["To store data in a sorted manner", "To store data in key-value pairs for fast retrieval", "To encrypt data", "To group data by type"], "correct_answer": "To store data in key-value pairs for fast retrieval"},
            {"question": "Which of the following sorting algorithms has the best average time complexity?", "options": ["Selection Sort", "Bubble Sort", "Quick Sort", "Merge Sort"], "correct_answer": "Merge Sort"},
            {"question": "What is the time complexity of the 'binary search' algorithm?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "correct_answer": "O(log n)"},
            {"question": "Which of the following is not a type of database?", "options": ["SQL", "NoSQL", "Document-based", "API"], "correct_answer": "API"},
            {"question": "Which of the following is a common use of regular expressions?", "options": ["Sorting data", "Searching for patterns in text", "Storing files", "Compressing files"], "correct_answer": "Searching for patterns in text"},
            {"question": "What is the purpose of a recursive function?", "options": ["To execute code sequentially", "To repeat code in a loop", "To call itself in its definition", "To check for errors in code"], "correct_answer": "To call itself in its definition"},
            {"question": "Which of these is an example of a distributed system?", "options": ["A local database", "A cloud storage system", "A single server", "A single application running on one machine"], "correct_answer": "A cloud storage system"}
        ]
        self.current_question = 0
        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            # Clear previous screen
            self.main_layout.clear_widgets()

            # Display the current question
            question_data = self.questions[self.current_question]
            question_label = Label(text=question_data['question'], font_size=18, size_hint_y=None, height=50)
            self.main_layout.add_widget(question_label)

            # Display options as buttons
            options_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=250)
            for option in question_data['options']:
                option_button = Button(text=option, size_hint_y=None, height=40, on_press=self.check_answer)
                options_layout.add_widget(option_button)

            self.main_layout.add_widget(options_layout)
        else:
            self.display_score()

    def check_answer(self, instance):
        answer = instance.text
        correct_answer = self.questions[self.current_question]['correct_answer']

        if answer == correct_answer:
            self.score += 1

        self.current_question += 1
        self.show_question()

    def display_score(self):
        # Display final score in a popup
        score_popup = Popup(title='Quiz Completed',
                            content=Label(text=f'Your Score: {self.score} out of {len(self.questions)}'),
                            size_hint=(None, None), size=(400, 200))
        score_popup.open()

        # After 10 seconds, return to the home screen
        Clock.schedule_once(self.reset_to_home, 10)

    def reset_to_home(self, dt):
        # Reset score and go back to the home page
        self.score = 0
        self.level = ''
        self.questions = []
        self.current_question = 0
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(self.welcome_layout)


if __name__ == '__main__':
    QuizApp().run()
