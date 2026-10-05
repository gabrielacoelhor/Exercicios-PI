import numpy as np

temperaturas = np.array([
    2.5, 3.2, 5.1, 6.3, 7.0, 8.1, 10.5, 9.8, 8.5, 7.3,
    6.2, 5.1, 4.5, 3.8, 5.6, 6.7, 7.2, 8.3, 10.1, 9.4,
    8.2, 7.0, 6.3, 5.4, 4.7, 3.9, 5.8, 6.9, 7.4, 8.5,
    10.3, 9.6, 8.4, 7.2, 6.5, 5.6, 4.9, 4.1, 5.9, 7.0,
    7.5, 8.6, 10.4, 9.7, 8.5, 7.3, 6.6, 5.7, 5.0, 4.2,
    6.0, 7.1, 7.6, 8.7, 10.6, 9.9, 8.7, 7.5, 6.8, 5.9,
    5.2, 4.4, 6.1, 7.2, 7.7, 8.8, 10.7, 10.0, 8.8, 7.6,
    6.9, 6.0, 5.3, 4.5, 6.2, 7.3, 7.8, 8.9, 10.8, 10.2,
    9.0, 7.8, 7.1, 6.2, 5.5, 4.7, 6.3, 7.4, 7.9, 9.0,
    10.9, 10.3, 9.1, 7.9, 7.2, 6.3, 5.6, 4.8, 6.4, 7.5
])

# 1- ANALISE ESTATISTICA
media = np.mean(temperaturas)
mediana = np.median(temperaturas)
desvio_padrao = np.std(temperaturas)

print("=== ANÁLISE ESTATÍSTICA ===")
print("Média:", round(media, 2))
print("Mediana:", round(mediana, 2))
print("Desvio padrão:", round(desvio_padrao, 2))


# 2- CLASSIFICACAO DE TEMPERATURAS
classificacao = np.where(
    temperaturas < 5,
    "frio",
    np.where(temperaturas <= 15, "moderado", "quente")
)

print()
print("=== CLASSIFICAÇÃO DAS TEMPERATURAS ===")

for dia, classe in enumerate(classificacao, start=1):
    print("Dia", dia, "-", temperaturas[dia - 1], "°C -", classe)


# 3- DIAS EXTREMOS
dia_mais_frio = np.argmin(temperaturas) + 1
dia_mais_quente = np.argmax(temperaturas) + 1

temperatura_minima = np.min(temperaturas)
temperatura_maxima = np.max(temperaturas)

print()
print("=== DIAS EXTREMOS ===")
print("Dia mais frio:", dia_mais_frio, "-", temperatura_minima, "°C")
print("Dia mais quente:", dia_mais_quente, "-", temperatura_maxima, "°C")