import json as js

class Quest:
    def __init__(self, pyt_load):
        self.pyt = pyt_load
        self.qus = self.pyt['question']
        self.answ = self.pyt['answers']
        self.cor_answ = self.pyt['correct_answer']


    def quest(self):
        print(self.qus)

        
    def answer(self):
        i = 0
        while i < len(self.answ):
            print(self.answ[i])
            i+=1

    def correct_answ(self):
        if self.cor_answ == int(input("Jaka jest twoja odpowiedź: ")):
            
            print("Brawo! To poprawna odpowiedź")
        else:
            print("No niestety, poprawna odp to ", int(self.cor_answ))

def js_load(path):
    f = open("praktyki/062021/kacper_milewski/repo/quiz/" + path)
    quest = js.loads(f.read())
    f.close()
    return quest

quiz = js_load("quiz.json")

quiz = [Quest(quiz[questions]) for questions in range(len(quiz))]

choose=int(input("Wybierz pytanie od 1 do 3: "))
choose -= 1

str(quiz[choose].quest())
quiz[choose].answer()
str(quiz[choose].correct_answ())


