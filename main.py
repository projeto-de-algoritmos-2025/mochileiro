import pygame
import sys
from typing import List, Tuple, Dict

# Inicialização do Pygame
pygame.init()

# Constantes
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
BACKGROUND_COLOR = (245, 245, 245)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 149, 237)
BUTTON_TEXT_COLOR = (255, 255, 255)
TEXT_COLOR = (33, 33, 33)
SUCCESS_COLOR = (34, 139, 34)
ERROR_COLOR = (220, 20, 60)
HEADER_COLOR = (25, 25, 112)
TABLE_HEADER_COLOR = (176, 196, 222)
TABLE_CELL_COLOR = (230, 230, 250)

# Fontes
font_large = pygame.font.Font(None, 36)
font_medium = pygame.font.Font(None, 24)
font_small = pygame.font.Font(None, 20)

class Item:
    def __init__(self, name: str, weight: int, value: int):
        self.name = name
        self.weight = weight
        self.value = value
        self.selected = False

class KnapsackGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Jogo do Mochileiro - Knapsack Game Show")
        
        # Itens fixos do jogo
        self.items = [
            Item("Smartphone", 2, 300),
            Item("Notebook", 5, 800),
            Item("Câmera", 3, 450),
            Item("Livro", 1, 50),
            Item("Tablet", 2, 250),
            Item("Fones", 1, 100),
            Item("Carregador", 1, 30),
            Item("Roupas", 3, 80),
            Item("Remédios", 1, 200),
            Item("Snacks", 2, 40)
        ]
        
        self.max_weight = 15
        self.current_weight = 0
        self.current_value = 0
        self.error_message = ""
        self.show_solution = False
        self.dp_table = []
        self.optimal_items = []
        self.optimal_value = 0
        self.optimal_weight = 0
        
        # Botões
        self.buttons = []
        self.solve_button = None
        self.reset_button = None
        
        self.create_buttons()
        
    def create_buttons(self):
        # Botões para adicionar/remover itens
        for i, item in enumerate(self.items):
            y_pos = 120 + i * 40
            button_rect = pygame.Rect(320, y_pos, 120, 30)
            self.buttons.append((button_rect, i))
        
        # Botão de resolver
        self.solve_button = pygame.Rect(50, 550, 200, 40)
        
        # Botão de reset
        self.reset_button = pygame.Rect(270, 550, 120, 40)
    
    def handle_click(self, pos):
        # Verificar cliques nos botões dos itens
        for button_rect, item_index in self.buttons:
            if button_rect.collidepoint(pos):
                self.toggle_item(item_index)
                return
        
        # Verificar clique no botão de resolver
        if self.solve_button.collidepoint(pos):
            self.solve_knapsack()
            return
        
        # Verificar clique no botão de reset
        if self.reset_button.collidepoint(pos):
            self.reset_game()
            return
    
    def toggle_item(self, item_index):
        item = self.items[item_index]
        
        if item.selected:
            # Remover item
            item.selected = False
            self.current_weight -= item.weight
            self.current_value -= item.value
            self.error_message = ""
        else:
            # Tentar adicionar item
            if self.current_weight + item.weight <= self.max_weight:
                item.selected = True
                self.current_weight += item.weight
                self.current_value += item.value
                self.error_message = ""
            else:
                self.error_message = "Peso excedido! Não é possível adicionar este item."
    
    def solve_knapsack(self):
        """Resolve o problema usando Programação Dinâmica"""
        n = len(self.items)
        w = self.max_weight
        
        # Criar tabela DP
        self.dp_table = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
        
        # Preencher tabela DP
        for i in range(1, n + 1):
            for weight in range(1, w + 1):
                item = self.items[i - 1]
                
                if item.weight <= weight:
                    # Pode incluir o item
                    include_value = item.value + self.dp_table[i - 1][weight - item.weight]
                    exclude_value = self.dp_table[i - 1][weight]
                    self.dp_table[i][weight] = max(include_value, exclude_value)
                else:
                    # Não pode incluir o item
                    self.dp_table[i][weight] = self.dp_table[i - 1][weight]
        
        # Reconstruir solução
        self.optimal_value = self.dp_table[n][w]
        self.optimal_items = []
        self.optimal_weight = 0
        
        weight = w
        for i in range(n, 0, -1):
            if self.dp_table[i][weight] != self.dp_table[i - 1][weight]:
                item = self.items[i - 1]
                self.optimal_items.append(item)
                self.optimal_weight += item.weight
                weight -= item.weight
        
        self.show_solution = True
    
    def reset_game(self):
        """Reset do jogo"""
        for item in self.items:
            item.selected = False
        
        self.current_weight = 0
        self.current_value = 0
        self.error_message = ""
        self.show_solution = False
        self.dp_table = []
        self.optimal_items = []
        self.optimal_value = 0
        self.optimal_weight = 0
    
    def draw_text(self, text, font, color, x, y):
        """Desenha texto na tela"""
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
        return text_surface.get_height()
    
    def draw_button(self, rect, text, font, bg_color, text_color, hover=False):
        """Desenha um botão"""
        color = BUTTON_HOVER_COLOR if hover else bg_color
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, TEXT_COLOR, rect, 2)
        
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)
    
    def draw_dp_table(self):
        """Desenha a tabela de Programação Dinâmica"""
        if not self.dp_table:
            return
        
        start_x = 450
        start_y = 120
        cell_width = 35
        cell_height = 25
        
        # Título
        self.draw_text("Tabela de Programação Dinâmica:", font_medium, HEADER_COLOR, start_x, start_y - 30)
        
        # Cabeçalho com pesos
        for w in range(len(self.dp_table[0])):
            x = start_x + w * cell_width
            pygame.draw.rect(self.screen, TABLE_HEADER_COLOR, (x, start_y, cell_width, cell_height))
            pygame.draw.rect(self.screen, TEXT_COLOR, (x, start_y, cell_width, cell_height), 1)
            self.draw_text(str(w), font_small, TEXT_COLOR, x + 10, start_y + 5)
        
        # Linhas da tabela
        for i in range(len(self.dp_table)):
            y = start_y + (i + 1) * cell_height
            
            # Cabeçalho da linha (nome do item ou vazio)
            if i == 0:
                item_name = "∅"
            else:
                item_name = self.items[i - 1].name[:8]
            
            # Célula do nome do item
            pygame.draw.rect(self.screen, TABLE_HEADER_COLOR, (start_x - 80, y, 75, cell_height))
            pygame.draw.rect(self.screen, TEXT_COLOR, (start_x - 80, y, 75, cell_height), 1)
            self.draw_text(item_name, font_small, TEXT_COLOR, start_x - 75, y + 5)
            
            # Células dos valores
            for w in range(len(self.dp_table[i])):
                x = start_x + w * cell_width
                pygame.draw.rect(self.screen, TABLE_CELL_COLOR, (x, y, cell_width, cell_height))
                pygame.draw.rect(self.screen, TEXT_COLOR, (x, y, cell_width, cell_height), 1)
                self.draw_text(str(self.dp_table[i][w]), font_small, TEXT_COLOR, x + 5, y + 5)
    
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        
        # Título
        self.draw_text("Jogo do Mochileiro", font_large, HEADER_COLOR, 50, 20)
        self.draw_text(f"Peso máximo da mochila: {self.max_weight} kg", font_medium, TEXT_COLOR, 50, 60)
        
        # Lista de itens disponíveis
        self.draw_text("Itens Disponíveis:", font_medium, HEADER_COLOR, 50, 90)
        
        for i, item in enumerate(self.items):
            y_pos = 120 + i * 40
            
            # Status do item
            status = "✓" if item.selected else "○"
            color = SUCCESS_COLOR if item.selected else TEXT_COLOR
            
            # Informações do item
            item_text = f"{status} {item.name} - Peso: {item.weight}kg, Valor: R${item.value}"
            self.draw_text(item_text, font_small, color, 50, y_pos + 5)
            
            # Botão adicionar/remover
            button_rect, _ = self.buttons[i]
            button_text = "Remover" if item.selected else "Adicionar"
            button_color = ERROR_COLOR if item.selected else BUTTON_COLOR
            self.draw_button(button_rect, button_text, font_small, button_color, BUTTON_TEXT_COLOR)
        
        # Status atual da mochila
        self.draw_text("Mochila Atual:", font_medium, HEADER_COLOR, 50, 520)
        self.draw_text(f"Peso total: {self.current_weight}/{self.max_weight} kg", font_small, TEXT_COLOR, 50, 540)
        self.draw_text(f"Valor total: R$ {self.current_value}", font_small, TEXT_COLOR, 50, 560)
        
        # Mensagem de erro
        if self.error_message:
            self.draw_text(self.error_message, font_small, ERROR_COLOR, 50, 580)
        
        # Botões de ação
        self.draw_button(self.solve_button, "Resolver com DP", font_small, SUCCESS_COLOR, BUTTON_TEXT_COLOR)
        self.draw_button(self.reset_button, "Reset", font_small, ERROR_COLOR, BUTTON_TEXT_COLOR)
        
        # Mostrar solução se calculada
        if self.show_solution:
            # Tabela DP
            self.draw_dp_table()
            
            # Solução ótima
            solution_y = 450
            self.draw_text("Solução Ótima (Programação Dinâmica):", font_medium, HEADER_COLOR, 450, solution_y)
            self.draw_text(f"Valor ótimo: R$ {self.optimal_value}", font_small, SUCCESS_COLOR, 450, solution_y + 25)
            self.draw_text(f"Peso ótimo: {self.optimal_weight} kg", font_small, SUCCESS_COLOR, 450, solution_y + 45)
            
            self.draw_text("Itens da solução ótima:", font_small, TEXT_COLOR, 450, solution_y + 70)
            for i, item in enumerate(self.optimal_items):
                self.draw_text(f"• {item.name} (Peso: {item.weight}kg, Valor: R${item.value})", 
                             font_small, TEXT_COLOR, 450, solution_y + 90 + i * 20)
            
            # Comparação
            comparison_y = solution_y + 90 + len(self.optimal_items) * 20 + 30
            self.draw_text("Comparação:", font_medium, HEADER_COLOR, 450, comparison_y)
            self.draw_text(f"Sua solução: R$ {self.current_value} ({self.current_weight} kg)", 
                         font_small, TEXT_COLOR, 450, comparison_y + 25)
            self.draw_text(f"Solução ótima: R$ {self.optimal_value} ({self.optimal_weight} kg)", 
                         font_small, SUCCESS_COLOR, 450, comparison_y + 45)
            
            if self.current_value == self.optimal_value:
                self.draw_text("Parabéns! Você encontrou a solução ótima!", 
                             font_small, SUCCESS_COLOR, 450, comparison_y + 70)
            else:
                efficiency = (self.current_value / self.optimal_value * 100) if self.optimal_value > 0 else 0
                self.draw_text(f"Eficiência: {efficiency:.1f}% da solução ótima", 
                             font_small, TEXT_COLOR, 450, comparison_y + 70)
        
        pygame.display.flip()
    
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clique esquerdo
                        self.handle_click(event.pos)
            
            self.draw()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = KnapsackGame()
    game.run()
