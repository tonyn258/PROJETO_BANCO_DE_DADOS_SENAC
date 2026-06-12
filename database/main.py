from conexao import ConexaoBD

bd = ConexaoBD()

try:

    bd.abrir_conexao()

    print("Conectado com sucesso!")

    clientes = bd.buscar_todos(
        "SELECT * FROM tb_clientes"
    )

    print(clientes)

finally:

    bd.fechar_conexao()