class ContaBancaria:
    def __init__(self, numero_conta, titular_conta):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = 0.0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo =+ valor
            print(f'Valor depositado de R${valor}.')
            
        else:
            print('Valor inválido')
        
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso')
            else: 
                print("saldo insuficiente")
            
conta = ContaBancaria(12345, "João da Silva")
print(f"Saldo inicial da conta de {conta.titular_conta}: R${conta.saldo}")

conta.depositar(1000)
print(f"Saldo após depósito: R${conta.saldo}")

conta.sacar(500)
print(f"Saldo após saque: R${conta.saldo}")