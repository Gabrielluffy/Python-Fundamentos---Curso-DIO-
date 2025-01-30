texto = input("digite uma palavra: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()

for numero in range(0, 10):
    print(numero, end=" ")

for numero in range(0,101,10):
    print(numero, end=" ")

