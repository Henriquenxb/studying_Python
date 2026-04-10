# Lista original para referência
cavaleiros = ['Seiya', 'Shiryu', 'Hyoga', 'Shun', 'Ikki', 'Jabu', 'Ichi', 'Ban', 'Geki', 'Nachi']

# Lista de Constelações correspondentes
constelacoes = ['Pégaso', 'Dragão', 'Cisne', 'Andrômeda', 'Fênix','Unicórnio', 'Hidra', 'Leão Menor', 'Urso', 'Lobo']

# Lista de Idades (Saga do Santuário)
idade = [13, 14, 14, 13, 15, 13, 14, 15, 15, 14]

# Estimativa de vitórias (inimigos nomeados/importantes)
vitorias = [15, 10, 8, 7, 12, 1, 0, 0, 0, 0]


# chamando o loop 'for' com 'enumerate()'
for i, cavaleiro in enumerate(cavaleiros):
    rank = vitorias[i]

    if rank > 7:
        classificacao = "Lenda do Santuário"
    elif rank > 3:
        classificacao = "Esforçado"
    else:
        classificacao = "Iniciante"

    print(f"O cavaleiro {cavaleiro} de {constelacoes[i]}, iniciou a sua jornada com {idade[i]} anos de idade, e possui {vitorias[i]} vitórias  (RANK: {classificacao})\n")