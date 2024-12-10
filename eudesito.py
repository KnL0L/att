import tkinter as tk
from tkinter import messagebox

import mysql.connector

# Estabelecer conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",      # ou o endereço do servidor MySQL
    user="root",    # seu usuário no MySQL
    password="senha12",  # sua senha no MySQL
    database="bd_sa"  # nome do banco de dados onde suas tabelas estão
)

# Criar um cursor para executar comandos SQL
cursor = db.cursor()

# Exemplo de inserção de dados na tabela Fornecedores
insert_fornecedores = """
INSERT INTO Fornecedores (nome, cnpj, endereco, telefone, email) 
VALUES (%s, %s, %s, %s, %s)
"""
valores_fornecedor = ("Fornecedor de Tecidos LTDA", "12.345.678/0001-90", "Rua das Flores, 123", "(11) 98765-4321", "contato@tecidos.com")

# Executar o comando de inserção
cursor.execute(insert_fornecedores, valores_fornecedor)

# Confirmar a transação (commit)
db.commit()

print(f"{cursor.rowcount} registro(s) inserido(s) na tabela Fornecedores.")

# Exemplo de inserção de dados na tabela Produtos
insert_produtos = """
INSERT INTO Produtos (nome, descricao, preco, quantidade_em_estoque, fornecedor_id) 
VALUES (%s, %s, %s, %s, %s)
"""
valores_produto = ("Camiseta Básica", "Camiseta 100% algodão, ideal para o dia a dia", 29.90, 100, 1)

# Executar o comando de inserção
cursor.execute(insert_produtos, valores_produto)

# Confirmar a transação (commit)
db.commit()

print(f"{cursor.rowcount} registro(s) inserido(s) na tabela Produtos.")

# Fechar a conexão com o banco de dados
cursor.close()
db.close()