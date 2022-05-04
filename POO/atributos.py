class Funcinarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def func(self):
        print(f'O funcionário {self.nome} recebe R${self.salario}')


func1 = Funcinarios('João', 8500)
print('----------USANDO ATRIBUTOS-----------')
print(hasattr(func1, 'nome'))
print(setattr(func1, 'salario', 7500))
print(getattr(func1, 'salario'))
delattr(func1, 'salario')
print(hasattr(func1, 'salario'))
