# Comitê de Análise de Ética e Viabilidade - CrewAI

Sistema de análise sequencial com dois agentes especializados para avaliar projetos de software sob perspectivas técnica, ética e legal.

## 📋 Descrição

Este projeto implementa um comitê automatizado que analisa propostas de projetos de software através de dois agentes especializados:

1. **Engenheiro de Confiabilidade (SRE)**: Analisa viabilidade técnica, performance e custos
2. **Especialista em Ética e LGPD**: Avalia conformidade legal e aspectos éticos

## 🏗️ Estrutura do Projeto

```
CrewAI_project/
│
├── agents.yaml           # Definição dos agentes
├── tasks.yaml            # Definição das tarefas
├── crew.py              # Código principal de execução
├── projeto.txt          # Descrição do projeto a ser analisado
├── requirements.txt     # Dependências Python
└── README.md           # Este arquivo
```

## 🚀 Como Executar

### Pré-requisitos

1. **Python 3.10 ou superior**
2. **Ollama** instalado e rodando localmente
3. Modelos LLM baixados no Ollama:
   - `llama3` (para análise técnica)
   - `gemma2` (para análise ética)

### Instalação do Ollama

**Windows:**
```powershell
# Baixe o instalador em: https://ollama.ai/download
# Após instalar, abra o terminal e baixe os modelos:
ollama pull llama3
ollama pull gemma2
```

**Verificar se Ollama está rodando:**
```powershell
ollama list
```

### Instalação do Projeto

1. **Clone ou navegue até o diretório do projeto:**
```powershell
cd C:\Users\yasmi\Downloads\CrewAI_project
```

2. **Crie um ambiente virtual (recomendado):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Instale as dependências:**
```powershell
pip install -r requirements.txt
```

### Execução

```powershell
python crew.py
```

## 📊 Saída Esperada

O sistema gerará dois arquivos:

1. **relatorio_tecnico.md**: Análise técnica de custos, performance e viabilidade
2. **parecer_final.md**: Parecer consolidado com recomendação final (Aprovação/Reprovação/Aprovação com Ressalvas)

## 📝 Observações Importantes

- O sistema usa **processo sequencial**: Agente 2 só executa APÓS o Agente 1 terminar
- A ferramenta `FileReadTool` permite que o Agente 1 leia o arquivo `projeto.txt`
- Agente 2 recebe o contexto da análise do Agente 1 automaticamente
- Logs verbosos mostram a "conversa" entre os agentes no terminal

