from banco import Banco
import os
import time


def limpar_tela():
    """
    Limpa o terminal de acordo com o sistema operacional.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    """
    Função principal do sistema bancário.
    Controla o menu e a interação com o usuário.
    """
    banco = Banco()

    while True:
        limpar_tela()
        opcao = input(
            '''
    1 - Criar cliente
    2 - Criar conta
    3 - Depositar
    4 - Sacar
    5 - Extrato
    0 - Sair

    Digite uma opção: '''
        )

        if opcao == '1':
            limpar_tela()
            nome = input('Nome: ')
            email = input('Email: ')
            cpf = input('CPF: ')

            banco.criar_cliente(nome, email, cpf)
            print('Cliente criado com sucesso!')
            time.sleep(2)

        elif opcao == '2':
            limpar_tela()
            cpf = input('CPF do cliente: ')
            numero = banco.criar_conta(cpf)

            if numero:
                print(f'Conta criada com sucesso! Número: {numero}')
            else:
                print('CPF não encontrado')

            time.sleep(2)

        elif opcao == '3':
            limpar_tela()
            try:
                valor = float(input('Valor do depósito: ').replace(',', '.'))
                cpf = input('CPF: ')
                numero = int(input('Número da conta: '))

                print(banco.deposito(valor, cpf, numero))
            except ValueError as erro:
                print(erro)

            time.sleep(2)

        elif opcao == '4':
            limpar_tela()
            try:
                valor = float(input('Valor do saque: ').replace(',', '.'))
                cpf = input('CPF: ')
                numero = int(input('Número da conta: '))

                print(banco.saque(valor, cpf, numero))
            except ValueError as erro:
                print(erro)

            time.sleep(2)

        elif opcao == '5':
            limpar_tela()
            cpf = input('CPF: ')
            numero = int(input('Número da conta: '))

            extrato = banco.exibir_extrato(cpf, numero)
            print(extrato)

            time.sleep(4)

        elif opcao == '0':
            print('Saindo do sistema...')
            break

        else:
            print('Opção inválida')
            time.sleep(1.5)


if __name__ == "__main__":
    main()
