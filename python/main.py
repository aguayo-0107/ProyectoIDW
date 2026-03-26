from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from models import ArtistaDTO, ArtistaResp, ConciertoDTO, ConciertoResp
from uuid import uuid4, UUID

app = FastAPI()
# Cambiar a los origenes permitidos
origins = ["http://127.0.0.1:5500",  # Para pruebas, quitar al final
           "https://musicaidw.site"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Diccionarios
artistas_db = {
    UUID('899cd06a-211b-41a0-998a-e90dbad30b69'): {
        'id': UUID('899cd06a-211b-41a0-998a-e90dbad30b69'), 
        'nombre': 'Daft Punk', 
        'genero': 'Electronic',
        'ranking': 1}, 
    UUID('ea44bd1d-00ee-431a-a6f3-0c949f4ca752'): {
        'id': UUID('ea44bd1d-00ee-431a-a6f3-0c949f4ca752'), 
        'nombre': 'Gustavo Cerati', 
        'genero': 'Rock Alternativo',
        'ranking': 2}, 
    UUID('46ae8541-51d1-4e23-ad61-a8c3cc64555e'): {
        'id': UUID('46ae8541-51d1-4e23-ad61-a8c3cc64555e'), 
        'nombre': 'Björk', 
        'genero': 'Art Pop',
        'ranking': 3}
}

conciertos_db = {
    UUID('cb110af9-4675-42e7-9a4b-724b66e6f682'): {
        'id': UUID('cb110af9-4675-42e7-9a4b-724b66e6f682'), 
        'lugar': 'Madison Square Garden, NY', 
        'artistaID': UUID('899cd06a-211b-41a0-998a-e90dbad30b69'), 
        'fecha': '2026-08-15'}, 
    UUID('fff3ee31-c90b-4f43-8372-9a0e7da5f5a5'): {
        'id': UUID('fff3ee31-c90b-4f43-8372-9a0e7da5f5a5'), 
        'lugar': 'Estadio River Plate, Buenos Aires', 
        'artistaID': UUID('ea44bd1d-00ee-431a-a6f3-0c949f4ca752'), 
        'fecha': '2026-11-20'}, 
    UUID('212ce98e-8b60-4612-b780-f13e00068501'): {
        'id': UUID('212ce98e-8b60-4612-b780-f13e00068501'), 
        'lugar': 'Harpa Concert Hall, Reykjavík', 
        'artistaID': UUID('46ae8541-51d1-4e23-ad61-a8c3cc64555e'), 
        'fecha': '2026-09-12'}
}


#---------------------
# Llamadas de Concierto
#---------------------

# POST - Crear concierto
@app.post(
    "/conciertos",
    response_model=ConciertoResp,
    status_code=status.HTTP_201_CREATED
)
async def crear_concierto(concierto: ConciertoDTO):
    nuevo_id = uuid4()

    nuevo_concierto = {
        "id": nuevo_id,
        "lugar": concierto.lugar,
        "artistaID": concierto.artistaID,
        "fecha": concierto.fecha
    }

    conciertos_db[nuevo_id] = nuevo_concierto
    return nuevo_concierto

#GET - Obtener conciertos por lugar o fecha
@app.get("/conciertos", response_model=list[ConciertoResp])
async def obtener_conciertos(lugar: str = "", fecha: str = ""):
    resultados = list(conciertos_db.values())
    if lugar:
        lugar_lower = lugar.lower()
        resultados = [
            s for s in resultados
            if lugar_lower in s["lugar"].lower()
        ]
    elif fecha:
        fecha_lower = fecha.lower()
        resultados = [
            s for s in resultados
            if fecha_lower in s["fecha"].lower()
        ]
    return resultados

# GET - Obtener concierto por id
@app.get("/conciertos/{id}", response_model=ConciertoResp)
async def obtener_por_id(id: UUID):
    if id not in conciertos_db:
        raise HTTPException(status_code=404, detail="Concierto no encontrado")
    return conciertos_db[id]


# PATCH - Actualizar la fecha de un concierto
@app.patch("/conciertos/{id}", response_model=ConciertoResp)
async def actualizar_fecha(id: UUID, nueva_fecha: str):
    if id not in conciertos_db:
        raise HTTPException(status_code=404, detail="Concierto no encontrado")

    concierto = conciertos_db[id]

    if nueva_fecha is not None:
        concierto["fecha"] = nueva_fecha

    return concierto

# DELETE - Eliminar un concierto
@app.delete("/concierto/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_concierto(id: UUID):
    if id not in conciertos_db:
        raise HTTPException(status_code=404, detail="Concierto no encontrado")

    del conciertos_db[id]
    return None

#---------------------
# Llamadas de Artista
#---------------------

# POST - Crear artista
@app.post(
    "/artistas",
    response_model=ArtistaResp,
    status_code=status.HTTP_201_CREATED
)
async def crear_artista(artista: ArtistaDTO):
    nuevo_id = uuid4()

    nuevo_artista = {
        "id": nuevo_id,
        "nombre": artista.nombre,
        "genero": artista.genero,
        "ranking": len(artistas_db) + 1
    }

    artistas_db[nuevo_id] = nuevo_artista
    return nuevo_artista

# GET - Obtener artistas por nombre o ranking
@app.get("/artistas", response_model=list[ArtistaResp])
async def obtener_artistas(nombre: str | None = None, ranking: int = -1):
    resultados = list(artistas_db.values())
    if nombre:
        nombre_lower = nombre.lower()
        resultados = [
            s for s in resultados
            if nombre_lower in s["nombre"].lower()
        ]
    elif ranking != -1:
        resultados = [
            s for s in resultados
            if ranking == s["ranking"]
        ]
    return resultados

# GET - Obtener artista por id
@app.get("/artistas/{id}", response_model=ArtistaResp)
async def obtener_artista_id(id: UUID):
    if id not in artistas_db:
        raise HTTPException(status_code=404, detail="Artista no encontrado")
    return artistas_db[id]


# PATCH - Actualizar el género de un artista
@app.patch("/artistas/{id}", response_model=ArtistaResp)
async def actualizar_genero(id: UUID, nuevo_genero: str):
    if id not in artistas_db:
        raise HTTPException(status_code=404, detail="Artista no encontrado")

    artista = artistas_db[id]

    if nuevo_genero is not None:
        artista["genero"] = nuevo_genero

    return artista

# DELETE - Eliminar a un artista
@app.delete("/artista/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_artista(id: UUID):
    if id not in artistas_db:
        raise HTTPException(status_code=404, detail="Artista no encontrado")

    del artistas_db[id]
    return None

@app.get("/listaArtistas")
def get_items(page: int = 1, size: int = 10):
    lista_completa = list(artistas_db.values())
    
    start = (page - 1) * size
    end = start + size
    
    items_paginados = lista_completa[start:end]
    
    return {"items": items_paginados,
        "total": len(artistas_db),
    }
    
@app.get("/listaConciertos")
def get_items(page: int = 1, size: int = 10):
    lista_completa = list(conciertos_db.values())
    
    start = (page - 1) * size
    end = start + size
    
    items_paginados = lista_completa[start:end]
    
    return {"items": items_paginados,
        "total": len(artistas_db),
    }