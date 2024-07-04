from fastapi import FastAPI
import uvicorn
from cadastro import insert_people, read_last_registration,insert_addres,query_by_name,change_registration,partially_registration
from models import CreatePeople, UpdatePeople,CreateAddres

app = FastAPI()



@app.post("/create_cad", tags=["Cadastro"])
def create(pessoa : CreatePeople):
    insert_people(pessoa)
    return read_last_registration()


@app.get("/query_by_name/{name}", tags=["Cadastro"])
def query_name(name: str) -> CreatePeople:         
    return query_by_name(name) 


@app.put("/update/{id}", tags=["Cadastro"])
def to_update(id: int, pessoa : CreatePeople):
    change_registration(id,pessoa)
    return {"message": "Cadastro alterado"}


@app.patch("/edit_cadastro/{id}", tags=["Cadastro"])
def edit_cad(id: int, pessoa : UpdatePeople):
    partially_registration(id,pessoa)
    return{"message": "Alteração concluída"}


@app.post("/create_addres", tags=["Endereço"])
def create(endereco : CreateAddres):
    insert_addres(endereco)
    return ('endereço criado')  





if __name__=="__main__":
    uvicorn.run(app)




   
