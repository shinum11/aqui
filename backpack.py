from algoritimo import *
                
pesos_valores = [[2, 40], [3, 15], [5, 13], [2, 100],
                   [4, 20], [3, 89], [0.9, 200], [1.3, 90], 
                   [5, 234], [2, 100]]

n_de_cromossomos = 200
peso_max = 20
n_de_itens = len(pesos_valores) 
geracoes = 100

populacao = populacao(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, peso_max, pesos_valores)]
for i in range(geracoes):
    populacao = evoluir(populacao, peso_max, pesos_valores, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, peso_max, pesos_valores))

for j,dados in enumerate(historico_de_fitness):
   print ("Geracao: ", j," --- Media de valor na mochila: ", dados)

valort = 0
print("\n")
for j,i in enumerate(pesos_valores):
    print("Item ",j+1,"- ",i[0],"Kg --- R$",i[1])
    valort += i[1]

print("\nValor total:",valort,"R$")
print("Peso total:",peso_max,"Kg")
    
print("\nSoluções Ótimas: ")
for i in range(5):
    print(populacao[i])
