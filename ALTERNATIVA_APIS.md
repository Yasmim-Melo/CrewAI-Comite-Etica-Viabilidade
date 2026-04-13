# 🌐 GUIA: Usar APIs Online ao invés de Ollama Local

Se você não quer instalar Ollama, pode usar APIs online (algumas gratuitas!).

## 🎯 OPÇÃO RECOMENDADA: Groq (GRATUITO e RÁPIDO)

### Passo 1: Criar conta gratuita no Groq
1. Acesse: https://console.groq.com/
2. Crie uma conta (gratuita, sem cartão de crédito)
3. Vá em "API Keys" e crie uma nova chave

### Passo 2: Configurar a chave no Windows
No PowerShell, execute:
```powershell
$env:GROQ_API_KEY = "sua_chave_aqui"
```

### Passo 3: Modificar o agents.yaml
Substitua o conteúdo do agents.yaml pelo agents_online.yaml:
```powershell
Copy-Item agents_online.yaml agents.yaml -Force
```

### Passo 4: Descomentar as linhas do Groq no agents.yaml
Abra o `agents.yaml` e modifique:

**No engenheiro_confiabilidade:**
```yaml
  # Comente esta linha:
  # llm: gpt-4o-mini
  
  # Descomente esta:
  llm: groq/llama-3.1-8b-instant
```

**No especialista_etica:**
```yaml
  # Comente esta linha:
  # llm: gpt-4o
  
  # Descomente esta:
  llm: groq/llama-3.1-70b-versatile
```

### Passo 5: Executar normalmente
```powershell
python crew.py
```

---

## 💰 Outras Opções de APIs

### OpenAI (Pago - ~$0.01 por execução)
```powershell
$env:OPENAI_API_KEY = "sua_chave_aqui"
```
Use no agents.yaml:
- `llm: gpt-4o-mini` (mais barato)
- `llm: gpt-4o` (melhor qualidade)

### Anthropic Claude (Pago - ~$0.02 por execução)
```powershell
$env:ANTHROPIC_API_KEY = "sua_chave_aqui"
```
Use no agents.yaml:
- `llm: claude-3-5-sonnet-20241022`

---

## 🔄 Script Automático para Usar Groq

Criei um script que facilita tudo. Siga os passos:

1. **Obtenha sua chave Groq** em: https://console.groq.com/
2. **Execute no PowerShell:**

```powershell
# Definir a chave (substitua pela sua)
$env:GROQ_API_KEY = "gsk_sua_chave_aqui"

# Fazer backup do agents.yaml original
Copy-Item agents.yaml agents_ollama.yaml

# Usar versão online
Copy-Item agents_online.yaml agents.yaml

# Agora execute
python crew.py
```

---

## ✅ Qual opção escolher?

| Opção | Custo | Velocidade | Instalação | Privacidade |
|-------|-------|------------|------------|-------------|
| **Ollama (local)** | ✅ Grátis | 🟡 Média | 🔴 Requer instalação | ✅ 100% privado |
| **Groq API** | ✅ Grátis | ✅ Rápido | ✅ Sem instalação | 🟡 Dados vão para nuvem |
| **OpenAI** | 🔴 Pago | ✅ Rápido | ✅ Sem instalação | 🟡 Dados vão para nuvem |

**Recomendação:** 
- **Para aprendizado:** Groq (gratuito e rápido)
- **Para produção:** Ollama (privado e sem custos contínuos)
