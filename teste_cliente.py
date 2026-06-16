# ===========================
# ARQUIVO: teste_cliente.py"
# ===========================

from model.cliente_model import ClienteModel


# =====================================================
# TESTE DO MÉTODO LISTAR
# =====================================================
# Cria um objeto ClienteModel
# e busca todos os clientes cadastrados
# no banco de dados.
m = ClienteModel()

print(m.listar())


# =====================================================
# TESTE DO MÉTODO SALVAR
# =====================================================
# Cria um novo cliente e envia os dados
# para o método salvar(), que executa
# um INSERT na tabela tb_clientes.
#
cliente = ClienteModel(
    nome="Mario",
    email="Mario@email.com",
    telefone="31 9 9999 9999"
)

cliente.salvar()

print("Cliente cadastrado com sucesso!")


# =====================================================
# TESTE DO MÉTODO ATUALIZAR
# =====================================================
# Atualiza um cliente já existente.
#
# O ID informado deve existir na tabela.
# O método atualizar() executa um UPDATE
# alterando nome, email e telefone do cliente.
# cliente = ClienteModel(
#     id=5,
#     nome="Lucas Atualizado",
#     email="lucas@email.com",
#     telefone="(31) 9 9999 9999"
# )

# cliente.atualizar()

# print("Cliente atualizado com sucesso!")

# =====================================================
# TESTE DO MÉTODO EXCLUIR
# =====================================================
# Exclui um cliente pelo ID.
# O ID informado deve existir na tabela.

# cliente = ClienteModel(
#     id=4
# )

# cliente.excluir()

# print("Cliente excluído com sucesso!")

# =====================================================
# TESTE DO MÉTODO BUSCAR POR ID
# =====================================================

# cliente = ClienteModel(
#     id=4
# )

# resultado = cliente.buscar_por_id()

# cliente = ClienteModel(...)
# resultado = ...

# print(resultado)

