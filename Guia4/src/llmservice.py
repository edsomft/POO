from typing import List, Tuple, Dict

import os
import json
from groq import Groq


class LLMService:
    def __init__(self, api_key=None, model="llama-3.3-70b-versatile"):
        self.api_key = api_key or os.environ.get("GROQ_API_KEY")
        self.model = model
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        self._client = None

        if self.api_key:
            try:
                self._client = Groq(api_key=self.api_key)
            except Exception as e:
                self._tratar_erro(e)

    def corrigir_resposta(self, pergunta, resposta_aluno):
        if not self._client:
            return {
                "correta": False,
                "pontuacao": 0.0,
                "feedback": "Serviço de correção indisponível (API key não configurada).",
                "explicacao": pergunta.get_explicacao() or ""
            }

        prompt = self._criar_prompt(pergunta, resposta_aluno)

        try:
            resposta_texto = self._fazer_chamada_api(prompt)
            resultado = json.loads(resposta_texto)

            return {
                "correta": bool(resultado.get("correta", False)),
                "pontuacao": float(resultado.get("pontuacao", 0.0)),
                "feedback": str(resultado.get("feedback", "")),
                "explicacao": str(resultado.get("explicacao", pergunta.get_explicacao() or ""))
            }
        except Exception as e:
            return self._tratar_erro(e)

    def _criar_prompt(self, pergunta, resposta_aluno):
        return (
            "Você é um corretor de provas. Avalie a resposta do aluno.\n\n"
            f"Pergunta: {pergunta.texto}\n"
            f"Resposta esperada: {pergunta.resposta_esperada}\n"
            f"Resposta do aluno: {resposta_aluno}\n\n"
            "Responda APENAS em JSON, sem texto adicional, no formato:\n"
            '{"correta": true ou false, "pontuacao": número de 0.0 a 1.0, '
            '"feedback": "comentário curto sobre a resposta", '
            '"explicacao": "explicação da resposta correta"}'
        )

    def _fazer_chamada_api(self, prompt):
        completion = self._client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"},
        )
        return completion.choices[0].message.content

    def _tratar_erro(self, e):
        return {
            "correta": False,
            "pontuacao": 0.0,
            "feedback": f"Não foi possível corrigir automaticamente (erro: {type(e).__name__}).",
            "explicacao": ""
        }