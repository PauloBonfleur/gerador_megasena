import PySimpleGUI as sg
from random import randint


class Telapython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Digite a quantidade de jogos que deseja fazer :'),sg.Input(key='Digite a quantidade de jogos que deseja fazer :')],
            [sg.Button('Criar Jogo')],
            [sg.Output(size=(30, 20))]
        ]
        # Janela
        self.janela = sg.Window('Gerador de Jogos da Megasena').layout(layout)
        # Dados
        self.button, self.values = self.janela.Read()

    def mega_sena(self, n):
        p = set()
        im = set()
        result = []
        for i in range(int(n)):
            while len(p) < 3:
                r = randint(1, 60)
                if r % 2 == 0 and r not in p:
                    p.add(r)
            while len(im) < 3:
                r = randint(1, 60)
                if r % 2 != 0 and r not in p:
                    im.add(r)
            for x in p:
                result.append(x)
            for x in im:
                result.append(x)
            print(result)
            p = set()
            im = set()
            result = []

    def iniciar(self):
        if Telapython.mega_sena(self, self.values['Digite a quantidade de jogos que deseja fazer :']) != None:
            print(Telapython.mega_sena(self, self.values['Digite a quantidade de jogos que deseja fazer :']))

        while True:
            self.button, self.values = self.janela.Read()
            print()
            if Telapython.mega_sena(self, self.values['Digite a quantidade de jogos que deseja fazer :']) != None:
                print(Telapython.mega_sena(self, self.values['Digite a quantidade de jogos que deseja fazer :']))


tela = Telapython()
tela.iniciar()

