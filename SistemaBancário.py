menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saques = 3
saque = 0

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        v1 = float(input("Digite o valor a ser depositado: "))
        
        if v1 > 0:
            saldo += v1
            extrato = f"Depósito: R$ {v1:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        
        if numero_saque < limite_saques:
            if saldo > 0:
               saque = float(input("Digite o valor a ser sacado: "))
               
            if saque <= 0:
                print("Valor inválido.")
                
            elif saldo < saque:
                print("Saldo insuficiente.")
                
            else:
                if saque <= limite:
                    saldo -= saque
                    print("O saque foi realizado com sucesso!")
                    extrato = f"Saque: R$ {saque:.2f}\n"
                    numero_saque += 1        
                else:
                    print("Valor do saque inválido.")
        else:
            print("Limite de saques atingido.")
             
    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(f"\nO Saldo: R$ {saldo:.2f}.") 
       
    elif opcao == "q":
        break
    
    else:
        print("Operação invalida, por favor selecione a operação desejada.")
