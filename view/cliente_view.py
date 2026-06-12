# =============================================================================
# ARQUIVO: view/cliente_view.py
#
# CAMADA: View (V do padrão MVC)
#
# RESPONSABILIDADE:
#   Exibir a interface gráfica da tela de Clientes.
#   Capturar eventos do usuário e delegá-los ao ClienteController.
#
# REGRAS DESTA CAMADA:
#   - NÃO contém lógica de negócio
#   - NÃO valida dados de domínio
#   - NÃO acessa banco de dados
#   - Apenas exibe dados e notifica o Controller sobre ações do usuário
#
# FLUXO MVC:
#   Usuário interage com a View
#       → View notifica o Controller (via callbacks registrados)
#           → Controller processa e chama a View para atualizar a tela
# =============================================================================

import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional


class ClienteView(ttk.Frame):
    """
    Tela de Cadastro de Clientes.

    Herda de ttk.Frame para poder ser incorporada na janela principal
    como um painel intercambiável (padrão de troca de telas sem
    abrir múltiplas janelas).
    """

    def __init__(self, parent: tk.Widget) -> None:
        """
        Inicializa a tela de Clientes.

        Args:
            parent: Frame container da janela principal (MainApp).
        """
        super().__init__(parent)
        self._criar_widgets()

    # =========================================================================
    # Construção dos Widgets
    # =========================================================================

    def _criar_widgets(self) -> None:
        """Orquestra a criação de todos os componentes visuais."""
        self._criar_cabecalho()
        self._criar_formulario()
        self._criar_barra_botoes()
        self._criar_tabela()

    def _criar_cabecalho(self) -> None:
        """Faixa colorida no topo com o título da tela."""
        faixa = tk.Frame(self, bg="#1565C0", height=45)
        faixa.pack(fill="x")
        faixa.pack_propagate(False)

        tk.Label(
            faixa,
            text="  Cadastro de Clientes",
            bg="#1565C0",
            fg="white",
            font=("Segoe UI", 13, "bold"),
            anchor="w",
        ).pack(fill="both", expand=True)

    def _criar_formulario(self) -> None:
        """Seção com os campos de entrada de dados do cliente."""
        frame_form = ttk.LabelFrame(
            self,
            text="Dados do Cliente",
            style="Section.TLabelframe",
            padding=(15, 10),
        )
        frame_form.pack(fill="x", padx=12, pady=(10, 4))

        # Colunas expansíveis para os campos de texto
        frame_form.columnconfigure(1, weight=1)
        frame_form.columnconfigure(3, weight=1)

        # --- Linha 0: campo ID (somente leitura) ---
        ttk.Label(frame_form, text="ID:").grid(
            row=0, column=0, sticky="e", padx=(0, 6), pady=4
        )
        self.entry_id = ttk.Entry(frame_form, width=8, state="readonly")
        self.entry_id.grid(row=0, column=1, sticky="w", padx=(0, 20), pady=4)

        ttk.Label(
            frame_form,
            text="(preenchido automaticamente pelo banco)",
            foreground="#888888",
            font=("Segoe UI", 8, "italic"),
        ).grid(row=0, column=2, columnspan=2, sticky="w", pady=4)

        # --- Linha 1: Nome e Email ---
        ttk.Label(frame_form, text="Nome: *").grid(
            row=1, column=0, sticky="e", padx=(0, 6), pady=4
        )
        self.entry_nome = ttk.Entry(frame_form)
        self.entry_nome.grid(row=1, column=1, sticky="ew", padx=(0, 20), pady=4)

        ttk.Label(frame_form, text="E-mail:").grid(
            row=1, column=2, sticky="e", padx=(0, 6), pady=4
        )
        self.entry_email = ttk.Entry(frame_form)
        self.entry_email.grid(row=1, column=3, sticky="ew", pady=4)

        # --- Linha 2: Telefone ---
        ttk.Label(frame_form, text="Telefone:").grid(
            row=2, column=0, sticky="e", padx=(0, 6), pady=4
        )
        self.entry_telefone = ttk.Entry(frame_form, width=20)
        self.entry_telefone.grid(row=2, column=1, sticky="w", padx=(0, 20), pady=4)

        # Legenda de campos obrigatórios
        ttk.Label(
            frame_form,
            text="* Campo obrigatório",
            foreground="#999999",
            font=("Segoe UI", 8, "italic"),
        ).grid(row=3, column=0, columnspan=4, sticky="w", pady=(4, 0))

    def _criar_barra_botoes(self) -> None:
        """Barra horizontal com os botões de ação e área de status."""
        frame = ttk.Frame(self, padding=(12, 6))
        frame.pack(fill="x")

        self.btn_novo = ttk.Button(frame, text="Novo",
                                   style="Secondary.TButton", width=10)
        self.btn_novo.pack(side="left", padx=(0, 5))

        self.btn_salvar = ttk.Button(frame, text="Salvar",
                                     style="Primary.TButton", width=10)
        self.btn_salvar.pack(side="left", padx=(0, 5))

        self.btn_atualizar = ttk.Button(frame, text="Atualizar",
                                        style="Primary.TButton", width=10)
        self.btn_atualizar.pack(side="left", padx=(0, 5))

        self.btn_excluir = ttk.Button(frame, text="Excluir",
                                      style="Danger.TButton", width=10)
        self.btn_excluir.pack(side="left", padx=(0, 5))

        self.btn_limpar = ttk.Button(frame, text="Limpar",
                                     style="Secondary.TButton", width=10)
        self.btn_limpar.pack(side="left")

        # Mensagem de feedback ao usuário (ex: "Salvo com sucesso!")
        self.label_status = tk.Label(
            frame, text="", fg="#4CAF50",
            font=("Segoe UI", 9, "italic"), bg="#f0f0f0"
        )
        self.label_status.pack(side="right", padx=10)

    def _criar_tabela(self) -> None:
        """Tabela Treeview com scroll para listar os clientes cadastrados."""
        frame_tab = ttk.LabelFrame(
            self,
            text="Clientes Cadastrados",
            style="Section.TLabelframe",
            padding=(8, 4),
        )
        frame_tab.pack(fill="both", expand=True, padx=12, pady=(4, 12))
        frame_tab.rowconfigure(0, weight=1)
        frame_tab.columnconfigure(0, weight=1)

        colunas = ("id", "nome", "email", "telefone")
        self.treeview = ttk.Treeview(
            frame_tab, columns=colunas, show="headings", selectmode="browse"
        )

        # Cabeçalhos das colunas
        self.treeview.heading("id",       text="ID",       anchor="center")
        self.treeview.heading("nome",     text="Nome",     anchor="w")
        self.treeview.heading("email",    text="E-mail",   anchor="w")
        self.treeview.heading("telefone", text="Telefone", anchor="center")

        # Larguras
        self.treeview.column("id",       width=55,  anchor="center", stretch=False)
        self.treeview.column("nome",     width=230, anchor="w",      minwidth=120)
        self.treeview.column("email",    width=230, anchor="w",      minwidth=120)
        self.treeview.column("telefone", width=140, anchor="center", stretch=False)

        # Scrollbars
        sb_v = ttk.Scrollbar(frame_tab, orient="vertical",   command=self.treeview.yview)
        sb_h = ttk.Scrollbar(frame_tab, orient="horizontal", command=self.treeview.xview)
        self.treeview.configure(yscrollcommand=sb_v.set, xscrollcommand=sb_h.set)

        self.treeview.grid(row=0, column=0, sticky="nsew")
        sb_v.grid(row=0, column=1, sticky="ns")
        sb_h.grid(row=1, column=0, sticky="ew")

    # =========================================================================
    # API Pública — usada pelo ClienteController para manipular a View
    # =========================================================================

    def vincular_eventos(
        self,
        ao_selecionar: Callable,
        ao_novo: Callable,
        ao_salvar: Callable,
        ao_atualizar: Callable,
        ao_excluir: Callable,
        ao_limpar: Callable,
    ) -> None:
        """
        Registra os callbacks do Controller nos widgets desta View.

        PONTO EDUCACIONAL:
        A View não sabe O QUE fazer com os eventos — ela apenas os
        repassa ao Controller, que contém a lógica de negócio.

        Args:
            ao_selecionar: Chamado ao clicar em uma linha da tabela.
            ao_novo:       Chamado ao clicar em "Novo".
            ao_salvar:     Chamado ao clicar em "Salvar".
            ao_atualizar:  Chamado ao clicar em "Atualizar".
            ao_excluir:    Chamado ao clicar em "Excluir".
            ao_limpar:     Chamado ao clicar em "Limpar".
        """
        self.treeview.bind("<<TreeviewSelect>>", ao_selecionar)
        self.btn_novo.configure(command=ao_novo)
        self.btn_salvar.configure(command=ao_salvar)
        self.btn_atualizar.configure(command=ao_atualizar)
        self.btn_excluir.configure(command=ao_excluir)
        self.btn_limpar.configure(command=ao_limpar)

    def obter_dados_formulario(self) -> dict:
        """
        Lê e retorna os valores digitados no formulário.

        Returns:
            dict: Chaves 'id', 'nome', 'email', 'telefone'.
        """
        return {
            "id":       self.entry_id.get().strip(),
            "nome":     self.entry_nome.get().strip(),
            "email":    self.entry_email.get().strip(),
            "telefone": self.entry_telefone.get().strip(),
        }

    def preencher_formulario(self, dados: dict) -> None:
        """
        Preenche os campos do formulário com os dados de um cliente.

        Chamado pelo Controller quando o usuário seleciona uma linha
        na tabela (para edição ou exclusão).

        Args:
            dados: Dict com chaves 'id', 'nome', 'email', 'telefone'.
        """
        self.limpar_formulario()

        self.entry_id.configure(state="normal")
        self.entry_id.insert(0, dados.get("id", ""))
        self.entry_id.configure(state="readonly")

        self.entry_nome.insert(0, dados.get("nome", ""))
        self.entry_email.insert(0, dados.get("email", ""))
        self.entry_telefone.insert(0, dados.get("telefone", ""))

    def limpar_formulario(self) -> None:
        """Apaga todos os campos e a mensagem de status."""
        self.entry_id.configure(state="normal")
        self.entry_id.delete(0, tk.END)
        self.entry_id.configure(state="readonly")

        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)

        self.definir_status("")

    def atualizar_tabela(self, registros: list) -> None:
        """
        Substitui o conteúdo da tabela pelos registros fornecidos.

        Chamado pelo Controller após qualquer operação de CRUD para
        manter a tabela sincronizada com os dados mais recentes.

        Args:
            registros: Lista de listas/tuplas [id, nome, email, telefone].
        """
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        for i, reg in enumerate(registros):
            tag = "par" if i % 2 == 0 else "impar"
            self.treeview.insert("", "end", values=reg, tags=(tag,))

        # Linhas alternadas (zebra striping) para melhor legibilidade
        self.treeview.tag_configure("par",   background="#FFFFFF")
        self.treeview.tag_configure("impar", background="#F5F5F5")

    def obter_item_selecionado(self) -> Optional[tuple]:
        """
        Retorna os valores da linha selecionada na tabela.

        Returns:
            tuple ou None: (id, nome, email, telefone) ou None.
        """
        sel = self.treeview.selection()
        if sel:
            return self.treeview.item(sel[0])["values"]
        return None

    def definir_status(self, mensagem: str, tipo: str = "sucesso") -> None:
        """
        Exibe uma mensagem de feedback na barra de botões.

        Args:
            mensagem: Texto a exibir.
            tipo: 'sucesso' (verde), 'erro' (vermelho) ou 'info' (azul).
        """
        cores = {"sucesso": "#2E7D32", "erro": "#C62828", "info": "#1565C0"}
        self.label_status.configure(
            text=mensagem,
            fg=cores.get(tipo, "#555555"),
        )
