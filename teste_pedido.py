# ===========================
# ARQUIVO: teste_pedido.py
# # ===========================

# from model.pedido_model import PedidoModel

# ###################################################
# # LISTAR PEDIDOS
# ###################################################

# n = PedidoModel()

# print(n.listar())

###################################################
# ATUALIZAR PEDIDO
###################################################

# pedido = PedidoModel()

# pedido.id = 1
# pedido.cliente_id = 1
# pedido.descricao = "Pizza Portuguesa"
# pedido.valor = 89.90
# pedido.data = "2026-06-11"

# pedido.atualizar()

# print("Pedido atualizado com sucesso!")


###########################################################
#excluir
###########################################################
#  from model.pedido_model import PedidoModel

# pedido = PedidoModel()

# pedido.id = 1

# pedido.excluir()

# print("Pedido excluído!")


#######################################
#Salvar
########################################

# from model.pedido_model import PedidoModel

# pedido = PedidoModel()

# pedido.cliente_id = 1
# pedido.descricao = "Pizza Calabresa Grande"
# pedido.valor = 69.90
# pedido.data = "2026-06-11"

# pedido.salvar()

# print("Pedido salvo com sucesso!")

#######################################
#listar
########################################


from model.pedido_model import PedidoModel

pedido = PedidoModel()

resultado = pedido.buscar_por_id(2)

print(resultado)