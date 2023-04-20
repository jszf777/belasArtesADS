#definindo a classe da impressora
class Impressora:
    def __init__(self):     #iniciando o programa
        self.nivelCartucho = 100    #definindo o nível inicial do cartucho para 100%


    def imprimir(self, texto):      #definindo o método imprimir da classe impressora
        if self.nivelCartucho <= 0:     #se o nível do cartucho for menor ou igual a 0 avisar ao usuário que a tinta do cartucho acabou
            print('A tinta do cartucho acabou! Recarregue o cartucho.') 
        else:
            print(f'Imprimindo "{texto}"...')   #imprimindo o texto digitado pelo usuário
            self.nivelCartucho -=20     # cada impressao consome 20% da tinta do cartucho
        
    def nivelTinta(self):       #definindo o método nível de tinta da classe impressora
        print(f'O nível do cartucho é: {self.nivelCartucho}%')     #impressao do nivel de tinta do cartucho em porcentagem 

    def recarregarCartucho(self):       #definindo o método recarregar cartucho de tinta da classe impressora
        self.nivelCartucho = 100        #nível de tinta retorna a ser de 100% após a recarga 
        print(f'Cartucho recarregado com sucesso! O nível de tinta agora é de {self.nivelCartucho}%.')


impressora1 = Impressora ()     #chamada da impressora 

while True:     #definindo o loop que mantém o programa em execução até que o usuário selecione a opção 4 = sair

    print('Menu: ')     #apresenta as opções do menu para o usuário 
    print('1 - Imprimir')
    print('2 - Nível do cartucho')
    print('3 - Recarregar o cartucho')
    print('4 - Sair')
    opcao = input('Escolha uma opção: ')        #solicita que o usuário selecione uma opção no console e armazena a seleção na váriavel opcao 

    if opcao == '1':        #verifica se a opção selecionada foi a 1 e caso seja imprime o texto
        texto = (input('Digite o texto que será impresso: '))
        impressora1.imprimir(texto)
        print()
    elif opcao == '2':      #verifica se a opção selecionada foi a 2 e caso seja informa o nível de tinta do cartucho 
        impressora1.nivelTinta()
        print()
    elif opcao == '3':      #verifica se a opção selecionada foi a 3 e caso seja realiza a recarga do cartucho de tinta 
        impressora1.recarregarCartucho()
        print()
    elif opcao == '4':      #encerra o loop while
        print('Finalizando programa...')
        break
    else:
        print('Opção inválida. Retorne ao menu e tente novamente.')     #caso nenhuma das opções acima sejam selecionadas, informa ao usuário que a opção é inválida 
        print()
