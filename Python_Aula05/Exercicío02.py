#       EXRECÍCIOS

# lista = [ x*3 for x in range(100)]
# print(lista)

# par = [x*2 for x in range(100)]
# print(par)

import matplotlib.pyplot as plt 
def jur_comp(tempo,capital,taxa):
    taxa = taxa / 100
    montante= capital * (1 + taxa) ** tempo
    return round(montante, 2)
tempo = [x for x in range(48)]

#montante = capital * (1+ taxa)** tempo
taxa = 3 / 100
tempo =[x for x in range(100)]
montante = [round(100 *(1+0.03)**t,2) for t in tempo]

if len(tempo) == montante:
    plt.plot(tempo,montante)
    plt.show()