import tkinter as tk
from tkinter import messagebox

# Função para abrir a janela de registro de funcionários
def abrir_registro_funcionarios():
    def registrar_funcionario():
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        endereco = entry_endereco.get()

        if not nome or not telefone or not email or not endereco:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        messagebox.showinfo("Sucesso", f"Funcionário {nome} registrado com sucesso!")
        limpar_campos()

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)

    # Criar uma nova janela
    janela_registro = tk.Toplevel(root)
    janela_registro.title("Registro de Funcionários")
    janela_registro.geometry("400x500")
    janela_registro.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_registro, text="Registro de Funcionários", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome
    label_nome = tk.Label(janela_registro, text="Nome:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_nome.pack(anchor="w", padx=20, pady=5)
    entry_nome = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_nome.pack(padx=20, pady=5)

    # Telefone
    label_telefone = tk.Label(janela_registro, text="Telefone:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_telefone.pack(anchor="w", padx=20, pady=5)
    entry_telefone = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_telefone.pack(padx=20, pady=5)

    # E-mail
    label_email = tk.Label(janela_registro, text="E-mail:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_email.pack(anchor="w", padx=20, pady=5)
    entry_email = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_email.pack(padx=20, pady=5)

    # Endereço
    label_endereco = tk.Label(janela_registro, text="Endereço:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_endereco.pack(anchor="w", padx=20, pady=5)
    entry_endereco = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_endereco.pack(padx=20, pady=5)

    # Botão Registrar
    btn_registrar = tk.Button(janela_registro, text="Registrar", font=("Arial", 14, "bold"), bg="green", fg="white", command=registrar_funcionario)
    btn_registrar.pack(pady=20)

# Função para abrir a janela de registro de fornecedores
def abrir_registro_fornecedores():
    def registrar_fornecedor():
        nome = entry_nome.get()
        categoria = entry_categoria.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        cnpj = entry_cnpj.get()

        # Verificar se todos os campos foram preenchidos
        if not nome or not categoria or not email or not telefone or not cnpj:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        messagebox.showinfo("Sucesso", f"Fornecedor {nome} registrado com sucesso!")
        limpar_campos()

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_categoria.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_cnpj.delete(0, tk.END)

    # Criar uma nova janela
    janela_registro = tk.Toplevel(root)
    janela_registro.title("Registro de Fornecedores")
    janela_registro.geometry("400x600")
    janela_registro.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_registro, text="Registro de Fornecedores", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome do Fornecedor
    label_nome = tk.Label(janela_registro, text="Nome do Fornecedor:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_nome.pack(anchor="w", padx=20, pady=5)
    entry_nome = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_nome.pack(padx=20, pady=5)

    # Categoria
    label_categoria = tk.Label(janela_registro, text="Categoria:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_categoria.pack(anchor="w", padx=20, pady=5)
    entry_categoria = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_categoria.pack(padx=20, pady=5)

    # E-mail
    label_email = tk.Label(janela_registro, text="E-mail:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_email.pack(anchor="w", padx=20, pady=5)
    entry_email = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_email.pack(padx=20, pady=5)

    # Telefone
    label_telefone = tk.Label(janela_registro, text="Telefone:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_telefone.pack(anchor="w", padx=20, pady=5)
    entry_telefone = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_telefone.pack(padx=20, pady=5)

    # CNPJ
    label_cnpj = tk.Label(janela_registro, text="CNPJ:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_cnpj.pack(anchor="w", padx=20, pady=5)
    entry_cnpj = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_cnpj.pack(padx=20, pady=5)

    # Botão Registrar
    btn_registrar = tk.Button(janela_registro, text="Registrar", font=("Arial", 14, "bold"), bg="green", fg="white", command=registrar_fornecedor)
    btn_registrar.pack(pady=20)

# Função para abrir a janela de registro de produtos
def abrir_registro_produtos():
    def registrar_produto():
        nome = entry_nome.get()
        descricao = entry_descricao.get()
        preco = entry_preco.get()
        fornecedor = entry_fornecedor.get()

        if not nome or not descricao or not preco or not fornecedor:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        messagebox.showinfo("Sucesso", f"Produto {nome} registrado com sucesso!")
        limpar_campos()

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        entry_fornecedor.delete(0, tk.END)

    # Criar uma nova janela
    janela_registro = tk.Toplevel(root)
    janela_registro.title("Registro de Produtos")
    janela_registro.geometry("400x500")
    janela_registro.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_registro, text="Registro de Produtos", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome do Produto
    label_nome = tk.Label(janela_registro, text="Nome do Produto:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_nome.pack(anchor="w", padx=20, pady=5)
    entry_nome = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_nome.pack(padx=20, pady=5)

    # Descrição
    label_descricao = tk.Label(janela_registro, text="Descrição:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_descricao.pack(anchor="w", padx=20, pady=5)
    entry_descricao = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_descricao.pack(padx=20, pady=5)

    # Preço
    label_preco = tk.Label(janela_registro, text="Preço:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_preco.pack(anchor="w", padx=20, pady=5)
    entry_preco = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_preco.pack(padx=20, pady=5)

    # Fornecedor
    label_fornecedor = tk.Label(janela_registro, text="Fornecedor:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_fornecedor.pack(anchor="w", padx=20, pady=5)
    entry_fornecedor = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_fornecedor.pack(padx=20, pady=5)

    # Botão Registrar
    btn_registrar = tk.Button(janela_registro, text="Registrar", font=("Arial", 14, "bold"), bg="green", fg="white", command=registrar_produto)
    btn_registrar.pack(pady=20)

# Função para sair do programa
def sair_programa():
    root.quit()

# Menu Principal
root = tk.Tk()
root.title("Menu do ADM")
root.geometry("800x600")
root.configure(bg="#8B0000")

# Título do Menu
titulo = tk.Label(root, text="Menu do ADM", font=("Arial", 30, "bold"), bg="#8B0000", fg="white")
titulo.pack(pady=20)

# Frame para organizar as seções
frame_menu = tk.Frame(root, bg="#8B0000")
frame_menu.pack(expand=True)

# Seção de Funcionários
frame_func = tk.Frame(frame_menu, bg="#8B0000", relief="groove", bd=2)
frame_func.grid(row=0, column=0, padx=20, pady=10)

label_func = tk.Label(frame_func, text="Funcionários", font=("Arial", 16, "bold"), bg="#8B0000", fg="white")
label_func.pack(pady=10)

btn_regis_func = tk.Button(frame_func, text="Registrar Funcionário", font=("Arial", 12), width=20, command=abrir_registro_funcionarios)
btn_regis_func.pack(pady=5)

btn_excluir_func = tk.Button(frame_func, text="Excluir Funcionário", font=("Arial", 12), width=20, command=lambda: messagebox.showinfo("Ação", "Abrindo tela para excluir funcionário..."))
btn_excluir_func.pack(pady=5)

# Seção de Produtos
frame_prod = tk.Frame(frame_menu, bg="#8B0000", relief="groove", bd=2)
frame_prod.grid(row=0, column=1, padx=20, pady=10)

label_prod = tk.Label(frame_prod, text="Produtos", font=("Arial", 16, "bold"), bg="#8B0000", fg="white")
label_prod.pack(pady=10)

btn_regis_prod = tk.Button(frame_prod, text="Registrar Produto", font=("Arial", 12), width=20, command=abrir_registro_produtos)
btn_regis_prod.pack(pady=5)

btn_comprar_prod = tk.Button(frame_prod, text="Comprar Produto", font=("Arial", 12), width=20, command=lambda: messagebox.showinfo("Ação", "Abrindo tela de compra de produtos..."))
btn_comprar_prod.pack(pady=5)

btn_excluir_prod = tk.Button(frame_prod, text="Excluir Produto", font=("Arial", 12), width=20, command=lambda: messagebox.showinfo("Ação", "Abrindo tela para excluir produto..."))
btn_excluir_prod.pack(pady=5)

# Seção de Fornecedores
frame_forn = tk.Frame(frame_menu, bg="#8B0000", relief="groove", bd=2)
frame_forn.grid(row=0, column=2, padx=20, pady=10)

label_forn = tk.Label(frame_forn, text="Fornecedores", font=("Arial", 16, "bold"), bg="#8B0000", fg="white")
label_forn.pack(pady=10)

btn_regis_forn = tk.Button(frame_forn, text="Registrar Fornecedor", font=("Arial", 12), width=20, command=abrir_registro_fornecedores)
btn_regis_forn.pack(pady=5)

btn_excluir_forn = tk.Button(frame_forn, text="Excluir Fornecedor", font=("Arial", 12), width=20, command=lambda: messagebox.showinfo("Ação", "Abrindo tela para excluir fornecedor..."))
btn_excluir_forn.pack(pady=5)

# Botão Sair
btn_sair = tk.Button(root, text="Sair", font=("Arial", 14, "bold"), bg="red", fg="white", command=sair_programa)
btn_sair.pack(pady=20)

# Inicia a interface
root.mainloop()