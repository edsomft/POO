import pytest
from src.professor import Professor
from src.disciplina import Disciplina


@pytest.fixture
def professor():
    return Professor("Rodrigo Alves", "12345678900", "Física", "senha123")


class TestDisciplinaCriacao:
    def test_criar_disciplina_valida(self, professor):
        d = Disciplina("Física Clássica", 80, professor)
        assert d.nome == "Física Clássica"
        assert d.carga_horaria == 80
        assert d.professor is professor

    def test_nome_vazio_levanta_erro(self, professor):
        with pytest.raises(ValueError):
            Disciplina("", 80, professor)

    def test_carga_horaria_invalida(self, professor):
        with pytest.raises(ValueError):
            Disciplina("Física", 0, professor)

    def test_professor_recebe_disciplina_automaticamente(self, professor):
        Disciplina("Física Moderna", 60, professor)
        assert "Física Moderna" in professor.disciplinas_ministradas


class TestDisciplinaSetters:
    def test_setter_carga_horaria(self, professor):
        d = Disciplina("Física", 80, professor)
        d.carga_horaria = 120
        assert d.carga_horaria == 120

    def test_setter_carga_horaria_invalida(self, professor):
        d = Disciplina("Física", 80, professor)
        with pytest.raises(ValueError):
            d.carga_horaria = -10

    def test_trocar_professor(self, professor):
        novo_prof = Professor("Beatriz Costa", "98765432100", "Física", "senha123")
        d = Disciplina("Física", 80, professor)
        d.professor = novo_prof
        assert d.professor is novo_prof
        assert "Física" not in professor.disciplinas_ministradas
        assert "Física" in novo_prof.disciplinas_ministradas


class TestDisciplinaStr:
    def test_str_contem_nome_e_professor(self, professor):
        d = Disciplina("Física", 80, professor)
        s = str(d)
        assert "Física" in s
        assert professor.nome in s
