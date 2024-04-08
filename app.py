


import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
import matplotlib.pyplot as plt
from datetime import datetime




# Variáveis para armazenar gastos e economias
gastos = []
economias = []




# Lista de transações
transacoes = [
    {'tipo': 'depósito', 'valor': 1800, 'categoria': 'trabalho', 'dia': 15, 'mes': '01', 'ANO': '2022'},
    {'tipo': 'saque', 'valor': 650, 'categoria': 'alimentação', 'dia': 5, 'mes': '03', 'ANO': '2023'},
    {'tipo': 'depósito', 'valor': 300, 'categoria': 'extra', 'dia': 6, 'mes': '02', 'ANO': '2023'},
    {'tipo': 'saque', 'valor': 600, 'categoria': 'aluguel', 'dia': 30, 'mes': '01', 'ANO': '2023'},
    {'tipo': 'saque', 'valor': 200, 'categoria': 'lazer', 'dia': 22, 'mes': '05', 'ANO': '2021'}
]




# Função para registrar transações em uma nova janela
def registrar_transacoes():
    nova_janela = tk.Toplevel(app)
    nova_janela.title('Registrar Transação')




    label_tipo = tk.Label(nova_janela, text='Esta transação foi de saída ou entrada de capital:')
    label_tipo.pack()




    botao_tipo = tk.IntVar()
    button_entrada = tk.Radiobutton(nova_janela, text="Entrada", variable=botao_tipo, value=1,width=100, height=4, bg='mediumpurple2')
    button_saida = tk.Radiobutton(nova_janela, text="Saída", variable=botao_tipo, value=2,width=100, height=4, bg='mediumpurple2')
    button_entrada.pack()
    button_saida.pack()




    categorias = ['Transporte', 'Alimentação', 'Moradia', 'Lazer', 'Compras', 'Outros']
    categoria_var = tk.StringVar(nova_janela)
    categoria_var.set("Selecione a Categoria")
    categoria_menu = tk.OptionMenu(nova_janela, categoria_var, *categorias)
    categoria_menu.pack()




    valor_label = tk.Label(nova_janela, text='Qual foi o valor da transação: ',width=100, height=4, bg='mediumpurple2')
    valor_entry = tk.Entry(nova_janela)
    valor_label.pack()
    valor_entry.pack()




    dia_label = tk.Label(nova_janela, text='Informe o dia da transação: ',width=100, height=4, bg='mediumpurple2')
    dia_entry = tk.Entry(nova_janela)
    dia_label.pack()
    dia_entry.pack()




    mes_label = tk.Label(nova_janela, text='Informe o mês da transação: ',width=100, height=4, bg='mediumpurple2')
    mes_entry = tk.Entry(nova_janela)
    mes_label.pack()
    mes_entry.pack()




    ano_label = tk.Label(nova_janela, text='Informe o ano da transação: ',width=100, height=4, bg='mediumpurple2')
    ano_entry = tk.Entry(nova_janela)
    ano_label.pack()
    ano_entry.pack()




    def salvar_transacao():
        tipo = 'depósito' if botao_tipo.get() == 1 else 'saque'
        categoria = categoria_var.get()
        valor = float(valor_entry.get())
        dia = int(dia_entry.get())
        mes = int(mes_entry.get())
        ano = int(ano_entry.get())




        transacoes.append({'dia': dia, 'mes': mes, 'ANO':ano, 'tipo': tipo, 'valor': valor, 'categoria': categoria})
        if tipo == 'depósito':
            economias.append(valor)
        else:
            gastos.append(valor)




        nova_janela.destroy()




    salvar_button = tk.Button(nova_janela, text="Salvar", command=salvar_transacao,width=100, height=4, bg='mediumpurple2')
    salvar_button.pack()




# Função para exibir um relatório
def relatorio():
    nova_janela = tk.Toplevel(app)
    nova_janela.title('Exibir Relatório')
    nova_janela.configure(bg='black')




    ordenar_label = tk.Label(nova_janela, text='Como deseja ordenar os dados (por data ou categoria): ',width=100, height=4, bg='mediumpurple2')
    ordenar_label.pack()




    ordenar_var = tk.StringVar()
    ordenar_entry = tk.Entry(nova_janela, textvariable=ordenar_var)
    ordenar_entry.pack()




   # Função para exibir um relatório
def relatorio():
    nova_janela = tk.Toplevel(app)
    nova_janela.title('Exibir Relatório')
    nova_janela.configure(bg='black')




    escolha_var = tk.StringVar()
    escolha_var.set("data")  # Valor padrão




    label_ordenar = tk.Label(nova_janela, text='Como deseja ordenar os dados:',width=100, height=4, bg='mediumpurple2')
    label_ordenar.pack()




    button_data = tk.Radiobutton(nova_janela, text="Por Data", variable=escolha_var, value="data",width=100, height=4, bg='mediumpurple2')
    button_categoria = tk.Radiobutton(nova_janela, text="Por Categoria", variable=escolha_var, value="categoria",width=100, height=4, bg='mediumpurple2')




    button_data.pack()
    button_categoria.pack()
escolha_var = None
nova_janela_relatorio = None




# Função para exibir um relatório
def relatorio():
    global escolha_var, nova_janela_relatorio
    nova_janela_relatorio = tk.Toplevel(app)
    nova_janela_relatorio.title('Exibir Relatório')
    nova_janela_relatorio.configure(bg='black')




    escolha_var = tk.StringVar()
    escolha_var.set("data")  # Valor padrão




    label_ordenar = tk.Label(nova_janela_relatorio, text='Como deseja ordenar os dados:',width=100, height=4, bg='mediumpurple2')
    label_ordenar.pack()




    button_data = tk.Radiobutton(nova_janela_relatorio, text="Por Data", variable=escolha_var, value="data",width=100, height=4, bg='mediumpurple2')
    button_categoria = tk.Radiobutton(nova_janela_relatorio, text="Por Categoria", variable=escolha_var, value="categoria",width=100, height=4, bg='mediumpurple2')




    button_data.pack()
    button_categoria.pack()




    exibir_button = tk.Button(nova_janela_relatorio, text="Exibir", command=exibir_relatorio,width=100, height=4, bg='mediumpurple2')
    exibir_button.pack()




# Função para exibir o relatório
def exibir_relatorio():
    global escolha_var, nova_janela_relatorio
    ordenar_por_data = escolha_var.get()




    text_area = tk.Text(nova_janela_relatorio)
    text_area.pack()




    if ordenar_por_data == 'data':
        # Converter datas para objetos de data e ordenar por data
        transacoes_ordenadas = sorted(transacoes, key=lambda x: datetime.strptime(f"{x['dia']}/{x['mes']}/{x['ANO']}", '%d/%m/%Y'), reverse=True)
    elif ordenar_por_data == 'categoria':
        # Ordenar por categoria
        transacoes_ordenadas = sorted(transacoes, key=lambda x: x['categoria'])
    else:
        print('Opção inválida!')
        return




    for transacao in transacoes_ordenadas:
        texto_transacao = f"Data: {transacao['dia']}/{transacao['mes']}/{transacao['ANO']}, Tipo: {transacao['tipo']}, Valor: {transacao['valor']}, Categoria: {transacao['categoria']}\n"
        text_area.insert(tk.END, texto_transacao)




    text_area.config(state=tk.DISABLED)  # Impede que o usuário edite o texto




# Função para calcular o saldo atual
def saldo_atual():
    total_gastos = sum(gastos)
    total_economias = sum(economias)
    saldo = total_economias - total_gastos




    nova_janela = tk.Toplevel(app)
    nova_janela.title('Calcular Saldo Atual')
    nova_janela.configure(bg='black')




    saldo_label = tk.Label(nova_janela, text=f"Saldo Atual: {saldo:.2f} reais",width=70, height=17, bg='mediumpurple2')
    saldo_label.pack()




# Função para calcular estatísticas
def calcular_estatisticas():
    # Inicializar dicionários para acompanhar gastos por categoria e a maior despesa
    gastos_por_categoria = {}
    ganhos_por_categoria = {}
    maior_despesa = {'valor': 0, 'transacao': None}




    # Iterar sobre as transações
    for transacao in transacoes:
        tipo = transacao['tipo']
        categoria = transacao['categoria']
        valor = transacao['valor']




        # Verificar se é uma despesa ou um ganho
        if tipo == 'saque':
            # Atualizar gastos por categoria
            if categoria in gastos_por_categoria:
                gastos_por_categoria[categoria] += valor
            else:
                gastos_por_categoria[categoria] = valor




            # Verificar se esta é a maior despesa
            if valor > maior_despesa['valor']:
                maior_despesa['valor'] = valor
                maior_despesa['transacao'] = transacao
        elif tipo == 'depósito':
            # Atualizar ganhos por categoria
            if categoria in ganhos_por_categoria:
                ganhos_por_categoria[categoria] += valor
            else:
                ganhos_por_categoria[categoria] = valor




    total_de_gastos = sum(gastos_por_categoria.values())
    total_de_ganhos = sum(ganhos_por_categoria.values())




    nova_janela = tk.Toplevel(app)
    nova_janela.title('Calcular Estatísticas')
    nova_janela.configure(bg='black')




    estatisticas_label = tk.Label(nova_janela, text="Estatísticas:",width=100, height=4, bg='mediumpurple2')
    estatisticas_label.pack()




    total_gastos_label = tk.Label(nova_janela, text=f"Total de Gastos: {total_de_gastos:.2f} reais",width=100, height=4, bg='mediumpurple2')
    total_gastos_label.pack()




    total_ganhos_label = tk.Label(nova_janela, text=f"Total de Ganhos: {total_de_ganhos:.2f} reais",width=100, height=4, bg='mediumpurple2')
    total_ganhos_label.pack()




    gastos_por_categoria_label = tk.Label(nova_janela, text="Gastos por Categoria:",width=100, height=4, bg='mediumpurple2')
    gastos_por_categoria_label.pack()




    for categoria, valor in gastos_por_categoria.items():
        categoria_label = tk.Label(nova_janela, text=f"{categoria}: {valor:.2f} reais",width=100, height=4, bg='mediumpurple2')
        categoria_label.pack()




    ganhos_por_categoria_label = tk.Label(nova_janela, text="Ganhos por Categoria:",width=100, height=4, bg='mediumpurple2')
    ganhos_por_categoria_label.pack()




    for categoria, valor in ganhos_por_categoria.items():
        categoria_label = tk.Label(nova_janela, text=f"{categoria}: {valor:.2f} reais",width=100, height=4, bg='mediumpurple2')
        categoria_label.pack()




    if maior_despesa['transacao'] is not None:
        maior_despesa_label = tk.Label(nova_janela, text="Maior Despesa:",width=100, height=4, bg='mediumpurple2')
        maior_despesa_label.pack()




        data_label = tk.Label(nova_janela, text=f"Data: {maior_despesa['transacao']['dia']}/{maior_despesa['transacao']['mes']}/{maior_despesa['transacao']['ANO']}",width=100, height=4, bg='mediumpurple2')
        data_label.pack()




        tipo_label = tk.Label(nova_janela, text=f"Tipo: {maior_despesa['transacao']['tipo']}",width=100, height=4, bg='mediumpurple2')
        tipo_label.pack()




        valor_label = tk.Label(nova_janela, text=f"Valor: {maior_despesa['valor']:.2f} reais",width=100, height=4, bg='mediumpurple2')
        valor_label.pack()




        categoria_label = tk.Label(nova_janela, text=f"Categoria: {maior_despesa['transacao']['categoria']}",width=100, height=4, bg='mediumpurple2')
        categoria_label.pack()




# Função para salvar transações em um arquivo CSV
def salvar_csv():
    filename = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('Arquivos CSV', '*.csv')])




    with open(filename, 'w') as file:
        # Escrever o cabeçalho
        file.write('Data,Tipo,Valor,Categoria\n')




        # Escrever as transações
        for transacao in transacoes:
            linha = f"{transacao['dia']}/{transacao['mes']}/{transacao['ANO']},{transacao['tipo']},{transacao['valor']},{transacao['categoria']}\n"
            file.write(linha)




    print(f'Transações salvas em {filename}')




# Função para exibir um gráfico de gastos por categoria
def grafico_gastos_por_categoria():
    categorias = []
    valores = []




    # Calcular os gastos por categoria
    for transacao in transacoes:
        if transacao['tipo'] == 'saque':
            categoria = transacao['categoria']
            valor = transacao['valor']




            if categoria in categorias:
                index = categorias.index(categoria)
                valores[index] += valor
            else:
                categorias.append(categoria)
                valores.append(valor)




    # Criar o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(categorias, valores,color='red',label='Gastos')
    plt.xlabel('Categoria')
    plt.ylabel('Valor (R$)')
    plt.title('Gastos por Categoria')
    plt.xticks(rotation=45)
    plt.tight_layout()




    # Exibir o gráfico
    plt.show()




# Criar a janela principal
app = tk.Tk()
app.title('Banco Santo André')




# Criar botões para as principais funcionalidades
registrar_transacoes_button = tk.Button(app, text='Registrar Transações', command=registrar_transacoes,width=100, height=4, bg='mediumpurple2')
relatorio_button = tk.Button(app, text='Exibir Relatório', command=relatorio,width=100, height=4, bg='mediumpurple2')
saldo_atual_button = tk.Button(app, text='Calcular Saldo Atual', command=saldo_atual,width=100, height=4, bg='mediumpurple2')
calcular_estatisticas_button = tk.Button(app, text='Calcular Estatísticas', command=calcular_estatisticas,width=100, height=4, bg='mediumpurple2')
salvar_csv_button = tk.Button(app, text='Salvar Transações em CSV', command=salvar_csv,width=100, height=4, bg='mediumpurple2')
grafico_button = tk.Button(app, text='Gráfico de Gastos por Categoria', command=grafico_gastos_por_categoria,width=100, height=4, bg='mediumpurple2')




# Colocar os botões na janela
registrar_transacoes_button.pack()
relatorio_button.pack()
saldo_atual_button.pack()
calcular_estatisticas_button.pack()
salvar_csv_button.pack()
grafico_button.pack()




# Iniciar o loop principal da interface gráfica




app.geometry("600x600")
app.configure(background='black')
app.mainloop()


