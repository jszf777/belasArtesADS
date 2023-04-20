pv = []

for x in range(1, 11, +1):
    vogais = input("Digite um caracter: ")

    if(vogais == 'a' or vogais == 'A' or 
       vogais == 'e' or vogais == 'E' or
       vogais == 'i' or vogais == 'I' or
       vogais == 'o' or vogais == 'O' or
       vogais == 'u' or vogais == 'U'):
        pv.append(vogais)

print("A pilha de vogais é: ", pv)

