from random import sample


def fabricar_produtos(qtd):
  return list(range(qtd))


def fabricar_compras(qtd, produtos, produtos_por_compra):
  return [
    sample(produtos, produtos_por_compra)
    for _ in range(qtd)
  ]
