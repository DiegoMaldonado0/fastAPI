from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Base de datos simulada en memoria
peliculas_db = []

# Modelo de datos para una película
class Pelicula(BaseModel):
    id: int
    titulo: str
    director: str
    genero: str
    año: int
    sinopsis: Optional[str] = None

# Endpoint raíz
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Gestión de Películas"}

# Ruta para obtener todas las películas
@app.get("/peliculas", response_model=List[Pelicula])
def obtener_peliculas():
    return peliculas_db

# Ruta para obtener una película por ID
@app.get("/peliculas/{pelicula_id}", response_model=Pelicula)
def obtener_pelicula(pelicula_id: int):
    for pelicula in peliculas_db:
        if pelicula.id == pelicula_id:
            return pelicula
    raise HTTPException(status_code=404, detail="Película no encontrada")

# Ruta para añadir una nueva película
@app.post("/peliculas", response_model=Pelicula)
def agregar_pelicula(pelicula: Pelicula):
    peliculas_db.append(pelicula)
    return pelicula

# Ruta para eliminar una película por ID
@app.delete("/peliculas/{pelicula_id}")
def eliminar_pelicula(pelicula_id: int):
    for index, pelicula in enumerate(peliculas_db):
        if pelicula.id == pelicula_id:
            del peliculas_db[index]
            return {"mensaje": "Película eliminada"}
    raise HTTPException(status_code=404, detail="Película no encontrada")

# Correr la aplicación usando: uvicorn main:app --reload
