from conta import ContaBancaria

p1 = ContaBancaria("Pedro", 123)
p1.depositar(500)
p1.sacar(250)
p1.sacar(50)
p1.extrato()
print(p1)

# p2 = ContaBancaria("Joana", 321)
# p2.depositar(500)
# print(p2)
# p2.transferir(p1, 500)
# print(p2)
# print(p1)