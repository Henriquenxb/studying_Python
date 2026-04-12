cavaleiros = {
    "Seiya": {
        "Constelação": "Pégaso",
        "Armaduras": ["Pégaso", "Sagitário", "Odin", "Pégaso Divina"],
        "Golpe1": "Meteoro de Pégaso",
        "Golpe2": "Cometa de Pégaso",
        "Golpe3": "Turbilhão de Pégaso",
        "Lealdade": "Atena"
    },
    "Shiryu": {
        "Constelação": "Dragão",
        "Armaduras": ["Dragão", "Libra", "Dragão Divina"],
        "Golpe1": "Cólera do Dragão",
        "Golpe2": "Dragão Nascente",
        "Golpe3": "Excalibur",
        "Lealdade": "Atena"
    },
    "Hyoga": {
        "Constelação": "Cisne",
        "Armaduras": ["Cisne", "Aquário", "Cisne Divina"],
        "Golpe1": "Pó de Diamante",
        "Golpe2": "Trovão Aurora Ataque",
        "Golpe3": "Execução Aurora",
        "Lealdade": "Atena"
    },
    "Shun": {
        "Constelação": "Andrômeda",
        "Armaduras": ["Andrômeda", "Virgem", "Andrômeda Divina"],
        "Golpe1": "Corrente de Andrômeda",
        "Golpe2": "Nebulosa de Andrômeda",
        "Golpe3": "Tempestade Nebulosa",
        "Lealdade": "Atena"
    },
    "Ikki": {
        "Constelação": "Fênix",
        "Armaduras": ["Fênix", "Leão", "Fênix Divina"],
        "Golpe1": "Ave Fênix",
        "Golpe2": "Golpe Fantasma de Fênix",
        "Golpe3": "Destruição Galáctica", # Golpe usado em episódios/mangas específicos
        "Lealdade": "Atena"
    }
}

for nome, atributos in cavaleiros.items():
    print(f"\n{nome}\n")
    for especificacao, valorEspecificacao in atributos.items():
        print(f"{especificacao}: {valorEspecificacao}")
    print("-"*20)