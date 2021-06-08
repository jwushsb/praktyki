print("Zadanie z ciągu Fibonacciego")
     
a, b = 0, 1
print("Wynik F0 to: ", a)


len = input("Wprowadź długość ciągu ")
len = int(len)
for suma in range(len):
    suma = a + b
    print("Wynik to: ", suma)
    a = b
    b = suma