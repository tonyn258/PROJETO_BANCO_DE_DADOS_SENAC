-- Seleciona uma coluna específica da tabela
SELECT colunas
FROM tabela;

-- Seleciona todos os campos da tabela de clientes
SELECT *
FROM tb_cliente;

-- Seleciona todos os registros de uma tabela em um banco específico
SELECT *
FROM nomebanco.tabela;

-- Seleciona todos os registros da tabela tb_clientes
-- dentro do banco db_clinica
SELECT *
FROM db_clinica.tb_clientes;

-- Seleciona apenas as colunas nome, email e telefone
SELECT nome, email, telefone
FROM tb_clientes;

-- Renomeia a coluna nome para nome_cliente no resultado
SELECT
    nome AS nome_cliente,
    email,
    telefone
FROM tb_clientes;

-- Retorna apenas valores únicos da coluna fabricantes
SELECT DISTINCT fabricantes
FROM tb_produtos;

-- Lista todos os produtos ordenados pelo valor em ordem crescente
SELECT *
FROM tb_produtos
ORDER BY valor ASC;

-- Lista os 5 produtos mais baratos
SELECT *
FROM tb_produtos
ORDER BY valor ASC
LIMIT 5;

-- Retorna clientes que possuem filhos
SELECT *
FROM tb_clientes
WHERE filhos > 0;

-- Retorna produtos da marca Dell
SELECT *
FROM tb_produtos
WHERE marca = 'Dell';

-- Retorna clientes que possuem filhos
-- e são do sexo feminino
SELECT *
FROM tb_clientes
WHERE filhos > 0
  AND sexo = 'Feminino';

-- Retorna produtos da Dell
-- ou produtos com valor maior ou igual a 1000
SELECT *
FROM tb_produtos
WHERE marca = 'Dell'
   OR valor >= 1000;

-- Retorna produtos da Dell ou Lenovo
SELECT *
FROM tb_produtos
WHERE marca = 'Dell'
   OR marca = 'Lenovo';

-- Mesmo resultado do exemplo anterior,
-- utilizando o operador IN
SELECT *
FROM tb_produtos
WHERE marca IN ('Dell', 'Lenovo');

-- Retorna produtos cujo valor está
-- entre 1200 e 4000
SELECT *
FROM tb_produtos
WHERE valor BETWEEN 1200 AND 4000;

-- Busca produtos que contenham a palavra Mouse
-- em qualquer posição do nome
SELECT *
FROM tb_produtos
WHERE nome_produto LIKE '%Mouse%';

-- Exemplos de LIKE:

-- Contém Mouse em qualquer posição
LIKE '%Mouse%';

-- Termina com Mouse
LIKE '%Mouse';

-- Começa com Mouse
LIKE 'Mouse%';

-- Retorna clientes sem telefone cadastrado
SELECT *
FROM tb_clientes
WHERE telefone IS NULL;

-- Conta quantos produtos possuem nome cadastrado
SELECT COUNT(nome_produto)
FROM tb_produtos;

-- Conta todos os registros da tabela
SELECT COUNT(*)
FROM tb_produtos;

-- Soma todos os valores da coluna preço_custo
SELECT SUM(preco_custo)
FROM tb_produtos;

-- Estatísticas dos preços de venda
SELECT
    AVG(preco_venda) AS media_precos,
    MIN(preco_venda) AS menor_preco,
    MAX(preco_venda) AS maior_preco
FROM tb_produtos;

-- Conta quantos produtos existem por marca
SELECT
    marca,
    COUNT(*) AS quantidade
FROM tb_produtos
GROUP BY marca;

-- Conta todos os produtos da tabela
SELECT COUNT(*)
FROM tb_produtos;

-- Conta produtos por marca
-- e ordena pela quantidade
SELECT
    marca,
    COUNT(*) AS quantidade
FROM tb_produtos
GROUP BY marca
ORDER BY COUNT(*);

-- Conta funcionários por cargo
-- apenas do campus Pouso Alegre
SELECT
    cargo,
    COUNT(*) AS quantidade
FROM tb_funcionarios
WHERE campus = 'Pouso Alegre'
GROUP BY cargo;

-- Exibe apenas cargos que possuem
-- 20 ou mais funcionários
SELECT
    cargo,
    COUNT(*) AS quantidade
FROM tb_funcionarios
GROUP BY cargo
HAVING COUNT(*) >= 20;

show databases;

use bd_turma_0275

show tables;

DESCRIBE tb_alunos;

USE bd_turma_0275;

SELECT * FROM tb_alunos;

-- criar tabela

USE bd_turma_0275;

CREATE TABLE tb_alunos (
    id_aluno INT PRIMARY KEY,
    nome_aluno VARCHAR(100) NOT NULL,
    nota_aluno DECIMAL(5,2) NOT NULL
);

-- inserir dados na tabela
INSERT INTO tb_alunos
(id_aluno, nome_aluno, nota_aluno)
VALUES
(1,'Gabriel',70),
(2,'Ludmila',80),
(3,'Amanda',90),
(4,'Ana Beatriz',90),
(5,'Anna',90),
(6,'Sarah',50),
(7,'Samuel',90),
(8,'Suina',90),
(9,'Victor',80),
(10,'Uilmer',80),
(11,'Marco Antonio',80),
(12,'Marcos Vinicios',80),
(13,'Pedro',70),
(14,'Frederico',90),
(15,'Thalita',80),
(16,'Alex',70),
(17,'Antonio',90),
(18,'Kadu',90),
(19,'Frederico',90),
(20,'João Vitor',80);

-- Criação do banco
CREATE DATABASE bd_banco_clientes_pedidos;

-- Seleção do banco
USE bd_banco_clientes_pedidos;

-- Criação da tabela clientes
CREATE TABLE tb_clientes (
    ID_clientes INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20)
);

-- Criação da tabela pedidos
CREATE TABLE tb_pedidos (
    ID_pedidos INT AUTO_INCREMENT PRIMARY KEY,
    clientes_ID INT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data DATE NOT NULL,

    FOREIGN KEY (clientes_ID)
    REFERENCES tb_clientes(ID)
);


-- CLIENTES

INSERT INTO tb_clientes (nome, email, telefone) VALUES
('Mercado São José', 'contato1@alfa.com', '(35)99999-0001'),
('Padaria Primavera', 'contato2@alfa.com', '(35)99999-0002'),
('Empório Mineiro', 'contato3@alfa.com', '(35)99999-0003'),
...
('Lanchonete Nova Era', 'contato320@alfa.com', '(35)99999-0320');



-- PEDIDOS

INSERT INTO tb_pedidos (cliente_ID, descricao, valor, data) VALUES
(12, 'Compra de refrigerantes', 180.50, '2023-01-10'),
(45, 'Compra de doces', 320.00, '2023-01-18'),
...
(287, 'Compra de produtos diversos', 4875.90, '2025-12-22');

--visualizar os registros
SELECT * FROM tb_clientes;

SELECT * FROM tb_pedidos;

--Atualizar os pedidos
UPDATE tb_pedidos
SET id_cliente = CASE id_cliente
    WHEN 5 THEN 1
    WHEN 6 THEN 2
END;

--Atualizar os clientes

UPDATE tb_clientes
SET id_cliente = CASE id_cliente
    WHEN 5 THEN 1
    WHEN 6 THEN 2
END;

--Ajustar o AUTO_INCREMENT
ALTER TABLE tb_clientes AUTO_INCREMENT = 3;
ALTER TABLE tb_pedidos AUTO_INCREMENT = 4;