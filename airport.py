from plane import Plane

class Airport:
    def __init__(self, nome:str):
        self.nome = nome
        self.fila = []  
       

    def __str__(self) -> str:
        return f'Aeropoto: {self.nome}\n Fila: {self.fila}'

    def add_fila(self, aviao:Plane):
        self.fila.append(aviao)

    def del_fila(self, aviao:Plane):
        self.fila.remove(aviao)




