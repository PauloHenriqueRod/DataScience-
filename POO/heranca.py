class Animal:
    def __init__(self):
        print('CRIADA A CLASSE ANIMAL')

    def identif(self):
        print('animal')

    def comer(self):
        print('comendo')


class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Objeto animal criado')

    def identif(self):
        print('cachorro')

    def latir(self):
        print('AUAU')


poodle = Cachorro()
poodle.comer()
poodle.identif()
poodle.latir()
