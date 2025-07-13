# Como Jogar - Jogo do Mochileiro

## Objetivo
Selecione itens para colocar em uma mochila com peso máximo de 15kg, tentando maximizar o valor total dos itens escolhidos.

## Interface do Jogo

### Área Principal (Esquerda)
- **Lista de Itens Disponíveis**: Mostra todos os itens com peso e valor
- **Status da Mochila**: Peso e valor total atual
- **Botões de Ação**:
  - **Adicionar/Remover**: Para cada item
  - **Resolver com DP**: Calcula a solução ótima
  - **Reset**: Limpa a seleção atual

### Área de Resultados (Direita)
- **Tabela de Programação Dinâmica**: Mostra como o algoritmo calcula a solução
- **Solução Ótima**: Lista dos itens que maximizam o valor
- **Comparação**: Sua solução vs. solução ótima

## Como Jogar

1. **Seleção Manual**:
   - Clique em "Adicionar" para incluir um item na mochila
   - Clique em "Remover" para retirar um item
   - Observe o peso total (não pode exceder 15kg)
   - Tente maximizar o valor total

2. **Verificar Solução Ótima**:
   - Clique em "Resolver com DP" para ver a melhor solução possível
   - Compare sua escolha com a solução ótima
   - Analise a tabela de Programação Dinâmica

3. **Recomeçar**:
   - Use "Reset" para limpar e tentar novamente

## Dicas de Estratégia

- Procure itens com boa relação valor/peso
- Não se esqueça de considerar combinações de itens menores
- O algoritmo de Programação Dinâmica sempre encontra a solução ótima
- Tente diferentes combinações para entender o problema

## Algoritmo de Programação Dinâmica

O jogo implementa a solução clássica do problema 0/1 Knapsack:

```
DP[i][w] = valor máximo usando os primeiros i itens com peso máximo w

DP[i][w] = max(
    DP[i-1][w],                           // não incluir item i
    DP[i-1][w-peso[i]] + valor[i]         // incluir item i
)
```

A tabela mostra todos os subproblemas calculados para chegar à solução ótima.
