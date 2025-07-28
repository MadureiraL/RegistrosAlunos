from tkcalendar import Calendar, DateEntry
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importnado pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando main
from main import *

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul escuro
co7 = "#ef5350"   # vermelha

co8 = "#146C94"   # azul claro
co9 = "#263238"   # + verde
co10 = "#e9edf5"   # + verde

# criando janela
janela = Tk()
janela.title('')
janela.geometry('810x535')
janela.configure(bg=co1)
janela.resizable(width=False, height=False)

Style = ttk.Style(janela)
Style.theme_use("clam")

# frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# logo ------------------------------------
global imagem, imagem_string, l_imagem

app_lg = Image.open('python SQLite/logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=' Sistema de Resgistro de Alunos',
                 width=800, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# abrindo a imagem

imagem = Image.open('python SQLite/logo.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=390, y=10)

# criando funções CRUD ------------------------------------

#função adicionar 
def adicionar():
    global imagem, imagem_string, l_imagem

    #obtendo os valores
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    sexo = c_sexo.get()
    data = c_data_nascimento.get()
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    if not all([nome, email, telefone, sexo, data, endereco, curso, img]):
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    estudante = (nome, email, telefone, sexo, data, endereco, curso, img)
    sistema.register_student(estudante)

    # função para limpar os campos
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    c_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    # mostrando valores na tabela
    mostrar_alunos()

# função procurar
def procurar():
    global imagem, imagem_string, l_imagem

    id = int(e_procurar.get())

    if not id:
        messagebox.showerror("Erro", "O campo ID é obrigatório!")
        return

    dados = sistema.search_student(id)

    if not dados:
        messagebox.showerror("Erro", "Estudante não encontrado!")
        return

    # limpando os campos
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    c_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    # preenchendo os campos com os dados do estudante
    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_tel.insert(END, dados[3])
    c_sexo.insert(END, dados[4])
    c_data_nascimento.set_date(dados[5])
    e_endereco.insert(END, dados[6])
    c_curso.insert(END, dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

# função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem

    id = int(e_procurar.get())

    # obtendo os valores
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    sexo = c_sexo.get()
    data = c_data_nascimento.get()
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    if not all([nome, email, telefone, sexo, data, endereco, curso, img, id]):
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    estudante = (nome, email, telefone, sexo, data, endereco, curso, img, id)

    sistema.update_student(estudante)

    # limpando os campos
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    c_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    imagem_string = imagem

    imagem = Image.open("python SQLite/logo.png")
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    # mostrando valores na tabela
    mostrar_alunos()

# função deletar
def deletar():  
    global imagem, imagem_string, l_imagem

    id = int(e_procurar.get())

    if not id:
        messagebox.showerror("Erro", "O campo ID é obrigatório!")
        return

    # confirmando a exclusão
    confirm = messagebox.askyesno("Confirmação", "Você tem certeza que deseja deletar este estudante?")
    if confirm:
        sistema.delete_student(id)

        # limpando os campos
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_tel.delete(0, END)
        c_sexo.delete(0, END)
        c_data_nascimento.delete(0, END)
        e_endereco.delete(0, END)
        c_curso.delete(0, END)

        # mostrando valores na tabela
        mostrar_alunos()

    

# Campos de entrada ------------------------------------

l_nome = Label(frame_detalhes, text='Nome *', anchor=NW,
               bg=co1, fg=co4, font=('Ivy 10'))
l_nome.place(x=4, y=10)
e_nome = Entry(frame_detalhes, width=30, justify='left',
               relief=SOLID)
e_nome.place(x=7, y=40)

l_email = Label(frame_detalhes, text='Email *', anchor=NW,
                bg=co1, fg=co4, font=('Ivy 10'))
l_email.place(x=4, y=70)
e_email = Entry(frame_detalhes, width=30, justify='left',
                relief=SOLID)
e_email.place(x=7, y=100)

l_tel = Label(frame_detalhes, text='Telefone *', anchor=NW,
              bg=co1, fg=co4, font=('Ivy 10'))
l_tel.place(x=4, y=130)
e_tel = Entry(frame_detalhes, width=15, justify='left',
              relief=SOLID)
e_tel.place(x=7, y=160)

l_sexo = Label(frame_detalhes, text='Sexo *', anchor=NW,
               bg=co1, fg=co4, font=('Ivy 10'))
l_sexo.place(x=127, y=130)
c_sexo = Combobox(frame_detalhes, width=7, justify='left',
                  font=('Ivy 8 bold'))
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=130, y=160)

l_data_nascimento = Label(frame_detalhes, text='Data de nascimento *', anchor=NW,
                          bg=co1, fg=co4, font=('Ivy 10'))
l_data_nascimento.place(x=220, y=10)
c_data_nascimento = DateEntry(frame_detalhes, width=18, background='darkblue',
                              foreground='white', borderwidth=2, year=date.today().year)

c_data_nascimento.place(x=220, y=40)

l_endereco = Label(frame_detalhes, text='Endereço *', anchor=NW,
                   bg=co1, fg=co4, font=('Ivy 10'))
l_endereco.place(x=220, y=70)
e_endereco = Entry(frame_detalhes, width=20, justify='left',
                   relief=SOLID)
e_endereco.place(x=224, y=100)

cursos = ['Python', 'Java', 'JavaScript', 'C#', 'C++', 'PHP']

l_curso = Label(frame_detalhes, text='Cursos *', anchor=NW,
                bg=co1, fg=co4, font=('Ivy 10'))
l_curso.place(x=220, y=130)
c_curso = Combobox(frame_detalhes, width=10, justify='left',
                   font=('Ivy 8 bold'))
c_curso['values'] = (cursos)
c_curso.place(x=224, y=160)

# Imagem------------------------------------


def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'Trocar de foto'.upper()


botao_carregar = Button(frame_detalhes, command=escolher_imagem, text='Carregar foto'.upper(
), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=390, y=160)

# Tabela Alunos------------------------------------


def mostrar_alunos():

    list_header = ['Id', 'Nome', 'Email',  'Telefone',
                   'Sexo', 'Data', 'Endereço', 'Curso']

    df_list = sistema.get_all_students()

    tree_aluno = ttk.Treeview(frame_tabela, selectmode='extended',
                              columns=list_header, show='headings')

    # scrollbar vertical
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical",
                        command=tree_aluno.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal",
                        command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')

    hd = ["nw", "nw", "nw", "center", "center",
          "center", "center", "center", "center"]
    h = [40, 150, 150, 70, 70, 70, 120, 100, 100]
    n = 0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)


# frame procurar aluno------------------------------------

frame_procurar = Frame(frame_botoes, width=40,
                       height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text='Procurar aluno[ID]', anchor=NW,
               bg=co1, fg=co4, font=('Ivy 10'))
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='left',
                   relief=SOLID, font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)
botao_procurar = Button(frame_procurar, command=procurar, text='Procurar',
                       width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# frame botoes------------------------------------

app_img_adicionar = Image.open('python SQLite/add.png')
app_img_adicionar = app_img_adicionar.resize((25, 25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)

app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar, text=' Adicionar',
                       relief=GROOVE, width=100, overrelief=RIDGE, compound=LEFT, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('python SQLite/update.png')
app_img_atualizar = app_img_atualizar.resize((25, 25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)

app_atualizar = Button(frame_botoes, command=atualizar,  image=app_img_atualizar, text=' Atualizar',
                       relief=GROOVE, width=100, overrelief=RIDGE, compound=LEFT, font=('Ivy 11'), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open('python SQLite/delete.png')
app_img_deletar = app_img_deletar.resize((25, 25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)

app_detelar = Button(frame_botoes, command=deletar, image=app_img_deletar, text=' Deletar',
                     relief=GROOVE, width=100, overrelief=RIDGE, compound=LEFT, font=('Ivy 11'), bg=co1, fg=co0)
app_detelar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# linha
l_linha = Label(frame_botoes, relief=GROOVE, width=10,
                 height=123, anchor=NW, font=('Ivy 1'), bg=co1, fg=co1)
l_linha.place(x=193, y=15)

# chamar a tabela------------------------------------
mostrar_alunos()


janela.mainloop()
