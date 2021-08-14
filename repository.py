import mysql.connector


def conexao():
    db = mysql.connector.connect(
        host='localhost',
        database='DADOS',
        user='root',
        password='Gui281209'
    )
    return db

def select(db):
    comando_sql = 'SELECT * FROM INFORMACOES'
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    except:
        print('não foi possivel visualizar os produtos')

def select_id(db, id_registro):
    comando_sql = f'SELECT * FROM INFORMACOES WHERE id = {id_registro}'
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
    except:
        print('não foi possível selecionar o produto')

def delete(db, id_registro):
    comando_sql = f'DELETE FROM INFORMACOES WHERE ID = {id_registro}'
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)

def insert(db,produto):
    comando_sql = 'INSERT INTO INFORMACOES (NOME, DESCRICAO, MARCA, PRECO, COR) VALUES (%s, %s, %s, %s, %s)'
    parametros = (produto.nome_produto, produto.descricao, produto.marca, produto.preco, produto.cor)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, parametros)
        db.commit()
        cursor.close()
        print('Registro inserido com sucesso.')
    except Exception as error:
        print(error)

def update(db, produto):
    comando_sql = "UPDATE INFORMACOES SET NOME = %s, DESCRICAO = %s, MARCA = %s, PRECO = %s, COR = %s WHERE ID = %s"
    parametros = (produto.nome_produto,
                  produto.descricao,
                  produto.marca,
                  produto.preco,
                  produto.cor,
                  produto.id)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, parametros)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)
