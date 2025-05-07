class Pessoa():
    def __init__(self,name,weight,age):
        self.nome=name
        self.peso=weight
        self.idade=age
        self.statusDormindo=False
        self.statusComendo=False
        self.statusFalando=False
        self.statusApresentando=False
        self.statusAtividade=""

    def apresentar(self):
        if self.statusApresentando==True:
            print(f"{self.nome} já está se apresentando")
        elif self.statusDormindo or self.statusFalando or self.statusComendo:
            print(f"{self.nome} não conseguiu, porque está {self.statusAtividade}")
        else:
            self.statusApresentando=True
            self.statusDormindo = False
            self.statusComendo = False
            self.statusFalando = False
            self.statusAtividade= " se apresentando "
            print(f"Olá, meu nome é {self.nome}, "
                  f"tenho {self.idade} anos, e "
                  f"peso {self.peso} kg")

    def comer(self,comida):
        if self.statusComendo==True:
            print(f"{self.nome} já está comendo")
        elif self.statusDormindo or self.statusFalando or self.statusApresentando:
            print(f"{self.nome} não conseguiu, porque está {self.statusAtividade}")
        else:
            self.statusComendo=True
            self.statusDormindo = False
            self.statusFalando = False
            self.statusApresentando = False
            print(f"{self.nome} está comendo {comida}")
            self.statusAtividade = " comendo "

    def falar(self):
        if self.statusFalando==True:
            print(f"{self.nome} já está falando")
        elif self.statusDormindo or self.statusComendo or self.statusApresentando:
            print(f"{self.nome} não conseguiu, porque está {self.statusAtividade}")
        else:
            self.statusComendo=False
            self.statusDormindo = False
            self.statusFalando = True
            self.statusApresentando = False
            print(f"{self.nome} está falando sobre sua idade"
                  f" ({self.idade} anos)")
            self.statusAtividade = " falando "
    def dormir(self):
        if self.statusDormindo==True:
            print(f"{self.nome} já está dormindo")
        elif self.statusComendo or self.statusFalando or self.statusApresentando:
            print(f"{self.nome} não conseguiu, porque está {self.statusAtividade}")
        else:
            self.statusComendo=False
            self.statusDormindo = True
            self.statusFalando = False
            self.statusApresentando = False
            print(f"{self.nome} foi dormir.")
            self.statusAtividade = " dormindo "





