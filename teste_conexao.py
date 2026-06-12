import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="372660"  # coloque sua senha aqui se existir
    )

    if conexao.is_connected():
        print("Conectado ao MySQL com sucesso!")

except Exception as erro:
    print("Erro:", erro)

finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()