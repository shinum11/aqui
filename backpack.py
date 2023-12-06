from algoritimo import *
                #[peso,valor]
pesos_e_valores = [[10, 40], [5, 15], [9, 13], [15, 100],
                   [4, 20], [16, 89], [7, 200], [4, 90], 
                   [133, 234], [2, 100]]

n_de_cromossomos = 150
peso_max = 200
n_de_itens = len(pesos_e_valores) 
geracoes = 100

populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, peso_max, pesos_e_valores)]
for i in range(geracoes):
    populacao = evolve(populacao, peso_max, pesos_e_valores, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, peso_max, pesos_e_valores))

for indice,dados in enumerate(historico_de_fitness):
   print ("Geracao: ", indice," | Media de valor na mochila: ", dados)

print("\nPeso total:",peso_max,"g\n\nItens:")
for indice,i in enumerate(pesos_e_valores):
    print("Item ",indice+1,": ",i[0],"g | R$",i[1])
    
print("\nSoluções Ótimas: ")
for i in range(5):
    print(populacao[i])
