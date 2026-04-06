class Computador():
    def __init__(self, ram = 0):
        self.ram_total = ram
        self.ram_disponivel = self.ram_total
        self.apps_abertos = []
    
    def abrir_app(self, app):
        if app.consumo_ram <= self.ram_disponivel:
            self.apps_abertos.append(app)
            self.ram_disponivel -= app.consumo_ram  
            print(f"Aplicativo aberto")
        else:
            print("Total de memória excedido!")

    def fechar_app(self, app):
        if app in self.apps_abertos:         
            self.apps_abertos.remove(app)
            self.ram_disponivel += app.consumo_ram
            print(f"{app.nome} fechado!")  
        else:
            print(f"O app {app.nome}não está aberto.")
    
    def mostrar_desempenho(self):
        print("\n--- Desempenho do Sistema ---")
        print(f"RAM Disponível: {self.ram_disponivel}MB / {self.ram_total}MB")
        print("Apps rodando no momento:")
        
        if not self.apps_abertos: 
            print("- Nenhum aplicativo aberto.")
        else:
            for app in self.apps_abertos:
                print(f"- {app.nome} (Consumo: {app.consumo_ram}MB)")
        print("-----------------------------\n")