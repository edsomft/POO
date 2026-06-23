import pytest
from src.aluno import Aluno


@pytest.fixture(autouse=True)
def resetar_matricula():
    Aluno.resetar_contador(1000)
    yield


class TestAlunoCriacao:
    def test_criar_aluno_valido(self):
        a = Aluno("Maria Silva", "111.222.333-44")
        assert a.nome == "Maria Silva"
        assert a.cpf == "111.222.333-44"
        assert a.matricula == 1001

    def test_matriculas_sao_incrementadas(self):
        a1 = Aluno("Ana", "000.000.000-01")
        a2 = Aluno("Bia", "000.000.000-02")
        assert a2.matricula == a1.matricula + 1

    def test_nome_vazio_levanta_erro(self):
        with pytest.raises(ValueError):
            Aluno("", "111.222.333-44")

    def test_cpf_vazio_levanta_erro(self):
        with pytest.raises(ValueError):
            Aluno("Maria", "")


class TestAlunoNotas:
    def test_adicionar_nota_valida(self):
        a = Aluno("Carlos", "222.333.444-55")
        a.adicionar_nota("Matemática", 8.5)
        assert 8.5 in a.notas["Matemática"]

    def test_nota_fora_do_intervalo(self):
        a = Aluno("Carlos", "222.333.444-55")
        with pytest.raises(ValueError):
            a.adicionar_nota("Matemática", 11.0)

    def test_nota_negativa(self):
        a = Aluno("Carlos", "222.333.444-55")
        with pytest.raises(ValueError):
            a.adicionar_nota("Matemática", -1.0)

    def test_media_calculada_corretamente(self):
        a = Aluno("Diana", "333.444.555-66")
        a.adicionar_nota("Física", 7.0)
        a.adicionar_nota("Física", 9.0)
        assert a.media("Física") == pytest.approx(8.0)

    def test_media_sem_notas_levanta_erro(self):
        a = Aluno("Eva", "444.555.666-77")
        with pytest.raises(ValueError):
            a.media("Química")

    def test_aprovado_acima_do_minimo(self):
        a = Aluno("Fábio", "555.666.777-88")
        a.adicionar_nota("História", 7.0)
        assert a.aprovado("História") is True

    def test_reprovado_abaixo_do_minimo(self):
        a = Aluno("Gabriela", "666.777.888-99")
        a.adicionar_nota("História", 4.0)
        assert a.aprovado("História") is False

    def test_notas_retorna_copia(self):
        a = Aluno("Henrique", "777.888.999-00")
        a.adicionar_nota("Arte", 9.0)
        copia = a.notas
        copia["Arte"].append(1.0)
        assert len(a.notas["Arte"]) == 1


class TestAlunoStr:
    def test_str_contem_nome_e_matricula(self):
        a = Aluno("Igor", "888.999.000-11")
        s = str(a)
        assert "Igor" in s
        assert str(a.matricula) in s
