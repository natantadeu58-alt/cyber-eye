import socket
import os
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
def escanear_portas(alvo, portas):
    print(f"\n[+] Iniciando varredura de no alvo: {alvo}")
    print(f"[+] Horário de início: {datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    print("-" * 50)
    portas_abertas = []
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        resultado = s.connect_ex((alvo, porta))
        if resultado == 0:
            print(f"[!] Porta {porta}: ABERTA")
            portas_abertas.append(porta)
        else:
            pass
        s.close()
        return portas_abertas
    def analisar_com_ia(lista_portas):
       client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        prompt = f"""
Portas encontradas abertas: {lista_portas}
Se a lista estiver vazia, explique que o ambiente local etá seguro e protegido. Se houver portas abertas (como 21, 22, 80, 443, 3306, 8080), explique detalhadamente qual serviço costuma rodar nelas, qual o risco dv segurança associado a deixá - las expostas e qual a recomendaçaõ técnica.
Formate a resposta em Markdown profissional, com títulos claros.
"""
        print("\n[+] Enviando relatório para a Inteligência Artificial analisar...")
        completion = client.chat.completions.create(model="llama3-3-70b-specdec", messages=[{"role": "user", "content": prompt}])
        return completion.choices[0].message.content
    if __name__== " __main__":
        ALVO_LOCAL = "127.0.0.1"
        PORTAS_TESTE = [21, 22, 23, 25, 53, 80, 110, 443, 1433, 3306, 8080]
        abertas = escanear_portas(ALVO_LOCAL, PORTAS_TESTE)
        print("-" * 50)
        print(f"[+]Varredura concluída. Total de portas abertas: {len(abertas)}")
        relatorio_ia = analisar_com_ia(abertas)
        print("\n" + "="*20 + "PARECER Técnico do SENTINELA" + "="*20)
        print(relatorio_ia)
        nome_arquivo = f"auditoria_redes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(relatorio_ia)
            print(f"\n[+] Relatório de auditoria salvo com sucesso em: {nome_arquivo}")           
