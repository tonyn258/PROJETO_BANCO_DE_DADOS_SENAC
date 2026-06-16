####################################################################
# Grupo 2 - 
# Antônio
# Leonardo
# Julinha
# Victor Gabriel
#####################################################################

# =============================================================================
# ARQUIVO: controller/pedido_controller.py
#
# CAMADA: Controller (C do padrão MVC)
#
# RESPONSABILIDADE:
#   Intermediar a comunicação entre PedidoView e PedidoModel.
#   Gerenciar o relacionamento entre Pedidos e Clientes:
#   popular o Combobox de clientes e vincular o clientes_ID ao salvar.
#
# FLUXO PRINCIPAL:
#   1. Ao carregar a tela → busca clientes para o Combobox
#   2. Usuário seleciona cliente, preenche campos, clica em "Salvar"
#   3. Controller valida dados e chama PedidoModel.salvar()
#   4. O banco cria o vínculo via FOREIGN KEY (clientes_ID)
#   5. Controller atualiza a tabela (com JOIN cliente + pedido)
# =============================================================================

from tkinter import messagebox
from typing import List

from model.pedido_model import PedidoModel
from model.cliente_model import ClienteModel
from view.pedido_view import PedidoView



# -----------------------------------------------------------------------------
# DADOS MOCKADOS — apenas para demonstração da interface
#
# Formato: [id, nome_cliente, descricao, valor_float, data_str]
#
# ATIVIDADE DOS ALUNOS:
# Após implementar a camada de banco, substituir por:
#   self.model.listar()  → que executará o INNER JOIN
# -----------------------------------------------------------------------------
PEDIDOS_MOCK: List[list] = [
    [1, "João Silva",   "Notebook Dell Inspiron",  3500.00, "15/05/2025"],
    [2, "Maria Souza",  "Mouse sem fio Logitech",   150.00, "16/05/2025"],
    [3, "João Silva",   "Teclado mecânico RGB",      280.00, "17/05/2025"],
    [4, "Pedro Costa",  "Monitor 24 polegadas",    1200.00, "18/05/2025"],
    [5, "Ana Oliveira", "Headset Gamer",             350.00, "20/05/2025"],
]


def _formatar_valor(valor: float) -> str:
    """Formata um float como moeda brasileira (ex: R$ 1.200,00)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _desformatar_valor(texto: str) -> float:
    """Converte string de moeda em float (ex: '1.200,00' → 1200.0)."""
    limpo = texto.replace("R$", "").strip().replace(".", "").replace(",", ".")
    return float(limpo)


class PedidoController:
    """
    Controller da tela de Pedidos.

    Além do CRUD padrão, gerencia o relacionamento N:1 com Clientes:
    popula o Combobox e obtém o clientes_ID para persistência.
    """

    def __init__(self, view: PedidoView) -> None:
        """
        Inicializa o Controller, vincula eventos e carrega dados.

        Args:
            view: Instância de PedidoView que este Controller gerencia.
        """
        self.view = view
        self.model = PedidoModel()
        self._proximo_id: int = len(PEDIDOS_MOCK) + 1

        self._vincular_eventos()
        self._carregar_clientes_combobox()
        self._carregar_dados()

    # =========================================================================
    # Inicialização
    # =========================================================================

    def _vincular_eventos(self) -> None:
        self.view.vincular_eventos(
            ao_selecionar=self._ao_selecionar_linha,
            ao_novo=self._ao_clicar_novo,
            ao_salvar=self._ao_clicar_salvar,
            ao_atualizar=self._ao_clicar_atualizar,
            ao_excluir=self._ao_clicar_excluir,
            ao_limpar=self._ao_clicar_limpar,
        )


    def _carregar_clientes_combobox(self) -> None:
        """
        Carrega os clientes do banco e popula o Combobox.
        """

        model_cliente = ClienteModel()

        clientes = model_cliente.listar()

        self.view.definir_clientes_combobox(clientes)

    def _carregar_dados(self) -> None:
        """
        Busca todos os pedidos (com nome do cliente) e atualiza a tabela.

        ATIVIDADE DOS ALUNOS:
        Após implementar PedidoModel.listar() com INNER JOIN, substituir:

            registros_dict = self.model.listar()
            registros = [
                [r["id"], r["cliente"], r["descricao"],
                 _formatar_valor(float(r["valor"])), r["data"]]
                for r in registros_dict
            ]
            self.view.atualizar_tabela(registros)
        """
        registros_dict = self.model.listar()

        registros = [
            [
                r["id"],
                r["cliente"],
                r["descricao"],
                _formatar_valor(float(r["valor"])),
                r["data"]
            ]
            for r in registros_dict
        ]

        self.view.atualizar_tabela(registros)
    # =========================================================================
    # Callbacks
    # =========================================================================

    def _ao_selecionar_linha(self, _event) -> None:
        """Preenche o formulário com os dados do pedido clicado na tabela."""
        valores = self.view.obter_item_selecionado()
        if not valores:
            return

        # Converte valor formatado "R$ 1.200,00" de volta para número
        try:
            valor_num = str(_desformatar_valor(str(valores[3])))
        except (ValueError, AttributeError):
            valor_num = str(valores[3])

        self.view.preencher_formulario({
            "id":           valores[0],
            "cliente_nome": valores[1],
            "descricao":    valores[2],
            "valor":        valor_num,
            "data":         valores[4],
        })

    def _ao_clicar_novo(self) -> None:
        """Limpa o formulário para inserção de novo pedido."""
        self.view.limpar_formulario()
        self.view.combo_cliente.focus()

    def _ao_clicar_salvar(self) -> None:
        """
        Valida os dados e salva um novo pedido.

        PONTO EDUCACIONAL:
        O campo 'clientes_ID' é a FOREIGN KEY que vincula o pedido
        ao cliente. Ao chamar self.model.salvar(), o banco validará
        automaticamente que o clientes_ID existe na tabela 'clientes'.

        ATIVIDADE DOS ALUNOS:
        Após implementar PedidoModel.salvar(), substituir o bloco
        mockado pelo seguinte:

            print("DADOS:", dados)
            print("CLIENTE ID:", dados["clientes_ID"])

            self.model.clientes_ID = dados["clientes_ID"]
            self.model.descricao  = dados["descricao"]
            self.model.valor      = valor_float
            self.model.data       = dados["data"]

            try:
                sucesso = self.model.salvar()
                if sucesso:
                    self._carregar_dados()
                    self.view.limpar_formulario()
                    self.view.definir_status("Pedido salvo!", "sucesso")
            except Exception as e:
                self.view.definir_status(f"Erro: {e}", "erro")
        """
        dados = self.view.obter_dados_formulario()
        print(dados)

        # --- Validações ---
        if not dados["cliente_nome"]:
            messagebox.showwarning("Campo obrigatório", "Selecione um Cliente.")
            self.view.combo_cliente.focus()
            return

        if not dados["descricao"]:
            messagebox.showwarning("Campo obrigatório", "Informe a Descrição do pedido.")
            self.view.entry_descricao.focus()
            return

        if not dados["valor"]:
            messagebox.showwarning("Campo obrigatório", "Informe o Valor do pedido.")
            self.view.entry_valor.focus()
            return

        if not dados["data"] or dados["data"] == "DD/MM/AAAA":
            messagebox.showwarning("Campo obrigatório", "Informe a Data do pedido.")
            self.view.entry_data.focus()
            return

        try:
            valor_float = float(dados["valor"].replace(",", "."))
            if valor_float <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showwarning(
                "Valor inválido",
                "Informe um valor numérico positivo (ex: 150.00 ou 150,00).",
            )
            self.view.entry_valor.focus()
            return

        if dados["id"]:
            messagebox.showinfo(
                "Atenção",
                "Um pedido já está selecionado.\n"
                "Use 'Atualizar' para editar ou 'Limpar' para novo cadastro.",
            )
            return

        # TODO (Alunos): substituir pelo bloco descrito na docstring acima
        self.model.clientes_ID = dados["clientes_ID"]
        self.model.descricao = dados["descricao"]
        self.model.valor = valor_float
        self.model.data = dados["data"]

        try:
            sucesso = self.model.salvar()

            if sucesso:
                self._carregar_dados()
                self.view.limpar_formulario()
                self.view.definir_status(
                    "Pedido salvo com sucesso!",
                    "sucesso"
                )

        except Exception as e:
            self.view.definir_status(
                f"Erro: {e}",
                "erro"
            )
            
    def _ao_clicar_atualizar(self) -> None:
        """
        Valida e atualiza os dados do pedido selecionado.

        ATIVIDADE DOS ALUNOS:
        Após implementar PedidoModel.atualizar(), substituir o bloco
        mockado pelo seguinte:

            self.model.id         = int(dados["id"])
            self.model.clientes_ID = dados["clientes_ID"]
            self.model.descricao  = dados["descricao"]
            self.model.valor      = valor_float
            self.model.data       = dados["data"]

            try:
                sucesso = self.model.atualizar()
                if sucesso:
                    self._carregar_dados()
                    self.view.limpar_formulario()
                    self.view.definir_status("Pedido atualizado!", "sucesso")
            except Exception as e:
                self.view.definir_status(f"Erro: {e}", "erro")
        """
        dados = self.view.obter_dados_formulario()

        if not dados["id"]:
            messagebox.showwarning(
                "Nenhum pedido selecionado",
                "Clique em um pedido na tabela antes de atualizar.",
            )
            return

        if not dados["cliente_nome"] or not dados["descricao"] or not dados["valor"]:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
            return

        try:
            valor_float = float(dados["valor"].replace(",", "."))
        except ValueError:
            messagebox.showwarning("Valor inválido", "Informe um número válido.")
            return

        # TODO (Alunos): substituir pelo bloco descrito na docstring acima
        self.model.id = int(dados["id"])
        self.model.clientes_ID = dados["clientes_ID"]
        self.model.descricao = dados["descricao"]
        self.model.valor = valor_float
        self.model.data = dados["data"]

        try:
            sucesso = self.model.atualizar()

            if sucesso:
                self._carregar_dados()
                self.view.limpar_formulario()
                self.view.definir_status(
                    "Pedido atualizado com sucesso!",
                    "sucesso"
                )

        except Exception as e:
            self.view.definir_status(
                f"Erro: {e}",
                "erro"
            )
    def _ao_clicar_excluir(self) -> None:
        """
        Solicita confirmação e exclui o pedido selecionado.

        ATIVIDADE DOS ALUNOS:
        Após implementar PedidoModel.excluir(), substituir o bloco
        mockado pelo seguinte:

            self.model.id = int(dados["id"])
            try:
                sucesso = self.model.excluir()
                if sucesso:
                    self._carregar_dados()
                    self.view.limpar_formulario()
                    self.view.definir_status("Pedido excluído.", "info")
            except Exception as e:
                self.view.definir_status(f"Erro: {e}", "erro")
        """
        dados = self.view.obter_dados_formulario()

        if not dados["id"]:
            messagebox.showwarning(
                "Nenhum pedido selecionado",
                "Clique em um pedido na tabela antes de excluir.",
            )
            return

        confirma = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Deseja excluir o pedido #{dados['id']}?\n"
            "Esta ação não pode ser desfeita.",
        )
        if not confirma:
            return

        # TODO (Alunos): substituir pelo bloco descrito na docstring acima
        self.model.id = int(dados["id"])

        try:

            sucesso = self.model.excluir()

            if sucesso:

                self._carregar_dados()

                self.view.limpar_formulario()

                self.view.definir_status(
                    "Pedido excluído com sucesso!",
                    "info"
                )

        except Exception as e:

            self.view.definir_status(
                f"Erro: {e}",
                "erro"
            )
    def _ao_clicar_limpar(self) -> None:
        """Limpa o formulário sem alterar dados."""
        self.view.limpar_formulario()
