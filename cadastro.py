import sqlite3
from models import CreatePeople, UpdatePeople, CreateAddres
from datetime import datetime





def insert_addres(endereco : CreateAddres):
    conn = sqlite3.connect("package.db")
    agora = datetime.now().strftime('%Y-%m-%d %H:%M')
    cursor = conn.cursor()
    query = "INSERT INTO addresses (state,city,street,created_at,updated_at) VALUES (?,?,?,?,?);"
    cursor.execute(query,(endereco.state,endereco.city,endereco.street,agora,agora))
    conn.commit()
    conn.close()


def insert_people(pessoa : CreatePeople):
    conn = sqlite3.connect("package.db")
    agora = datetime.now().strftime('%Y-%m-%d %H:%M')
    cursor = conn.cursor()
    query = "INSERT INTO people (name,fk_addres,fk_graduation,birth_date,email,phone,cpf,is_student,is_teacher,created_at) VALUES (?,?,?,?,?,?,?,?,?,?);"
    cursor.execute(query,(pessoa.name,pessoa.fk_addres,pessoa.fk_graduation,pessoa.birth_date,pessoa.email,pessoa.phone,pessoa.cpf,pessoa.is_student,pessoa.is_teacher,agora))
    conn.commit()
    conn.close()


def read_last_registration():
    conn = sqlite3.connect("package.db")
    cursor = conn.cursor()
    query = "SELECT * FROM people ORDER BY ROWID DESC LIMIT 1;" 
    cursor.execute(query)
    last_registro = cursor.fetchone()
    conn.close()

    if last_registro:
        return "Cadastrado com sucesso"  
    else:
        return "Erro ao cadastrar"   


def query_by_name(name: str) -> CreatePeople:
    conn = sqlite3.connect("package.db")
    cursor = conn.cursor()
    query = "SELECT * FROM people WHERE name = ?;"
    cursor.execute(query, (name,))
    results = cursor.fetchone()
    conn.close()

    if results:    
        return CreatePeople(name=results[1], fk_addres=str(results[2]), fk_graduation=str(results[3]), birth_date=results[4], email=results[5], phone=str(results[6]), cpf=str(results[7]), is_student=results[8], is_teacher=results[9])
    else:
        return "Nenhum cadastro"
    

def change_registration(id: int, pessoa : CreatePeople):
    conn = sqlite3.connect("package.db")
    agora = datetime.now().strftime('%Y-%m-%d %H:%M')
    cursor = conn.cursor()
    query = "UPDATE people SET name = ?, fk_addres = ?, fk_graduation = ?, birth_date = ?, email = ?, phone = ?, cpf = ?, is_student = ?, is_teacher = ? WHERE id = ?; "    
    cursor.execute(query, (pessoa.name,pessoa.fk_addres,pessoa.fk_graduation,pessoa.birth_date,pessoa.email,pessoa.phone,pessoa.cpf,pessoa.is_student,pessoa.is_teacher, id ))
    conn.commit()
    conn.close()

