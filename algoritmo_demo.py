"""
Demonstração do Algoritmo de Programação Dinâmica para o Problema do Knapsack 0/1
Este script mostra como o algoritmo funciona passo a passo, sem interface gráfica.
"""

def knapsack_dp_demo():
    # Dados do problema (mesmos do jogo)
    items = [
        ("Smartphone", 2, 300),
        ("Notebook", 5, 800),
        ("Câmera", 3, 450),
        ("Livro", 1, 50),
        ("Tablet", 2, 250),
        ("Fones", 1, 100),
        ("Carregador", 1, 30),
        ("Roupas", 3, 80),
        ("Remédios", 1, 200),
        ("Snacks", 2, 40)
    ]
    
    max_weight = 15
    n = len(items)
    
    print("=== PROBLEMA DO KNAPSACK 0/1 ===")
    print(f"Peso máximo da mochila: {max_weight} kg")
    print("\nItens disponíveis:")
    for i, (name, weight, value) in enumerate(items):
        print(f"{i+1:2d}. {name:12s} - Peso: {weight:2d}kg, Valor: R${value:3d}")
    
    # Criar e preencher tabela DP
    print("\n=== ALGORITMO DE PROGRAMAÇÃO DINÂMICA ===")
    
    # Inicializar tabela
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    print("\nPreenchendo a tabela DP...")
    print("DP[i][w] = valor máximo usando os primeiros i itens com peso máximo w")
    
    # Preencher tabela
    for i in range(1, n + 1):
        item_name, item_weight, item_value = items[i - 1]
        print(f"\nProcessando item {i}: {item_name} (peso: {item_weight}, valor: {item_value})")
        
        for w in range(1, max_weight + 1):
            if item_weight <= w:
                # Pode incluir o item
                include_value = item_value + dp[i - 1][w - item_weight]
                exclude_value = dp[i - 1][w]
                dp[i][w] = max(include_value, exclude_value)
                
                if include_value > exclude_value:
                    action = "INCLUIR"
                else:
                    action = "NÃO INCLUIR"
                
                if w <= 10:  # Mostrar apenas alguns pesos para não sobrecarregar
                    print(f"  w={w:2d}: incluir={include_value:3d}, excluir={exclude_value:3d} → {dp[i][w]:3d} ({action})")
            else:
                # Não pode incluir o item
                dp[i][w] = dp[i - 1][w]
    
    # Mostrar tabela final (apenas parte dela)
    print("\n=== TABELA DP FINAL (primeiros 11 pesos) ===")
    print("     ", end="")
    for w in range(11):
        print(f"{w:4d}", end="")
    print()
    
    for i in range(min(6, n + 1)):  # Mostrar apenas primeiros itens
        if i == 0:
            print("∅    ", end="")
        else:
            print(f"{items[i-1][0][:4]:4s} ", end="")
        
        for w in range(11):
            print(f"{dp[i][w]:4d}", end="")
        print()
    
    if n > 5:
        print("  ... (mais linhas)")
    
    # Valor ótimo
    optimal_value = dp[n][max_weight]
    print(f"\n=== VALOR ÓTIMO ===")
    print(f"Valor máximo possível: R$ {optimal_value}")
    
    # Reconstruir solução
    print("\n=== RECONSTRUINDO A SOLUÇÃO ===")
    selected_items = []
    total_weight = 0
    w = max_weight
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, item_weight, item_value = items[i - 1]
            selected_items.append((item_name, item_weight, item_value))
            total_weight += item_weight
            w -= item_weight
            print(f"Item selecionado: {item_name} (peso: {item_weight}, valor: {item_value})")
    
    print(f"\n=== SOLUÇÃO ÓTIMA ===")
    print(f"Itens selecionados: {len(selected_items)}")
    print(f"Peso total: {total_weight} kg (de {max_weight} kg)")
    print(f"Valor total: R$ {optimal_value}")
    
    print("\nLista final dos itens:")
    for name, weight, value in selected_items:
        print(f"• {name} - Peso: {weight}kg, Valor: R${value}")
    
    # Análise de eficiência
    print(f"\n=== ANÁLISE ===")
    print(f"Taxa de ocupação da mochila: {total_weight/max_weight*100:.1f}%")
    print(f"Valor médio por kg: R$ {optimal_value/total_weight:.2f}")

def compare_greedy_vs_dp():
    """Compara solução gulosa (por valor/peso) com DP"""
    items = [
        ("Smartphone", 2, 300),
        ("Notebook", 5, 800),
        ("Câmera", 3, 450),
        ("Livro", 1, 50),
        ("Tablet", 2, 250),
        ("Fones", 1, 100),
        ("Carregador", 1, 30),
        ("Roupas", 3, 80),
        ("Remédios", 1, 200),
        ("Snacks", 2, 40)
    ]
    
    max_weight = 15
    
    print("\n" + "="*60)
    print("COMPARAÇÃO: ALGORITMO GULOSO vs PROGRAMAÇÃO DINÂMICA")
    print("="*60)
    
    # Algoritmo guloso (ordenar por valor/peso)
    items_with_ratio = [(name, weight, value, value/weight) for name, weight, value in items]
    items_with_ratio.sort(key=lambda x: x[3], reverse=True)
    
    print("\nItens ordenados por relação valor/peso:")
    for name, weight, value, ratio in items_with_ratio:
        print(f"{name:12s} - Ratio: {ratio:6.2f} (valor: {value}, peso: {weight})")
    
    # Solução gulosa
    greedy_items = []
    greedy_weight = 0
    greedy_value = 0
    
    for name, weight, value, ratio in items_with_ratio:
        if greedy_weight + weight <= max_weight:
            greedy_items.append((name, weight, value))
            greedy_weight += weight
            greedy_value += value
    
    print(f"\n=== SOLUÇÃO GULOSA ===")
    print(f"Valor: R$ {greedy_value}")
    print(f"Peso: {greedy_weight} kg")
    print("Itens:", [item[0] for item in greedy_items])
    
    # Solução DP (já calculada na função anterior)
    # Para simplicidade, vou recalcular aqui
    n = len(items)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            item_weight = items[i - 1][1]
            item_value = items[i - 1][2]
            
            if item_weight <= w:
                include_value = item_value + dp[i - 1][w - item_weight]
                exclude_value = dp[i - 1][w]
                dp[i][w] = max(include_value, exclude_value)
            else:
                dp[i][w] = dp[i - 1][w]
    
    dp_value = dp[n][max_weight]
    
    print(f"\n=== SOLUÇÃO PROGRAMAÇÃO DINÂMICA ===")
    print(f"Valor: R$ {dp_value}")
    print(f"Diferença: R$ {dp_value - greedy_value} ({((dp_value - greedy_value)/greedy_value*100):.1f}% melhor)")
    
    if greedy_value == dp_value:
        print("🎉 Neste caso, o algoritmo guloso encontrou a solução ótima!")
    else:
        print("⚠️  O algoritmo guloso não encontrou a solução ótima.")
        print("   Este é o motivo pelo qual precisamos da Programação Dinâmica!")

if __name__ == "__main__":
    knapsack_dp_demo()
    compare_greedy_vs_dp()
