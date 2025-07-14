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
  - **Demonstração Passo-a-Passo**: Visualiza a construção da tabela DP animadamente
  - **Próximo Passo**: Avança a animação da DP
  - **Reset**: Limpa a seleção atual

### Área de Resultados (Direita)
- **Tabela de Programação Dinâmica**: Mostra como o algoritmo calcula a solução (agora animada no modo demonstração)
- **Solução Ótima**: Lista dos itens que maximizam o valor
- **Comparação**: Sua solução vs. solução ótima
- **Explicações do Algoritmo**: Mostra o raciocínio do DP em cada passo
- **Histórico de Tentativas**: Lista as últimas tentativas do jogador
- **Ranking**: Mostra as melhores pontuações


## Como Jogar

1. **Seleção Manual**:
   - Clique em "Adicionar" para incluir um item na mochila
   - Clique em "Remover" para retirar um item
   - Observe o peso total (não pode exceder 15kg)
   - Tente maximizar o valor total

2. **Demonstração Passo-a-Passo**:
   - Clique em "Demonstração Passo-a-Passo" para ver a construção animada da tabela DP
   - Use "Próximo Passo" para avançar célula a célula
   - Leia as explicações do algoritmo exibidas na tela

3. **Verificar Solução Ótima**:
   - Clique em "Resolver com DP" para ver a melhor solução possível
   - Compare sua escolha com a solução ótima
   - Analise a tabela de Programação Dinâmica

4. **Histórico e Ranking**:
   - Veja o histórico das suas últimas tentativas e o ranking das melhores pontuações

5. **Recomeçar**:
   - Use "Reset" para limpar e tentar novamente


## Dicas de Estratégia

- Procure itens com boa relação valor/peso
- Não se esqueça de considerar combinações de itens menores
- O algoritmo de Programação Dinâmica sempre encontra a solução ótima
- Tente diferentes combinações para entender o problema
- Use o modo demonstração para aprender como o algoritmo pensa!


## Algoritmo de Programação Dinâmica

O jogo implementa a solução clássica do problema 0/1 Knapsack, agora com visualização animada e explicações passo-a-passo:

```
DP[i][w] = valor máximo usando os primeiros i itens com peso máximo w

DP[i][w] = max(
    DP[i-1][w],                           // não incluir item i
    DP[i-1][w-peso[i]] + valor[i]         // incluir item i
)
```

A tabela mostra todos os subproblemas calculados para chegar à solução ótima. No modo demonstração, cada célula é preenchida animadamente e explicada.
