import json as js

f = open("praktyki/062021/kacper_milewski/repo/quiz/pyt.json", "rt")
quest = js.loads(f.read())
f.close()

x = int(input("Wybierz pytanie od 1 do 3: "))
x -= 1
cos = quest[x]
print(cos["question"], "\n")

cos = cos["answers"]
i = 0
while i < 4:
    print(cos[i])
    i+=1
ans = int(input("Wprowadż odpowiedź: "))
ans -= 1
cos = quest[x]
if ans == int(cos["correct_answer"]):
    print("Łał udało się")
else:
    print("nie udało się sadge")
