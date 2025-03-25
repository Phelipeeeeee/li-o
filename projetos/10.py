def realizar_login():
    conta_valida = "000323"
    senha_valida = "9883"
    
    
    conta = input("Digite o número da conta: ")
    senha = input("Digite a senha: ")

    
    if conta == conta_valida and senha == senha_valida:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Conta ou senha inválidos. Programa encerrado.")
        return False

def realizar_saque(saldo):
    while True:
        print(f"\nSaldo disponível: R${saldo:.2f}")
        try:
            saque = int(input("Digite o valor para saque: R$"))
            
            # Verifica se o valor do saque é válido
            if saque <= 0:
                print("O valor do saque deve ser positivo.")
                continue

            if saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
                return saldo

            # Definição das notas disponíveis
            notas = [100, 50, 20, 10]
            notas_entregues = {}

            for nota in notas:
                notas_entregues[nota] = saque // nota
                saque %= nota

            # Se ainda restar valor, não será possível realizar o saque
            if saque > 0:
                print("Valor não pode ser sacado com as notas disponíveis.")
                return saldo

            # Exibe as notas a serem entregues
            print("\nNotas entregues:")
            for nota, quantidade in notas_entregues.items():
                if quantidade > 0:
                    print(f"{quantidade} notas de R${nota}")
            
            # Atualiza o saldo após o saque
            saldo -= sum(notas_entregues[nota] * nota for nota in notas_entregues)
            return saldo
        except ValueError:
            print("Por favor, insira um valor válido para o saque.")

def main():
    saldo_inicial = 1000  

    if realizar_login():
        saldo = saldo_inicial
        while True:
            saldo = realizar_saque(saldo)

            
            resposta = input("\nDeseja realizar outro saque? (s/n): ").strip().lower()
            if resposta != 's':
                print("Atendimento encerrado.")
                break

if __name__ == "__main__":
    main()