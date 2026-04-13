# Script para executar com Groq API
# Carrega a chave do arquivo .env e executa o crew

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Executando com Groq API (Online)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Carrega variáveis do arquivo .env
if (Test-Path ".env") {
    Write-Host "✅ Carregando configurações do .env..." -ForegroundColor Green
    Get-Content .env | ForEach-Object {
        if ($_ -match '^\s*([^#][^=]+)=(.+)$') {
            $name = $matches[1].Trim()
            $value = $matches[2].Trim()
            Set-Item -Path "env:$name" -Value $value
            Write-Host "   → $name configurado" -ForegroundColor Gray
        }
    }
    Write-Host ""
} else {
    Write-Host "❌ Arquivo .env não encontrado!" -ForegroundColor Red
    Write-Host "Crie um arquivo .env com sua GROQ_API_KEY" -ForegroundColor Yellow
    exit 1
}

# Verifica se a chave foi carregada
if ([string]::IsNullOrWhiteSpace($env:GROQ_API_KEY)) {
    Write-Host "❌ GROQ_API_KEY não encontrada no .env!" -ForegroundColor Red
    exit 1
}

Write-Host "🔑 API Key carregada com sucesso!" -ForegroundColor Green
Write-Host ""

# Atualizar agents.yaml para usar Groq (se necessário)
$agentsContent = Get-Content "agents.yaml" -Raw
if ($agentsContent -match "ollama/") {
    Write-Host "⚠️  agents.yaml está configurado para Ollama" -ForegroundColor Yellow
    Write-Host "   Sugestão: Use agents_online.yaml ou atualize para groq/" -ForegroundColor Yellow
    Write-Host ""
}

# Executar o crew
Write-Host "🚀 Iniciando execução..." -ForegroundColor Cyan
Write-Host ""

.\venv\Scripts\python.exe crew_direto.py

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "           Execução concluída!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
