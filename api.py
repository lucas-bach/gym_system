from fastapi import FastAPI
import uvicorn
from cadastro import insert_people, read_last_registration,insert_addres
from models import CreatePeople, UpdatePeople,CreateAddres

app = FastAPI()


@app.post("/create_addres")
def create(endereco : CreateAddres):
    insert_addres(endereco)
    return ('endereço criado')
    



@app.post("/create_cad")
def create(pessoa : CreatePeople):
    insert_people(pessoa)
    return read_last_registration(pessoa)



if __name__=="__main__":
    uvicorn.run(app)





   
