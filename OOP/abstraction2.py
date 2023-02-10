class SingleChoiceQuestion:

    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers


    def ask(self):
        print(self.question)
        index = 0
        for i in self.answers:
            print(chr(97 + index) + ".", i)
            index += 1
        answer = input("Wybierz odpowiedź: ")
        while True:
            if answer not in ["a", "A", "b", "B", "c", "C"]:
                print("Nie ma takiej odpowiedzi!")
                answer = input("Wybierz odpowiedź: ")
            else:
                print("\n")
                print(f"Twoja odpowiedź to {answer}")
                return answer



class Questionnaire:

    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        return self.questions.append(question)

    def run(self):
        print(self.title)
        print("\n")
        answers = []
        for element in self.questions:
            answers.append(element.ask())
        print("Dziękuję!")
        new_list = []
        for i, j in enumerate(answers):
            new_list.append((i, j))
        return dict(new_list)





questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa')
q1 = SingleChoiceQuestion('Matryca', ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali'])
q2 = SingleChoiceQuestion('Rodzaj ekranu', ['matowy', 'błyszczący'])
q3 = SingleChoiceQuestion('Czy polecisz go znajomemu?', ['zdecydowanie tak', 'raczej tak', 'nie mam zdania', 'raczej nie', 'zdecydowanie nie'])
questionnaire.add_question(q1)
questionnaire.add_question(q2)
questionnaire.add_question(q3)
print(questionnaire.run())
