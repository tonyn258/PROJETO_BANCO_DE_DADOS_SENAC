# =============================================================================
# ARQUIVO: controller/cliente_controller.py
#
# CAMADA: Controller (C do padrão MVC)
#
# RESPONSABILIDADE:
#   Intermediar a comunicação entre ClienteView e ClienteModel.
#   Receber eventos da View, chamar o Model e atualizar a View.
#
# FLUXO COMPLETO:
#   1. Usuário clica em "Salvar"
#   2. ClienteView chama o callback ao_salvar (registrado aqui)
#   3. ClienteController._ao_clicar_salvar() é executado:
#      a. Lê os dados do formulário via view.obter_dados_formulario()
#      b. Valida os dados
#      c. Chama ClienteModel.salvar()   ← AQUI os alunos integram o SQL
#      d. Atualiza a tabela via view.atualizar_tabela()
#      e. Exibe mensagem via view.definir_status()
#
# DADOS MOCKADOS:
#   Enquanto os alunos não implementam o banco, os dados são armazenados
#   nesta lista em memória. Após a integração com MySQL, os dados mockados
#   são substituídos pelas chamadas ao ClienteModel.
# =============================================================================

from tkinter import messagebox
from typing import List

from model.cliente_model import ClienteModel
from view.cliente_view import ClienteView


# -----------------------------------------------------------------------------
# DADOS MOCKADOS — apenas para demonstração da interface
#
# ATIVIDADE DOS ALUNOS:
# Após implementar a classe Conexao e os métodos do ClienteModel,
# substituir o uso desta lista pelas chamadas:
#   self.model.listar()   → para carregar dados
#   self.model.salvar()   → para inserir
#   self.model.atualizar() → para editar
#   self.model.excluir()  → para remover
# -----------------------------------------------------------------------------
CLIENTES_MOCK: List[list] = [
    [1, "João Silva",    "joao.silva@email.com",    "(35) 99999-1111"],
    #[2, "Maria Souza",   "maria.souza@email.com",   "(35) 98888-2222"],
    #[3, "Pedro Costa",   "pedro.costa@email.com",   "(35) 97777-3333"],
    #[4, "Ana Oliveira",  "ana.oliveira@email.com",  "(35) 96666-4444"],
    #[5, "Carlos Lima",   "carlos.lima@email.com",   "(35) 95555-5555"],
]


class ClienteController:
    """
    Controller da tela de Clientes.

    Gerencia toda a lógica entre a View (o que o usuário vê)
    e o Model (os dados persistidos no banco).
    """

    def __init__(self, view: ClienteView) -> None:
        """
        Inicializa o Controller, vincula eventos e carrega dados iniciais.

        Args:
            view: Instância de ClienteView que este Controller gerencia.
        """
        self.view = view
        self.model = ClienteModel()

        # Contador para simular AUTO_INCREMENT (somente no modo mockado)
        self._proximo_id: int = len(CLIENTES_MOCK) + 1

        self._vincular_eventos()
        self._carregar_dados()

    # =========================================================================
    # Inicialização
    # =========================================================================

    def _vincular_eventos(self) -> None:
        """
        Registra os métodos deste Controller como callbacks da View.

        PONTO EDUCACIONAL:
        Este é o mecanismo central do MVC: a View não sabe nada sobre
        o Controller, mas o Controller se "registra" na View para ser
        notificado quando o usuário agir.
        """
        self.view.vincular_eventos(
            ao_selecionar=self._ao_selecionar_linha,
            ao_novo=self._ao_clicar_novo,
            ao_salvar=self._ao_clicar_salvar,
            ao_atualizar=self._ao_clicar_atualizar,
            ao_excluir=self._ao_clicar_excluir,
            ao_limpar=self._ao_clicar_limpar,
        )

    def _carregar_dados(self) -> None:
        """
        Busca os clientes e atualiza a tabela na View.

        ATIVIDADE DOS ALUNOS:
        Substituir a linha com CLIENTES_MOCK pela chamada ao Model:

            registros_dict = self.model.listar()
            registros = [
                [r["id"], r["nome"], r["email"], r["telefone"]]
                for r in registros_dict
            ]
            self.view.atualizar_tabela(registros)
        """
        # TODO (Alunos): substituir por self.model.listar()
        #self.view.atualizar_tabela(CLIENTES_MOCK)

        registros_dict = self.model.listar()

        registros = [
            [r["id"], r["nome"], r["email"], r["telefone"]]
            for r in registros_dict
        ]

        self.view.atualizar_tabela(registros)

    # =========================================================================
    # Callbacks — executados quando o usuário interage com a View
    # =========================================================================

    def _ao_selecionar_linha(self, _event) -> None:
        """Preenche o formulário com os dados da linha clicada na tabela."""
        valores = self.view.obter_item_selecionado()
        if not valores:
            return

        self.view.preencher_formulario({
            "id":       valores[0],
            "nome":     valores[1],
            "email":    valores[2],
            "telefone": valores[3],
        })

    def _ao_clicar_novo(self) -> None:
        """Limpa o formulário para inserção de um novo cliente."""
        self.view.limpar_formulario()
        self.view.entry_nome.focus()

    # =====================================================
    # MÉTODO SALVAR
    # =====================================================

    def _ao_clicar_salvar(self) -> None:
        """
        Valida os dados e salva um novo cliente.

        ATIVIDADE DOS ALUNOS:
        Após implementar ClienteModel.salvar(), substituir o bloco
        mockado pelo seguinte:

            self.model.nome     = dados["nome"]
            self.model.email    = dados["email"]
            self.model.telefone = dados["telefone"]

            try:
                sucesso = self.model.salvar()
                if sucesso:
                    self._carregar_dados()
                    self.view.limpar_formulario()
                    self.view.definir_status("Cliente salvo!", "sucesso")
            except Exception as e:
                self.view.definir_status(f"Erro: {e}", "erro")
        """
        dados = self.view.obter_dados_formulario()

        # --- Validação básica (mantida mesmo após integração com banco) ---
        if not dados["nome"]:
            messagebox.showwarning("Campo obrigatório", "Informe o Nome do cliente.")
            self.view.entry_nome.focus()
            return

        if dados["id"]:
            messagebox.showinfo(
                "Atenção",
                "Um cliente já está selecionado.\n"
                "Use 'Atualizar' para editar ou 'Limpar' para um novo cadastro.",
            )
            return

        # --- Bloco mockado (substituir após integração com banco) ---
        # TODO (Alunos): substituir pelo bloco descrito na docstring acima
        # novo = [self._proximo_id, dados["nome"], dados["email"], dados["telefone"]]
        # CLIENTES_MOCK.append(novo)
        # self._proximo_id += 1

        # self._carregar_dados()
        # self.view.limpar_formulario()
        # self.view.definir_status(f"Cliente '{dados['nome']}' salvo com sucesso!", "sucesso")
        self.model.nome = dados["nome"]
        self.model.email = dados["email"]
        self.model.telefone = dados["telefone"]

        try:

            sucesso = self.model.salvar()

            if sucesso:

                self._carregar_dados()

                self.view.limpar_formulario()

                self.view.definir_status(
                    f"Cliente '{dados['nome']}' salvo com sucesso!",
                    "sucesso"
                )

        except Exception as e:

            self.view.definir_status(
                f"Erro: {e}",
                "erro"
            )

    # =====================================================
    # MÉTODO ATUALIZAR
    # =====================================================

    def _ao_clicar_atualizar(self) -> None:
        """
        Valida e atualiza os dados do cliente selecionado.

        ATIVIDADE DOS ALUNOS:
        Após implementar ClienteModel.atualizar(), substituir o bloco
        mockado pelo seguinte:

            self.model.id       = int(dados["id"])
            self.model.nome     = dados["nome"]
            self.model.email    = dados["email"]
            self.model.telefone = dados["telefone"]

            try:
                sucesso = self.model.atualizar()
                if sucesso:
                    self._carregar_dados()
                    self.view.limpar_formulario()
                    self.view.definir_status("Cliente atualizado!", "sucesso")
            except Exception as e:
                self.view.definir_status(f"Erro: {e}", "erro")
        """
        dados = self.view.obter_dados_formulario()

        if not dados["id"]:
            messagebox.showwarning(
                "Nenhum cliente selecionado",
                "Clique em um cliente na tabela antes de atualizar.",
            )
            return

        if not dados["nome"]:
            messagebox.showwarning("Campo obrigatório", "Informe o Nome do cliente.")
            return

        # TODO (Alunos): substituir pelo bloco descrito na docstring acima
        # id_upd = int(dados["id"])
        # for i, c in enumerate(CLIENTES_MOCK):
        #     if c[0] == id_upd:
        #         CLIENTES_MOCK[i] = [id_upd, dados["nome"], dados["email"], dados["telefone"]]
        #         break

        # self._carregar_dados()
        # self.view.limpar_formulario()
        # self.view.definir_status(f"Cliente '{dados['nome']}' atualizado!", "sucesso")

        self.model.id = int(dados["id"])

        self.model.nome = dados["nome"]

        self.model.email = dados["email"]

        self.model.telefone = dados["telefone"]

        try:

            sucesso = self.model.atualizar()

            if sucesso:

                self._carregar_dados()

                self.view.limpar_formulario()

                self.view.definir_status(
                    f"Cliente '{dados['nome']}' atualizado!",
                    "sucesso"
                )

        except Exception as e:

            self.view.definir_status(
                f"Erro: {e}",
                "erro"
            )

    # =====================================================
    # MÉTODO EXCLUIR
    # =====================================================

    def _ao_clicar_excluir(self) -> None:
        """
        Solicita confirmação e exclui o cliente selecionado.

        PONTO EDUCACIONAL:
        Ao integrar com o banco, se o cliente possuir pedidos cadastrados,
        o MySQL pode rejeitar a exclusão por integridade referencial (FK).
        Soluções possíveis:
          1. Excluir os pedidos do cliente antes de excluir o cliente.
          2. Configurar a FK com ON DELETE CASCADE.

        ATIVIDADE DOS ALUNOS:
        Após implementar ClienteModel.excluir(), substituir o bloco
        mockado pelo seguinte:

            self.model.id = int(dados["id"])
            try:
                sucesso = self.model.excluir()
                if sucesso:
                    self._carregar_dados()
                    self.view.limpar_formulario()
                    self.view.definir_status("Cliente excluído.", "info")
            except Exception as e:
                self.view.definir_status(f"Erro: {e}", "erro")
        """
        dados = self.view.obter_dados_formulario()

        if not dados["id"]:
            messagebox.showwarning(
                "Nenhum cliente selecionado",
                "Clique em um cliente na tabela antes de excluir.",
            )
            return

        confirma = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Deseja excluir o cliente '{dados['nome']}'?\n"
            "Esta ação não pode ser desfeita.",
        )
        if not confirma:
            return

        # TODO (Alunos): substituir pelo bloco descrito na docstring acima
        # id_del = int(dados["id"])
        # CLIENTES_MOCK[:] = [c for c in CLIENTES_MOCK if c[0] != id_del]

        # self._carregar_dados()
        # self.view.limpar_formulario()
        # self.view.definir_status(f"Cliente '{dados['nome']}' excluído.", "info")

        self.model.id = int(dados["id"])

        try:

            sucesso = self.model.excluir()

            if sucesso:

                self._carregar_dados()

                self.view.limpar_formulario()

                self.view.definir_status(
                    f"Cliente '{dados['nome']}' excluído.",
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

    # =========================================================================
    # Método utilitário — usado por outros Controllers
    # =========================================================================

    def obter_clientes_para_combobox(self) -> List[dict]:
        """
        Retorna a lista de clientes formatada para Comboboxes.

        Utilizado pelo PedidoController para popular o seletor de clientes.

        Returns:
            List[dict]: Lista de dicts com 'id' e 'nome'.

        ATIVIDADE DOS ALUNOS:
        Após implementar ClienteModel.listar(), substituir por:
            return self.model.listar()
        """
        # TODO (Alunos): substituir por self.model.listar()
        return [{"id": c[0], "nome": c[1]} for c in CLIENTES_MOCK]

    # =====================================================
    # MÉTODO BUSCAR CLIENTE POR ID
    # =====================================================

    def buscar_cliente_por_id(self, id_cliente):
        """
        Busca um cliente pelo ID informado.

        Fluxo:
            View -> Controller -> Model -> Banco

        Args:
            id_cliente (int): ID do cliente.

        Returns:
            dict | None:
                Retorna os dados do cliente caso exista,
                ou None se não encontrar.
        """

        self.model.id = id_cliente

        return self.model.buscar_por_id()
