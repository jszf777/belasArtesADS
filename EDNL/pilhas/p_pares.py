'''2. Desenvolva um algoritmo que receba do usuário 8 números inteiros e construa uma pilha apenas com os números pares.
Algoritmo pilha_pares
Inicio
	pp[8] Pilha;
	x,pi_int Inteiro;
	
	//empilhando na Pilha pp, 8 números digitados pelo usuário
	para x = 1 até 8 passo +1 faça
		pi_int = ler(mostrar ("digite um inteiro));
		Se(pi_int mod 2 == 0)//Se (pi_int for par)
			Então pp.Empilhar(pi_int);
	fimpara
		
	pp.mostrar( );
fim'''

pp = [];

for x in range(1, 9, +1):
    pi_int = int(input("Digite um número: "));
    if(pi_int % 2 == 0):
        pp.append(pi_int);

print("Pilha de pares: ", pp)

