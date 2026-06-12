# Sistema de Clientes e Pedidos
### Projeto Base — Disciplina de Banco de Dados

---

## Objetivo do Projeto

Este sistema foi desenvolvido como **base estrutural** para a disciplina de Banco de Dados.

A interface gráfica e a arquitetura já estão prontas. Os alunos são responsáveis por:

- Modelar o banco de dados no MySQL
- Criar as tabelas e relacionamentos
- Implementar a conexão com o banco
- Escrever as queries SQL (CRUD + JOIN)
- Integrar o banco ao sistema existente

> O sistema funciona com dados temporários (mock) enquanto o banco não está integrado.

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| Tkinter + ttk | Interface gráfica desktop |
| Arquitetura MVC | Organização do código |
| MySQL | Banco de dados (a implementar pelos alunos) |
| mysql-connector-python | Conector Python-MySQL (a instalar) |

---

## Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado
- Tkinter já incluído na instalação padrão do Python

### Executar o sistema

```bash
python main.py
```

Nenhuma instalação adicional é necessária para rodar o sistema com dados mockados.

---

## Estrutura do Projeto (MVC)

```
projeto/
│
├── main.py                       ← Ponto de entrada — janela principal + menu
│
├── model/                        ← Camada MODEL (dados)
│   ├── __init__.py
│   ├── cliente_model.py          ← Entidade Cliente + operações SQL
│   └── pedido_model.py           ← Entidade Pedido + operações SQL
│
├── view/                         ← Camada VIEW (interface)
│   ├── __init__.py
│   ├── cliente_view.py           ← Tela de Clientes (formulário + tabela)
│   └── pedido_view.py            ← Tela de Pedidos (formulário + tabela)
│
├── controller/                   ← Camada CONTROLLER (lógica)
│   ├── __init__.py
│   ├── cliente_controller.py     ← Controla ações da tela de Clientes
│   └── pedido_controller.py      ← Controla ações da tela de Pedidos
│
├── database/
│   ├── __init__.py
│   └── conexao.py                ← Classe de conexão MySQL (a implementar)
│
├── assets/                       ← Imagens, ícones (opcional)
└── README.md                     ← Este arquivo
```

---

## Explicação da Arquitetura MVC

### Model (model/)
Representa os **dados** da aplicação. Cada classe corresponde a uma tabela no banco.
- Define a estrutura da entidade (atributos = colunas da tabela)
- Contém os métodos de acesso ao banco: `salvar()`, `listar()`, `atualizar()`, `excluir()`
- É a **única camada** que se comunica com o banco de dados
- A View e o Controller **nunca** acessam o banco diretamente

### View (view/)
Representa a **interface gráfica**. Cada classe é uma tela do sistema.
- Exibe formulários, tabelas e botões
- **Não contém lógica de negócio**
- Captura eventos (cliques) e os repassa ao Controller via callbacks
- Recebe dados do Controller para atualizar a tela

### Controller (controller/)
Representa a **lógica de controle**. Faz a ponte entre View e Model.
- Recebe os eventos da View
- Valida os dados do formulário
- Chama os métodos do Model (que executa o SQL)
- Atualiza a View com o resultado

### Fluxo Completo (exemplo: Salvar Cliente)

```
Usuário clica "Salvar"
    → ClienteView.btn_salvar (evento)
        → ClienteController._ao_clicar_salvar()
            → lê dados: view.obter_dados_formulario()
            → valida: nome não pode estar vazio
            → chama: ClienteModel.salvar()
                → Conexao.executar_query("INSERT INTO clientes ...")
            → atualiza tabela: view.atualizar_tabela()
            → exibe status: view.definir_status("Salvo!")
```

---

## Atividades dos Alunos

### Etapa 1 — Criar o Banco de Dados

```sql
CREATE DATABASE banco_clientes_pedidos
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE banco_clientes_pedidos;
```

### Etapa 2 — Criar a Tabela de Clientes

```sql
CREATE TABLE clientes (
    id       INT          AUTO_INCREMENT PRIMARY KEY,
    nome     VARCHAR(100) NOT NULL,
    email    VARCHAR(100),
    telefone VARCHAR(20)
);
```

**Inserir dados de teste:**
```sql
INSERT INTO clientes (nome, email, telefone) VALUES
    ('João Silva',   'joao.silva@email.com',   '(35) 99999-1111'),
    ('Maria Souza',  'maria.souza@email.com',  '(35) 98888-2222'),
    ('Pedro Costa',  'pedro.costa@email.com',  '(35) 97777-3333');
```

### Etapa 3 — Criar a Tabela de Pedidos com FOREIGN KEY

```sql
CREATE TABLE pedidos (
    id         INT            AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT            NOT NULL,
    descricao  VARCHAR(255)   NOT NULL,
    valor      DECIMAL(10, 2) NOT NULL,
    data       DATE           NOT NULL,

    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

**Inserir dados de teste:**
```sql
INSERT INTO pedidos (cliente_id, descricao, valor, data) VALUES
    (1, 'Notebook Dell Inspiron', 3500.00, '2025-05-15'),
    (2, 'Mouse sem fio Logitech',  150.00, '2025-05-16'),
    (1, 'Teclado mecânico RGB',    280.00, '2025-05-17');
```

> **Dica:** A FOREIGN KEY garante que não é possível inserir um pedido
> com um `cliente_id` que não existe na tabela `clientes`.
> Teste isso! Tente inserir um pedido com `cliente_id = 999` e observe o erro.

### Etapa 4 — Implementar a Conexão MySQL

**1. Instalar o conector:**
```bash
pip install mysql-connector-python
```

**2. Implementar `database/conexao.py`:**

Abra o arquivo `database/conexao.py` e implemente os métodos da classe `Conexao`.
Consulte os comentários dentro do arquivo para orientação passo a passo.

Exemplo esperado:
```python
import mysql.connector

class Conexao:
    def abrir_conexao(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sua_senha",
            database="banco_clientes_pedidos"
        )
        self.cursor = self.conexao.cursor()

    def fechar_conexao(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conexao') and self.conexao.is_connected():
            self.conexao.close()

    def executar_query(self, sql, parametros=()):
        self.cursor.execute(sql, parametros)
        self.conexao.commit()

    def buscar_todos(self, sql, parametros=()):
        self.cursor.execute(sql, parametros)
        return self.cursor.fetchall()

    def buscar_um(self, sql, parametros=()):
        self.cursor.execute(sql, parametros)
        return self.cursor.fetchone()
```

### Etapa 5 — Implementar o CRUD nos Models

Abra `model/cliente_model.py` e implemente cada método.
Consulte as docstrings de cada método — elas contêm o SQL esperado e o código de exemplo.

**Exemplo — método `listar()` do ClienteModel:**
```python
def listar(self):
    from database.conexao import Conexao
    sql = "SELECT id, nome, email, telefone FROM clientes ORDER BY nome"
    db = Conexao()
    db.abrir_conexao()
    registros = db.buscar_todos(sql)
    db.fechar_conexao()
    return [
        {"id": r[0], "nome": r[1], "email": r[2], "telefone": r[3]}
        for r in registros
    ]
```

Faça o mesmo para `salvar()`, `atualizar()`, `excluir()` e `buscar_por_id()`.

Repita o processo para `model/pedido_model.py`.

### Etapa 6 — Implementar o JOIN nos Pedidos

O método `PedidoModel.listar()` deve usar `INNER JOIN` para trazer o nome do cliente:

```sql
SELECT
    p.id,
    c.nome      AS cliente,
    p.descricao,
    p.valor,
    p.data
FROM pedidos p
INNER JOIN clientes c ON p.cliente_id = c.id
ORDER BY p.data DESC;
```

> **Por que JOIN?** A tabela `pedidos` armazena apenas o `cliente_id` (FK),
> não o nome do cliente. Para exibir o nome na interface, precisamos cruzar
> as duas tabelas com `INNER JOIN`.

### Etapa 7 — Integrar o Banco nos Controllers

Nos arquivos `controller/cliente_controller.py` e `controller/pedido_controller.py`,
localize todos os comentários marcados com `# TODO (Alunos)` e substitua
o código mockado pelas chamadas ao Model.

**Exemplo — `_carregar_dados()` no ClienteController:**
```python
def _carregar_dados(self):
    # ANTES (mockado):
    # self.view.atualizar_tabela(CLIENTES_MOCK)

    # DEPOIS (integrado com banco):
    registros_dict = self.model.listar()
    registros = [
        [r["id"], r["nome"], r["email"], r["telefone"]]
        for r in registros_dict
    ]
    self.view.atualizar_tabela(registros)
```

---

## Diagrama do Relacionamento

```
┌─────────────────────────────┐        ┌──────────────────────────────────────┐
│          CLIENTES           │        │               PEDIDOS                │
├─────────────────────────────┤        ├──────────────────────────────────────┤
│  id       INT  PK  AI       │ 1    N │  id         INT  PK  AI              │
│  nome     VARCHAR(100) NN   │◄───────│  cliente_id INT  FK  NN              │
│  email    VARCHAR(100)      │        │  descricao  VARCHAR(255) NN          │
│  telefone VARCHAR(20)       │        │  valor      DECIMAL(10,2) NN         │
└─────────────────────────────┘        │  data       DATE  NN                 │
                                       └──────────────────────────────────────┘

  PK = PRIMARY KEY    AI = AUTO_INCREMENT
  FK = FOREIGN KEY    NN = NOT NULL
```

**Regras do relacionamento:**
- Um cliente pode ter **zero ou muitos** pedidos (1:N)
- Um pedido pertence a **exatamente um** cliente (N:1)
- Não é possível cadastrar um pedido sem um cliente existente (FK constraint)

---

## Dicas e Boas Práticas

### Parâmetros SQL (evitar SQL Injection)

Sempre use `%s` como placeholder em vez de concatenar strings:

```python
# CORRETO — parametrizado
sql = "INSERT INTO clientes (nome) VALUES (%s)"
cursor.execute(sql, (nome,))

# ERRADO — vulnerável a SQL Injection
sql = "INSERT INTO clientes (nome) VALUES ('" + nome + "')"
```

### Tratamento de Erros

Envolva as operações de banco em `try/except`:

```python
from mysql.connector import Error

try:
    db.abrir_conexao()
    db.executar_query(sql, parametros)
except Error as e:
    print(f"Erro MySQL: {e}")
finally:
    db.fechar_conexao()
```

### Testar a Conexão Isoladamente

Antes de integrar ao sistema, crie um arquivo de teste separado:

```python
# teste_conexao.py
from database.conexao import Conexao

db = Conexao()
db.abrir_conexao()
registros = db.buscar_todos("SELECT * FROM clientes")
for r in registros:
    print(r)
db.fechar_conexao()
```

Execute com `python teste_conexao.py` para validar a conexão antes de integrar.

---

## Checklist de Entrega

- [ ] Banco de dados criado no MySQL
- [ ] Tabela `clientes` criada com estrutura correta
- [ ] Tabela `pedidos` criada com FOREIGN KEY para clientes
- [ ] `database/conexao.py` implementado e testado
- [ ] `model/cliente_model.py` — todos os métodos implementados
- [ ] `model/pedido_model.py` — todos os métodos implementados (incluindo JOIN)
- [ ] Controllers atualizados (substituídos os TODOs)
- [ ] Sistema funcional com dados reais do MySQL
- [ ] Testados: inserir, listar, atualizar e excluir clientes e pedidos

---

*Projeto desenvolvido para a Disciplina de Banco de Dados.*
