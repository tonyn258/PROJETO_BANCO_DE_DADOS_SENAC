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
('João Silva', 'joao@email.com', '(35)99999-1001'),
('Maria Souza', 'maria@email.com', '(35)99999-1002'),
('Pedro Santos', 'pedro@email.com', '(35)99999-1003'),
('Ana Oliveira', 'ana@email.com', '(35)99999-1004'),
('Carlos Lima', 'carlos@email.com', '(35)99999-1005'),
('Fernanda Costa', 'fernanda@email.com', '(35)99999-1006'),
('Lucas Rocha', 'lucas@email.com', '(35)99999-1007'),
('Juliana Alves', 'juliana@email.com', '(35)99999-1008'),
('Ricardo Gomes', 'ricardo@email.com', '(35)99999-1009'),
('Patricia Martins', 'patricia@email.com', '(35)99999-1010');



-- PEDIDOS

INSERT INTO tb_pedidos (cliente_id, descricao, valor, data) VALUES
(1, 'Notebook Dell Inspiron i5', 3500.00, '2025-06-01'),
(2, 'Mouse Gamer Logitech G203', 120.00, '2025-06-02'),
(3, 'Teclado Mecânico Redragon Kumara', 250.00, '2025-06-03'),
(4, 'Monitor LG 24 Polegadas', 899.90, '2025-06-04'),
(5, 'SSD Kingston 1TB', 420.00, '2025-06-05'),
(6, 'Memória RAM DDR4 16GB', 280.00, '2025-06-06'),
(7, 'Placa de Vídeo RTX 4060', 2450.00, '2025-06-07'),
(8, 'Processador Ryzen 5 5600', 850.00, '2025-06-08'),
(9, 'Fonte Corsair 650W', 430.00, '2025-06-09'),
(10, 'Gabinete Gamer RGB', 320.00, '2025-06-10'),
(1, 'Webcam Full HD Logitech', 210.00, '2025-06-11'),
(2, 'Headset HyperX Cloud', 390.00, '2025-06-12'),
(3, 'Impressora Epson EcoTank', 1350.00, '2025-06-13'),
(4, 'HD Externo Seagate 2TB', 520.00, '2025-06-14'),
(5, 'Switch TP-Link 8 Portas', 180.00, '2025-06-15'),
(6, 'Roteador Wi-Fi 6', 450.00, '2025-06-16'),
(7, 'Notebook Lenovo IdeaPad', 4200.00, '2025-06-17'),
(8, 'Monitor Gamer AOC 27"', 1499.90, '2025-06-18'),
(9, 'Kit Teclado e Mouse Sem Fio', 180.00, '2025-06-19'),
(10, 'Cadeira Gamer ThunderX3', 1299.90, '2025-06-20');

--visualizar os registros
SELECT * FROM tb_clientes;

SELECT * FROM tb_pedidos;