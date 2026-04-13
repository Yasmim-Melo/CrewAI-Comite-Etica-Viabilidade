#!/usr/bin/env python
"""
Comitê de Análise de Ética e Viabilidade - Versão Direta com Ollama
Sem dependências complexas - funciona com Python puro + requests
"""

import json
import os

try:
    import requests
except ImportError:
    print("❌ Instalando requests...")
    os.system(f'{os.path.join("venv", "Scripts", "pip.exe")} install requests')
    import requests

def ler_projeto():
    """Lê o arquivo projeto.txt"""
    try:
        with open('projeto.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Projeto não encontrado"

def chamar_ollama(modelo, prompt):
    """Chama o Ollama via API local"""
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False
    }
    
    # Timeout maior para modelos grandes como Gemma2
    timeout = 600 if modelo == "gemma2" else 300
    
    try:
        response = requests.post(url, json=payload, timeout=timeout)
        response.raise_for_status()
        return response.json()['response']
    except Exception as e:
        return f"Erro ao chamar {modelo}: {e}"

def agente_sre(projeto):
    """Agente 1: Engenheiro de Confiabilidade"""
    prompt = f"""Você é um Engenheiro de Confiabilidade (SRE/Performance) sênior especializado em arquitetura de sistemas de alto desempenho e computação em nuvem.

PROJETO A ANALISAR:
{projeto}

SUA TAREFA:
Faça uma análise técnica completa incluindo:

1. ANÁLISE DE PERFORMANCE:
   - Avalie se o processamento em tempo real de 50 câmeras é viável
   - Calcule se 6x NVIDIA A100 são suf​icientes para 100 faces/segundo/câmera
   - Identifique possíveis gargalos de latência (meta: < 500ms)
   - Analise o bandwidth de 2Gbps

2. ANÁLISE DE CUSTOS:
   - Valide se R$ 85.000/mês é realista para AWS
   - Calcule o TCO (Total Cost of Ownership) para 3 anos
   - Avalie o  impacto do crescimento de 5TB/mês

3. ANÁLISE DE ESCALABILIDADE:
   - Projete o sistema com 100 câmeras (2x crescimento)
   - Identifique pontos de falha únicos

4. RECOMENDAÇÕES TÉCNICAS:
   - Liste pelo menos 3 ajustes necessários
   - Forneça estimativas otimizadas

Forneça um relatório técnico estruturado e quantitativo."""
    
    return chamar_ollama("llama3", prompt)

def agente_etica(projeto, analise_tecnica):
    """Agente 2: Especialista em Ética e LGPD"""
    prompt = f"""Você é uma Especialista em Compliance e Ética Digital com formação em Direito Digital e certificações em LGPD/GDPR.

PROJETO ORIGINAL:
{projeto}

ANÁLISE TÉCNICA DO SRE:
{analise_tecnica}

SUA TAREFA:
Avalie o projeto sob a perspectiva da LGPD (Lei Geral de Proteção de Dados) e ética em IA:

1. CONFORMIDADE COM LGPD:
   - Dados biométricos (Art. 5º, II - dados sensíveis)
   - Base legal para tratamento (Art. 7º e 11)
   - Armazenamento por 5 anos sem política de exclusão
   - Compartilhamento com terceiros (Art. 5º, XVIII)
   - Direitos do titular: acesso, correção, exclusão (Art. 18)

2. ÉTICA EM INTELIGÊNCIA ARTIFICIAL:
   - VIÉS ALGORÍTMICO: avaliacute;vel o texto mencionando "viés em reconhecimento de diferentes etnias"
   - TRANSPARÊNCIA: Funcionários são informados?
   - PROPORCIONALIDADE: Sistema adequado ou excessivo?
   - VIGILÂNCIA CONTÍNUA: Captura 24/7 viola privacidade?

3. RISCOS JURÍDICOS:
   - Multas ANPD (até 2% faturamento, máx R$ 50 milhões)
   - Ações trabalhistas por violação de privacidade

4. PARECER FINAL:
   Com base na análise técnica E ética/legal, emita um parecer recomendando:
   - APROVAÇÃO
   - REPROVAÇÃO
   - APROVAÇÃO COM RESSALVAS (liste correções obrigatórias)
   
   Justifique com artigos da LGPD e princípios éticos."""
    
    return chamar_ollama("gemma2", prompt)

def main():
    print("="*80)
    print("COMITÊ DE ANÁLISE DE ÉTICA E VIABILIDADE DE PROJETOS")
    print("Sistema de Dois Agentes Sequenciais")
    print("="*80)
    print()
    
    # Verifica arquivo
    if not os.path.exists('projeto.txt'):
        print("❌ ERRO: Arquivo 'projeto.txt' não encontrado!")
        return
    
    # Verifica conectividade com Ollama
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        modelos = response.json().get('models', [])
        print(f"✅ Ollama conectado ({len(modelos)} modelos disponíveis)")
    except:
        print("❌ ERRO: Ollama não est​á rodando!")
        print("Execute: ollama serve")
        return
    
    print()
    print("📋 Lendo projeto...")
    projeto = ler_projeto()
    print(f"✅ Projeto carregado ({len(projeto)} caracteres)")
    print()
    
    # AGENTE 1: Engenheiro SRE
    print("-" * 80)
    print("🤖 AGENTE 1: Engenheiro de Confiabilidade (SRE/Performance)")
    print("   Modelo: Llama3")
    print("   Tarefa: Análise Técnica e de Custos")
    print("-" * 80)
    print()
    print("⏳ Analisando viabilidade técnica e custos...")
    print()
    
    analise_tecnica = agente_sre(projeto)
    
    print("📊 RELATÓRIO TÉCNICO:")
    print("=" * 80)
    print(analise_tecnica)
    print("=" * 80)
    print()
    
    # Salva o relatório técnico
    with open('relatorio_tecnico.md', 'w', encoding='utf-8') as f:
        f.write(f"# Relatório Técnico de Custos e Performance\n\n")
        f.write(f"**Agente:** Engenheiro de Confiabilidade (SRE)\n")
        f.write(f"**Modelo:** Llama3\n\n")
        f.write(analise_tecnica)
    
    print("💾 Relatório técnico salvo em: relatorio_tecnico.md")
    print()
    
    # AGENTE 2: Especialista em Ética
    print("-" * 80)
    print("🤖 AGENTE 2: Especialista em Compliance e Ética Digital")
    print("   Modelo: Gemma2")
    print("   Tarefa: Análise Ética e LGPD")
    print("   Contexto: Receberá análise do Agente 1")
    print("-" * 80)
    print()    
    print("⏳ Avaliando conformidade LGPD e aspectos éticos...")
    print()
    
    parecer_etico = agente_etica(projeto, analise_tecnica)
    
    print("⚖️ PARECER CONSOLIDADO:")
    print("=" * 80)
    print(parecer_etico)
    print("=" * 80)
    print()
    
    # Salva o parecer final
    with open('parecer_final.md', 'w', encoding='utf-8') as f:
        f.write(f"# Parecer Consolidado - Ética e Viabilidade\n\n")
        f.write(f"**Agente:** Especialista em Compliance e Ética Digital\n")
        f.write(f"**Modelo:** Gemma2\n\n")
        f.write(f"## Análise Técnica (Contexto do Agente 1)\n\n")
        f.write(f"```\n{analise_tecnica[:500]}...\n```\n\n")
        f.write(f"## Parecer Ético e Legal\n\n")
        f.write(parecer_etico)
    
    print("💾 Parecer final salvo em: parecer_final.md")
    print()
    
    print("="*80)
    print("✅ EXECUÇÃO CONCLUÍDA!")
    print("="*80)
    print()
    print("📄 Arquivos gerados:")
    print("  1. relatorio_tecnico.md - Análise do Agente SRE")
    print("  2. parecer_final.md - Parecer do Agente de Ética")
    print()
    print("🎯 TIRE PRINTS DESTA TELA para a entrega da atividade!")
    print()

if __name__ == "__main__":
    main()
