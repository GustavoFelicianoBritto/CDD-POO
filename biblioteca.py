class Pessoa():
    def __init__(self,name,weight,age):
        self.nome=name
        self.peso=weight
        self.idade=age
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, "
              f"tenho {self.idade} anos, e "
              f"peso {self.peso} kg")

    def comer(self):
        print(f"{self.nome} está comendo")
    def falar(self):
        print(f"{self.nome} está falando sobre sua idade"
              f" ({self.idade} anos)")
    def dormir(self):
        print(f"{self.nome} foi dormir pelas próximas por 20 horas")




