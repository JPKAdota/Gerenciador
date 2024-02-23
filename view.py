import sqlite3 as lite

con = lite.connect('dados.bd')


#Funções de Inserção----------------------------------
# Inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query ="INSERT INTO Categoria (NOME) VALUES (?)"
        cur.execute(query, i)

# Inserir Receita
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query ="INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

#Inserir Gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query ="INSERT INTO Gastos (categoria, retirado_em,valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Funções para deletar -------------------------------------------
#Deletar receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

#Deletar Gastos
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)

# Funções para ver dados ----------------------

# Ver categoria
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute ("SELECT * FROM Categoria")
        linha =  cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Ver receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute ("SELECT * FROM Receitas")
        linha =  cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Ver gastos
def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute ("SELECT * FROM gastos")
        linha =  cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens




