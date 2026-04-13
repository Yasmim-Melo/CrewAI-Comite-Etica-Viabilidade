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

## 🎯 Justificativa dos Modelos LLM

### Agente 1 - Engenheiro de Confiabilidade: Llama3

**Por que Llama3?**

O modelo Llama3 foi escolhido para a tarefa de análise técnica e custos pelos seguintes motivos:

- **Forte capacidade lógica e matemática**: Llama3 demonstra excelente performance em raciocínio quantitativo, essencial para cálculos de TCO (Total Cost of Ownership), estimativas de performance e análise de escalabilidade
- **Foco em código e arquitetura**: Modelos da família Llama são treinados com grande ênfase em código e documentação técnica, tornando-os ideais para avaliar arquiteturas de sistemas, identificar gargalos e propor otimizações
- **Eficiência**: Com 8B de parâmetros, oferece excelente custo-benefício para tarefas técnicas objetivas, mantendo latência baixa
- **Raciocínio estruturado**: Capacidade de seguir metodologias de análise (performance → custos → escalabilidade → recomendações) de forma sistemática

### Agente 2 - Especialista em Ética e LGPD: Gemma2

**Por que Gemma2?**

O modelo Gemma2 foi selecionado para análise ética e legal pelos seguintes motivos:

- **Alta capacidade de nuance e contexto**: Gemma2, desenvolvido pelo Google, possui forte habilidade em entender contextos complexos e nuances legais, fundamentais para interpretar artigos da LGPD
- **Raciocínio ético sofisticado**: Demonstra capacidade superior em análise de dilemas éticos, identificação de viés algorítmico e avaliação de impactos sociais
- **Argumentação estruturada**: Excelente em construir argumentos fundamentados com citações legais e justificativas coerentes
- **Consciência de riscos**: Modelo otimizado para identificar riscos de compliance, privacidade e questões sensíveis relacionadas a dados pessoais
- **Linguagem natural fluente**: Produz pareceres bem articulados, essenciais para documentos que podem ser apresentados a stakeholders não-técnicos

### Por que dois LLMs diferentes?

A separação de modelos otimiza a qualidade da análise:

- **Especialização**: Cada modelo foca em sua área de expertise (técnica vs. legal/ética)
- **Complementaridade**: Llama3 fornece dados quantitativos objetivos, Gemma2 adiciona análise qualitativa e contextual
- **Redução de viés**: Usar modelos diferentes evita vieses sistemáticos de um único modelo
- **Qualidade do parecer final**: O Gemma2 recebe análise técnica estruturada e pode focar em argumentação ética sem precisar "fazer matemática"

## 📁 Arquivos de Entrega

Para a atividade acadêmica, você precisa entregar (PDF único):

1. ✅ **Código Fonte**: Conteúdo de `agents.yaml`, `tasks.yaml` e `crew.py`
2. ✅ **Evidência de Execução**: Print do terminal com log de execução
3. ✅ **Justificativa de Modelos**: Texto acima explicando escolha dos LLMs

## 🔧 Personalização

Para analisar outro projeto, edite o arquivo `projeto.txt` com a nova descrição.

## 📝 Observações Importantes

- O sistema usa **processo sequencial**: Agente 2 só executa APÓS o Agente 1 terminar
- A ferramenta `FileReadTool` permite que o Agente 1 leia o arquivo `projeto.txt`
- Agente 2 recebe o contexto da análise do Agente 1 automaticamente
- Logs verbosos mostram a "conversa" entre os agentes no terminal

## 🎓 Créditos Acadêmicos

Desenvolvido para atividade de Inteligência Artificial - Análise de Ética e Viabilidade com CrewAI.
