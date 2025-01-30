saldo = 1000.0

opcao = int(input("informe sua opção [1] sacar/ [2] extrato: "))

if opcao == 1:
    saque = float (input("informe o valor de saque:"))
    status = "sucesso" if saldo >= saque else "falhou"
    if saldo >= saque:
        print("seu saque foi realizado")
        print(saque)
        saldo -= saque
    else:
        print("você não tem saldo para realizar seu saque")
    print(f" seu status foi {status} ao realizar o saque")
elif opcao == 2:
    print("seu extrato é de ...")
    print(saldo)
else:
    print("não existe essa opção")


