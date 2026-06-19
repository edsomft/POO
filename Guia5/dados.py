from src import *
from utils import *

def popular_banco(
    turmas: list,
    professores: list,
    disciplinas: list,
    alunos: list,
) -> None:
    """Popula as listas do sistema com dados de exemplo para demonstração.

    Deve ser chamada no início de menu_principal(), passando as próprias
    listas já criadas lá. Exemplo de uso:

        def menu_principal() -> None:
            turmas, professores, disciplinas, alunos = [], [], [], []
            popular_banco(turmas, professores, disciplinas, alunos)
            ...
    """

    # ── Professores (nome com sobrenome, CPF 11 dígitos sem repetição, senha ≥ 4) ──
    prof_mat = Professor("RODRIGO ALVES", "12345678901", "MATEMATICA", "mat123")
    prof_por = Professor("ANA LIMA",     "23456789012", "PORTUGUES",  "por123")
    prof_cis = Professor("BEATRIZ COSTA", "34567890123", "CIENCIAS",   "cis123")
    prof_his = Professor("CARLOS MENDES", "45678901234", "HISTORIA",   "his123")
    professores.extend([prof_mat, prof_por, prof_cis, prof_his])

    # ── Disciplinas (nome não vazio, carga horária 1–400) ────────────────────────
    disc_mat = Disciplina("MATEMATICA",  80, prof_mat)
    disc_por = Disciplina("PORTUGUES",   80, prof_por)
    disc_cis = Disciplina("CIENCIAS",    60, prof_cis)
    disc_his = Disciplina("HISTORIA",    60, prof_his)
    disc_geo = Disciplina("GEOGRAFIA",   40, prof_his)
    disciplinas.extend([disc_mat, disc_por, disc_cis, disc_his, disc_geo])

    # ── Turmas (código e série não vazios, capacidade 1–100) ─────────────────────
    turma_9a = Turma("9A", "9 ANO", 30)
    turma_9b = Turma("9B", "9 ANO", 30)
    turma_8a = Turma("8A", "8 ANO", 30)

    for disc in [disc_mat, disc_por, disc_cis, disc_his, disc_geo]:
        turma_9a.adicionar_disciplina(disc)
        turma_9b.adicionar_disciplina(disc)

    for disc in [disc_mat, disc_por, disc_cis]:
        turma_8a.adicionar_disciplina(disc)

    turmas.extend([turma_9a, turma_9b, turma_8a])

    # ── Alunos turma 9A ──────────────────────────────────────────────────────────
    dados_9a = [
        ("ALICE SOUZA",    "56789012345"),
        ("BRUNO SILVA",    "67890123456"),
        ("CAMILA SANTOS",  "78901234567"),
        ("DANIEL LIMA",    "89012345678"),
        ("EDUARDA COSTA",  "90123456789"),
    ]
    alunos_9a = []
    for nome, cpf in dados_9a:
        a = Aluno(nome, cpf)
        turma_9a.matricular_aluno(a)
        alunos_9a.append(a)
        alunos.append(a)

    # ── Alunos turma 9B ──────────────────────────────────────────────────────────
    dados_9b = [
        ("FELIPE ROCHA",   "10234567891"),
        ("GABRIELA NUNES", "20345678912"),
        ("HENRIQUE DIAS",  "30456789123"),
    ]
    alunos_9b = []
    for nome, cpf in dados_9b:
        a = Aluno(nome, cpf)
        turma_9b.matricular_aluno(a)
        alunos_9b.append(a)
        alunos.append(a)

    # ── Alunos turma 8A ──────────────────────────────────────────────────────────
    dados_8a = [
        ("IGOR FERREIRA",  "40567891234"),
        ("JULIA MORAES",   "50678912345"),
        ("LUCAS MARTINS",  "60789123456"),
    ]
    alunos_8a = []
    for nome, cpf in dados_8a:
        a = Aluno(nome, cpf)
        turma_8a.matricular_aluno(a)
        alunos_8a.append(a)
        alunos.append(a)

    # ── Notas turma 9A ───────────────────────────────────────────────────────────
    notas_9a = {
        "ALICE SOUZA":   {"MATEMATICA": [9.0, 8.5], "PORTUGUES": [7.0, 8.0], "CIENCIAS": [9.5, 10.0], "HISTORIA": [6.0, 7.5], "GEOGRAFIA": [8.0]},
        "BRUNO SILVA":   {"MATEMATICA": [4.0, 5.5], "PORTUGUES": [6.0, 6.5], "CIENCIAS": [3.0, 4.0],  "HISTORIA": [5.0, 5.5], "GEOGRAFIA": [5.0]},
        "CAMILA SANTOS": {"MATEMATICA": [7.0, 7.5], "PORTUGUES": [9.0, 9.5], "CIENCIAS": [7.0, 8.0],  "HISTORIA": [8.0, 8.5], "GEOGRAFIA": [9.0]},
        "DANIEL LIMA":   {"MATEMATICA": [6.0, 6.5], "PORTUGUES": [5.0, 5.5], "CIENCIAS": [6.5, 7.0],  "HISTORIA": [4.0, 3.5], "GEOGRAFIA": [6.0]},
        "EDUARDA COSTA": {"MATEMATICA": [8.0, 9.0], "PORTUGUES": [8.5, 7.5], "CIENCIAS": [9.0, 9.5],  "HISTORIA": [7.0, 8.0], "GEOGRAFIA": [8.5]},
    }
    for aluno in alunos_9a:
        for disc, notas in notas_9a[aluno.nome].items():
            for n in notas:
                aluno.adicionar_nota(disc, n)

    # ── Notas turma 9B (parcialmente lançadas) ───────────────────────────────────
    notas_9b = {
        "FELIPE ROCHA":   {"MATEMATICA": [7.0], "PORTUGUES": [6.5]},
        "GABRIELA NUNES": {"MATEMATICA": [9.5], "CIENCIAS":  [8.0]},
        "HENRIQUE DIAS":  {"HISTORIA":   [5.0], "GEOGRAFIA": [4.5]},
    }
    for aluno in alunos_9b:
        for disc, notas in notas_9b[aluno.nome].items():
            for n in notas:
                aluno.adicionar_nota(disc, n)

    # ── Notas turma 8A (sem notas — turma recém-criada para demonstrar estado inicial)
        # alunos_8a propositalmente sem notas lançadas ──────────────────────────

    print("✔ Banco de dados de exemplo carregado com sucesso!")
    print(f"  {len(professores)} professores | {len(disciplinas)} disciplinas | "
          f"{len(turmas)} turmas | {len(alunos)} alunos")
