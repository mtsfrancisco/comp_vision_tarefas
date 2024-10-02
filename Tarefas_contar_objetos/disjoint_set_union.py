import cv2
import numpy as np


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  
        return self.parent[p]
        
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

def contar_componentes_union_find(matriz, valor):
    rows, cols = len(matriz), len(matriz[0])
    uf = UnionFind(rows * cols)
    index = lambda r, c: r * cols + c  # Fun ção para mapear 2D para 1D

    for i in range(rows):
        for j in range(cols):
            if matriz[i][j] == valor:
                # Unir com vizinhos se forem iguais ao valor
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < rows and 0 <= nj < cols and matriz[ni][nj] == valor:
                        uf.union(index(i, j), index(ni, nj))

    # Contar os componentes únicos
    root_set = set()
    for i in range(rows):
        for j in range(cols):
            if matriz[i][j] == valor:
                root_set.add(uf.find(index(i, j)))

    return len(root_set)

image = cv2.imread("images/moedas3.webp")
image = cv2.medianBlur(image, 5)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((5,5),np.uint8)
binary_image = cv2.dilate(binary_image, kernel, iterations=2)


# Contar componentes conectados de '1'
print(f"Componentes conectados de '0': {contar_componentes_union_find(binary_image, 255)}")
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
