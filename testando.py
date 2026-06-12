import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA"
    )

    if conexao.is_connected():
        print("Conectado ao MySQL!")

except Exception as erro:
    print("Erro:", erro)

finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()