from dotenv import load_dotenv
load_dotenv()

from src.alternativa import Alternativa
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.perguntadiscursiva import PerguntaDiscursiva
from src.questionario import Questionario
from src.correcao import Correcao


def main():
    # 1. Criar o questionário (quiz)
    quiz = Questionario("Quiz de Programação")

    # 2. Pergunta de múltipla escolha
    p1 = PerguntaMultiplaEscolha(
        texto="Qual linguagem é interpretada?",
        alternativas=[
            Alternativa("Java", False),
            Alternativa("Python", True, explicacao="Python é interpretada por padrão."),
            Alternativa("C", False),
        ],
        explicacao_geral="Python normalmente é interpretada."
    )
    quiz.adicionar_pergunta(p1)

    # 3. Pergunta discursiva
    p2 = PerguntaDiscursiva(
        texto="O que significa CPU?",
        resposta_esperada="Central Processing Unit"
    )
    quiz.adicionar_pergunta(p2)

    print(f"Quiz criado: '{quiz.titulo}' com {len(quiz.perguntas)} perguntas.\n")

    # 4. Criar tentativa
    tentativa = quiz.criar_attempt("valter")
    print(f"Tentativa criada para usuário: {tentativa.usuario}")
    print(f"Finalizada? {tentativa.is_finalizado()}\n")

    # 5. Registrar respostas
    print("--- Registrando respostas ---")
    tentativa.registrar_resposta(0, 1)  # "Python" -> correta
    tentativa.registrar_resposta(1, "Central Processing Unit")  # discursiva correta

    print(f"Total de respostas registradas: {len(tentativa.respostas)}\n")

    # 6. Pontuação parcial
    print(f"Pontuação atual: {tentativa.calcular_pontuacao()}\n")

    # 7. Finalizar
    pontuacao, feedback = tentativa.finalizar()
    print("--- Resultado Final ---")
    print(f"Pontuação: {pontuacao}")
    print(f"Feedback: {feedback}")
    print(f"Finalizada? {tentativa.is_finalizado()}\n")

    # 8. Correção discursiva via LLM (Groq)
    print("--- Teste de Correção Discursiva via LLM ---")
    pergunta_discursiva = PerguntaDiscursiva(
        texto="O que é encapsulamento em POO?",
        resposta_esperada="É o princípio que esconde os detalhes internos de um objeto, "
                           "expondo apenas o necessário através de uma interface."
    )

    resposta_aluno = "É quando você protege os atributos da classe e só permite acesso via métodos."

    resultado = Correcao.corrigir_discursiva(pergunta_discursiva, resposta_aluno)

    print(f"Correta: {resultado['correta']}")
    print(f"Pontuação: {resultado['pontuacao']}")
    print(f"Feedback: {resultado['feedback']}")
    print(f"Explicação: {resultado['explicacao']}")


if __name__ == "__main__":
    main()