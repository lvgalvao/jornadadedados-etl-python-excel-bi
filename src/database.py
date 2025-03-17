import sqlite3

def conectar_db():
    conn = sqlite3.connect('database.db')
    return conn

def salvar_dados(valores):
    conn = conectar_db()
    cursor = conn.cursor()
    # Aqui você pode definir a tabela e a inserção
    cursor.execute("INSERT INTO users (Nome, Idade, Email) VALUES (?, ?, ?)", valores)
    conn.commit()
    conn.close()