--GRUPO 2--
--Antônio--
--Leonardo--
--Julinha--

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
    REFERENCES tb_clientes(ID_clientes)
);




