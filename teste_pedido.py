# ===========================
# ARQUIVO: teste_pedido.py
# ===========================

from model.pedido_model import PedidoModel


# =====================================================
# TESTE 1 - LISTAR TODOS OS PEDIDOS
# =====================================================
# pedido = PedidoModel()
# print(pedido.listar())


# =====================================================
# TESTE 2 - SALVAR PEDIDO
# =====================================================
# pedido = PedidoModel()

# pedido.cliente_id = 1
# pedido.descricao = "Pizza Calabresa Grande"
# pedido.valor = 69.90
# pedido.data = "2026-06-11"

# pedido.salvar()

# print("Pedido salvo com sucesso!")


# =====================================================
# TESTE 3 - ATUALIZAR PEDIDO
# =====================================================
# pedido = PedidoModel()

# pedido.id = 1
# pedido.cliente_id = 1
# pedido.descricao = "Pizza Portuguesa"
# pedido.valor = 89.90
# pedido.data = "2026-06-11"

# pedido.atualizar()

# print("Pedido atualizado com sucesso!")


# =====================================================
# TESTE 4 - EXCLUIR PEDIDO
# =====================================================
# pedido = PedidoModel()

# pedido.id = 1

# pedido.excluir()

# print("Pedido excluído com sucesso!")


# =====================================================
# TESTE 5 - BUSCAR PEDIDO POR ID
# =====================================================
pedido = PedidoModel()

resultado = pedido.buscar_por_id(2)

print(resultado)