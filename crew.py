#!/usr/bin/env python
"""
Comitê de Análise de Ética e Viabilidade de Projetos de Software
Sistema de dois agentes sequenciais usando CrewAI
"""

from crewai import Agent, Task, Crew, Process
from crewai_tools import FileReadTool
import yaml
import os

def carregar_config(arquivo):
    """Carrega configurações dos arquivos YAML"""
    with open(arquivo, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def criar_agentes():
    """Cria os agentes a partir do arquivo agents.yaml"""
    config_agentes = carregar_config('agents.yaml')
    
    # Ferramenta para leitura de arquivos
    file_read_tool = FileReadTool(
        file_path='projeto.txt',
        description='Ferramenta para ler o arquivo projeto.txt que contém a descrição do projeto a ser analisado'
    )
    
    # Agente 1: Engenheiro de Confiabilidade (SRE/Performance)
    config_sre = config_agentes['engenheiro_confiabilidade']
    engenheiro = Agent(
        role=config_sre['role'],
        goal=config_sre['goal'],
        backstory=config_sre['backstory'],
        verbose=config_sre['verbose'],
        allow_delegation=config_sre['allow_delegation'],
        llm=config_sre['llm'],
        max_iter=config_sre['max_iter'],
        tools=[file_read_tool]
    )
    
    # Agente 2: Especialista em Compliance e Ética Digital
    config_etica = config_agentes['especialista_etica']
    especialista = Agent(
        role=config_etica['role'],
        goal=config_etica['goal'],
        backstory=config_etica['backstory'],
        verbose=config_etica['verbose'],
        allow_delegation=config_etica['allow_delegation'],
        llm=config_etica['llm'],
        max_iter=config_etica['max_iter'],
        tools=[]  # Não precisa ler arquivo, recebe contexto do agente anterior
    )
    
    return engenheiro, especialista

def criar_tarefas(engenheiro, especialista):
    """Cria as tarefas a partir do arquivo tasks.yaml"""
    config_tarefas = carregar_config('tasks.yaml')
    
    # Ferramenta para leitura de arquivos
    file_read_tool = FileReadTool(
        file_path='projeto.txt',
        description='Ferramenta para ler o arquivo projeto.txt'
    )
    
    # Tarefa 1: Análise Técnica e de Custos
    config_task1 = config_tarefas['analise_tecnica_custos']
    tarefa_tecnica = Task(
        description=config_task1['description'],
        expected_output=config_task1['expected_output'],
        agent=engenheiro,
        tools=[file_read_tool],
        output_file=config_task1['output_file']
    )
    
    # Tarefa 2: Análise Ética e LGPD
    config_task2 = config_tarefas['analise_etica_lgpd']
    tarefa_etica = Task(
        description=config_task2['description'],
        expected_output=config_task2['expected_output'],
        agent=especialista,
        context=[tarefa_tecnica],  # Recebe output da tarefa anterior
        output_file=config_task2['output_file']
    )
    
    return tarefa_tecnica, tarefa_etica

def main():
    """Função principal que executa o Crew"""
    print("="*80)
    print("COMITÊ DE ANÁLISE DE ÉTICA E VIABILIDADE DE PROJETOS")
    print("="*80)
    print()
    print("Iniciando análise do projeto...")
    print()
    
    # Verifica se o arquivo projeto.txt existe
    if not os.path.exists('projeto.txt'):
        print("❌ ERRO: Arquivo 'projeto.txt' não encontrado!")
        print("Por favor, crie o arquivo com a descrição do projeto.")
        return
    
    # Cria os agentes
    print("📋 Carregando agentes...")
    engenheiro, especialista = criar_agentes()
    print(f"✅ Agente 1: {engenheiro.role}")
    print(f"✅ Agente 2: {especialista.role}")
    print()
    
    # Cria as tarefas
    print("📋 Carregando tarefas...")
    tarefa_tecnica, tarefa_etica = criar_tarefas(engenheiro, especialista)
    print(f"✅ Tarefa 1: Análise Técnica e de Custos")
    print(f"✅ Tarefa 2: Análise Ética e LGPD")
    print()
    
    # Cria o Crew (equipe sequencial)
    print("🚀 Iniciando execução do Crew (modo sequencial)...")
    print()
    
    crew = Crew(
        agents=[engenheiro, especialista],
        tasks=[tarefa_tecnica, tarefa_etica],
        process=Process.sequential,  # Processo SEQUENCIAL é fundamental
        verbose=True
    )
    
    # Executa o Crew
    resultado = crew.kickoff()
    
    print()
    print("="*80)
    print("EXECUÇÃO CONCLUÍDA")
    print("="*80)
    print()
    print("📄 Relatórios gerados:")
    print("  - relatorio_tecnico.md (Análise de Custos e Performance)")
    print("  - parecer_final.md (Parecer Consolidado de Ética e LGPD)")
    print()
    print("="*80)
    print("RESULTADO FINAL:")
    print("="*80)
    print(resultado)
    print()

if __name__ == "__main__":
    main()
