modelos = []
modelos_consumo = []

def entrada_carro(): 
    for i in range(4):
        modelo = input()
        modelos.append(modelo)   

def entrada_consumo():
    for i in range(4):
        consumo = float(input())
        modelos_consumo.append(consumo)       
           
def economico():
    index = modelos_consumo.index(min(modelos_consumo))
    return modelos[index]