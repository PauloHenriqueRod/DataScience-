from random import choice

evoulucao_personagem = [
    '''  *_______
  |       |
          |
          |
          |
  ________|''',
    '''  *_______
  |       |
  O       |
          |
          |
  ________|''',
    '''  *_______
  |       |
  O       |  
  |       |
          |
  ________|''',
    '''  *_______
  |       |
  O       |  
 /|       |
          |
  ________|''',
    '''  *_______
  |       |
  O       |  
 /|\\      |
          |
  ________|''',
    '''  *_______
  |       |
  O       |  
 /|\\      |
 /        |
  ________|''',
    '''  *_______
  |       |
  O       |  
 /|\\      |
 / \\      |
  ________|'''

]
palavras_jogo = ['teste', 'testando', 'fluminense', 'formula', 'torcedor', 'treino',
                 'aprendendo', 'python', 'errando', 'fracassando', 'seguindo',
                 'frente', 'jamais', 'parar', 'amor', 'romance', 'sofrer', 'sofrimento',
                 'corrida', 'corredor', 'amar', 'brasileiro', 'computador', 'dados',
                 'estudo', 'livro', 'livramento']


class Forca:
    def __init__(self, palavras):
        self.palavras = palavras
        print('Jogo Iniciado')
        x = Forca.escolher_palavras(self, self.palavras)
        Forca.jogo(self, x)

    def escolher_palavras(self, palavras):
        palavra = choice(palavras)
        return palavra

    def jogo(self, palabra):
        erro = 0
        listas = []
        letras_erradas = []
        letras_certas = []
        for c in palabra:
            listas.append('_')
        while '_' in listas:
            print(evoulucao_personagem[erro])
            print(f'Letras certas: {letras_certas}')
            print(f'Letras erradas: {letras_erradas}')
            for z in listas:
                print(z, end='')
            palpite = str(input('\nDigite uma letra')).strip().lower()
            while palpite in letras_erradas or palpite in letras_certas:
                palpite = str(input('DIGITE UMA LETRA QUE NÃO SEJA REPETIDA\n')).lower()
            letras_na_palavra = 0
            for num, letra in enumerate(listas):
                if palpite == palabra[num]:
                    listas[num] = palpite
                    letras_na_palavra += 1
                else:
                    pass
            if letras_na_palavra == 0:
                letras_erradas += [palpite]
                erro += 1
            elif letras_na_palavra != 0:
                letras_certas += [palpite]
            if erro == 6:
                print(evoulucao_personagem[6])
                print('FIM DE JOGO, VOCÊ PERDEU!!!!')
                print(f'A palavra era {palabra}')
                break
        if '_' not in listas:
            print(palabra)
            print('Parabés, você ganhou!!!')


jogo = Forca(palavras_jogo)
