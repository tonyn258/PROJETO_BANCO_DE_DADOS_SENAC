####################################################################
# Grupo 2 - 
# Antônio
# Leonardo
# Julinha
#####################################################################

# =============================================================================
# ARQUIVO: model/pedido_model.py
#
# CAMADA: Model (M do padrão MVC)
#
# RESPONSABILIDADE:
#   Representa a entidade Pedido e define as operações de persistência.
#   Possui relacionamento N:1 com Cliente (muitos pedidos para um cliente).
#
# ATIVIDADE DOS ALUNOS — ETAPAS 4, 5 e 6:
#   - Implementar conexão (Etapa 4)
#   - Implementar CRUD (Etapa 5)
#   - Implementar JOIN com a tabela clientes (Etapa 6)
#
# TABELA ESPERADA NO BANCO:
#   CREATE TABLE pedidos (
#       id         INT            AUTO_INCREMENT PRIMARY KEY,
#       cliente_id INT            NOT NULL,
#       descricao  VARCHAR(255)   NOT NULL,
#       valor      DECIMAL(10, 2) NOT NULL,
#       data       DATE           NOT NULL,
#       FOREIGN KEY (cliente_id) REFERENCES clientes(id)
#   );
#
# RELACIONAMENTO:
#   CLIENTE (1) ----< PEDIDOS (N)
#   Um cliente pode ter muitos pedidos.
#   Um pedido pertence a exatamente um cliente.
# =============================================================================

from __future__ import annotations
from typing import Optional, List, Dict, Any
from database.conexao import ConexaoBD


class PedidoModel:
    """
    Model da entidade Pedido.

    Cada instância corresponde a um pedido (uma linha da tabela 'pedidos').

    Atributos:
        id (int):          Chave primária — gerada automaticamente.
        cliente_id (int):  Chave estrangeira → clientes.id (NOT NULL).
        descricao (str):   Descrição do produto/serviço pedido (NOT NULL).
        valor (float):     Valor total do pedido em reais (NOT NULL).
        data (str):        Data do pedido no formato 'AAAA-MM-DD' (NOT NULL).
    """

    def __init__(
        self,
        id: Optional[int] = None,
        cliente_id: Optional[int] = None,
        descricao: str = "",
        valor: float = 0.0,
        data: str = "",
    ) -> None:
        self.id = id
        self.cliente_id = cliente_id
        self.descricao = descricao
        self.valor = valor
        self.data = data

    def salvar(self) -> bool:
        """
        Persiste um novo pedido no banco de dados.
        """

        sql = """
            INSERT INTO tb_pedidos
            (
                cliente_id,
                descricao,
                valor,
                data
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s
            )
        """

        parametros = (
            self.cliente_id,
            self.descricao,
            self.valor,
            self.data
        )

        db = ConexaoBD()

        db.abrir_conexao()

        db.executar_query(sql, parametros)

        db.fechar_conexao()

        return True

    def listar(self) -> List[Dict[str, Any]]:
        """
        Retorna todos os pedidos com o nome do cliente.
        """

        sql = """
            SELECT
                p.ID_pedidos,
                c.nome,
                p.descricao,
                p.valor,
                p.data
            FROM tb_pedidos p
            INNER JOIN tb_clientes c
                ON p.cliente_id = c.ID_clientes
            ORDER BY p.data DESC
        """

        db = ConexaoBD()

        db.abrir_conexao()

        registros = db.buscar_todos(sql)

        db.fechar_conexao()

        return [
            {
                "id": r[0],
                "cliente": r[1],
                "descricao": r[2],
                "valor": float(r[3]),
                "data": str(r[4])
            }
            for r in registros
        ]
    def salvar(self) -> bool:
        """
        Persiste um novo pedido no banco de dados.
        """

        sql = """
            INSERT INTO tb_pedidos
            (
                cliente_id,
                descricao,
                valor,
                data
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s
            )
        """

        parametros = (
            self.cliente_id,
            self.descricao,
            self.valor,
            self.data
        )

        db = ConexaoBD()

        db.abrir_conexao()

        db.executar_query(sql, parametros)

        db.fechar_conexao()

        return True

    def atualizar(self) -> bool:
        """
        Atualiza os dados de um pedido existente.
        """

        sql = """
            UPDATE tb_pedidos
            SET
                cliente_id = %s,
                descricao = %s,
                valor = %s,
                data = %s
            WHERE ID_pedidos = %s
        """

        parametros = (
            self.cliente_id,
            self.descricao,
            self.valor,
            self.data,
            self.id
        )

        db = ConexaoBD()

        db.abrir_conexao()

        db.executar_query(sql, parametros)

        db.fechar_conexao()

        return True

    def excluir(self) -> bool:
        """
        Exclui um pedido pelo ID.
        """

        sql = """
            DELETE FROM tb_pedidos
            WHERE ID_pedidos = %s
        """

        parametros = (self.id,)

        db = ConexaoBD()

        db.abrir_conexao()

        db.executar_query(sql, parametros)

        db.fechar_conexao()

        return True

    #def listar_por_cliente(self, cliente_id: int) -> List[Dict[str, Any]]:
    def buscar_por_id(self, id: int):
        """
        Retorna todos os pedidos de um cliente específico.

        ATIVIDADE DOS ALUNOS — Implementar com:

            from database.conexao import Conexao

            sql = \"\"\"
                SELECT
                    p.id,
                    c.nome   AS cliente,
                    p.descricao,
                    p.valor,
                    p.data
                FROM pedidos p
                INNER JOIN clientes c ON p.cliente_id = c.id
                WHERE p.cliente_id = %s
                ORDER BY p.data DESC
            \"\"\"
            db = Conexao()
            db.abrir_conexao()
            registros = db.buscar_todos(sql, (cliente_id,))
            db.fechar_conexao()
            return [...]

        PONTO EDUCACIONAL:
        A cláusula WHERE filtra apenas os pedidos do cliente informado.
        Útil para exibir o histórico de pedidos de um cliente específico.

        Args:
            cliente_id: ID do cliente cujos pedidos serão buscados.

        Returns:
            List[Dict]: Lista de pedidos do cliente.

        Raises:
            NotImplementedError: Até que os alunos implementem.
        """
        # raise NotImplementedError(
        #     "Implemente listar_por_cliente() com SELECT ... WHERE cliente_id = %s."
        # )
        """
    Busca um pedido pelo ID.
    """

        sql = """
            SELECT
                ID_pedidos,
                cliente_id,
                descricao,
                valor,
                data
            FROM tb_pedidos
            WHERE ID_pedidos = %s
        """

        db = ConexaoBD()

        db.abrir_conexao()

        registro = db.buscar_um(sql, (id,))

        db.fechar_conexao()

        if registro:
            return {
                "id": registro[0],
                "cliente_id": registro[1],
                "descricao": registro[2],
                "valor": float(registro[3]),
                "data": str(registro[4])
            }

        return None

    def __repr__(self) -> str:
        return f"PedidoModel(id={self.id!r}, cliente_id={self.cliente_id!r})"
