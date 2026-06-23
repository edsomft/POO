import pytest
from src.aluno import Aluno
from src.professor import Professor
from src.disciplina import Disciplina
from src.turma import Turma


@pytest.fixture(autouse=True)
def resetar_matricula():
    Aluno.resetar_contador(1000)
    yield


@pytest.fixture
def professor():
    return Professor("Letícia Nunes", "00011122233", "Matemática", "senha123")


@pytest.fixture
def disciplina(professor):
    return Disciplina("Matemática", 80, professor)


@pytest.fixture
def turma():
    return Turma("9A", "9º Ano", capacidade=3)


@pytest.fixture
def alunos():
    return [Aluno(f"Aluno {i}", f"00{i}.000.000-00") for i in range(1, 4)]


class TestTurmaCriacao:
    def test_criar_turma_valida(self, turma):
        assert turma.codigo == "9A"
        assert turma.serie == "9º Ano"
        assert turma.capacidade == 3

    def test_codigo_vazio_levanta_erro(self):
        with pytest.raises(ValueError):
            Turma("", "9º Ano")

    def test_capacidade_invalida(self):
        with pytest.raises(ValueError):
            Turma("9A", "9º Ano", capacidade=0)


class TestTurmaMatricula:
    def test_matricular_aluno(self, turma, alunos):
        turma.matricular_aluno(alunos[0])
        assert alunos[0] in turma.alunos

    def test_turma_cheia_levanta_erro(self, turma, alunos):
        for a in alunos:
            turma.matricular_aluno(a)
        extra = Aluno("Extra", "999.999.999-99")
        with pytest.raises(OverflowError):
            turma.matricular_aluno(extra)

    def test_aluno_duplicado_levanta_erro(self, turma, alunos):
        turma.matricular_aluno(alunos[0])
        with pytest.raises(ValueError):
            turma.matricular_aluno(alunos[0])

    def test_remover_aluno(self, turma, alunos):
        turma.matricular_aluno(alunos[0])
        turma.remover_aluno(alunos[0])
        assert alunos[0] not in turma.alunos

    def test_remover_aluno_ausente_levanta_erro(self, turma, alunos):
        with pytest.raises(ValueError):
            turma.remover_aluno(alunos[0])

    def test_vagas_disponiveis(self, turma, alunos):
        turma.matricular_aluno(alunos[0])
        assert turma.vagas_disponiveis == 2

    def test_total_alunos(self, turma, alunos):
        turma.matricular_aluno(alunos[0])
        turma.matricular_aluno(alunos[1])
        assert turma.total_alunos() == 2


class TestTurmaDisciplinas:
    def test_adicionar_disciplina(self, turma, disciplina):
        turma.adicionar_disciplina(disciplina)
        assert disciplina in turma.disciplinas

    def test_disciplina_duplicada_levanta_erro(self, turma, disciplina):
        turma.adicionar_disciplina(disciplina)
        with pytest.raises(ValueError):
            turma.adicionar_disciplina(disciplina)


class TestTurmaBoletim:
    def test_boletim_com_notas(self, turma, alunos, disciplina):
        turma.matricular_aluno(alunos[0])
        turma.adicionar_disciplina(disciplina)
        alunos[0].adicionar_nota("Matemática", 8.0)
        alunos[0].adicionar_nota("Matemática", 6.0)
        boletim = turma.gerar_boletim(alunos[0])
        assert boletim["Matemática"]["media"] == pytest.approx(7.0)
        assert boletim["Matemática"]["situacao"] == "Aprovado"
        assert boletim["Matemática"]["notas"] == [8.0, 6.0]

    def test_boletim_sem_notas(self, turma, alunos, disciplina):
        turma.matricular_aluno(alunos[0])
        turma.adicionar_disciplina(disciplina)
        boletim = turma.gerar_boletim(alunos[0])
        assert boletim["Matemática"]["situacao"] == "Sem notas"
        assert boletim["Matemática"]["media"] is None

    def test_boletim_reprovado(self, turma, alunos, disciplina):
        turma.matricular_aluno(alunos[0])
        turma.adicionar_disciplina(disciplina)
        alunos[0].adicionar_nota("Matemática", 3.0)
        boletim = turma.gerar_boletim(alunos[0])
        assert boletim["Matemática"]["situacao"] == "Reprovado"

    def test_boletim_aluno_nao_matriculado_levanta_erro(self, turma, alunos):
        with pytest.raises(ValueError):
            turma.gerar_boletim(alunos[0])

    def test_boletim_turma_inteira(self, turma, alunos, disciplina):
        turma.adicionar_disciplina(disciplina)
        turma.matricular_aluno(alunos[0])
        turma.matricular_aluno(alunos[1])
        alunos[0].adicionar_nota("Matemática", 9.0)
        alunos[1].adicionar_nota("Matemática", 4.0)

        boletim_turma = turma.gerar_boletim_turma()

        assert alunos[0].nome in boletim_turma
        assert alunos[1].nome in boletim_turma
        assert boletim_turma[alunos[0].nome]["Matemática"]["situacao"] == "Aprovado"
        assert boletim_turma[alunos[1].nome]["Matemática"]["situacao"] == "Reprovado"

    def test_boletim_turma_vazia(self, turma):
        assert turma.gerar_boletim_turma() == {}


class TestTurmaStr:
    def test_str_contem_codigo_e_serie(self, turma):
        s = str(turma)
        assert "9A" in s
        assert "9º Ano" in s
