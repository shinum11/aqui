import tkinter as tk
from tkinter import ttk
import random

def individual(n_de_itens):
    """Cria um membro da população"""
    return [random.choice([0, 1]) for _ in range(n_de_itens)]

def population(n_de_individuos, n_de_itens):
    """Cria a população"""
    return [individual(n_de_itens) for _ in range(n_de_individuos)]

def fitness(individuo, peso_maximo, pesos_e_valores):
    """Faz avaliação do indivíduo"""
    peso_total = sum(individuo[i] * pesos_e_valores[i][0] for i in range(len(individuo)))
    valor_total = sum(individuo[i] * pesos_e_valores[i][1] for i in range(len(individuo)))

    if peso_total > peso_maximo:
        return 0  # Penaliza se o peso total exceder o limite da mochila
    else:
        return valor_total

def media_fitness(populacao, peso_maximo, pesos_e_valores):
    """Encontra a avaliação média da população"""
    avaliacoes = [fitness(individuo, peso_maximo, pesos_e_valores) for individuo in populacao]
    populacao_valida = [populacao[i] for i in range(len(populacao)) if avaliacoes[i] > 0]

    if not populacao_valida:
        return 0  # Evita a divisão por zero

    return sum(avaliacoes) / len(populacao_valida)

def selecao_roleta(pais):
    """Seleciona um pai e uma mãe baseado nas regras da roleta"""
    fitness_total = sum(pais[i][0] for i in range(len(pais)))
    valor_sorteado = random.uniform(0, fitness_total)

    acumulado = 0
    for i in range(len(pais)):
        acumulado += pais[i][0]
        if acumulado >= valor_sorteado:
            return pais[i][1]

def crossover(pai1, pai2):
    """Realiza o crossover de ponto único"""
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

def mutacao(individuo, taxa_mutacao):
    """Realiza a mutação por inversão de bit"""
    for i in range(len(individuo)):
        if random.uniform(0, 1) < taxa_mutacao:
            individuo[i] = 1 - individuo[i]  # Inverte o bit

def evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos, taxa_crossover, taxa_mutacao):
    """Executa uma geração do algoritmo genético"""
    pais = [[fitness(x, peso_maximo, pesos_e_valores), x] for x in populacao]
    pais.sort(reverse=True)

    # REPRODUÇÃO
    filhos = []
    while len(filhos) < n_de_cromossomos:
        homem = selecao_roleta(pais)
        mulher = selecao_roleta(pais)
        filho1, filho2 = crossover(homem, mulher)
        mutacao(filho1, taxa_mutacao)
        mutacao(filho2, taxa_mutacao)
        filhos.extend([filho1, filho2])

    return filhos

class ProblemaMochilaInterface:
    def __init__(self, master):
        self.master = master
        self.inicializar_interface()

    def inicializar_interface(self):
        self.master.title("Algoritmo Genético - Problema da Mochila")

        ttk.Label(self.master, text="Parâmetros do Problema").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.master, text="Peso Máximo da Mochila:").grid(row=1, column=0, padx=5, pady=5)
        self.peso_maximo_entry = ttk.Entry(self.master)
        self.peso_maximo_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.master, text="Número de Gerações:").grid(row=2, column=0, padx=5, pady=5)
        self.num_geracoes_entry = ttk.Entry(self.master)
        self.num_geracoes_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.master, text="Número de Cromossomos:").grid(row=3, column=0, padx=5, pady=5)
        self.num_cromossomos_entry = ttk.Entry(self.master)
        self.num_cromossomos_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.master, text="Taxa de Crossover (0.0 - 1.0):").grid(row=4, column=0, padx=5, pady=5)
        self.taxa_crossover_entry = ttk.Entry(self.master)
        self.taxa_crossover_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(self.master, text="Taxa de Mutação (0.0 - 1.0):").grid(row=5, column=0, padx=5, pady=5)
        self.taxa_mutacao_entry = ttk.Entry(self.master)
        self.taxa_mutacao_entry.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(self.master, text="Pesos e Valores (separados por vírgula):").grid(row=6, column=0, padx=5, pady=5)
        self.pesos_valores_entry = ttk.Entry(self.master)
        self.pesos_valores_entry.grid(row=6, column=1, padx=5, pady=5)

        ttk.Button(self.master, text="Executar Algoritmo Genético", command=self.executar_algoritmo_genetico).grid(row=7, columnspan=2, pady=10)

        self.resultado_text = tk.StringVar()
        ttk.Label(self.master, textvariable=self.resultado_text).grid(row=8, columnspan=2, pady=10)

    def executar_algoritmo_genetico(self):
        try:
            peso_maximo = int(self.peso_maximo_entry.get())
            num_geracoes = int(self.num_geracoes_entry.get())
            num_cromossomos = int(self.num_cromossomos_entry.get())
            taxa_crossover = float(self.taxa_crossover_entry.get())
            taxa_mutacao = float(self.taxa_mutacao_entry.get())
            pesos_valores = list(map(int, self.pesos_valores_entry.get().split(',')))

            pesos_e_valores = [(pesos_valores[i], pesos_valores[i + 1]) for i in range(0, len(pesos_valores), 2)]
        except ValueError:
            self.resultado_text.set("Erro: Insira valores válidos.")
            return

        geracoes = num_geracoes
        n_de_itens = len(pesos_e_valores)

        populacao = population(num_cromossomos, n_de_itens)
        historico_cromossomos = []
        historico_fitness = []

        for i in range(geracoes):
            populacao = evolve(populacao, peso_maximo, pesos_e_valores, num_cromossomos, taxa_crossover, taxa_mutacao)
            historico_cromossomos.append(populacao[0].copy())
            historico_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))

        # Atualiza a interface com o resultado
        resultado_final = f"Melhor Solução:\n{populacao[0]}\nValor Fitness: {fitness(populacao[0], peso_maximo, pesos_e_valores)}"
        historico_str = "\n\nCromossomos da Melhor Solução por Geração:\n"
        for i, cromossomos in enumerate(historico_cromossomos):
            historico_str += f"Geração {i + 1}: {cromossomos} | Média Fitness: {historico_fitness[i]:.2f}\n"
        self.resultado_text.set(resultado_final + historico_str)

# Criar a aplicação
root = tk.Tk()
app = ProblemaMochilaInterface(root)
root.mainloop()
