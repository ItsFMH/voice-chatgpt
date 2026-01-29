# 🎙️ Voice ChatGPT

Este projeto é um experimento em Python que permite conversar por voz com o ChatGPT. 🤖

A ideia é simples: você fala no microfone 🎤, sua fala é transcrita automaticamente, enviada ao ChatGPT e a resposta é reproduzida em áudio.

Por segurança, este repositório **não inclui nenhuma chave de API**. 🔐

---

## 🚀 Como usar

1. Crie sua API key em:
   https://platform.openai.com/api-keys

2. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
OPENAI_API_KEY=sua_api_key_aqui

3. Instale as dependências:
pip install -r requirements.txt

4. Execute o projeto:
python main.py

## ⚠️ Observação

Se o microfone ou o áudio não funcionarem, verifique primeiro as configurações de som do sistema operacional antes de rodar o projeto.

