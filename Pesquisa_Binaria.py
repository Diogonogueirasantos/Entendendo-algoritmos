from random import randint

class Pesquisa_binaria:
    def __init__(self):
        self.pesquisa()

    def pesquisa(self):
        self.usuarios = [int(c) for c in range(0, 128)]
        origem = 0
        extremidade = len(self.usuarios)
        marcador = randint(0, 128)
        nova_origem = (origem + extremidade) / 2
        if nova_origem == marcador:
            return nova_origem
        elif nova_origem > marcador:
            extremidade = nova_origem - 1
            return self.pesquisa()
        else:
            origem = nova_origem + 1
            return self.pesquisa()






Instanciador = Pesquisa_binaria()
