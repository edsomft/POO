from src import *
from utils import *
from dados import popular_banco


def menu_principal() -> None:
    turmas: list[Turma] = []
    professores: list[Professor] = []
    disciplinas: list[Disciplina] = []
    alunos: list[Aluno] = []

    popular_banco(turmas, professores, disciplinas, alunos)

    opcoes = {
        "1": "Cadastrar Professor",
        "2": "Cadastrar Disciplina",
        "3": "Criar Turma",
        "4": "Matricular Aluno",
        "5": "Lançar Nota  [requer acesso de professor]",
        "6": "Exibir Boletim de um Aluno",
        "7": "Exibir Boletim da Turma Inteira",
        "8": "Listar Turmas",
        "0": "Sair",
    }

    while True:
        separador("SISTEMA DE ESCOLA — MENU PRINCIPAL")
        for k, v in opcoes.items():
            print(f"  [{k}] {v}")
        escolha = input("\nEscolha uma opção: ").strip()

        # ── 1. Cadastrar Professor ────────────────────────────────────────────
        if escolha == "1":
            separador("CADASTRAR PROFESSOR")
            nome  = ler_nome("Nome completo: ")
            cpf   = ler_cpf("CPF (somente números): ")
            esp   = ler_texto_validado("Especialidade: ", "Especialidade")
            senha = ler_senha("Senha (mín. 4 caracteres): ")
            try:
                prof = Professor(nome, cpf, esp, senha)
                professores.append(prof)
                print(f"\n✔ {prof} cadastrado com sucesso!")
            except ValueError as e:
                print(f"\n✖ Erro: {e}")

        # ── 2. Cadastrar Disciplina ───────────────────────────────────────────
        elif escolha == "2":
            separador("CADASTRAR DISCIPLINA")
            prof_sel = escolher_da_lista(professores, "professor")
            if prof_sel is None:
                continue
            nome_disc = ler_texto_validado("Nome da disciplina: ", "Nome da disciplina")
            ch = ler_carga_horaria()
            try:
                disc = Disciplina(nome_disc, ch, prof_sel)
                disciplinas.append(disc)
                print(f"\n✔ {disc} cadastrada com sucesso!")
            except ValueError as e:
                print(f"\n✖ Erro: {e}")

        # ── 3. Criar Turma ───────────────────────────────────────────────────
        elif escolha == "3":
            separador("CRIAR TURMA")
            codigo = ler_texto_validado("Código da turma (ex: 9A): ", "Código")
            serie  = ler_texto_validado("Série (ex: 9º ANO): ", "Série")
            cap    = ler_capacidade()
            try:
                t = Turma(codigo, serie, cap)
                turmas.append(t)
                print(f"\n✔ {t} criada com sucesso!")
            except ValueError as e:
                print(f"\n✖ Erro: {e}")
                continue

            if disciplinas:
                print("\nDeseja adicionar disciplinas a esta turma?")
                while True:
                    disponiveis = [d for d in disciplinas if d not in t.disciplinas]
                    if not disponiveis:
                        print("Todas as disciplinas já foram adicionadas.")
                        break
                    disc_sel = escolher_da_lista(disponiveis, "disciplina")
                    if disc_sel is None:
                        break
                    t.adicionar_disciplina(disc_sel)
                    print(f"✔ '{disc_sel.nome}' adicionada à turma.")
                    if input("Adicionar outra disciplina? (s/n): ").strip().upper() != "S":
                        break

        # ── 4. Matricular Aluno ──────────────────────────────────────────────
        elif escolha == "4":
            separador("MATRICULAR ALUNO")
            turma_sel = escolher_da_lista(turmas, "turma")
            if turma_sel is None:
                continue
            nome = ler_nome("Nome completo do aluno: ")
            cpf  = ler_cpf("CPF do aluno (somente números): ")
            try:
                aluno = Aluno(nome, cpf)
                turma_sel.matricular_aluno(aluno)
                alunos.append(aluno)
                print(f"\n✔ {aluno} matriculado em '{turma_sel.codigo}'!")
            except (ValueError, OverflowError) as e:
                print(f"\n✖ Erro: {e}")

        # ── 5. Lançar Nota  [requer acesso de professor] ─────────────────────
        elif escolha == "5":
            separador("LANÇAR NOTA")

            if not professores:
                print("✖ Nenhum professor cadastrado. Cadastre um professor primeiro.")
                continue

            prof_autenticado = autenticar_professor(professores)
            if prof_autenticado is None:
                continue

            alunos_disponiveis = [
                a for a in alunos
                if any(
                    a in t.alunos and any(d.professor == prof_autenticado for d in t.disciplinas)
                    for t in turmas
                )
            ]
            if not alunos_disponiveis:
                print("✖ Nenhum aluno encontrado nas turmas com disciplinas deste professor.")
                continue

            aluno_sel = escolher_da_lista(alunos_disponiveis, "aluno")
            if aluno_sel is None:
                continue

            turma_do_aluno = next((t for t in turmas if aluno_sel in t.alunos), None)
            if turma_do_aluno is None:
                print("✖ Turma do aluno não encontrada.")
                continue

            discs_professor = [d for d in turma_do_aluno.disciplinas if d.professor == prof_autenticado]
            if not discs_professor:
                print("✖ Este professor não ministra disciplinas na turma deste aluno.")
                continue

            disc_sel = escolher_da_lista(discs_professor, "disciplina")
            if disc_sel is None:
                continue

            nota = ler_nota()
            try:
                aluno_sel.adicionar_nota(disc_sel.nome, nota)
                print(f"\n✔ Nota {nota} registrada para '{aluno_sel.nome}' em '{disc_sel.nome}'.")
            except ValueError as e:
                print(f"\n✖ Erro: {e}")

        # ── 6. Boletim de um Aluno ───────────────────────────────────────────
        elif escolha == "6":
            separador("BOLETIM DO ALUNO")
            if not turmas:
                print("✖ Nenhuma turma cadastrada.")
                continue
            print("Selecione a turma:")
            turma_sel = escolher_da_lista(turmas, "turma")
            if turma_sel is None:
                continue
            if not turma_sel.alunos:
                print(f"✖ A turma '{turma_sel.codigo}' não possui alunos matriculados.")
                continue
            print(f"\nAlunos da turma {turma_sel.codigo} — {turma_sel.serie}:")
            aluno_sel = escolher_da_lista(turma_sel.alunos, "aluno")
            if aluno_sel is None:
                continue
            try:
                boletim = turma_sel.gerar_boletim(aluno_sel)
                print(f"\nBoletim de {aluno_sel.nome} — Turma {turma_sel.codigo}")
                print(f"{'DISCIPLINA':<20} {'NOTAS':<20} {'MÉDIA':>8} {'SITUAÇÃO':>12}")
                print("-" * 62)
                if not boletim:
                    print("Nenhuma disciplina cadastrada nesta turma.")
                for disc_nome, dados in boletim.items():
                    notas_str = ", ".join(str(n) for n in dados["notas"]) or "—"
                    media_str = f"{dados['media']:.2f}" if dados["media"] is not None else "—"
                    print(f"{disc_nome:<20} {notas_str:<20} {media_str:>8} {dados['situacao']:>12}")
            except ValueError as e:
                print(f"\n✖ Erro: {e}")

        # ── 7. Boletim da Turma Inteira ──────────────────────────────────────
        elif escolha == "7":
            separador("BOLETIM DA TURMA INTEIRA")
            turma_sel = escolher_da_lista(turmas, "turma")
            if turma_sel is None:
                continue
            boletim_turma = turma_sel.gerar_boletim_turma()
            if not boletim_turma:
                print("✖ Nenhum aluno matriculado nesta turma.")
                continue
            for nome_aluno, boletim in boletim_turma.items():
                print(f"\n• {nome_aluno}")
                print(f"  {'DISCIPLINA':<20} {'NOTAS':<20} {'MÉDIA':>8} {'SITUAÇÃO':>12}")
                print("  " + "-" * 60)
                if not boletim:
                    print("  Nenhuma disciplina cadastrada nesta turma.")
                for disc_nome, dados in boletim.items():
                    notas_str = ", ".join(str(n) for n in dados["notas"]) or "—"
                    media_str = f"{dados['media']:.2f}" if dados["media"] is not None else "—"
                    print(f"  {disc_nome:<20} {notas_str:<20} {media_str:>8} {dados['situacao']:>12}")

        # ── 8. Listar Turmas ─────────────────────────────────────────────────
        elif escolha == "8":
            separador("TURMAS CADASTRADAS")
            if not turmas:
                print("Nenhuma turma cadastrada.")
            for t in turmas:
                print(f"\n{t}")
                print("  Disciplinas:", ", ".join(d.nome for d in t.disciplinas) or "—")
                print("  Alunos:", ", ".join(a.nome for a in t.alunos) or "—")

        # ── 0. Sair ──────────────────────────────────────────────────────────
        elif escolha == "0":
            print("\nAté logo! 👋\n")
            break
        else:
            print("\n✖ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
