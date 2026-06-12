# ESTUDO DE CASO
## Sistema de Gestão de Clientes e Pedidos
### Comercial Alfa Distribuidora

---

```
╔══════════════════════════════════════════════════════════════════╗
║              DOCUMENTO DE LEVANTAMENTO DE REQUISITOS             ║
║                  E ORDEM DE SERVIÇO — OS #2025-047               ║
╠══════════════════════════════════════════════════════════════════╣
║  Cliente:      Comercial Alfa Distribuidora Ltda.                ║
║  Projeto:      Sistema de Gestão de Clientes e Pedidos (SGCP)    ║
║  Documento:    Levantamento de Requisitos / Continuidade         ║
║  Versão:       2.1 — Repasse para Nova Equipe                    ║
║  Data:         Junho de 2025                                     ║
║  Status:       PENDENTE — Aguardando implementação de banco      ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## SUMÁRIO

1. [Apresentação da Empresa Cliente](#1-apresentação-da-empresa-cliente)
2. [Contexto e Problema Enfrentado](#2-contexto-e-problema-enfrentado)
3. [Histórico do Projeto](#3-histórico-do-projeto)
4. [Cenário Atual e Missão da Nova Equipe](#4-cenário-atual-e-missão-da-nova-equipe)
5. [Objetivos do Projeto](#5-objetivos-do-projeto)
6. [Escopo da Solução](#6-escopo-da-solução)
7. [Requisitos Funcionais](#7-requisitos-funcionais)
8. [Regras de Negócio](#8-regras-de-negócio)
9. [Restrições e Premissas Técnicas](#9-restrições-e-premissas-técnicas)
10. [Responsabilidades da Equipe](#10-responsabilidades-da-equipe)
11. [Entregáveis](#11-entregáveis)
12. [Critérios de Avaliação](#12-critérios-de-avaliação)
13. [Cronograma Sugerido](#13-cronograma-sugerido)
14. [Considerações Finais](#14-considerações-finais)

---

## 1. Apresentação da Empresa Cliente

**Razão Social:** Comercial Alfa Distribuidora Ltda.
**Segmento:** Distribuição regional de mercadorias
**Porte:** Médio porte — 45 colaboradores
**Sede:** Sul de Minas Gerais
**Tempo de mercado:** 18 anos

A **Comercial Alfa Distribuidora** é uma empresa regional com 18 anos de atuação no mercado de distribuição de produtos para pequenos comércios — padarias, mercadinhos, bares, mercearias e lanchonetes do interior e cidades de médio porte da região.

A empresa se orgulha do atendimento personalizado aos clientes e da capilaridade de sua rede de entrega, que hoje abrange mais de 30 municípios. Com uma carteira ativa de aproximadamente **320 clientes** e um volume médio de **180 pedidos por mês**, a Alfa construiu sua reputação na confiança e no relacionamento de longo prazo.

Nos últimos três anos, a empresa experimentou crescimento consistente de 22% ao ano, o que trouxe prosperidade — mas também trouxe um problema que a direção não pode mais ignorar: **os processos de controle não acompanharam o crescimento**.

---

## 2. Contexto e Problema Enfrentado

### 2.1 Situação Atual

Até hoje, todo o controle de clientes e pedidos da Comercial Alfa é realizado por meio de **planilhas eletrônicas** — principalmente Microsoft Excel. Cada colaborador mantém sua própria planilha, que é salva em pen drives ou enviada por e-mail entre os setores.

Segundo depoimento da Sra. **Renata Alvarenga**, Diretora Administrativa da empresa:

> *"A gente não sabe mais quantos clientes temos de verdade. Tem cliente cadastrado três vezes com nome diferente. Tem pedido que sumiu e a gente só descobriu quando o cliente ligou reclamando. Toda semana perdemos tempo corrigindo erros que não deveriam existir. Precisamos de uma solução."*

### 2.2 Problemas Identificados

A equipe de consultoria da software house realizou visitas técnicas às instalações da Comercial Alfa e identificou os seguintes problemas críticos:

| Problema | Impacto | Frequência |
|---|---|---|
| Duplicidade de cadastros de clientes | Relatórios incorretos, retrabalho | Diária |
| Perda de registros de pedidos | Prejuízo financeiro, litígio com clientes | Semanal |
| Falta de histórico por cliente | Impossibilidade de análise comercial | Contínua |
| Erros em totalizações financeiras | Relatórios de faturamento incorretos | Mensal |
| Demora para localizar informações | Atendimento lento ao telefone | Diária |
| Ausência de backup centralizado | Risco de perda total de dados | Permanente |

### 2.3 Impacto no Negócio

Os problemas listados acima têm gerado consequências diretas e mensuráveis para a empresa:

- Estimativa de **R$ 4.800,00/mês** em retrabalho administrativo
- Perda estimada de **3 a 5 clientes por trimestre** por má experiência no atendimento
- Impossibilidade de escalar operações sem contratar mais pessoal administrativo
- Risco de **autuação fiscal** por inconsistências nos registros de vendas

A direção da Comercial Alfa tomou a decisão estratégica de **modernizar seus processos** e contratou a software house para desenvolvimento de uma solução desktop personalizada.

---

## 3. Histórico do Projeto

### 3.1 Contratação e Início do Desenvolvimento

Em março de 2025, a **Comercial Alfa Distribuidora** firmou contrato com a software house para desenvolvimento do **Sistema de Gestão de Clientes e Pedidos (SGCP)**.

O projeto foi dividido em duas frentes de trabalho:

**Equipe A — Responsável pela Interface:**
Desenvolveu a aplicação desktop utilizando Python 3 e Tkinter, seguindo o padrão arquitetural MVC (Model-View-Controller). Esta equipe concluiu seu trabalho dentro do prazo e entregou:

- Interface gráfica profissional completa
- Tela de Cadastro de Clientes (formulário + tabela)
- Tela de Cadastro de Pedidos (formulário + tabela com seleção de cliente)
- Navegação por menu superior
- Arquitetura MVC organizada em camadas bem definidas
- Código documentado e preparado para integração com banco de dados

**Equipe B — Responsável pelo Banco de Dados:**
Era a equipe responsável por modelar o banco, criar as tabelas MySQL e integrar a camada de persistência ao sistema desenvolvido pela Equipe A. **Esta equipe não concluiu o trabalho.** Por motivos internos à software house — divergências contratuais com os desenvolvedores —, a Equipe B deixou o projeto antes de realizar qualquer entrega.

### 3.2 Situação no Momento do Repasse

Quando a Equipe B saiu do projeto, o sistema estava no seguinte estado:

```
✅ Interface gráfica — CONCLUÍDA
✅ Arquitetura MVC   — CONCLUÍDA
✅ Models            — Estrutura criada, métodos sem implementação
✅ Views             — 100% funcionais com dados de demonstração
✅ Controllers       — Funcionam com dados temporários (mock)
✅ database/conexao.py — Arquivo criado, classe vazia aguardando implementação

❌ Banco de dados MySQL — NÃO CRIADO
❌ Tabelas              — NÃO CRIADAS
❌ Conexão Python-MySQL — NÃO IMPLEMENTADA
❌ Queries SQL (CRUD)   — NÃO IMPLEMENTADAS
❌ Consultas JOIN        — NÃO IMPLEMENTADAS
```

O cliente **Comercial Alfa** está ansioso para utilizar o sistema. A software house comprometeu-se a entregar a solução completa e, para cumprir o prazo, decidiu acionar uma nova equipe de desenvolvimento.

---

## 4. Cenário Atual e Missão da Nova Equipe

### 4.1 Contexto da Contratação

Você e sua equipe foram contratados como **Desenvolvedores Júnior** pela software house para **assumir e concluir o projeto**.

O gerente do projeto, Sr. **Marcos Duarte**, passou o seguinte briefing na reunião de onboarding:

> *"Pessoal, o sistema está praticamente pronto. A interface foi muito bem feita pelo time anterior. O que precisamos agora é da parte que faltou: modelar o banco, criar as tabelas e fazer o sistema de fato salvar os dados. O cliente está esperando há semanas. Vocês têm o código, têm o projeto, têm os requisitos. Precisamos dessa entrega."*

### 4.2 O Que Vocês Recebem

Ao assumir o projeto, a nova equipe recebe:

- Código-fonte completo do sistema (interface + arquitetura)
- Este documento de requisitos
- Acesso ao ambiente de desenvolvimento

### 4.3 O Que Vocês NÃO Recebem

- Nenhum banco de dados criado
- Nenhum script SQL pronto
- Nenhuma documentação de banco de dados deixada pela equipe anterior

**A modelagem, as decisões de estrutura e a implementação são inteiramente responsabilidade de vocês.**

---

## 5. Objetivos do Projeto

### 5.1 Objetivo Geral

Concluir o Sistema de Gestão de Clientes e Pedidos (SGCP) da Comercial Alfa Distribuidora, implementando a camada de persistência de dados em MySQL e integrando-a ao sistema Python/Tkinter já desenvolvido.

### 5.2 Objetivos Específicos

| # | Objetivo | Resultado Esperado |
|---|---|---|
| 1 | Modelar o banco de dados | DER e Modelo Relacional documentados |
| 2 | Criar o banco MySQL | Banco criado e funcional |
| 3 | Criar as tabelas | Estrutura com PKs, FKs e constraints |
| 4 | Implementar conexão | Python conectando ao MySQL com sucesso |
| 5 | Implementar CRUD de Clientes | Insert, Select, Update, Delete funcionando |
| 6 | Implementar CRUD de Pedidos | Insert, Select, Update, Delete funcionando |
| 7 | Implementar consulta avançada | JOIN retornando dados de ambas as tabelas |
| 8 | Testar o sistema | Sistema funcionando com dados reais |

---

## 6. Escopo da Solução

### 6.1 O Que Está no Escopo

- Banco de dados MySQL local (localhost)
- Duas entidades: **Clientes** e **Pedidos**
- Relacionamento entre as entidades (a definir pela equipe durante a modelagem)
- CRUD completo para ambas as entidades
- Consulta SQL que apresente pedidos com o nome do cliente associado
- Integração da camada de banco ao código Python existente

### 6.2 O Que Está Fora do Escopo

- Alterações na interface gráfica
- Desenvolvimento de relatórios
- Sistema de login e autenticação
- Controle de estoque ou produtos
- Módulo financeiro
- Deploy em servidor remoto

> **Nota:** Qualquer alteração solicitada fora deste escopo deverá ser tratada como um novo projeto e orçada separadamente.

---

## 7. Requisitos Funcionais

Os requisitos abaixo foram levantados junto à Sra. Renata Alvarenga (Diretora Administrativa) e ao Sr. Paulo Mendes (Supervisor de Vendas) da Comercial Alfa Distribuidora.

### RF-01 — Cadastro de Clientes

O sistema deve permitir o **registro de novos clientes** com as seguintes informações:

| Campo | Tipo | Obrigatoriedade |
|---|---|---|
| Nome completo | Texto | **Obrigatório** |
| Endereço de e-mail | Texto | Opcional |
| Número de telefone | Texto | Opcional |

**Comportamentos esperados:**
- Ao clicar em "Salvar", os dados devem ser gravados permanentemente no banco de dados
- O sistema deve exibir uma confirmação de sucesso após o cadastro
- Após salvar, o formulário deve ser limpo automaticamente
- A tabela de clientes deve ser atualizada imediatamente

### RF-02 — Listagem de Clientes

O sistema deve exibir todos os clientes cadastrados em uma tabela, contendo as colunas:

- ID (gerado automaticamente pelo banco)
- Nome
- E-mail
- Telefone

**Comportamento esperado:**
- A tabela deve ser carregada automaticamente ao abrir a tela
- Ao clicar em um cliente na tabela, seus dados devem preencher o formulário automaticamente

### RF-03 — Atualização de Clientes

O sistema deve permitir a **edição dos dados** de um cliente já cadastrado.

**Comportamento esperado:**
- O usuário seleciona o cliente na tabela
- Os dados aparecem no formulário
- O usuário altera os campos desejados e clica em "Atualizar"
- As alterações devem ser salvas no banco de dados

### RF-04 — Exclusão de Clientes

O sistema deve permitir a **remoção** de um cliente do cadastro.

**Comportamento esperado:**
- Deve ser solicitada confirmação antes de excluir
- Após confirmação, o registro deve ser removido do banco de dados

### RF-05 — Cadastro de Pedidos

O sistema deve permitir o **registro de novos pedidos** com as seguintes informações:

| Campo | Tipo | Obrigatoriedade |
|---|---|---|
| Cliente | Seleção (lista) | **Obrigatório** |
| Descrição do pedido | Texto | **Obrigatório** |
| Valor total | Numérico (decimal) | **Obrigatório** |
| Data do pedido | Data | **Obrigatório** |

**Comportamento esperado:**
- O campo "Cliente" deve apresentar uma lista com os clientes já cadastrados
- Não deve ser possível salvar um pedido sem selecionar um cliente válido
- Os dados devem ser gravados permanentemente no banco de dados

### RF-06 — Listagem de Pedidos

O sistema deve exibir todos os pedidos cadastrados em uma tabela, contendo as colunas:

- ID do Pedido (gerado automaticamente pelo banco)
- Nome do Cliente (e não apenas o código)
- Descrição
- Valor
- Data

> **Atenção:** Esta tela exige que os dados de **duas tabelas diferentes** sejam combinados.
> A equipe deverá identificar e implementar a consulta SQL adequada para este requisito.

### RF-07 — Atualização de Pedidos

O sistema deve permitir a **edição** de um pedido existente, incluindo a possibilidade de alterar o cliente associado.

### RF-08 — Exclusão de Pedidos

O sistema deve permitir a **remoção** de um pedido, mediante confirmação do usuário.

---

## 8. Regras de Negócio

As seguintes regras foram definidas pela direção da Comercial Alfa e devem ser respeitadas na implementação do banco de dados:

### RN-01 — Unicidade do Cadastro de Clientes

Cada cliente representa um único estabelecimento comercial. O banco de dados deve ser estruturado de forma que cada cliente possua um identificador único e exclusivo, gerado automaticamente pelo sistema.

### RN-02 — Vínculo entre Pedido e Cliente

Todo pedido registrado no sistema deve, **obrigatoriamente**, estar associado a um cliente previamente cadastrado. Não é permitido o registro de pedidos sem cliente definido.

> *"A gente não faz pedido para ninguém. Todo pedido tem um dono."*
> — Sr. Paulo Mendes, Supervisor de Vendas

### RN-03 — Histórico de Pedidos por Cliente

O sistema deve ser capaz de preservar o **histórico completo de pedidos** de cada cliente. Cada cliente pode ter um ou mais pedidos registrados ao longo do tempo, e esses registros não devem ser perdidos.

### RN-04 — Integridade dos Dados

Não deve ser possível, em hipótese alguma, que um pedido fique "órfão" — ou seja, vinculado a um cliente que não existe no banco de dados. A implementação deve garantir esta integridade ao nível do banco de dados, e não apenas na camada de aplicação.

### RN-05 — Permanência dos Dados

Os dados inseridos, alterados ou removidos devem persistir de forma permanente no banco de dados MySQL. O encerramento do sistema não deve resultar em perda de informações.

### RN-06 — Valor do Pedido

O valor de um pedido deve ser um número positivo. O banco deve ser estruturado para armazenar valores monetários com precisão de duas casas decimais.

---

## 9. Restrições e Premissas Técnicas

### 9.1 Tecnologias Obrigatórias

| Tecnologia | Justificativa |
|---|---|
| Python 3 | Linguagem da aplicação já desenvolvida |
| Tkinter | Framework de interface já utilizado |
| MySQL | Banco de dados definido em contrato |
| mysql-connector-python | Biblioteca de integração Python-MySQL |
| Arquitetura MVC | Padrão já adotado no projeto |

### 9.2 Tecnologias Proibidas

A equipe **não deve** utilizar as seguintes tecnologias, pois fogem do escopo contratado e da capacidade de manutenção da equipe técnica do cliente:

- SQLite (não atende ao requisito de banco centralizado)
- SQLAlchemy ou qualquer ORM
- Django, Flask ou qualquer framework web
- Bibliotecas de interface diferentes de Tkinter

### 9.3 Premissas

- O banco de dados MySQL estará disponível no ambiente local (localhost)
- A equipe terá acesso a um servidor MySQL com permissões de criação de banco e tabelas
- O código-fonte do sistema está disponível e funcional para análise

### 9.4 Ambiente de Desenvolvimento

```
Sistema Operacional: Windows 10/11 ou Linux
Python:             3.8 ou superior
MySQL:              8.0 ou superior
Conector Python:    mysql-connector-python (pip install)
IDE:                Visual Studio Code (recomendado)
```

---

## 10. Responsabilidades da Equipe

A equipe de desenvolvimento assumirá as seguintes responsabilidades ao longo do projeto:

### Etapa 1 — Análise de Requisitos

Ler e compreender integralmente este documento. Identificar as entidades do sistema, seus atributos e o relacionamento entre elas. Registrar dúvidas e apresentar ao professor/gerente para esclarecimento.

> **Entregável:** Mapa de entidades e atributos identificados.

### Etapa 2 — Modelagem de Dados

Projetar o banco de dados com base nos requisitos levantados. Elaborar o **Diagrama Entidade-Relacionamento (DER)**, identificando:

- Entidades
- Atributos de cada entidade
- Relacionamentos entre entidades
- Cardinalidade do relacionamento

> **Atenção:** O tipo de relacionamento não está descrito explicitamente neste documento.
> A equipe deverá identificá-lo durante a análise das regras de negócio.

> **Entregável:** DER desenhado (pode ser feito à mão, no draw.io, brModelo ou ferramenta similar).

### Etapa 3 — Modelo Relacional

Converter o DER em **Modelo Relacional**, definindo:

- Nome de cada tabela
- Colunas e tipos de dados
- Chave Primária (PK) de cada tabela
- Chave Estrangeira (FK) que implementa o relacionamento
- Constraints necessárias (NOT NULL, etc.)

> **Entregável:** Modelo relacional documentado no formato tabela.

### Etapa 4 — Script SQL de Criação

Escrever o script SQL completo de criação do banco, contendo:

```sql
-- Criação do banco
CREATE DATABASE ...;

-- Seleção do banco
USE ...;

-- Criação das tabelas
CREATE TABLE clientes (...);
CREATE TABLE pedidos (...);
```

O script deve poder ser executado do zero em qualquer ambiente MySQL limpo.

> **Entregável:** Arquivo `.sql` com o script completo.

### Etapa 5 — Implementação da Conexão

Implementar a classe `Conexao` no arquivo `database/conexao.py`, utilizando `mysql-connector-python`. A implementação deve incluir:

- Abertura de conexão
- Fechamento de conexão
- Execução de queries de escrita (INSERT, UPDATE, DELETE)
- Execução de queries de leitura (SELECT)
- Tratamento básico de erros

> **Entregável:** Arquivo `database/conexao.py` implementado e testado.

### Etapa 6 — CRUD de Clientes

Implementar todos os métodos da classe `ClienteModel` no arquivo `model/cliente_model.py`:

- `salvar()` → INSERT INTO clientes
- `listar()` → SELECT FROM clientes
- `atualizar()` → UPDATE clientes
- `excluir()` → DELETE FROM clientes
- `buscar_por_id()` → SELECT com WHERE

Após implementar, atualizar o `ClienteController` substituindo os dados mockados pelas chamadas ao Model.

> **Entregável:** CRUD de clientes funcionando com dados reais do MySQL.

### Etapa 7 — CRUD de Pedidos + JOIN

Implementar todos os métodos da classe `PedidoModel` no arquivo `model/pedido_model.py`. Especial atenção ao método `listar()`, que deve utilizar **JOIN** para trazer o nome do cliente junto com os dados do pedido.

Após implementar, atualizar o `PedidoController`.

> **Entregável:** CRUD de pedidos funcionando, com a tabela da tela exibindo o nome do cliente.

### Etapa 8 — Testes

Realizar testes funcionais completos do sistema:

- Cadastrar clientes e verificar no banco (via MySQL Workbench ou similar)
- Cadastrar pedidos associados a clientes
- Editar registros e confirmar as alterações no banco
- Excluir registros e verificar a remoção
- Testar regras de integridade (tentar salvar pedido sem cliente)

> **Entregável:** Checklist de testes preenchido e assinado.

### Etapa 9 — Apresentação

Apresentar a solução concluída, conforme detalhado na seção de Entregáveis.

---

## 11. Entregáveis

Ao final do projeto, cada equipe deverá apresentar os seguintes itens:

### 11.1 Documentação de Modelagem

**DER — Diagrama Entidade-Relacionamento**
- Deve conter as entidades, atributos e o relacionamento entre elas
- Deve indicar a cardinalidade do relacionamento
- Pode ser feito em ferramenta gráfica ou à mão (desde que legível)

**Modelo Relacional**
Apresentado no seguinte formato:

```
NOME_TABELA (atributo1, atributo2, atributo3_FK → OUTRA_TABELA)
```

Onde:
- Atributos sublinhados = Chave Primária
- Sufixo _FK = Chave Estrangeira
- → indica a tabela referenciada

### 11.2 Script SQL

Arquivo `.sql` contendo:

- `CREATE DATABASE` com charset UTF-8
- `CREATE TABLE` para cada entidade
- Definição de `PRIMARY KEY` com `AUTO_INCREMENT`
- Definição de `FOREIGN KEY` com referência correta
- `INSERT INTO` com pelo menos 5 registros de teste em cada tabela
- Ao menos uma query `SELECT` com `JOIN` demonstrando o funcionamento

### 11.3 Código Python Implementado

Arquivos modificados e funcionais:

- `database/conexao.py` — Conexão MySQL implementada
- `model/cliente_model.py` — Todos os métodos implementados
- `model/pedido_model.py` — Todos os métodos implementados
- `controller/cliente_controller.py` — TODOs substituídos por chamadas ao Model
- `controller/pedido_controller.py` — TODOs substituídos por chamadas ao Model

### 11.4 Demonstração do Sistema

Demonstração ao vivo do sistema funcionando com dados reais no MySQL, cobrindo:

- [ ] Cadastrar um novo cliente
- [ ] Listar clientes na tabela
- [ ] Editar os dados de um cliente
- [ ] Excluir um cliente (observar regra de integridade, se aplicável)
- [ ] Cadastrar um novo pedido associado a um cliente
- [ ] Listar pedidos com o nome do cliente exibido na tabela
- [ ] Editar um pedido
- [ ] Excluir um pedido

### 11.5 Apresentação Técnica (10 minutos)

A equipe deverá apresentar oralmente:

1. **Modelagem escolhida** — Por que estruturaram o banco desta forma?
2. **Tipo de relacionamento identificado** — Qual é e por quê?
3. **Decisões técnicas** — Que tipos de dados escolheram e por quê?
4. **Dificuldades encontradas** — O que foi mais difícil? Como resolveram?
5. **Demonstração ao vivo** — Sistema funcionando em tempo real

---

## 12. Critérios de Avaliação

| Critério | Descrição | Peso |
|---|---|---|
| **Modelagem de Dados** | Qualidade do DER, identificação correta das entidades, atributos e relacionamento | 20% |
| **Estrutura das Tabelas** | Tipos de dados adequados, constraints corretas, nomenclatura | 15% |
| **Relacionamentos** | Implementação correta da FK, identificação da cardinalidade | 15% |
| **Implementação SQL** | Scripts CREATE TABLE, INSERT, UPDATE, DELETE funcionando | 20% |
| **Integração Python-MySQL** | Conexão estável, dados persistindo corretamente | 15% |
| **Consulta JOIN** | Pedidos listados com nome do cliente via JOIN | 10% |
| **Apresentação** | Clareza na explicação das decisões técnicas | 5% |
| **Total** | | **100%** |

### Detalhamento dos Critérios

**Modelagem de Dados (20%)**
- DER entregue e correto: 10 pontos
- Cardinalidade identificada corretamente: 5 pontos
- Atributos completos e adequados: 5 pontos

**Estrutura das Tabelas (15%)**
- Tipos de dados escolhidos adequadamente (INT, VARCHAR, DECIMAL, DATE): 8 pontos
- Constraints NOT NULL nos campos obrigatórios: 4 pontos
- Nomenclatura clara e padronizada: 3 pontos

**Relacionamentos (15%)**
- FOREIGN KEY criada e referenciando corretamente: 10 pontos
- Integridade referencial sendo respeitada pelo banco: 5 pontos

**Implementação SQL (20%)**
- INSERT funcionando para clientes e pedidos: 5 pontos
- SELECT retornando dados corretos: 5 pontos
- UPDATE persistindo alterações no banco: 5 pontos
- DELETE removendo registros do banco: 5 pontos

**Integração Python-MySQL (15%)**
- Classe Conexao implementada: 5 pontos
- ClienteModel com todos os métodos funcionando: 5 pontos
- PedidoModel com todos os métodos funcionando: 5 pontos

**Consulta JOIN (10%)**
- SELECT com JOIN retornando nome do cliente nos pedidos: 10 pontos

**Apresentação (5%)**
- Clareza, organização, capacidade de explicar as decisões técnicas: 5 pontos

---

## 13. Cronograma Sugerido

| Semana | Atividade | Entregável |
|---|---|---|
| **Semana 1** | Leitura do documento, análise do código, levantamento de dúvidas | Mapa de entidades identificadas |
| **Semana 2** | Modelagem: DER + Modelo Relacional | DER e Modelo Relacional |
| **Semana 3** | Script SQL: criação de banco e tabelas + dados de teste | Arquivo `.sql` |
| **Semana 4** | Implementação da conexão Python-MySQL | `database/conexao.py` |
| **Semana 5** | CRUD de Clientes + integração ao Controller | `cliente_model.py` + `cliente_controller.py` |
| **Semana 6** | CRUD de Pedidos + JOIN + integração ao Controller | `pedido_model.py` + `pedido_controller.py` |
| **Semana 7** | Testes, correções e ajustes finais | Checklist de testes |
| **Semana 8** | Apresentação final ao cliente (professor) | Apresentação + sistema funcionando |

> **Nota:** O cronograma é uma sugestão. O professor pode ajustá-lo conforme a carga horária da disciplina.

---

## 14. Considerações Finais

### 14.1 Mensagem do Gerente de Projeto

> *"Equipe, vocês estão assumindo um projeto real. O cliente existe, o problema existe, a pressão existe. A interface que vocês receberam foi desenvolvida por profissionais que pensaram em cada detalhe: separação de responsabilidades, código limpo, arquitetura sólida. O respeito ao trabalho que já foi feito começa por não alterar o que não precisa ser alterado.*
>
> *A missão de vocês é clara: fazer o sistema persistir dados de verdade. Quando vocês salvarem o primeiro cliente no banco, conectar o primeiro pedido ao seu cliente via foreign key, e listar os pedidos com o nome do cliente vindo de um JOIN real — aí vocês vão entender por que banco de dados é a fundação de qualquer sistema sério.*
>
> *O cliente está esperando. Bom trabalho."*
>
> — Marcos Duarte, Gerente de Projeto

### 14.2 Dica Técnica da Equipe Anterior

A Equipe A deixou o seguinte recado nos comentários do código:

> *"Olá para quem vier depois. Deixamos o código bem documentado. Cada método nos Models tem um TODO explicando exatamente o que precisa ser feito e um exemplo de SQL. Cada Controller tem um bloco de código mockado com um comentário dizendo exatamente como substituí-lo pelo código real. Siga os TODOs, leia as docstrings, e vai dar certo."*

### 14.3 Orientação Pedagógica

Este projeto foi cuidadosamente desenhado para que vocês **descubram** ao invés de receberem respostas prontas. Alguns pontos intencionalmente não estão explícitos neste documento:

- O tipo de relacionamento entre Clientes e Pedidos não está nomeado — vocês devem identificá-lo
- A consulta SQL necessária para a tela de Pedidos não está especificada — vocês devem decidir qual usar
- Os tipos de dados das colunas não estão definidos — vocês devem escolher os mais adequados

Essas lacunas não são esquecimentos. São **exercícios de análise e tomada de decisão** — habilidades essenciais para qualquer desenvolvedor.

---

```
═══════════════════════════════════════════════════════════════
APROVAÇÃO DO DOCUMENTO

Cliente:    Comercial Alfa Distribuidora Ltda.
            Renata Alvarenga — Diretora Administrativa
            Data: ___/___/______    Assinatura: ________________

Fornecedor: Software House
            Marcos Duarte — Gerente de Projetos
            Data: ___/___/______    Assinatura: ________________

Equipe:     Desenvolvedores Responsáveis
            Nome(s): _______________________________________
            Data: ___/___/______    Assinatura: ________________
═══════════════════════════════════════════════════════════════

          SISTEMA DE GESTÃO DE CLIENTES E PEDIDOS — SGCP
                  OS #2025-047 | Versão 2.1
               Comercial Alfa Distribuidora Ltda.
                   Documento Confidencial
═══════════════════════════════════════════════════════════════
```

---

*Documento gerado pela equipe de Pré-Vendas e Análise de Sistemas.*
*Qualquer alteração neste documento deve ser registrada com nova versão e aprovação de ambas as partes.*
