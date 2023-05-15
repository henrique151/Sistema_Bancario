import textwrap


def menu():
    menu = """\n
    
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato 
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuários
    [q]\tSair
"""
    return input(textwrap.dedent(menu))


def depositar(saldo, v1, extrato, /):
    if v1 > 0:
        saldo += v1
        extrato += f"Depósito:\tR$ {v1:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
    return saldo, extrato    
    
def sacar(*, saldo, v1, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = v1 > saldo
    excedeu_limite = v1 > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        
    elif v1 > 0:
        saldo -= v1
        extrato += f"Saque:\t\tR$ {v1:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
        
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato
        
def exibir_extrato(saldo, /, *, extrato):
    print("\n========================= EXTRATO ========================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("============================================================")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro, cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("==== Usuário criado com sucesso! ====")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):   
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
   
            
def main():
    AGENCIA = '0001'
    LIMITE_SAQUES = 3
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            v1 = float(input("Digite o valor a ser depositado: "))
        
            saldo, extrato = depositar(saldo, v1, extrato)
        
        elif opcao == "s":
            v1 = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                v1=v1,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione a operação desejada.")

main()

