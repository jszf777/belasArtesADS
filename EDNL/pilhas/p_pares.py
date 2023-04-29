'''Desenvolva um algoritmo que receba do usuário 8 números inteiros e construa uma pilha apenas com os números pares'''

pp = [];

for x in range(1, 9, +1):
    pi_int = int(input("Digite um número: "));
    if(pi_int % 2 == 0):
        pp.append(pi_int);

print("Pilha de pares: ", pp)
