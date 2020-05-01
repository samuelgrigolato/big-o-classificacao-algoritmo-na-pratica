"""
Essa solução possui complexidade O(C + P), muito eficaz mesmo com entradas bem grandes.
"""
from dados import fabricar_produtos, fabricar_compras


QTD_PRODUTOS = 200000
QTD_COMPRAS = 200000

PRODUTOS = fabricar_produtos(QTD_PRODUTOS)
COMPRAS = fabricar_compras(QTD_COMPRAS, PRODUTOS, 3)

resultado = set()

aparicoes = [0 for _ in range(QTD_PRODUTOS)]

for c in COMPRAS:
  for p in c:
    aparicoes[p] = aparicoes[p] + 1

for p in PRODUTOS:
  if aparicoes[p] >= 4:
    resultado.add(p)

print(f"Resultado: {resultado}")
