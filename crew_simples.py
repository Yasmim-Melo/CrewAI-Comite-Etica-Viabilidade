#!/usr/bin/env python
"""
Vers​ão simplificada do Comitê de Análise de Ética e Viabilidade
Compatível com CrewAI 0.11.2 e Python 3.14
"""

from crewai import Agent, Task, Crew
import os

# Certifique-se de que o Ollama está rodando
os.environ['OPENAI_API_BASE'] = 'http://localhost:11434/v1'
os.environ['OPENAI_API_KEY'] = 'ollama'  # Ollama não precisa de API key real

def criar_agentes():
    """Cria os agentes especializados"""
    
    # Agente 1: Engenheiro de Confiabilidade
    engenheiro = Agent(
        role='Engenheiro de Confiabilidade (SRE/Performance)',
        goal='Analisar viabilidade técnica e financeira da infraestrutura proposta',
        backstory='''Você é um engenheiro sênior especializado em arquitetura de sistemas 
        de alto desempenho e computação em nuvem. Possui 10 anos de experiência otimizando 
        infraestruturas de processamento em tempo real e análise de custos em ambientes AWS.''',
        verbose=True,
        allow_delegation=False
    )
    
    # Agente 2: Especialista em Ética e LGPD
    especialista = Agent(
        role='Especialista em Compliance e Ética Digital',
        goal='Avaliar conformidade com LGPD e princípios éticos de IA',
        backstory='''Você é uma especialista renomada em privacidade de dados, ética em 
        inteligência artificial e conformidade regulatória. Possui formação em Direito Digital 
        e certificações em proteção de dados (LGPD, GDPR). Atua há 8 anos analisando projetos 
        de IA sob a ótica de viés algorítmico e conformidade legal.''',
        verbose=True,
        allow_delegation=False
    )
    
    return engenheiro, especialista

def ler_projeto():
    """Lê o arquivo projeto.txt"""
    try:
        with open('projeto.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Projeto de exemplo não encontrado."

def criar_tarefas(engenheiro, especialista, conteudo_projeto):
    """Cria as tarefas sequenciais"""
    
    # Tarefa 1: Análise Técnica
    tarefa1 = Task(
        description=f'''Analise o seguinte projeto:\n\n{conteudo_projeto}\n\n
        Faça uma análise técnica completa incluindo:
        1. Análise de Performance (latência, throughput, gargalos)
        2. Análise de Custos (TCO estimado para 3 anos)
        3. Análise de Escalabilidade
        4. Recomendações Técnicas (pelo menos 3 sugestões)
        
        Seja quantitativo e objetivo. Forneça cálculos e estimativas.''',
        agent=engenheiro,
        expected_output='Relatório técnico estruturado com análises quantitativas'
    )
    
    # Tarefa 2: Análise Ética e LGPD
    tarefa2 = Task(
        description='''Com base no relatório técnico anterior e no projeto original, 
        faça uma análise de conformidade LGPD e ética em IA:
        
        1. CONFORMIDADE LGPD:
           - Dados biométricos (Art. 5º, II - dados sensíveis)
           - Base legal para tratamento (Art. 7º e 11)
           - Armazenamento e prazo de retenção
           - Compartilhamento com terceiros
           - Direitos do titular (Art. 18)
        
        2. ÉTICA EM IA:
           - Viés algorítmico (racial, etário)
           - Transparência e consentimento
           - Proporcionalidade
           - Privacidade dos trabalhadores
        
        3. DECISÃO FINAL:
           Emita parecer recomendando:
           - APROVAÇÃO
           - REPROVAÇÃO  
           - APROVAÇÃO COM RESSALVAS (liste as correções obrigatórias)
           
        Justifique com base em artigos da LGPD e princípios éticos.''',
        agent=especialista,
        expected_output='Parecer consolidado com decisão fundamentada',
        context=[tarefa1]  # Recebe contexto da tarefa anterior
    )
    
    return tarefa1, tarefa2

def main():
    """Função principal"""
    print("="*80)
    print("COMITÊ DE ANÁLISE DE ÉTICA E VIABILIDADE DE PROJETOS")
    print("="*80)
    print()
    
    # Verifica se projeto.txt existe
    if not os.path.exists('projeto.txt'):
        print("❌ ERRO: Arquivo 'projeto.txt' não encontrado!")
        return
    
    print("📋 Carregando projeto")
    conteudo_projeto = ler_projeto()
    
    print("📋 Criando agentes...")
    engenheiro, especialista = criar_agentes()
    print(f"✅ Agente 1: {engenheiro.role}")
    print(f"✅ Agente 2: {especialista.role}")
    print()
    
    print("📋 Criando tarefas. ..")
    tarefa1, tarefa2 = criar_tarefas(engenheiro, especialista, conteudo_projeto)
    print("✅ Tarefa 1: Análise Técnica e de Custos")
    print("✅ Tarefa 2: Análise Ética e LGPD")
    print()
    
    print("🚀 Iniciando execução do Crew (modo sequencial)...")
    print()
    
    # Cria e executa o Crew
    crew = Crew(
        agents=[engenheiro, especialista],
        tasks=[tarefa1, tarefa2],
        verbose=True
    )
    
    resultado = crew.kickoff()
    
    print()
    print("="*80)
    print("EXECUÇÃO CONCLUÍDA")
    print("="*80)
    print()
    print("RESULTADO FINAL:")
    print("="*80)
    print(resultado)
    print()
    
    # Salva o resultado
    with open('parecer_final.txt', 'w', encoding='utf-8') as f:
        f.write(str(resultado))
    print("📄 Parecer salvo em: parecer_final.txt")

if __name__ == "__main__":
    main()
