import pytest
from src.professor import Professor


SENHA_PADRAO = "senha123"


def make_professor(nome="João Souza", cpf="99988877766", esp="Matemática", senha=SENHA_PADRAO):
    return Professor(nome, cpf, esp, senha)


class TestProfessorCriacao:
    def test_criar_professor_valido(self):
        p = make_professor()
        assert p.nome == "João Souza"
        assert p.especialidade == "Matemática"

    def test_especialidade_vazia_levanta_erro(self):
        with pytest.raises(ValueError):
            Professor("João Souza", "99988877766", "", SENHA_PADRAO)

    def test_senha_curta_levanta_erro(self):
        with pytest.raises(ValueError):
            Professor("João Souza", "99988877766", "Matemática", "abc")

    def test_setter_especialidade(self):
        p = make_professor()
        p.especialidade = "Física"
        assert p.especialidade == "Física"

    def test_setter_especialidade_vazia_levanta_erro(self):
        p = make_professor()
        with pytest.raises(ValueError):
            p.especialidade = "   "


class TestProfessorAutenticacao:
    def test_autenticar_senha_correta(self):
        p = make_professor()
        assert p.autenticar(SENHA_PADRAO) is True

    def test_autenticar_senha_errada(self):
        p = make_professor()
        assert p.autenticar("senhaerrada") is False

    def test_autenticar_senha_vazia(self):
        p = make_professor()
        assert p.autenticar("") is False


class TestProfessorDisciplinas:
    def test_adicionar_disciplina(self):
        p = make_professor(nome="Ana Lima", cpf="11100022233", esp="Química")
        p.adicionar_disciplina("Química Orgânica")
        assert "Química Orgânica" in p.disciplinas_ministradas

    def test_disciplina_duplicada_ignorada(self):
        p = make_professor(nome="Ana Lima", cpf="11100022233", esp="Química")
        p.adicionar_disciplina("Química Orgânica")
        p.adicionar_disciplina("Química Orgânica")
        assert p.disciplinas_ministradas.count("Química Orgânica") == 1

    def test_remover_disciplina(self):
        p = make_professor(nome="Ana Lima", cpf="11100022233", esp="Química")
        p.adicionar_disciplina("Química Orgânica")
        p.remover_disciplina("Química Orgânica")
        assert "Química Orgânica" not in p.disciplinas_ministradas

    def test_remover_disciplina_inexistente_levanta_erro(self):
        p = make_professor(nome="Ana Lima", cpf="11100022233", esp="Química")
        with pytest.raises(ValueError):
            p.remover_disciplina("Biologia")

    def test_disciplinas_retorna_copia(self):
        p = make_professor(nome="Ana Lima", cpf="11100022233", esp="Química")
        lista = p.disciplinas_ministradas
        lista.append("Invasora")
        assert "Invasora" not in p.disciplinas_ministradas


class TestProfessorStr:
    def test_str_contem_nome_e_especialidade(self):
        p = make_professor(nome="Carlos Matos", cpf="33344455566", esp="Biologia")
        s = str(p)
        assert "Carlos Matos" in s
        assert "Biologia" in s
