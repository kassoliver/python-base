#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""

__version__ = "0.1.0"

# Dados

salas = {
    "01": ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "02": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}


disciplina_aluno = {
    "ingles": ["Erick", "Maia", "Joana", "Carlos", "Antonio"],
    "musica": ["Erick", "Carlos", "Maria"],
    "danca": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

atividades = [
    ("Inglês", disciplina_aluno["ingles"]),
    ("Música", disciplina_aluno["musica"]),
    ("Dança", disciplina_aluno["danca"]),
]

# Listar alunos de cada atividade por sala

for nome_atividade, atividade in atividades:
    print()
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 45)

    # Retonar todos os alunos da sala 1 que tem interseção com a atividade
    atividade_sala1 = set(salas["01"]) & set(atividade)
    atividade_sala2 = set(salas["02"]) & set(atividade)

    print("Sala 1 - ", atividade_sala1)
    print("Sala 2 - ", atividade_sala2)
    print()
    print("-" * 45)