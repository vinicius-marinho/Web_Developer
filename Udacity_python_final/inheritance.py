class Veiculo():
    def __init__(self,rodas,combustivel):
        self.rodas = rodas
        self.combustivel = combustivel

    def show_info(self):
        print("Tipo de combustivel: " + self.combustivel)

gol = Veiculo(4,"Gas")
# print(gol.combustivel)
gol.show_info()

class Carro(Veiculo): # Classe filha Carro herda da classe pai Veiculo
    def __init__(self, rodas, combustivel, cor):
        Veiculo.__init__(self, rodas, combustivel) #Chamo o construtor da classe pai
        self.cor = cor #variavel apenas da classe filha

    def show_info(self):

        print("Cor do carro: " + self.cor)


porsche = Carro(4, "gasolina", "preta")
porsche.show_info()