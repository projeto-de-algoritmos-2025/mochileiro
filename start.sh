#!/bin/bash

# Script de inicialização do Jogo do Mochileiro
echo "🎒 Iniciando o Jogo do Mochileiro..."

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Por favor, instale o Python3."
    exit 1
fi

# Verificar se pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Por favor, instale o pip3."
    exit 1
fi

# Instalar dependências
echo "📦 Instalando dependências..."
pip3 install -r requirements.txt

# Verificar se a instalação foi bem-sucedida
if [ $? -eq 0 ]; then
    echo "✅ Dependências instaladas com sucesso!"
    echo ""
    echo "🎮 Iniciando o jogo..."
    echo "   Use as setas e mouse para interagir"
    echo "   Feche a janela ou pressione ESC para sair"
    echo ""
    python3 main.py
else
    echo "❌ Erro ao instalar dependências."
    exit 1
fi
