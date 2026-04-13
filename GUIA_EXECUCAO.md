# 🚀 GUIA COMPLETO DE EXECUÇÃO - PASSO A PASSO

## Checklist Rápido

Antes de executar, verifique:
- [ ] Python 3.10+ instalado
- [ ] Ollama instalado
- [ ] Modelos llama3 e gemma2 baixados no Ollama
- [ ] Dependências Python instaladas

---

## PASSO 1: Instalar Ollama (se ainda não tiver)

### Windows

1. Acesse: https://ollama.ai/download
2. Baixe o instalador para Windows
3. Execute o instalador
4. Abra um novo terminal PowerShell

### Verificar instalação:
```powershell
ollama --version
```

---

## PASSO 2: Baixar os Modelos LLM

No terminal PowerShell, execute:

```powershell
# Baixar Llama3 (para análise técnica)
ollama pull llama3

# Baixar Gemma2 (para análise ética)
ollama pull gemma2
```

**Tempo estimado**: 5-15 minutos dependendo da conexão.

### Verificar se os modelos foram instalados:
```powershell
ollama list
```

Você deve ver algo como:
```
NAME            ID              SIZE      MODIFIED
llama3:latest   ...             4.7 GB    X days ago
gemma2:latest   ...             5.4 GB    X days ago
```

---

## PASSO 3: Configurar o Ambiente Python

### Navegar até o diretório do projeto:
```powershell
cd C:\Users\yasmi\Downloads\CrewAI_project
```

### Criar ambiente virtual (RECOMENDADO):
```powershell
python -m venv venv
```

### Ativar o ambiente virtual:
```powershell
.\venv\Scripts\Activate.ps1
```

Se der erro de política de execução, execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois tente ativar novamente.

### Instalar dependências:
```powershell
pip install -r requirements.txt
```

---

## PASSO 4: Verificar Arquivos do Projeto

Certifique-se de que os seguintes arquivos existem:

```
CrewAI_project/
├── agents.yaml          ✓ Configuração dos agentes
├── tasks.yaml           ✓ Configuração das tarefas
├── crew.py             ✓ Código principal
├── projeto.txt         ✓ Projeto a ser analisado
└── requirements.txt    ✓ Dependências
```

---

## PASSO 5: Executar o Sistema

### Certifique-se de que Ollama está rodando:
```powershell
# Em um terminal separado (opcional, Ollama geralmente roda como serviço)
ollama serve
```

### Execute o crew:
```powershell
python crew.py
```

---

## PASSO 6: Acompanhar a Execução

Você verá no terminal:

```
================================================================================
COMITÊ DE ANÁLISE DE ÉTICA E VIABILIDADE DE PROJETOS
================================================================================

Iniciando análise do projeto...

📋 Carregando agentes...
✅ Agente 1: Engenheiro de Confiabilidade (SRE/Performance)
✅ Agente 2: Especialista em Compliance e Ética Digital

📋 Carregando tarefas...
✅ Tarefa 1: Análise Técnica e de Custos
✅ Tarefa 2: Análise Ética e LGPD

🚀 Iniciando execução do Crew (modo sequencial)...
```

**IMPORTANTE**: Tire um **print desta tela** enquanto o sistema está executando!

### O que você verá durante a execução:

1. **Agente 1 trabalhando** (Engenheiro de Confiabilidade):
   - Lendo o arquivo projeto.txt
   - Analisando custos, performance, escalabilidade
   - Gerando o arquivo `relatorio_tecnico.md`

2. **Agente 2 trabalhando** (Especialista em Ética):
   - Recebendo o relatório do Agente 1
   - Analisando conformidade LGPD
   - Avaliando aspectos éticos
   - Gerando o arquivo `parecer_final.md`

---

## PASSO 7: Verificar Resultados

Após a execução, dois arquivos serão criados:

### 1. relatorio_tecnico.md
Contém a análise técnica de custos e performance.

### 2. parecer_final.md
Contém o parecer consolidado com recomendação final:
- **APROVAÇÃO**
- **REPROVAÇÃO**
- **APROVAÇÃO COM RESSALVAS**

Abra estes arquivos para ver as análises completas!

---

## PASSO 8: Capturar Evidências para o PDF

Para a entrega da atividade, você precisa:

### 1. Código Fonte
Abra e copie o conteúdo de:
- `agents.yaml`
- `tasks.yaml`
- `crew.py`

### 2. Evidência de Execução
**TIRE PRINTS** do terminal mostrando:
- ✅ Início da execução com carregamento dos agentes
- ✅ Logs da execução (mensagens trocadas entre agentes)
- ✅ Conclusão com "EXECUÇÃO CONCLUÍDA"

### 3. Justificativa de Modelos
Copie o conteúdo do arquivo:
- `JUSTIFICATIVA_MODELOS.md`

### 4. Resultados (OPCIONAL, mas recomendado)
Inclua trechos dos arquivos gerados:
- `relatorio_tecnico.md`
- `parecer_final.md`

---

## ⚠️ Possíveis Problemas e Soluções

### Erro: "Ollama connection refused"
**Solução**: Certifique-se de que Ollama está rodando:
```powershell
ollama serve
```

### Erro: "Model not found"
**Solução**: Baixe os modelos novamente:
```powershell
ollama pull llama3
ollama pull gemma2
```

### Erro: "FileReadTool cannot read projeto.txt"
**Solução**: Certifique-se de estar no diretório correto:
```powershell
cd C:\Users\yasmi\Downloads\CrewAI_project
ls  # Deve mostrar projeto.txt
```

### Execução muito lenta
**Solução**: 
- Modelos LLM locais podem ser lentos
- Aguarde pacientemente (pode levar 5-15 minutos)
- Verifique se seu computador tem RAM suficiente (mínimo 16GB recomendado)

### Agentes não trocam mensagens visíveis
**Solução**: Já está configurado `verbose: True` nos agentes. Os logs devem aparecer automaticamente.

---

## 📋 Resumo Final

1. ✅ Instalar Ollama
2. ✅ Baixar modelos (llama3, gemma2)
3. ✅ Criar ambiente virtual Python
4. ✅ Instalar dependências (pip install -r requirements.txt)
5. ✅ Executar: `python crew.py`
6. ✅ Capturar prints do terminal
7. ✅ Coletar os arquivos gerados
8. ✅ Montar o PDF com código + prints + justificativa

---

## 🎯 Dica Final

Para impressionar na entrega:
- 📸 Tire prints claros e legíveis do terminal
- 📝 Inclua trechos relevantes dos relatórios gerados
- 🎨 Formate bem o PDF (use cabeçalhos, negritos, organize por seções)
- 👥 Não esqueça de colocar o nome dos DOIS acadêmicos no PDF

**Boa sorte com a atividade! 🚀**
