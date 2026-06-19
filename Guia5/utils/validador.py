import re


class Validador:
    """Classe utilitária com métodos estáticos de validação de dados de entrada."""

    @staticmethod
    def cpf(cpf: str) -> tuple[bool, str]:
        cpf_limpo = re.sub(r"[\.\-]", "", cpf).strip()
        if not cpf_limpo.isdigit():
            return False, "CPF deve conter apenas números (e opcionalmente pontos/traços)."
        if len(cpf_limpo) != 11:
            return False, f"CPF deve ter exatamente 11 dígitos. Informado: {len(cpf_limpo)} dígito(s)."
        if len(set(cpf_limpo)) == 1:
            return False, "CPF inválido (todos os dígitos iguais)."
        return True, cpf_limpo

    @staticmethod
    def nome(nome: str) -> tuple[bool, str]:
        nome_limpo = nome.strip()
        if not nome_limpo:
            return False, "Nome não pode ser vazio."
        if not re.match(r"^[A-ZÀ-Ÿa-zà-ÿ\s]+$", nome_limpo):
            return False, "Nome deve conter apenas letras e espaços (sem números ou símbolos)."
        partes = nome_limpo.split()
        if len(partes) < 2:
            return False, "Informe nome e sobrenome (ao menos duas palavras)."
        return True, nome_limpo

    @staticmethod
    def senha(senha: str) -> tuple[bool, str]:
        if len(senha) < 4:
            return False, "A senha deve ter ao menos 4 caracteres."
        return True, senha

    @staticmethod
    def carga_horaria(valor: str) -> tuple[bool, str]:
        try:
            ch = int(valor)
        except ValueError:
            return False, "Carga horária deve ser um número inteiro."
        if ch <= 0:
            return False, "Carga horária deve ser positiva."
        if ch > 400:
            return False, "Carga horária não pode ultrapassar 400 horas."
        return True, ch

    @staticmethod
    def capacidade(valor: str) -> tuple[bool, str]:
        try:
            cap = int(valor)
        except ValueError:
            return False, "Capacidade deve ser um número inteiro."
        if cap <= 0:
            return False, "Capacidade deve ser positiva."
        if cap > 100:
            return False, "Capacidade máxima permitida é 100 alunos."
        return True, cap

    @staticmethod
    def nota(valor: str) -> tuple[bool, str]:
        try:
            nota = float(valor.replace(",", "."))
        except ValueError:
            return False, "Nota deve ser um número (ex: 7.5)."
        if not (0.0 <= nota <= 10.0):
            return False, f"Nota deve estar entre 0 e 10. Informado: {nota}."
        return True, nota

    @staticmethod
    def texto_nao_vazio(valor: str, campo: str = "Campo") -> tuple[bool, str]:
        limpo = valor.strip()
        if not limpo:
            return False, f"{campo} não pode ser vazio."
        return True, limpo
