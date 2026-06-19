from .validador import Validador

def separador(titulo: str = "") -> None:
    print("\n" + "=" * 55)
    if titulo:
        print(f"  {titulo}")
        print("=" * 55)


def escolher_da_lista(lista: list, rotulo_item: str = "item") -> "object | None":
    if not lista:
        print(f"✖ Nenhum(a) {rotulo_item} cadastrado(a).")
        return None
    for i, item in enumerate(lista):
        print(f"  {i + 1}. {item}")
    try:
        idx = int(input(f"\nEscolha o número do(a) {rotulo_item}: ")) - 1
        if 0 <= idx < len(lista):
            return lista[idx]
        print("✖ Número fora da lista.")
        return None
    except ValueError:
        print("✖ Entrada inválida. Digite um número.")
        return None

def ler_texto(rotulo: str) -> str:
    return input(rotulo).strip().upper()


def ler_texto_simples(rotulo: str) -> str:
    return input(rotulo).strip()


def ler_cpf(rotulo: str = "CPF: ") -> str:
    while True:
        valor = input(rotulo).strip()
        ok, resultado = Validador.cpf(valor)
        if ok:
            return resultado
        print(f"  ✖ {resultado}")


def ler_nome(rotulo: str = "Nome: ") -> str:
    while True:
        valor = ler_texto(rotulo)
        ok, resultado = Validador.nome(valor)
        if ok:
            return resultado
        print(f"  ✖ {resultado}")


def ler_senha(rotulo: str = "Senha: ") -> str:
    while True:
        valor = ler_texto_simples(rotulo)
        ok, resultado = Validador.senha(valor)
        if ok:
            return resultado
        print(f"  ✖ {resultado}")


def ler_carga_horaria(rotulo: str = "Carga horária (horas): ") -> int:
    while True:
        valor = input(rotulo).strip()
        ok, resultado = Validador.carga_horaria(valor)
        if ok:
            return resultado
        print(f"  ✖ {resultado}")


def ler_capacidade(rotulo: str = "Capacidade máxima de alunos: ") -> int:
    while True:
        valor = input(rotulo).strip()
        ok, resultado = Validador.capacidade(valor)
        if ok:
            return resultado
        print(f"  ✖ {resultado}")


def ler_nota(rotulo: str = "Nota (0–10): ") -> float:
    while True:
        valor = input(rotulo).strip()
        ok, resultado = Validador.nota(valor)
        if ok:
            return resultado
        print(f"  ✖ {resultado}")


def ler_texto_validado(rotulo: str, campo: str) -> str:
    while True:
        valor = ler_texto(rotulo)
        ok, resultado = Validador.texto_nao_vazio(valor, campo)
        if ok:
            return resultado
        print(f"  ✖ {resultado}")

def autenticar_professor(professores: list) -> "object | None":
    print("\nIdentifique-se como professor para lançar notas.")
    prof_sel = escolher_da_lista(professores, "professor")
    if prof_sel is None:
        return None
    senha = ler_texto_simples("Senha do professor: ")
    if prof_sel.autenticar(senha):
        print(f"✔ Acesso concedido. Bem-vindo, {prof_sel.nome}!")
        return prof_sel
    print("✖ Senha incorreta. Acesso negado.")
    return None
