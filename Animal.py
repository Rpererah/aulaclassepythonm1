class Animal:
    def __init__(self,nome):
        self.nome=nome

    def reproduzirSom(self):
        pass

class Cachorro(Animal):
    def __init__(self,nome,raca):
        super().__init__(nome)
        self.raca=raca
    

cachorro1=Cachorro("rex","chiaua")

