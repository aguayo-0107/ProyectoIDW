from fastapi import FastAPI, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from models import ArtistaDTO, ArtistaResp, ConciertoDTO, ConciertoResp
from uuid import uuid4, UUID
import random
import os
import time

app = FastAPI()
# Cambiar a los origenes permitidos
origins = ["https://musicaidw.site"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Diccionarios
artistas_db = {
	UUID('2829057f-745b-447b-8ce1-811e7f966c03'): {
 		'id': UUID('2829057f-745b-447b-8ce1-811e7f966c03'),
 		'nombre': 'Daft Punk',
 		'genero': 'Electronic',
 		'fans': 53828},
 	UUID('4e57bb44-0766-42d4-8565-87a964e94f5e'): {
 		'id': UUID('4e57bb44-0766-42d4-8565-87a964e94f5e'),
 		'nombre': 'Gustavo Cerati',
 		'genero': 'Rock Latino',
 		'fans': 31260},
 	UUID('751b83c0-2a1b-47b5-9198-5b708f3f22a1'): {
 		'id': UUID('751b83c0-2a1b-47b5-9198-5b708f3f22a1'),
 		'nombre': 'Björk',
 		'genero': 'Art Pop',
 		'fans': 2511},
 	UUID('f5d99345-87bf-4384-adfc-f07debc82929'): {
 		'id': UUID('f5d99345-87bf-4384-adfc-f07debc82929'),
 		'nombre': 'The Strokes',
 		'genero': 'Indie Rock',
 		'fans': 35478},
 	UUID('85f6ba5e-82a2-4712-85a3-ac34e6c65420'): {
 		'id': UUID('85f6ba5e-82a2-4712-85a3-ac34e6c65420'),
 		'nombre': 'Rosalía',
 		'genero': 'Flamenco Pop',
 		'fans': 75752},
 	UUID('bfce4ac3-7b7b-40ba-a53f-644d1b5cb760'): {
 		'id': UUID('bfce4ac3-7b7b-40ba-a53f-644d1b5cb760'),
 		'nombre': 'Arctic Monkeys',
 		'genero': 'Indie Rock',
 		'fans': 27314},
 	UUID('a0c9e27c-08c8-488d-a7f7-df1c61af1f1e'): {
 		'id': UUID('a0c9e27c-08c8-488d-a7f7-df1c61af1f1e'),
 		'nombre': 'Radiohead',
 		'genero': 'Alternative Rock',
 		'fans': 40341},
 	UUID('90b6292c-d8ff-4bf0-843c-3d76039c1af2'): {
 		'id': UUID('90b6292c-d8ff-4bf0-843c-3d76039c1af2'),
 		'nombre': 'Tame Impala',
 		'genero': 'Psychedelic Pop',
 		'fans': 27428},
 	UUID('1b58b226-c59b-4239-96b1-35cbb7f1e811'): {
 		'id': UUID('1b58b226-c59b-4239-96b1-35cbb7f1e811'),
 		'nombre': 'Bad Bunny',
 		'genero': 'Reggaeton',
 		'fans': 7026},
 	UUID('aa4be2ff-a9e2-44f4-9273-718c4f0798ce'): {
 		'id': UUID('aa4be2ff-a9e2-44f4-9273-718c4f0798ce'),
 		'nombre': 'Taylor Swift',
 		'genero': 'Pop',
 		'fans': 61167},
 	UUID('7c0d22bc-7f1d-489d-9c4d-04fe26568628'): {
 		'id': UUID('7c0d22bc-7f1d-489d-9c4d-04fe26568628'),
 		'nombre': 'Gorillaz',
 		'genero': 'Alternative',
 		'fans': 55258},
 	UUID('1969f011-57ba-47b8-afa2-b90e87f4cebf'): {
 		'id': UUID('1969f011-57ba-47b8-afa2-b90e87f4cebf'),
 		'nombre': 'Kendrick Lamar',
 		'genero': 'Hip Hop',
 		'fans': 89154},
 	UUID('80e2d9b5-7c9d-4843-9dda-1cb43b1c6359'): {
 		'id': UUID('80e2d9b5-7c9d-4843-9dda-1cb43b1c6359'),
 		'nombre': 'Dua Lipa',
 		'genero': 'Disco Pop',
 		'fans': 27834},
 	UUID('702ae6e2-1c50-4e2a-9421-0401c61c9a4c'): {
 		'id': UUID('702ae6e2-1c50-4e2a-9421-0401c61c9a4c'),
 		'nombre': 'Soda Stereo',
 		'genero': 'Rock en Español',
 		'fans': 93550},
 	UUID('7f684f76-a88f-4299-8930-6377a8a79ae4'): {
 		'id': UUID('7f684f76-a88f-4299-8930-6377a8a79ae4'),
 		'nombre': 'Fleetwood Mac',
 		'genero': 'Soft Rock',
 		'fans': 26718},
 }
conciertos_db = {
	UUID('27c0e8ab-ee0d-4430-8990-74c4e37c9a42'): {
 		'id': UUID('27c0e8ab-ee0d-4430-8990-74c4e37c9a42'),
 		'lugar': 'Foro Sol, CDMX',
 		'artistaID': UUID('2829057f-745b-447b-8ce1-811e7f966c03'),
 		'fecha': '2026-05-15'},
 	UUID('f1b3c641-dc0d-4f1c-9352-724a78bc1cdd'): {
 		'id': UUID('f1b3c641-dc0d-4f1c-9352-724a78bc1cdd'),
 		'lugar': 'Movistar Arena, Bogotá',
 		'artistaID': UUID('4e57bb44-0766-42d4-8565-87a964e94f5e'),
 		'fecha': '2026-06-20'},
 	UUID('ff5d165c-70dd-4ffc-b7b3-ede3bd81ac42'): {
 		'id': UUID('ff5d165c-70dd-4ffc-b7b3-ede3bd81ac42'),
 		'lugar': 'Harpa Concert Hall, Reikiavik',
 		'artistaID': UUID('751b83c0-2a1b-47b5-9198-5b708f3f22a1'),
 		'fecha': '2026-07-10'},
 	UUID('cd7e02c7-d1be-4db3-8f65-f8957a0acb05'): {
 		'id': UUID('cd7e02c7-d1be-4db3-8f65-f8957a0acb05'),
 		'lugar': 'Madison Square Garden, NY',
 		'artistaID': UUID('f5d99345-87bf-4384-adfc-f07debc82929'),
 		'fecha': '2026-08-05'},
 	UUID('567980cd-2bd2-4396-8037-bc2de59e6077'): {
 		'id': UUID('567980cd-2bd2-4396-8037-bc2de59e6077'),
 		'lugar': 'Wizink Center, Madrid',
 		'artistaID': UUID('85f6ba5e-82a2-4712-85a3-ac34e6c65420'),
 		'fecha': '2026-09-12'},
 	UUID('389ef5ed-c60e-43d0-ac76-d791829dcb9b'): {
 		'id': UUID('389ef5ed-c60e-43d0-ac76-d791829dcb9b'),
 		'lugar': 'O2 Arena, Londres',
 		'artistaID': UUID('bfce4ac3-7b7b-40ba-a53f-644d1b5cb760'),
 		'fecha': '2026-10-01'},
 	UUID('82be66e7-f7e9-4bb5-854b-cb590d401ad8'): {
 		'id': UUID('82be66e7-f7e9-4bb5-854b-cb590d401ad8'),
 		'lugar': 'Teatro Gran Rex, Buenos Aires',
 		'artistaID': UUID('a0c9e27c-08c8-488d-a7f7-df1c61af1f1e'),
 		'fecha': '2026-11-20'},
 	UUID('e38a325b-1c6a-4c71-b308-6c5c839e6f5b'): {
 		'id': UUID('e38a325b-1c6a-4c71-b308-6c5c839e6f5b'),
 		'lugar': 'Hollywood Bowl, LA',
 		'artistaID': UUID('90b6292c-d8ff-4bf0-843c-3d76039c1af2'),
 		'fecha': '2026-12-05'},
 	UUID('3fa2c900-aa70-4672-a146-90d614c4e91d'): {
 		'id': UUID('3fa2c900-aa70-4672-a146-90d614c4e91d'),
 		'lugar': 'Estadio Azteca, CDMX',
 		'artistaID': UUID('1b58b226-c59b-4239-96b1-35cbb7f1e811'),
 		'fecha': '2026-04-18'},
 	UUID('c0351c2e-5b4b-4a70-972e-34f132421114'): {
 		'id': UUID('c0351c2e-5b4b-4a70-972e-34f132421114'),
 		'lugar': 'SoFi Stadium, Inglewood',
 		'artistaID': UUID('aa4be2ff-a9e2-44f4-9273-718c4f0798ce'),
 		'fecha': '2026-05-22'},
 	UUID('55c537a0-75a3-4aaf-8bc2-0d1d62edd637'): {
 		'id': UUID('55c537a0-75a3-4aaf-8bc2-0d1d62edd637'),
 		'lugar': 'Accor Arena, París',
 		'artistaID': UUID('7c0d22bc-7f1d-489d-9c4d-04fe26568628'),
 		'fecha': '2026-06-14'},
 	UUID('50beccfb-4f95-476c-92d1-97d9b848c3b9'): {
 		'id': UUID('50beccfb-4f95-476c-92d1-97d9b848c3b9'),
 		'lugar': 'Rose Bowl, Pasadena',
 		'artistaID': UUID('1969f011-57ba-47b8-afa2-b90e87f4cebf'),
 		'fecha': '2026-07-28'},
 	UUID('7745fc1e-ea11-4cc6-9727-6e2846fb8114'): {
 		'id': UUID('7745fc1e-ea11-4cc6-9727-6e2846fb8114'),
 		'lugar': 'Ziggo Dome, Ámsterdam',
 		'artistaID': UUID('80e2d9b5-7c9d-4843-9dda-1cb43b1c6359'),
 		'fecha': '2026-08-19'},
 	UUID('ac46d455-62f8-4ed0-a0c8-05cbba5b56ca'): {
 		'id': UUID('ac46d455-62f8-4ed0-a0c8-05cbba5b56ca'),
 		'lugar': 'Estadio Nacional, Santiago',
 		'artistaID': UUID('702ae6e2-1c50-4e2a-9421-0401c61c9a4c'),
 		'fecha': '2026-09-30'},
 	UUID('64282179-14dd-4c9c-83c4-c67e949a77ce'): {
 		'id': UUID('64282179-14dd-4c9c-83c4-c67e949a77ce'),
 		'lugar': 'Red Rocks Amphitheatre, Denver',
 		'artistaID': UUID('7f684f76-a88f-4299-8930-6377a8a79ae4'),
 		'fecha': '2026-10-15'},
 }


start_time = time.time()

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

# GET - Obtener conciertos por lugar o fecha
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
        "fans": random.randint(1000, 100000)
    }

    artistas_db[nuevo_id] = nuevo_artista
    return nuevo_artista

# GET - Obtener artistas por nombre
@app.get("/artistas", response_model=list[ArtistaResp])
async def obtener_artistas(nombre: str | None = None, ranking: int = -1):
    resultados = list(artistas_db.values())
    if nombre:
        nombre_lower = nombre.lower()
        resultados = [
            s for s in resultados
            if nombre_lower in s["nombre"].lower()
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
        "total": len(conciertos_db),
    }
    
# ---------------------
# Health Endpoint
# ---------------------
@app.get("/health")
async def health_check():
    uptime_seconds = time.time() - start_time
    
    data_ok = isinstance(artistas_db, dict) and len(artistas_db) >= 0 and isinstance(conciertos_db, dict) and len(conciertos_db) >= 0;
    
    is_on_render = os.getenv("RENDER", "false") == "true"

    if not data_ok:
        return Response(
            content='{"status": "unhealthy", "reason": "data_structure_corrupted"}',
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            media_type="application/json"
        )

    return {
        "status": "healthy",
        "environment": "render" if is_on_render else "local",
        "uptime_human": f"{uptime_seconds:.2f} seconds",
        "version": "1.0.0",
        "checks": {
            "memory_data": "ok",
            "render_env": "detected" if is_on_render else "not_detected"
        }
    }