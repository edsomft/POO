"""
Testes de integração do Sistema de Escola.
Simulam um cenário realista com turma, disciplina, professor e alunos.
"""
import pytest
from src.aluno import Aluno
from src.professor import Professor
from src.disciplina import Disciplina
from src.turma import Turma


SENHA = "senha123"


@pytest.fixture(autouse=True)
def resetar_matricula():
    Aluno.resetar_contador(1000)
    yield


def test_fluxo_completo_turma():
    """Cria turma, matricula alunos, lança notas e gera boletim."""
    prof = Professor("Marcos Vinicius", "01002003040", "Ciências", SENHA)
    mat = Disciplina("Ciências", 60, prof)
    turma = Turma("6B", "6º Ano", capacidade=5)
    turma.adicionar_disciplina(mat)

    nomes = ["Alice Silva", "Bruno Costa", "Camila Dias"]
    alunos = [Aluno(n, f"0000000000{i+1}") for i, n in enumerate(nomes)]
    for a in alunos:
        turma.matricular_aluno(a)

    alunos[0].adicionar_nota("Ciências", 9.0)
    alunos[1].adicionar_nota("Ciências", 5.5)
    alunos[2].adicionar_nota("Ciências", 7.0)
    alunos[2].adicionar_nota("Ciências", 9.0)

    boletim_turma = turma.gerar_boletim_turma()

    assert boletim_turma["Alice Silva"]["Ciências"]["situacao"] == "Aprovado"
    assert boletim_turma["Bruno Costa"]["Ciências"]["situacao"] == "Reprovado"
    assert boletim_turma["Camila Dias"]["Ciências"]["media"] == pytest.approx(8.0)
    assert boletim_turma["Camila Dias"]["Ciências"]["situacao"] == "Aprovado"


def test_professor_ministra_varias_disciplinas():
    prof = Professor("Juliana Ramos", "05006007080", "Português", SENHA)
    Disciplina("Português", 80, prof)
    Disciplina("Literatura", 40, prof)
    assert "Português" in prof.disciplinas_ministradas
    assert "Literatura" in prof.disciplinas_ministradas


def test_professor_autenticacao():
    prof = Professor("Rodrigo Alves", "12345678901", "Matemática", SENHA)
    assert prof.autenticar(SENHA) is True
    assert prof.autenticar("senhaerrada") is False


def test_pessoa_nao_pode_ser_instanciada_diretamente():
    from src.pessoa import Pessoa
    with pytest.raises(TypeError):
        Pessoa("Teste Silva", "00000000000")  # type: ignore


def test_aluno_apresentar():
    a = Aluno("Eduardo Lima", "12312312312")
    apresentacao = a.apresentar()
    assert "Eduardo Lima" in apresentacao
    assert str(a.matricula) in apresentacao
