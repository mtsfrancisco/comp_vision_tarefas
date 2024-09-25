import numpy as np

# Função de Flood Fill para marcar todos os pixels conectados
def flood_fill(imagem, x, y, visitado):
    # Definindo os limites da imagem
    altura, largura = imagem.shape
    
    # Stack para realizar o Flood Fill (iterativo)
    stack = [(x, y)]
    
    while stack:
        x, y = stack.pop()
        
        # Verifica se o pixel está dentro dos limites e não foi visitado
        if x < 0 or x >= altura or y < 0 or y >= largura or visitado[x, y] or imagem[x, y] == 0:
            continue
        
        # Marca o pixel como visitado
        visitado[x, y] = True
        
        # Adiciona os vizinhos (4-conectividade: cima, baixo, esquerda, direita)
        stack.append((x-1, y))  # Cima
        stack.append((x+1, y))  # Baixo
        stack.append((x, y-1))  # Esquerda
        stack.append((x, y+1))  # Direita

# Função para contar objetos na imagem
def contar_objetos(imagem_binaria):
    altura, largura = imagem_binaria.shape
    
    # Matriz para marcar os pixels visitados
    visitado = np.zeros_like(imagem_binaria, dtype=bool)
    
    num_objetos = 0
    
    # Percorrer a imagem pixel por pixel
    for x in range(altura):
        for y in range(largura):
            # Se o pixel for parte de um objeto (valor 1) e ainda não foi visitado
            if imagem_binaria[x, y] == 1 and not visitado[x, y]:
                # Aplicar Flood Fill a partir deste pixel
                flood_fill(imagem_binaria, x, y, visitado)
                # Incrementa o contador de objetos
                num_objetos += 1
    
    return num_objetos

# Exemplo de uma matriz binária simples (imagem)
imagem_binaria = np.array([[0, 0, 1, 1, 0],
                           [0, 1, 1, 0, 0],
                           [0, 0, 0, 0, 1],
                           [1, 1, 0, 0, 1]])

# Contar os objetos na imagem binária
num_objetos = contar_objetos(imagem_binaria)

print(f"Número de objetos encontrados: {num_objetos}")
