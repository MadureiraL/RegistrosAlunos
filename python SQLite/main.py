import sqlite3
from tkinter import messagebox


class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')  # criação do banco
        self.cursor = self.conn.cursor()  # manipulacao do banco
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            sexo TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            endereco TEXT NOT NULL,
            curso TEXT NOT NULL,
            picture TEXT NOT NULL )''')

    def register_student(self, estudantes):
        self.cursor.execute(
            "INSERT INTO estudantes (nome, email, telefone, sexo, data_nascimento, endereco, curso, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", estudantes)
        self.conn.commit()

        messagebox.showinfo("Sucesso", "Resgistrado com sucesso!")

    def get_all_students(self):
        self.cursor.execute("SELECT * FROM estudantes")
        dados = self.cursor.fetchall()

        return dados
        

    def search_student(self, id):
        self.cursor.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.cursor.fetchone()

        print(f'ID: {dados[0]} | Nome: {dados[1]} | Email: {dados[2]} | Telefone: {dados[3]} | Sexo: {dados[4]} | Data de Nascimento: {dados[5]} | Endereço: {dados[6]} | Curso: {dados[7]} | Foto: {dados[8]}')

        return dados

    def update_student(self, novo_valor):
        query = 'UPDATE estudantes SET nome = ?, email = ?, telefone = ?, sexo = ?, data_nascimento = ?, endereco = ?, curso = ?, picture = ? WHERE id = ?'

        self.cursor.execute(query, novo_valor)
        self.conn.commit()
        

        messagebox.showinfo(
        'Sucesso', f'Estudante com id:{novo_valor[8]} atualizado com sucesso!')

        return novo_valor[8]

    
    def delete_student(self, id):
        self.cursor.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

        messagebox.showinfo(
            'Sucesso', f'Estudante com id:{id} deletado com sucesso!')
        
# instancia da classe
sistema = SistemaDeRegistro()

#informacoes do estudante
#estudante = ('Manu', 'manu@example.com', '(11) 99999-9999', 'Feminino', '1990-02-02', 'Rua B, 200', 'Medicina', 'imagem2.jpg')
#registro do estudante
#sistema.register_student(estudante)

#busca todos os estudantes
#sistema.get_all_students()

#buscar um estudante
#print(sistema.search_student(2))

#atualizar um estudante
#novo_valor = ('Manu', 'manu@example.com', '(11) 99999-9999', 'Feminino', '1990-02-02', 'Rua B, 200', 'Medicina', 'imagem2.jpg', 1)
#sistema.update_student(novo_valor)

#deletar um estudante
#sistema.delete_student(1)