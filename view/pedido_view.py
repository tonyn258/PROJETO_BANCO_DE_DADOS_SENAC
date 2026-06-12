# =============================================================================
# ARQUIVO: view/pedido_view.py
#
# CAMADA: View (V do padrão MVC)
#
# RESPONSABILIDADE:
#   Exibir a interface gráfica da tela de Pedidos.
#   Inclui um Combobox para selecionar o cliente vinculado ao pedido,
#   demonstrando o relacionamento 1:N entre Clientes e Pedidos.
#
# REGRAS DESTA CAMADA:
#   - NÃO contém lógica de negócio
#   - NÃO acessa banco de dados
#   - Repassa todos os eventos ao PedidoController
# =============================================================================

import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Optional


class PedidoView(ttk.Frame):
    """
    Tela de Cadastro de Pedidos.

    Herda de ttk.Frame para ser carregada no container da janela
    principal sem abrir uma nova janela.
    """

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent)
        # Mapeamento interno: nome do cliente → id do cliente
        # Populado pelo Controller via definir_clientes_combobox()
        self._mapa_clientes: dict = {}
        self._criar_widgets()

    # =========================================================================
    # Construção dos Widgets
    # =========================================================================

    def _criar_widgets(self) -> None:
        self._criar_cabecalho()
        self._criar_formulario()
        self._criar_barra_botoes()
        self._criar_tabela()

    def _criar_cabecalho(self) -> None:
        faixa = tk.Frame(self, bg="#1565C0", height=45)
        faixa.pack(fill="x")
        faixa.pack_propagate(False)

        tk.Label(
            faixa,
            text="  Cadastro de Pedidos",
            bg="#1565C0",
            fg="white",
            font=("Segoe UI", 13, "bold"),
            anchor="w",
        ).pack(fill="both", expand=True)

    def _criar_formulario(self) -> None:
        frame_form = ttk.LabelFrame(
            self,
            text="Dados do Pedido",
            style="Section.TLabelframe",
            padding=(15, 10),
        )
        frame_form.pack(fill="x", padx=12, pady=(10, 4))

        frame_form.columnconfigure(1, weight=2)
        frame_form.columnconfigure(3, weight=1)

        # --- Linha 0: ID ---
        ttk.Label(frame_form, text="ID Pedido:").grid(
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

        # --- Linha 1: Cliente (Combobox) e Data ---
        ttk.Label(frame_form, text="Cliente: *").grid(
            row=1, column=0, sticky="e", padx=(0, 6), pady=4
        )
        self.combo_cliente = ttk.Combobox(frame_form, state="readonly")
        self.combo_cliente.grid(row=1, column=1, sticky="ew", padx=(0, 20), pady=4)

        ttk.Label(frame_form, text="Data: *").grid(
            row=1, column=2, sticky="e", padx=(0, 6), pady=4
        )
        self.entry_data = ttk.Entry(frame_form, width=14)
        self.entry_data.grid(row=1, column=3, sticky="w", pady=4)
        self._inserir_placeholder_data()

        # --- Linha 2: Descrição ---
        ttk.Label(frame_form, text="Descrição: *").grid(
            row=2, column=0, sticky="e", padx=(0, 6), pady=4
        )
        self.entry_descricao = ttk.Entry(frame_form)
        self.entry_descricao.grid(
            row=2, column=1, columnspan=3, sticky="ew", padx=(0, 0), pady=4
        )

        # --- Linha 3: Valor ---
        ttk.Label(frame_form, text="Valor (R$): *").grid(
            row=3, column=0, sticky="e", padx=(0, 6), pady=4
        )
        frame_valor = ttk.Frame(frame_form)
        frame_valor.grid(row=3, column=1, sticky="w", pady=4)

        ttk.Label(frame_valor, text="R$").pack(side="left", padx=(0, 4))
        self.entry_valor = ttk.Entry(frame_valor, width=14)
        self.entry_valor.pack(side="left")

        # Legenda
        ttk.Label(
            frame_form,
            text="* Campos obrigatórios  |  Data: DD/MM/AAAA",
            foreground="#999999",
            font=("Segoe UI", 8, "italic"),
        ).grid(row=4, column=0, columnspan=4, sticky="w", pady=(4, 0))

    def _inserir_placeholder_data(self) -> None:
        """Insere texto de exemplo no campo de data."""
        self.entry_data.insert(0, "DD/MM/AAAA")
        self.entry_data.configure(foreground="#AAAAAA")
        self.entry_data.bind("<FocusIn>",  self._ao_focar_data)
        self.entry_data.bind("<FocusOut>", self._ao_sair_data)

    def _ao_focar_data(self, _event: tk.Event) -> None:
        if self.entry_data.get() == "DD/MM/AAAA":
            self.entry_data.delete(0, tk.END)
            self.entry_data.configure(foreground="black")

    def _ao_sair_data(self, _event: tk.Event) -> None:
        if not self.entry_data.get():
            self.entry_data.insert(0, "DD/MM/AAAA")
            self.entry_data.configure(foreground="#AAAAAA")

    def _criar_barra_botoes(self) -> None:
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

        self.label_status = tk.Label(
            frame, text="", fg="#4CAF50",
            font=("Segoe UI", 9, "italic"), bg="#f0f0f0",
        )
        self.label_status.pack(side="right", padx=10)

    def _criar_tabela(self) -> None:
        frame_tab = ttk.LabelFrame(
            self,
            text="Pedidos Cadastrados",
            style="Section.TLabelframe",
            padding=(8, 4),
        )
        frame_tab.pack(fill="both", expand=True, padx=12, pady=(4, 12))
        frame_tab.rowconfigure(0, weight=1)
        frame_tab.columnconfigure(0, weight=1)

        colunas = ("id", "cliente", "descricao", "valor", "data")
        self.treeview = ttk.Treeview(
            frame_tab, columns=colunas, show="headings", selectmode="browse"
        )

        self.treeview.heading("id",        text="ID Pedido", anchor="center")
        self.treeview.heading("cliente",   text="Cliente",   anchor="w")
        self.treeview.heading("descricao", text="Descrição", anchor="w")
        self.treeview.heading("valor",     text="Valor",     anchor="e")
        self.treeview.heading("data",      text="Data",      anchor="center")

        self.treeview.column("id",        width=75,  anchor="center", stretch=False)
        self.treeview.column("cliente",   width=190, anchor="w",      minwidth=100)
        self.treeview.column("descricao", width=260, anchor="w",      minwidth=120)
        self.treeview.column("valor",     width=110, anchor="e",      stretch=False)
        self.treeview.column("data",      width=100, anchor="center", stretch=False)

        sb_v = ttk.Scrollbar(frame_tab, orient="vertical",   command=self.treeview.yview)
        sb_h = ttk.Scrollbar(frame_tab, orient="horizontal", command=self.treeview.xview)
        self.treeview.configure(yscrollcommand=sb_v.set, xscrollcommand=sb_h.set)

        self.treeview.grid(row=0, column=0, sticky="nsew")
        sb_v.grid(row=0, column=1, sticky="ns")
        sb_h.grid(row=1, column=0, sticky="ew")

    # =========================================================================
    # API Pública — usada pelo PedidoController
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
        """Registra os callbacks do Controller nos widgets desta View."""
        self.treeview.bind("<<TreeviewSelect>>", ao_selecionar)
        self.btn_novo.configure(command=ao_novo)
        self.btn_salvar.configure(command=ao_salvar)
        self.btn_atualizar.configure(command=ao_atualizar)
        self.btn_excluir.configure(command=ao_excluir)
        self.btn_limpar.configure(command=ao_limpar)

    def definir_clientes_combobox(self, clientes: List[dict]) -> None:
        """
        Popula o Combobox com a lista de clientes disponíveis.

        Chamado pelo Controller ao carregar a tela, para que o usuário
        possa associar um pedido a um cliente existente.

        PONTO EDUCACIONAL:
        Este Combobox demonstra o relacionamento 1:N:
        um cliente pode aparecer em múltiplos pedidos.

        Args:
            clientes: Lista de dicts com chaves 'id' e 'nome'.
        """
        self._mapa_clientes = {c["nome"]: c["id"] for c in clientes}
        self.combo_cliente["values"] = list(self._mapa_clientes.keys())

    def obter_cliente_id_selecionado(self) -> Optional[int]:
        """
        Retorna o ID do cliente escolhido no Combobox.

        Returns:
            int ou None: ID do cliente, ou None se nenhum selecionado.
        """
        return self._mapa_clientes.get(self.combo_cliente.get())

    def obter_dados_formulario(self) -> dict:
        """
        Lê e retorna os valores preenchidos no formulário.

        Returns:
            dict: Chaves 'id', 'cliente_nome', 'cliente_id',
                  'descricao', 'valor', 'data'.
        """
        data_val = self.entry_data.get()
        if data_val == "DD/MM/AAAA":
            data_val = ""

        return {
            "id":           self.entry_id.get().strip(),
            "cliente_nome": self.combo_cliente.get().strip(),
            "cliente_id":   self.obter_cliente_id_selecionado(),
            "descricao":    self.entry_descricao.get().strip(),
            "valor":        self.entry_valor.get().strip(),
            "data":         data_val.strip(),
        }

    def preencher_formulario(self, dados: dict) -> None:
        """
        Preenche os campos com os dados de um pedido selecionado.

        Args:
            dados: Dict com chaves 'id', 'cliente_nome', 'descricao',
                   'valor', 'data'.
        """
        self.limpar_formulario()

        self.entry_id.configure(state="normal")
        self.entry_id.insert(0, dados.get("id", ""))
        self.entry_id.configure(state="readonly")

        if dados.get("cliente_nome"):
            self.combo_cliente.set(dados["cliente_nome"])

        self.entry_descricao.insert(0, dados.get("descricao", ""))
        self.entry_valor.insert(0, dados.get("valor", ""))

        if dados.get("data"):
            self.entry_data.configure(foreground="black")
            self.entry_data.delete(0, tk.END)
            self.entry_data.insert(0, dados["data"])

    def limpar_formulario(self) -> None:
        """Apaga todos os campos e restaura o placeholder de data."""
        self.entry_id.configure(state="normal")
        self.entry_id.delete(0, tk.END)
        self.entry_id.configure(state="readonly")

        self.combo_cliente.set("")
        self.entry_descricao.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)

        self.entry_data.delete(0, tk.END)
        self.entry_data.insert(0, "DD/MM/AAAA")
        self.entry_data.configure(foreground="#AAAAAA")

        self.definir_status("")

    def atualizar_tabela(self, registros: list) -> None:
        """
        Substitui o conteúdo da tabela pelos registros fornecidos.

        Args:
            registros: Lista de listas [id, cliente, descricao, valor, data].
        """
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        for i, reg in enumerate(registros):
            tag = "par" if i % 2 == 0 else "impar"
            self.treeview.insert("", "end", values=reg, tags=(tag,))

        self.treeview.tag_configure("par",   background="#FFFFFF")
        self.treeview.tag_configure("impar", background="#F5F5F5")

    def obter_item_selecionado(self) -> Optional[tuple]:
        """Retorna os valores da linha selecionada, ou None."""
        sel = self.treeview.selection()
        if sel:
            return self.treeview.item(sel[0])["values"]
        return None

    def definir_status(self, mensagem: str, tipo: str = "sucesso") -> None:
        """
        Exibe mensagem de feedback ao usuário.

        Args:
            mensagem: Texto a exibir.
            tipo: 'sucesso', 'erro' ou 'info'.
        """
        cores = {"sucesso": "#2E7D32", "erro": "#C62828", "info": "#1565C0"}
        self.label_status.configure(
            text=mensagem,
            fg=cores.get(tipo, "#555555"),
        )
