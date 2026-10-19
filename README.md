# cyber-eye

Scanner de portas em Python com análise de risco de segurança gerada por IA. A ferramenta varre um alvo em busca de portas abertas e envia o resultado para um modelo LLM (via Groq) que produz um parecer técnico sobre os riscos de cada serviço exposto, salvo automaticamente em um relatório Markdown.



---

## Funcionalidades

* **Varredura de Portas (`escanear_portas`):** conecta via socket TCP a uma lista de portas de um alvo (`127.0.0.1` por padrão) e identifica quais estão abertas, com timeout de 0.5s por tentativa.
* **Análise de Risco com IA (`analisar_com_ia`):** envia a lista de portas abertas para a API da Groq (modelo `llama3-3-70b-specdec`), que gera um parecer técnico explicando quais serviços costumam rodar em cada porta, os riscos de segurança associados e recomendações técnicas de mitigação.
* **Geração de Relatório:** salva o parecer da IA automaticamente em um arquivo Markdown (`auditoria_redes_[timestamp].md`), com data e hora no nome do arquivo.

---

## Tecnologias Utilizadas

* Python 3.x
* `socket` (varredura de conectividade TCP)
* `groq` (SDK para chamadas ao modelo LLM `llama3-3-70b-specdec`)
* `python-dotenv` (carregamento seguro da chave de API a partir de variável de ambiente)
* `datetime` (timestamp da varredura e do relatório gerado)

---

## Como Funciona

O script varre uma lista pré-definida de portas comumente associadas a serviços críticos (21, 22, 23, 25, 53, 80, 110, 443, 1433, 3306, 8080) contra um alvo local. Para cada porta aberta encontrada, a lista é enviada como prompt para o modelo da Groq, que atua como um "parecerista técnico": explica o serviço típico daquela porta, o risco de mantê-la exposta e a recomendação de mitigação — tudo formatado em Markdown profissional. O relatório final é salvo em disco com timestamp, funcionando como registro de auditoria.

---

## Como Usar

```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
groq==0.9.0
python-dotenv==1.0.1
```

> `socket` e `datetime` são módulos nativos do Python — não precisam ser instalados via pip.

Crie um arquivo `.env` na raiz do projeto com sua chave da Groq:

```
GROQ_API_KEY=sua_chave_aqui
```

Execute o script:

```bash
python cyber_eye.py
```

O relatório será impresso no terminal e salvo automaticamente como `auditoria_redes_AAAAMMDD_HHMMSS.md`.

---

## Próximos Passos / Roadmap

* Permitir varredura de alvo customizado via argumento de linha de comando (hoje fixo em `127.0.0.1`)
* Expandir a lista de portas analisadas
* Adicionar monitoramento de tráfego em tempo real e análise de logs de sistema (conforme escopo original do projeto)
