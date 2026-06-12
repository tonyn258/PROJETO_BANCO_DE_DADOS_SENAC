# Guia de Execução
## Sistema de Gestão de Clientes e Pedidos (SGCP)

---

## Estado Atual do Projeto

```
┌─────────────────────────────────────────────────────────────────┐
│                    DIAGNÓSTICO DO PROJETO                       │
├────────────────────────────────────┬───────────────────────────┤
│ Interface Gráfica (Tkinter)        │  ✅ CONCLUÍDA             │
│ Arquitetura MVC                    │  ✅ CONCLUÍDA             │
│ Tela de Clientes                   │  ✅ FUNCIONAL (mock)      │
│ Tela de Pedidos                    │  ✅ FUNCIONAL (mock)      │
│ Navegação por Menu                 │  ✅ FUNCIONAL             │
│ Troca de Telas (Single Window)     │  ✅ FUNCIONAL             │
├────────────────────────────────────┼───────────────────────────┤
│ Banco de Dados MySQL               │  ❌ NÃO CRIADO            │
│ Tabela clientes                    │  ❌ NÃO CRIADA            │
│ Tabela pedidos                     │  ❌ NÃO CRIADA            │
│ Conexão Python → MySQL             │  ❌ NÃO IMPLEMENTADA      │
│ CRUD de Clientes (SQL real)        │  ❌ NÃO IMPLEMENTADO      │
│ CRUD de Pedidos (SQL real)         │  ❌ NÃO IMPLEMENTADO      │
│ Consulta JOIN                      │  ❌ NÃO IMPLEMENTADA      │
├────────────────────────────────────┼───────────────────────────┤
│ TODOs pendentes no código          │  11 ocorrências           │
│ NotImplementedError a resolver     │  15 ocorrências           │
└────────────────────────────────────┴───────────────────────────┘
```

> O sistema está funcional para demonstração da interface. Os dados exibidos
> são temporários (mockados em memória) e se perdem ao fechar o programa.

---

## Pré-requisitos

### Obrigatórios

| Requisito | Versão mínima | Como verificar |
|---|---|---|
| Python | 3.8+ | `python --version` |
| Tkinter | Incluído no Python | `python -m tkinter` |

### Necessários após integração com banco (Etapas 4-9)

| Requisito | Versão mínima | Como instalar |
|---|---|---|
| MySQL Server | 8.0+ | [mysql.com/downloads](https://dev.mysql.com/downloads/mysql/) |
| mysql-connector-python | 8.3.0 | `pip install -r requirements.txt` |

---

## Parte 1 — Executar o Sistema no Estado Atual (sem banco)

### Passo 1 — Verificar o Python

Abra o terminal (Prompt de Comando ou PowerShell) e execute:

```bash
python --version
```

Saída esperada: `Python 3.x.x`

Se o comando não for reconhecido, instale o Python em [python.org](https://python.org/downloads).

**Windows:** marque a opção **"Add Python to PATH"** durante a instalação.

---

### Passo 2 — Navegar até a pasta do projeto

```bash
cd "c:\Users\jerem\OneDrive\Desktop\projeto banco de dados"
```

Ou, no Windows Explorer, navegue até a pasta e abra o terminal com:
`Shift + clique direito` → "Abrir janela do PowerShell aqui"

---

### Passo 3 — Verificar a estrutura de arquivos

```bash
# Windows (PowerShell)
Get-ChildItem -Recurse -Include "*.py" | Select-Object Name
```

Você deverá ver os arquivos: `main.py`, `cliente_model.py`, `pedido_model.py`,
`cliente_view.py`, `pedido_view.py`, `cliente_controller.py`,
`pedido_controller.py`, `conexao.py`.

---

### Passo 4 — Executar o sistema

```bash
python main.py
```

A janela do sistema abrirá **maximizada**.

---

### O que você verá (estado atual com mock)

**Tela Inicial — Boas-vindas**

```
┌──────────────────────────────────────────────────────────┐
│  ♥  Sistema de Clientes e Pedidos          [menu]        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│        Bem-vindo ao Sistema de Clientes e Pedidos        │
│     Utilize o menu superior para navegar entre telas.    │
│               Disciplina de Banco de Dados               │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Menu superior:**
```
Cadastros ▼          Sistema ▼
  ├─ Clientes           └─ Sair
  └─ Pedidos
```

---

### Testando a tela de Clientes (mock)

1. Clique em **Cadastros → Clientes**
2. A tabela exibirá 5 clientes de demonstração:

```
ID │ Nome           │ E-mail                      │ Telefone
───┼────────────────┼─────────────────────────────┼────────────────
 1 │ João Silva     │ joao.silva@email.com         │ (35) 99999-1111
 2 │ Maria Souza    │ maria.souza@email.com        │ (35) 98888-2222
 3 │ Pedro Costa    │ pedro.costa@email.com        │ (35) 97777-3333
 4 │ Ana Oliveira   │ ana.oliveira@email.com       │ (35) 96666-4444
 5 │ Carlos Lima    │ carlos.lima@email.com        │ (35) 95555-5555
```

3. Clique em um cliente → dados preenchem o formulário
4. Teste os botões: **Novo**, **Salvar**, **Atualizar**, **Excluir**, **Limpar**

> **Importante:** As alterações existem apenas em memória.
> Fechar e reabrir o sistema restaura os dados originais.

---

### Testando a tela de Pedidos (mock)

1. Clique em **Cadastros → Pedidos**
2. A tabela exibirá 5 pedidos de demonstração
3. O campo **Cliente** é um Combobox com os 5 clientes disponíveis
4. Funcionalidade de CRUD está simulada (sem persistência)

---

## Parte 2 — Implementar o Banco de Dados (Tarefa dos Alunos)

Esta seção descreve o caminho completo de implementação. Siga as etapas **em ordem**.

---

### Etapa 1 — Instalar o MySQL Server

Baixe e instale o **MySQL Community Server 8.0** em:
`https://dev.mysql.com/downloads/mysql/`

Durante a instalação:
- Tipo: **Developer Default** (ou apenas Server + Workbench)
- Defina uma senha para o usuário `root` — **anote essa senha**

Verifique a instalação:
```bash
mysql --version
```

---

### Etapa 2 — Instalar o Conector Python

```bash
pip install -r requirements.txt
```

Ou individualmente:
```bash
pip install mysql-connector-python==8.3.0
```

Verificar instalação:
```bash
python -c "import mysql.connector; print('Conector instalado:', mysql.connector.__version__)"
```

---

### Etapa 3 — Criar o Banco de Dados

Abra o **MySQL Workbench** ou o terminal MySQL e execute:

```sql
CREATE DATABASE banco_clientes_pedidos
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE banco_clientes_pedidos;
```

---

### Etapa 4 — Criar as Tabelas

**Atenção:** A estrutura abaixo é a estrutura mínima esperada.
Os alunos devem **modelar** antes de criar (ver ESTUDO_DE_CASO.md).

```sql
-- Tabela de Clientes
CREATE TABLE clientes (
    id       INT          AUTO_INCREMENT PRIMARY KEY,
    nome     VARCHAR(100) NOT NULL,
    email    VARCHAR(100),
    telefone VARCHAR(20)
);

-- Tabela de Pedidos (com FOREIGN KEY para Clientes)
CREATE TABLE pedidos (
    id         INT            AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT            NOT NULL,
    descricao  VARCHAR(255)   NOT NULL,
    valor      DECIMAL(10, 2) NOT NULL,
    data       DATE           NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

Verifique as tabelas criadas:
```sql
SHOW TABLES;
DESCRIBE clientes;
DESCRIBE pedidos;
```

---

### Etapa 5 — Implementar `database/conexao.py`

Abra o arquivo [database/conexao.py](database/conexao.py) e implemente os 5 métodos
da classe `Conexao`. Consulte os comentários dentro do arquivo.

Após implementar, teste a conexão isoladamente com o script abaixo.
Crie um arquivo `teste_conexao.py` na raiz do projeto:

```python
# teste_conexao.py — arquivo temporário de teste, não faz parte do sistema
from database.conexao import Conexao

try:
    db = Conexao()
    db.abrir_conexao()
    print("✅ Conexão com MySQL estabelecida com sucesso!")

    resultado = db.buscar_todos("SELECT VERSION()")
    print(f"   MySQL versão: {resultado[0][0]}")

    db.fechar_conexao()
    print("✅ Conexão encerrada.")
except Exception as e:
    print(f"❌ Erro: {e}")
```

Execute:
```bash
python teste_conexao.py
```

Saída esperada:
```
✅ Conexão com MySQL estabelecida com sucesso!
   MySQL versão: 8.x.x
✅ Conexão encerrada.
```

---

### Etapa 6 — Implementar `model/cliente_model.py`

Abra [model/cliente_model.py](model/cliente_model.py) e implemente os 5 métodos.
Cada método possui na sua docstring:
- A query SQL esperada
- Um exemplo de código completo

Métodos a implementar:

| Método | SQL | Prioridade |
|---|---|---|
| `listar()` | `SELECT ... FROM clientes ORDER BY nome` | Alta (testa leitura) |
| `salvar()` | `INSERT INTO clientes (nome, email, telefone) VALUES (...)` | Alta |
| `atualizar()` | `UPDATE clientes SET ... WHERE id = %s` | Média |
| `excluir()` | `DELETE FROM clientes WHERE id = %s` | Média |
| `buscar_por_id()` | `SELECT ... FROM clientes WHERE id = %s` | Baixa |

Teste rápido após implementar `listar()`:
```python
# Insira um cliente pelo MySQL Workbench primeiro, depois teste:
from model.cliente_model import ClienteModel
m = ClienteModel()
print(m.listar())
```

---

### Etapa 7 — Integrar ClienteController com o banco real

Abra [controller/cliente_controller.py](controller/cliente_controller.py) e
localize os **5 comentários `# TODO (Alunos)`**.

Cada TODO possui logo abaixo um bloco comentado com o código correto.
Descomente o bloco e remova ou comente o código mockado.

```python
# ANTES (mockado):
self.view.atualizar_tabela(CLIENTES_MOCK)

# DEPOIS (integrado):
registros_dict = self.model.listar()
registros = [[r["id"], r["nome"], r["email"], r["telefone"]] for r in registros_dict]
self.view.atualizar_tabela(registros)
```

Teste rodando `python main.py` → Clientes → a tabela deve mostrar dados do MySQL.

---

### Etapa 8 — Implementar `model/pedido_model.py`

Abra [model/pedido_model.py](model/pedido_model.py) e implemente os 5 métodos.

**Atenção especial ao método `listar()`:** ele requer um `INNER JOIN`:

```sql
SELECT
    p.id,
    c.nome      AS cliente,
    p.descricao,
    p.valor,
    p.data
FROM pedidos p
INNER JOIN clientes c ON p.cliente_id = c.id
ORDER BY p.data DESC
```

Este é o JOIN que aparece na tela de Pedidos para exibir o **nome do cliente**
em vez do `cliente_id` (número).

---

### Etapa 9 — Integrar PedidoController com o banco real

Abra [controller/pedido_controller.py](controller/pedido_controller.py) e
localize os **5 comentários `# TODO (Alunos)`**.

Siga o mesmo processo da Etapa 7.

Atenção especial ao método `_carregar_clientes_combobox()`:
após integração, ele deve buscar clientes do banco em vez de importar `CLIENTES_MOCK`.

---

### Etapa 10 — Teste Final Completo

Execute `python main.py` e percorra o seguinte roteiro de testes:

```
TESTES DE CLIENTES
──────────────────
[ ] 1. Cadastrar novo cliente → verificar no MySQL Workbench (SELECT * FROM clientes)
[ ] 2. Listar clientes → tabela deve mostrar o registro salvo
[ ] 3. Selecionar cliente → formulário preenchido automaticamente
[ ] 4. Editar nome do cliente → salvar e verificar no banco
[ ] 5. Excluir cliente → confirmar e verificar remoção no banco

TESTES DE PEDIDOS
─────────────────
[ ] 6. Abrir tela de Pedidos → Combobox deve listar clientes do banco
[ ] 7. Cadastrar novo pedido → verificar no banco com JOIN:
       SELECT p.id, c.nome, p.descricao, p.valor, p.data
       FROM pedidos p INNER JOIN clientes c ON p.cliente_id = c.id;
[ ] 8. Listar pedidos → tabela deve exibir NOME do cliente (não ID)
[ ] 9. Editar pedido → salvar e verificar alteração no banco
[  ] 10. Excluir pedido → confirmar remoção no banco

TESTES DE INTEGRIDADE
─────────────────────
[ ] 11. Tentar excluir cliente com pedidos → observar comportamento
[ ] 12. Verificar que ao fechar e reabrir o sistema, os dados persistem
```

---

## Solução de Problemas Comuns

### ❌ `python` não é reconhecido

**Windows:** adicione o Python ao PATH do sistema.
No instalador Python, marque: ☑ "Add Python to PATH"

Ou execute com caminho completo:
```bash
py main.py
```

---

### ❌ `No module named 'mysql'`

O conector não está instalado. Execute:
```bash
pip install mysql-connector-python==8.3.0
```

Se `pip` não for encontrado:
```bash
python -m pip install mysql-connector-python==8.3.0
```

---

### ❌ `Access denied for user 'root'@'localhost'`

Senha incorreta na `Conexao`. Verifique o método `abrir_conexao()` em
`database/conexao.py` — o campo `password` deve corresponder à senha
definida durante a instalação do MySQL.

---

### ❌ `Unknown database 'banco_clientes_pedidos'`

O banco ainda não foi criado. Execute no MySQL:
```sql
CREATE DATABASE banco_clientes_pedidos CHARACTER SET utf8mb4;
```

---

### ❌ `tkinter.TclError: can't invoke "..." command` ao trocar telas

Pode ser causado por referência a um widget destruído. Certifique-se de que
não está acessando widgets da view anterior após chamar `_limpar_container()`.
Reinicie o sistema se o erro aparecer.

---

### ❌ `NotImplementedError: Implemente salvar()...`

Este erro é esperado enquanto os métodos do Model não forem implementados.
Implemente o método indicado na mensagem de erro e teste novamente.

---

## Resumo de Comandos

```bash
# Executar o sistema (estado atual)
python main.py

# Instalar dependências do banco (quando for integrar)
pip install -r requirements.txt

# Verificar instalação do conector
python -c "import mysql.connector; print(mysql.connector.__version__)"

# Testar conexão com o banco (criar o arquivo teste_conexao.py primeiro)
python teste_conexao.py

# Verificar quantos TODOs ainda existem no código
# Windows PowerShell:
Select-String -Path "**\*.py" -Pattern "# TODO" -Recurse | Measure-Object
```

---

## Referências

| Recurso | Link |
|---|---|
| Documentação Python 3 | https://docs.python.org/3/ |
| Documentação Tkinter | https://docs.python.org/3/library/tkinter.html |
| MySQL Connector Python | https://dev.mysql.com/doc/connector-python/en/ |
| MySQL 8.0 Reference | https://dev.mysql.com/doc/refman/8.0/en/ |
| W3Schools SQL | https://www.w3schools.com/sql/ |
| brModelo (DER) | https://www.brmodeloweb.com/ |

---

*SGCP v1.0 — Disciplina de Banco de Dados*
*Interface: concluída · Banco de dados: aguardando implementação dos alunos*
