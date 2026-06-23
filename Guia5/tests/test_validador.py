import pytest
from utils import Validador


class TestValidadorCpf:
    def test_cpf_valido_somente_digitos(self):
        ok, resultado = Validador.cpf("12345678901")
        assert ok is True
        assert resultado == "12345678901"

    def test_cpf_valido_com_formatacao(self):
        ok, resultado = Validador.cpf("123.456.789-01")
        assert ok is True
        assert resultado == "12345678901"

    def test_cpf_com_menos_de_11_digitos(self):
        ok, msg = Validador.cpf("1234567890")
        assert ok is False
        assert "11 dígitos" in msg

    def test_cpf_com_mais_de_11_digitos(self):
        ok, msg = Validador.cpf("123456789012")
        assert ok is False
        assert "11 dígitos" in msg

    def test_cpf_com_letras(self):
        ok, msg = Validador.cpf("1234567890A")
        assert ok is False
        assert "apenas números" in msg

    def test_cpf_todos_iguais(self):
        ok, msg = Validador.cpf("11111111111")
        assert ok is False
        assert "inválido" in msg.lower()

    def test_cpf_vazio(self):
        ok, msg = Validador.cpf("")
        assert ok is False


class TestValidadorNome:
    def test_nome_valido(self):
        ok, resultado = Validador.nome("João Silva")
        assert ok is True

    def test_nome_sem_sobrenome(self):
        ok, msg = Validador.nome("João")
        assert ok is False
        assert "sobrenome" in msg.lower() or "duas palavras" in msg.lower()

    def test_nome_com_numeros(self):
        ok, msg = Validador.nome("João123 Silva")
        assert ok is False
        assert "letras" in msg.lower()

    def test_nome_vazio(self):
        ok, msg = Validador.nome("")
        assert ok is False

    def test_nome_com_acentos(self):
        ok, resultado = Validador.nome("Lívia Gonçalves")
        assert ok is True


class TestValidadorSenha:
    def test_senha_valida(self):
        ok, resultado = Validador.senha("abcd")
        assert ok is True

    def test_senha_curta(self):
        ok, msg = Validador.senha("abc")
        assert ok is False
        assert "4 caracteres" in msg

    def test_senha_vazia(self):
        ok, msg = Validador.senha("")
        assert ok is False


class TestValidadorCargaHoraria:
    def test_carga_valida(self):
        ok, resultado = Validador.carga_horaria("80")
        assert ok is True
        assert resultado == 80

    def test_carga_zero(self):
        ok, msg = Validador.carga_horaria("0")
        assert ok is False

    def test_carga_negativa(self):
        ok, msg = Validador.carga_horaria("-10")
        assert ok is False

    def test_carga_texto(self):
        ok, msg = Validador.carga_horaria("oitenta")
        assert ok is False

    def test_carga_acima_limite(self):
        ok, msg = Validador.carga_horaria("401")
        assert ok is False


class TestValidadorNota:
    def test_nota_valida(self):
        ok, resultado = Validador.nota("7.5")
        assert ok is True
        assert resultado == pytest.approx(7.5)

    def test_nota_virgula(self):
        ok, resultado = Validador.nota("8,5")
        assert ok is True
        assert resultado == pytest.approx(8.5)

    def test_nota_zero(self):
        ok, resultado = Validador.nota("0")
        assert ok is True

    def test_nota_dez(self):
        ok, resultado = Validador.nota("10")
        assert ok is True

    def test_nota_acima_de_dez(self):
        ok, msg = Validador.nota("10.1")
        assert ok is False

    def test_nota_negativa(self):
        ok, msg = Validador.nota("-1")
        assert ok is False

    def test_nota_texto(self):
        ok, msg = Validador.nota("nota")
        assert ok is False
