# =============================================================================
# ARQUIVO: main.py
#
# PONTO DE ENTRADA DA APLICAÇÃO
#
# Este é o arquivo principal. Execute-o para iniciar o sistema:
#   python main.py
#
# RESPONSABILIDADES:
#   - Criar e configurar a janela principal (Tk root)
#   - Definir o estilo visual global (ttk.Style)
#   - Criar o menu superior
#   - Gerenciar o container central de telas
#   - Orquestrar a troca de telas sem abrir novas janelas
#
# PADRÃO ARQUITETURAL: MVC (Model-View-Controller)
#   Model      → model/          (dados e regras de negócio)
#   View       → view/           (interface gráfica)
#   Controller → controller/     (intermediação View ↔ Model)
#   Database   → database/       (conexão com MySQL — a implementar)
# =============================================================================

import tkinter as tk
from tkinter import ttk, messagebox

from view.cliente_view import ClienteView
from view.pedido_view import PedidoView
from controller.cliente_controller import ClienteController
from controller.pedido_controller import PedidoController


class MainApp:
    """
    Classe principal da aplicação — orquestra toda a interface.

    Cria a janela raiz, configura estilos, monta o menu e controla
    qual tela está visível no momento (padrão Single-Window Navigation).
    """

    def __init__(self) -> None:
        self.root = tk.Tk()
        self._tela_atual: tk.Widget | None = None

        self._configurar_janela()
        self._configurar_estilos()
        self._criar_cabecalho()
        self._criar_menu()
        self._criar_container()
        self._exibir_tela_boas_vindas()

    # =========================================================================
    # Configuração Inicial
    # =========================================================================

    def _configurar_janela(self) -> None:
        """Define título, tamanho mínimo e inicializa maximizada."""
        self.root.title("Sistema de Clientes e Pedidos — Disciplina de Banco de Dados")
        self.root.minsize(900, 650)
        self.root.configure(bg="#ECEFF1")

        # Maximiza a janela ao abrir (funciona em Windows e Linux)
        try:
            self.root.state("zoomed")       # Windows
        except tk.TclError:
            self.root.attributes("-zoomed", True)  # Linux/X11

    def _configurar_estilos(self) -> None:
        """
        Configura o tema e os estilos visuais globais (ttk.Style).

        Os estilos definidos aqui são reutilizados por todos os widgets
        ttk em qualquer tela carregada na aplicação.
        """
        style = ttk.Style()
        style.theme_use("clam")

        # --- Botão primário (ações principais: Salvar, Atualizar) ---
        style.configure(
            "Primary.TButton",
            background="#1976D2",
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=(10, 5),
            relief="flat",
        )
        style.map("Primary.TButton",
                  background=[("active", "#1565C0"), ("pressed", "#0D47A1")])

        # --- Botão de perigo (Excluir) ---
        style.configure(
            "Danger.TButton",
            background="#D32F2F",
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=(10, 5),
            relief="flat",
        )
        style.map("Danger.TButton",
                  background=[("active", "#C62828"), ("pressed", "#B71C1C")])

        # --- Botão secundário (Novo, Limpar) ---
        style.configure(
            "Secondary.TButton",
            background="#546E7A",
            foreground="white",
            font=("Segoe UI", 10),
            padding=(10, 5),
            relief="flat",
        )
        style.map("Secondary.TButton",
                  background=[("active", "#455A64"), ("pressed", "#37474F")])

        # --- Frame do formulário (LabelFrame) ---
        style.configure(
            "Section.TLabelframe",
            background="#ECEFF1",
        )
        style.configure(
            "Section.TLabelframe.Label",
            background="#ECEFF1",
            foreground="#1565C0",
            font=("Segoe UI", 10, "bold"),
        )

        # --- Treeview (tabelas) ---
        style.configure(
            "Treeview",
            background="white",
            foreground="#212121",
            rowheight=30,
            fieldbackground="white",
            font=("Segoe UI", 10),
        )
        style.configure(
            "Treeview.Heading",
            background="#1565C0",
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
        )
        style.map("Treeview",
                  background=[("selected", "#BBDEFB")],
                  foreground=[("selected", "#0D47A1")])

        # --- Frame padrão ---
        style.configure("TFrame", background="#ECEFF1")
        style.configure("TLabel", background="#ECEFF1", font=("Segoe UI", 10))
        style.configure("TEntry", font=("Segoe UI", 10))
        style.configure("TCombobox", font=("Segoe UI", 10))

        # Faz o fundo dos LabelFrames herdarem a cor do tema
        style.configure("TLabelframe",      background="#ECEFF1")
        style.configure("TLabelframe.Label", background="#ECEFF1")

    def _criar_cabecalho(self) -> None:
        """Faixa azul no topo com o título dinâmico da tela atual."""
        self._frame_header = tk.Frame(self.root, bg="#0D47A1", height=55)
        self._frame_header.pack(fill="x", side="top")
        self._frame_header.pack_propagate(False)

        # Ícone textual + título
        tk.Label(
            self._frame_header,
            text="  ♥  Sistema de Clientes e Pedidos",
            bg="#0D47A1",
            fg="white",
            font=("Segoe UI", 15, "bold"),
            anchor="w",
        ).pack(side="left", fill="y", padx=8)

        # Subtítulo / breadcrumb da tela atual
        self._label_subtitulo = tk.Label(
            self._frame_header,
            text="",
            bg="#0D47A1",
            fg="#90CAF9",
            font=("Segoe UI", 10, "italic"),
            anchor="e",
        )
        self._label_subtitulo.pack(side="right", fill="y", padx=16)

    def _criar_menu(self) -> None:
        """Cria a barra de menus superior."""
        menubar = tk.Menu(self.root, font=("Segoe UI", 10))
        self.root.config(menu=menubar)

        # Menu Cadastros
        m_cadastros = tk.Menu(menubar, tearoff=0, font=("Segoe UI", 10))
        menubar.add_cascade(label="Cadastros", menu=m_cadastros)
        m_cadastros.add_command(label="Clientes",
                                command=self._carregar_tela_clientes)
        m_cadastros.add_command(label="Pedidos",
                                command=self._carregar_tela_pedidos)

        # Menu Sistema
        m_sistema = tk.Menu(menubar, tearoff=0, font=("Segoe UI", 10))
        menubar.add_cascade(label="Sistema", menu=m_sistema)
        m_sistema.add_command(label="Sair", command=self._sair)

    def _criar_container(self) -> None:
        """
        Área central onde as telas (Views) são carregadas dinamicamente.

        A troca de telas é feita destruindo a tela anterior e criando
        a nova no mesmo container — sem abrir novas janelas.
        """
        self._container = ttk.Frame(self.root, style="TFrame")
        self._container.pack(fill="both", expand=True)

    # =========================================================================
    # Gerenciamento de Telas
    # =========================================================================

    def _limpar_container(self) -> None:
        """Remove a tela atual para preparar o carregamento da próxima."""
        if self._tela_atual is not None:
            self._tela_atual.destroy()
            self._tela_atual = None

    def _carregar_tela_clientes(self) -> None:
        """
        Carrega a tela de Clientes no container principal.

        PONTO EDUCACIONAL — Fluxo de carregamento:
        1. Destrói a tela atual (se houver)
        2. Cria a ClienteView (apenas a interface)
        3. Cria o ClienteController (liga eventos e carrega dados)
        4. O Controller popula a tabela via self.model.listar()
           (ou CLIENTES_MOCK, enquanto o banco não está integrado)
        """
        self._limpar_container()
        self._label_subtitulo.configure(text="Cadastros  >  Clientes")

        tela = ClienteView(self._container)
        tela.pack(fill="both", expand=True)
        ClienteController(tela)

        self._tela_atual = tela

    def _carregar_tela_pedidos(self) -> None:
        """Carrega a tela de Pedidos no container principal."""
        self._limpar_container()
        self._label_subtitulo.configure(text="Cadastros  >  Pedidos")

        tela = PedidoView(self._container)
        tela.pack(fill="both", expand=True)
        PedidoController(tela)

        self._tela_atual = tela

    def _exibir_tela_boas_vindas(self) -> None:
        """Tela inicial exibida ao abrir o sistema."""
        frame = ttk.Frame(self._container, style="TFrame")
        frame.pack(fill="both", expand=True)

        # Centraliza o conteúdo verticalmente
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(4, weight=1)
        frame.columnconfigure(0, weight=1)

        tk.Label(
            frame,
            text="Bem-vindo ao Sistema de Clientes e Pedidos",
            font=("Segoe UI", 18, "bold"),
            fg="#1565C0",
            bg="#ECEFF1",
        ).grid(row=1, column=0, pady=(0, 10))

        tk.Label(
            frame,
            text="Utilize o menu superior para navegar entre as telas.",
            font=("Segoe UI", 12),
            fg="#546E7A",
            bg="#ECEFF1",
        ).grid(row=2, column=0, pady=(0, 6))

        tk.Label(
            frame,
            text="Disciplina de Banco de Dados",
            font=("Segoe UI", 10, "italic"),
            fg="#90A4AE",
            bg="#ECEFF1",
        ).grid(row=3, column=0)

        self._tela_atual = frame

    def _sair(self) -> None:
        """Encerra a aplicação após confirmação do usuário."""
        if messagebox.askyesno("Sair", "Deseja realmente sair do sistema?"):
            self.root.destroy()

    # =========================================================================
    # Ponto de entrada
    # =========================================================================

    def executar(self) -> None:
        """Inicia o loop principal de eventos do Tkinter."""
        self.root.mainloop()


# -----------------------------------------------------------------------------
# Execução direta: python main.py
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app = MainApp()
    app.executar()
