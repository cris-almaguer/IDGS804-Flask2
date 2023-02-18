from collections import Counter

class Calculos:
    def __init__(self, listaNumeros):
        self.listaNumeros = listaNumeros
    
    def calcularMaximo(self):
        return max(self.listaNumeros)
    
    def calcularMinimo(self):
        return min(self.listaNumeros)
    
    def calcularPromedio(self):
        return sum(self.listaNumeros) / len(self.listaNumeros)
    
    def calcularMasComun(self):
        contador = Counter(self.listaNumeros)
        valorMComun = contador.most_common(1)
        return valorMComun[0][0]
