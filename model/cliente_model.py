####################################################################
# Grupo 2 - 
# Antônio
# Leonardo
# Julinha
#####################################################################


# =============================================================================
# ARQUIVO: model/cliente_model.py
#
# CAMADA: Model (M do padrão MVC)
#
# RESPONSABILIDADE:
#   Representa a entidade Cliente e define as operações de persistência.
#   Esta camada é a ÚNICA que deve se comunicar com o banco de dados.
#   A View e o Controller NUNCA acessam o banco diretamente.
#
# ATIVIDADE DOS ALUNOS — ETAPAS 4 e 5:
#   Implementar cada método usando a classe Conexao (database/conexao.py)
#   e as queries SQL correspondentes.
#
# TABELA ESPERADA NO BANCO:
#   CREATE TABLE clientes (
#       id       INT          AUTO_INCREMENT PRIMARY KEY,
#       nome     VARCHAR(100) NOT NULL,
#       email    VARCHAR(100),
#       telefone VARCHAR(20)
#   );
# =============================================================================
 
from __future__ import annotations
from typing import Optional, List, Dict, Any
from database.conexao import ConexaoBD
 
class ClienteModel:
    """
    Model da entidade Cliente.
 
    Representa um registro da tabela 'clientes' no banco de dados.
    Cada instância corresponde a um cliente (uma linha da tabela).
 
    Atributos:
        id (int):       Chave primária — gerada automaticamente pelo banco.
        nome (str):     Nome completo do cliente (NOT NULL).
        email (str):    Endereço de e-mail do cliente.
        telefone (str): Número de telefone do cliente.
    """
 
    def __init__(
        self,
        id: Optional[int] = None,
        nome: str = "",
        email: str = "",
        telefone: str = "",
    ) -> None:
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
 
    # -------------------------------------------------------------------------
    # PONTO EDUCACIONAL — Como usar esta classe nos Controllers:
    #
    #   cliente = ClienteModel(nome="João", email="joao@email.com")
    #   cliente.salvar()   ← INSERT no banco
    #
    #   cliente = ClienteModel(id=1, nome="João Atualizado")
    #   cliente.atualizar() ← UPDATE no banco
    #
    #   cliente = ClienteModel(id=1)
    #   cliente.excluir()  ← DELETE no banco
    # -------------------------------------------------------------------------

# =====================================================
# MÉTODO SALVAR
# =====================================================
 
    def salvar(self) -> bool:

        sql = """
            INSERT INTO tb_clientes
            (nome, email, telefone)
            VALUES
            (%s, %s, %s)
        """

        parametros = (
            self.nome,
            self.email,
            self.telefone
        )

        db = ConexaoBD()

        db.abrir_conexao()

        db.executar_query(sql, parametros)

        db.fechar_conexao()

        return True
    
# =====================================================
# MÉTODO LISTAR
# =====================================================

    def listar(self):

        sql = """
            SELECT ID_clientes, nome, email, telefone
            FROM tb_clientes
            ORDER BY nome ASC
        """

        db = ConexaoBD()

        db.abrir_conexao()

        registros = db.buscar_todos(sql)

        db.fechar_conexao()

        return [
            {
                "id": r[0],
                "nome": r[1],
                "email": r[2],
                "telefone": r[3]
            }
            for r in registros
        ]
    
# =====================================================
# MÉTODO ATUALIZAR
# =====================================================
 
    def atualizar(self) -> bool:
        """
        Atualiza os dados de um cliente existente no banco.
 
        ATIVIDADE DOS ALUNOS — Implementar com:
 
            from database.conexao import Conexao
 
            sql = \"\"\"
                UPDATE clientes
                SET nome = %s, email = %s, telefone = %s
                WHERE id = %s
            \"\"\"
            db = Conexao()
            db.abrir_conexao()
            db.executar_query(sql, (self.nome, self.email, self.telefone, self.id))
            db.fechar_conexao()
            return True
 
        ATENÇÃO: self.id deve estar preenchido antes de chamar este método.
 
        Returns:
            bool: True se o registro foi atualizado com sucesso.
 
        Raises:
            NotImplementedError: Até que os alunos implementem.
        """
        # raise NotImplementedError(
        #     "Implemente atualizar() com UPDATE clientes SET ... WHERE id."
        # )

        sql = """
            UPDATE tb_clientes
            SET nome = %s,
                email = %s,
                telefone = %s
            WHERE ID_clientes = %s
        """

        parametros = (
            self.nome,
            self.email,
            self.telefone,
            self.id
        )

        db = ConexaoBD()

        db.abrir_conexao()

        db.executar_query(sql, parametros)

        db.fechar_conexao()

        return True
    
# =====================================================
# MÉTODO EXCLUIR
# =====================================================
 
    def excluir(self) -> bool:
        """
        Remove um cliente do banco de dados pelo ID.
 
        ATIVIDADE DOS ALUNOS — Implementar com:
 
            from database.conexao import Conexao
 
            sql = "DELETE FROM clientes WHERE id = %s"
            db = Conexao()
            db.abrir_conexao()
            db.executar_query(sql, (self.id,))
            db.fechar_conexao()
            return True
 
        ATENÇÃO: Verificar integridade referencial!
        Se o cliente possuir pedidos vinculados, o banco pode
        rejeitar a exclusão por conta da FOREIGN KEY.
        Solução: usar ON DELETE CASCADE na FOREIGN KEY, ou
        excluir os pedidos antes de excluir o cliente.
 
        Returns:
            bool: True se o registro foi excluído com sucesso.
 
        Raises:
            NotImplementedError: Até que os alunos implementem.
        """
        # raise NotImplementedError(
        #     "Implemente excluir() com DELETE FROM clientes WHERE id."
        # )



        
        """
        Exclui um cliente do banco de dados
        utilizando o ID informado.
        """

        sql = """
            DELETE FROM tb_clientes
            WHERE ID_clientes = %s
        """

        parametros = (
            self.id,
        )

        db = ConexaoBD()

        db.abrir_conexao()

        db.executar_query(sql, parametros)

        db.fechar_conexao()

        return True
    
# =====================================================
# MÉTODO BUSCAR POR ID
# =====================================================
 
    #def buscar_por_id(self, id: int) -> Optional[Dict[str, Any]]:
    def buscar_por_id(self):
    
        """
        Busca um cliente específico pelo ID.
 
        ATIVIDADE DOS ALUNOS — Implementar com:
 
            from database.conexao import Conexao
 
            sql = \"\"\"
                SELECT id, nome, email, telefone
                FROM clientes
                WHERE id = %s
            \"\"\"
            db = Conexao()
            db.abrir_conexao()
            registro = db.buscar_um(sql, (id,))
            db.fechar_conexao()
 
            if registro:
                return {"id": registro[0], "nome": registro[1],
                        "email": registro[2], "telefone": registro[3]}
            return None
 
        Args:
            id: Chave primária do cliente a buscar.
 
        Returns:
            Dict ou None: Dados do cliente, ou None se não encontrado.
 
        Raises:
            NotImplementedError: Até que os alunos implementem.
        """
        # raise NotImplementedError(
        #     "Implemente buscar_por_id() com SELECT WHERE id = %s."
        # )

        sql = """
            SELECT ID_clientes, nome, email, telefone
            FROM tb_clientes
            WHERE ID_clientes = %s
        """

        parametros = (
            self.id,
        )

        db = ConexaoBD()

        db.abrir_conexao()

        registro = db.buscar_um(sql, parametros)

        db.fechar_conexao()

        if registro is None:
            return None

        return {
            "id": registro[0],
            "nome": registro[1],
            "email": registro[2],
            "telefone": registro[3]
        }        
 
    def __repr__(self) -> str:
        return f"ClienteModel(id={self.id!r}, nome={self.nome!r})"