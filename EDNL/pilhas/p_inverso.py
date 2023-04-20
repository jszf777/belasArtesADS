#Desenvolva um programa python que receba do usuário 10 numeros inteiros
#em uma pilha e inverta a ordem dos elementos desta pilha usando duas pilhas adicionais

P = []
P1 = []
P2 = []

for x in range(1, 11, +1): #11 pq ai vai até o 10
    num = int(input("Digite um número inteiro: "))
    P.append(num)

print("Pilha P: ", P)

for x in range(1, 11, +1): 
    num = P.pop()
    P1.append(num)

for x in range(1, 11, +1): 
    num = P1.pop()
    P2.append(num)

for x in range(1, 11, +1): 
    num = P2.pop()
    P.append(num)

print("Pilha P invertido: ", P)