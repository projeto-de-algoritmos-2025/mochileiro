# Documentação Técnica - Jogo do Mochileiro

## Arquitetura do Sistema

### Estrutura Principal (`main.py`)

#### Classes Principais

**1. `Item`**
- Representa um item disponível para a mochila
- Propriedades: `name`, `weight`, `value`, `selected`

**2. `KnapsackGame`**
- Classe principal que gerencia todo o jogo
- Controla interface, lógica e algoritmos

#### Métodos Principais

**Inicialização:**
- `__init__()` - Configura pygame, itens e botões
- `create_buttons()` - Cria elementos da interface

**Interação:**
- `handle_click(pos)` - Processa cliques do mouse
- `toggle_item(item_index)` - Adiciona/remove itens
- `reset_game()` - Reinicia o jogo

**Algoritmo:**
- `solve_knapsack()` - Implementa DP para solução ótima
- Constrói tabela DP iterativamente
- Reconstrói solução através de backtracking

**Visualização:**
- `draw()` - Renderiza toda a interface
- `draw_text()` - Renderiza texto
- `draw_button()` - Renderiza botões
- `draw_dp_table()` - Renderiza tabela de DP

#### Algoritmo de Programação Dinâmica

```python
# Pseudocódigo da implementação
for i in range(1, n + 1):
    for weight in range(1, max_weight + 1):
        item = items[i - 1]
        
        if item.weight <= weight:
            include_value = item.value + dp[i-1][weight - item.weight]
            exclude_value = dp[i-1][weight]
            dp[i][weight] = max(include_value, exclude_value)
        else:
            dp[i][weight] = dp[i-1][weight]
```

#### Reconstrução da Solução

```python
# Backtracking para encontrar itens selecionados
weight = max_weight
for i in range(n, 0, -1):
    if dp[i][weight] != dp[i-1][weight]:
        # Item i foi incluído na solução ótima
        selected_items.append(items[i-1])
        weight -= items[i-1].weight
```

## Estrutura da Interface

### Layout da Tela (1200x800)

**Área Esquerda (0-440px):**
- Título e informações da mochila
- Lista de itens com botões
- Status atual (peso/valor)
- Botões de ação (Resolver DP, Reset)

**Área Direita (450-1200px):**
- Tabela de Programação Dinâmica
- Solução ótima calculada
- Comparação de resultados
- Análise de eficiência

### Cores e Estilo

```python
BACKGROUND_COLOR = (245, 245, 245)    # Cinza claro
BUTTON_COLOR = (70, 130, 180)         # Azul
SUCCESS_COLOR = (34, 139, 34)         # Verde
ERROR_COLOR = (220, 20, 60)           # Vermelho
HEADER_COLOR = (25, 25, 112)          # Azul escuro
```

## Fluxo de Execução

1. **Inicialização**
   - Pygame setup
   - Criação de itens predefinidos
   - Setup da interface

2. **Loop Principal**
   - Captura eventos (cliques, teclas)
   - Processa interações
   - Atualiza estado do jogo
   - Renderiza interface

3. **Resolução DP**
   - Constrói matriz DP
   - Calcula valor ótimo
   - Reconstrói solução
   - Exibe resultados

## Performance e Complexidade

### Complexidade Temporal
- **Algoritmo DP**: O(n × W)
  - n = número de itens (10)
  - W = capacidade da mochila (15)
  - Total: ~150 operações

### Complexidade Espacial
- **Tabela DP**: O(n × W) = ~150 células
- **Memória adicional**: O(n) para reconstrução

### Otimizações Implementadas
- Interface responsiva (60 FPS)
- Renderização eficiente
- Estruturas de dados simples
- Algoritmo DP clássico (não otimizado em espaço)

## Extensibilidade

### Adicionando Novos Itens
```python
# Em __init__() da classe KnapsackGame
self.items.append(Item("Nome", peso, valor))
```

### Modificando Capacidade
```python
self.max_weight = nova_capacidade
```

### Personalizando Interface
- Modificar constantes de cores
- Ajustar posições em `draw()` e `create_buttons()`
- Alterar fontes e tamanhos

## Testes e Validação

### Casos de Teste Implementados
- Solução ótima conhecida: R$ 2.150
- Verificação de peso máximo
- Validação da tabela DP
- Comparação com algoritmo guloso

### Debugging
- Mensagens de erro para peso excedido
- Verificação de cliques válidos
- Validação de estado do jogo

## Dependências

### Pygame 2.5.2
- Renderização gráfica
- Gerenciamento de eventos
- Loop de jogo

### Python 3.6+
- Type hints
- F-strings
- Métodos de lista modernos

## Arquivos de Configuração

- **`requirements.txt`**: Dependências Python
- **`start.sh`**: Script de inicialização
- **`.git/`**: Controle de versão

---

**Esta documentação técnica serve como referência para desenvolvedores que queiram entender ou modificar o código do jogo.**
