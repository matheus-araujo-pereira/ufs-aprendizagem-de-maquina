import random


# Função objetivo: soma dos quadrados dos elementos
def objetivo(solucao):
    return sum(x**2 for x in solucao)


# Função para gerar uma solução aleatória (subconjunto de números entre -10 e 10)
def gerar_solucao(tamanho=5, limite=-10, max_value=10):
    return [random.randint(limite, max_value) for _ in range(tamanho)]


# Parâmetros da busca
num_solucoes = 100  # Número de soluções geradas
tamanho_subconjunto = 5  # Tamanho do subconjunto (tamanho do vetor)
melhor_solucao = None
melhor_valor = float("inf")  # Inicializando com um valor muito alto

# Estratégia de busca por geração aleatória
for _ in range(num_solucoes):
    solucao_aleatoria = gerar_solucao(tamanho_subconjunto)
    valor = objetivo(solucao_aleatoria)

    if valor < melhor_valor:  # Se encontramos uma solução melhor, atualizamos
        melhor_valor = valor
        melhor_solucao = solucao_aleatoria

# Resultado final
print("Melhor solução encontrada:", melhor_solucao)
print("Valor da função objetivo:", melhor_valor)
