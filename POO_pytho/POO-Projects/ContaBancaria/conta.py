class ContaBancaria():
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.saldo = 0
        self.numero_conta = numero_conta
        self.historico = []
        
    def depositar (self, valor):
       if valor > 0:
        self.saldo += valor
        self.historico.append(f"+ Deposito de R${valor} realizado com sucesso.")
        print("OK")
       else:
           print("Valor inválido para depósito..")
    
    def sacar (self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"- Saque de R${valor} realizado com sucesso.")
            print("OK")
        else:
            print(f"Valor Indisponivel")    
            
    def ver_saldo (self):
        print(f"Saldo atual: R${self.saldo}")
            
    def transferir (self, conta_destino, valor):
        if valor <= 0:
            print("Valor inválido para transferência.")
        elif valor <= self.saldo:
            self.saldo -= valor 
            conta_destino.depositar(valor)
            print(f"- Tranferência para {self.nome}no valor de {valor} realizada com sucesso!")
        else:
            print(f"Valor Indisponivel")
            
    def extrato(self):
        print("--- EXTRATO ---")
        for i in self.historico:
            print(f"{i}")
        print("---------------")
        
    def __str__(self):
        return f"Nome: {self.titular}, Saldo: {self.saldo}, Nº Conta: {self.numero_conta}"
    