"""
Essa solução demonstra que mesmo utilizando bibliotecas, a complexidade
do algoritmo não muda, pois é fundamental à estratégia adotada para
resolver o problema.
"""
from itertools import combinations

from dados import fabricar_produtos, fabricar_compras


QTD_PRODUTOS = 20
QTD_COMPRAS = 20 # altere para 75 e veja o que acontece

PRODUTOS = fabricar_produtos(QTD_PRODUTOS)
COMPRAS = fabricar_compras(QTD_COMPRAS, PRODUTOS, 3)

resultado = set()

for c in combinations(COMPRAS, 4):
  for p in range(QTD_PRODUTOS):
    if p in c[0] and p in c[1] and p in c[2] and p in c[3]:
      resultado.add(p)

print(f"Resultado: {resultado}")
