"""

Nesta primeira solução, temos complexidade O(C^4 + P), sendo C a quantidade de compras e P a quantidade de produtos.
Aumentando a quantidade de compras de 20 para 75 já é possível observar que o algoritmo começa a ficar inviável.

Como executar:

$ python compras_solucao1.py

Como mensurar o tempo (caso esteja utilizando Linux):

$ time python compras_solucao1.py

"""

from dados import fabricar_produtos, fabricar_compras


QTD_PRODUTOS = 20
QTD_COMPRAS = 20 # altere para 75 e veja o que acontece

PRODUTOS = fabricar_produtos(QTD_PRODUTOS)
COMPRAS = fabricar_compras(QTD_COMPRAS, PRODUTOS, 3)

resultado = set()

for i in range(QTD_COMPRAS):
  for j in range(i + 1, QTD_COMPRAS):
    for k in range(j + 1, QTD_COMPRAS):
      for l in range(k + 1, QTD_COMPRAS):
        for p in range(QTD_PRODUTOS):
          if p in COMPRAS[i] and p in COMPRAS[j] and p in COMPRAS[k] and p in COMPRAS[l]:
            resultado.add(p)

print(f"Resultado: {resultado}")
