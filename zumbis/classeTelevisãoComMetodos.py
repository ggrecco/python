class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 0

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1
