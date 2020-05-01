"""
Essa solução possui complexidade O(P * C).

Um pouco mais viável que a anterior, mas continua se mostrando ineficaz com o crescimento das entradas.
"""
from dados import fabricar_produtos, fabricar_compras


QTD_PRODUTOS = 20000 # altere para 20000 e veja o que acontece
QTD_COMPRAS = 2000

PRODUTOS = fabricar_produtos(QTD_PRODUTOS)
COMPRAS = fabricar_compras(QTD_COMPRAS, PRODUTOS, 3)

resultado = set()

for p in range(QTD_PRODUTOS):
  aparicoes = 0
  for c in COMPRAS:
    if p in c:
      aparicoes = aparicoes + 1
  if aparicoes >= 4:
    resultado.add(p)

print(f"Resultado: {resultado}")
