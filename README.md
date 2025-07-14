# Jogo do Mochileiro (Knapsack Game Show)

## 📋 Descrição
Um jogo educacional interativo que implementa o problema clássico do **0/1 Knapsack** usando **Programação Dinâmica**. O jogador deve selecionar itens para maximizar o valor total respeitando o limite de peso da mochila, comparando sua solução com a solução ótima calculada pelo algoritmo.

## 👥 Alunos
| Matrícula | Nome |
|----------|------|
| 222006641 | Davi de Aguiar Vieira |
| 222006801 | Henrique Carvalho Neves |

## 📝 Entregas
| Programação Dinâmica |
|----------|
| [Apresentação](https://www.youtube.com/watch?v=Q5gyoOPqcGo)
---

### Versão Anterior (1.0)
- ✅ Interface gráfica interativa com Pygame
- ✅ Seleção manual de itens pelo jogador
- ✅ Resolução automática usando Programação Dinâmica
- ✅ Visualização completa da tabela de DP
- ✅ Comparação entre solução manual e ótima
- ✅ Feedback educacional sobre eficiência
- ✅ 10 itens predefinidos com diferentes pesos e valores
- ✅ Mochila com capacidade de 15kg

### Versão Atual (2.0)
- ✅ Visualização animada da construção da tabela DP
- ✅ Modo de demonstração passo-a-passo
- ✅ Explicações em texto do algoritmo durante execução
- ✅ Histórico de tentativas do jogador
- ✅ Sistema de pontuação e ranking

## 🚀 Como Executar

### Método 1: Script de Inicialização (Recomendado)
```bash
./start.sh
```

### Método 2: Manual
```bash
# Instalar dependências
pip3 install -r requirements.txt

# Executar o jogo
python3 main.py

# Executar demonstração do algoritmo
python3 algoritmo_demo.py
```

## 📚 Arquivos do Projeto

- **`main.py`** - Jogo principal com interface gráfica
- **`algoritmo_demo.py`** - Demonstração textual do algoritmo de DP
- **`COMO_JOGAR.md`** - Tutorial completo de como jogar
- **`ROADMAP.md`** - Planejamento de melhorias futuras
- **`requirements.txt`** - Dependências do projeto
- **`start.sh`** - Script de inicialização automatizada

## 🎯 Como Jogar

1. **Seleção Manual**:
   - Clique em "Adicionar" para incluir um item na mochila
   - Clique em "Remover" para retirar um item da mochila
   - Observe o peso total (máximo: 15kg)
   - Tente maximizar o valor total

2. **Verificar Solução Ótima**:
   - Clique em "Resolver com DP" 
   - Analise a tabela de Programação Dinâmica
   - Compare sua solução com a solução ótima

3. **Análise de Resultados**:
   - Veja sua eficiência em relação à solução ótima
   - Estude os itens selecionados pelo algoritmo
   - Use "Reset" para tentar novamente

## 🧮 Algoritmo Implementado

### Programação Dinâmica (DP)
```
DP[i][w] = valor máximo usando os primeiros i itens com peso máximo w

DP[i][w] = max(
    DP[i-1][w],                           // não incluir item i
    DP[i-1][w-peso[i]] + valor[i]         // incluir item i (se peso[i] ≤ w)
)
```

**Complexidade**: O(n × W), onde n é o número de itens e W é a capacidade da mochila.

## 📊 Itens do Jogo

| Item       | Peso | Valor | Ratio V/P |
|------------|------|-------|-----------|
| Smartphone | 2kg  | R$300 | 150.00    |
| Notebook   | 5kg  | R$800 | 160.00    |
| Câmera     | 3kg  | R$450 | 150.00    |
| Livro      | 1kg  | R$50  | 50.00     |
| Tablet     | 2kg  | R$250 | 125.00    |
| Fones      | 1kg  | R$100 | 100.00    |
| Carregador | 1kg  | R$30  | 30.00     |
| Roupas     | 3kg  | R$80  | 26.67     |
| Remédios   | 1kg  | R$200 | 200.00    |
| Snacks     | 2kg  | R$40  | 20.00     |

**Solução Ótima**: R$ 2.150 (7 itens, 15kg - 100% da capacidade)

## 🛠️ Requisitos Técnicos

- **Python 3.6+**
- **Pygame 2.5.2**
- **Sistema Operacional**: Linux, Windows, macOS
- **Memória**: Mínimo 512MB RAM
- **Tela**: Resolução mínima 1200x800

## 🎓 Objetivo Educacional

Este jogo foi desenvolvido para:
- Introduzir visualmente o problema do 0/1 Knapsack
- Demonstrar a eficiência da Programação Dinâmica
- Comparar solução manual vs. algoritmo ótimo
- Facilitar o entendimento de subproblemas e tabela DP
- Incentivar o estudo de algoritmos de otimização

## 🤝 Contribuições

Contribuições são bem-vindas! Consulte `ROADMAP.md` para ideias de melhorias.

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

---

**Desenvolvido como projeto educacional para demonstração de algoritmos de Programação Dinâmica.**
