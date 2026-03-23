from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from models import ArtistaDTO, ArtistaResp, ConciertoDTO, ConciertoResp
from uuid import uuid4, UUID

app = FastAPI()
# Cambiar a los origenes permitidos
origins = ["*"] 

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
        'genero': 'Electronic'}, 
    UUID('ea44bd1d-00ee-431a-a6f3-0c949f4ca752'): {
        'id': UUID('ea44bd1d-00ee-431a-a6f3-0c949f4ca752'), 
        'nombre': 'Gustavo Cerati', 
        'genero': 'Rock Alternativo'}, 
    UUID('46ae8541-51d1-4e23-ad61-a8c3cc64555e'): {
        'id': UUID('46ae8541-51d1-4e23-ad61-a8c3cc64555e'), 
        'nombre': 'Björk', 
        'genero': 'Art Pop'}, 
    UUID('10b36124-4949-4d97-beed-c37ce5c9899f'): {
        'id': UUID('10b36124-4949-4d97-beed-c37ce5c9899f'), 
        'nombre': 'Miles Davis', 
        'genero': 'Jazz'}, 
    UUID('ec56665a-017b-4099-95d7-4e119e36a825'): {
        'id': UUID('ec56665a-017b-4099-95d7-4e119e36a825'), 
        'nombre': 'Aphex Twin', 
        'genero': 'IDM'}, 
    UUID('ed439459-09bd-4d0b-abd4-130160788785'): {
        'id': UUID('ed439459-09bd-4d0b-abd4-130160788785'), 
        'nombre': 'Rosalía', 
        'genero': 'Nuevo Flamenco'}, 
    UUID('894888ab-646e-472a-af1d-7d839aaec1a7'): {
        'id': UUID('894888ab-646e-472a-af1d-7d839aaec1a7'), 
        'nombre': 'Radiohead', 
        'genero': 'Art Rock'}, 
    UUID('825b3f72-f465-4dee-9687-b1714c63f85b'): {
        'id': UUID('825b3f72-f465-4dee-9687-b1714c63f85b'), 
        'nombre': 'Kendrick Lamar', 
        'genero': 'Hip Hop'}, 
    UUID('128298e7-b6a3-40a2-980f-877d6af4521e'): {
        'id': UUID('128298e7-b6a3-40a2-980f-877d6af4521e'), 
        'nombre': 'Florence + The Machine', 
        'genero': 'Indie Rock'}, 
    UUID('c26212ab-0f7c-4a4f-ab68-3f7916e41e79'): {
        'id': UUID('c26212ab-0f7c-4a4f-ab68-3f7916e41e79'), 
        'nombre': 'Nina Simone', 
        'genero': 'Soul/Jazz'}, 
    UUID('d34017d7-2410-409e-9470-4e3c924a9211'): {
        'id': UUID('d34017d7-2410-409e-9470-4e3c924a9211'), 
        'nombre': 'Gorillaz', 
        'genero': 'Alternative Rock'}, 
    UUID('5f13dc6f-a30f-49a4-9f1f-a13c770cbfe7'): {
        'id': UUID('5f13dc6f-a30f-49a4-9f1f-a13c770cbfe7'), 
        'nombre': 'Tame Impala', 
        'genero': 'Psychedelic Pop'}, 
    UUID('f61d01b8-0c99-4d42-83e6-21db52186026'): {
        'id': UUID('f61d01b8-0c99-4d42-83e6-21db52186026'), 
        'nombre': 'Jorge Drexler', 
        'genero': 'Indie Folk'}, 
    UUID('3005b616-4c05-498a-978c-da796c92762c'): {
        'id': UUID('3005b616-4c05-498a-978c-da796c92762c'), 
        'nombre': 'Kraftwerk', 
        'genero': 'Krautrock/Electronic'}, 
    UUID('81ec85f2-aa7a-4735-9c93-6770345e2d1b'): {
        'id': UUID('81ec85f2-aa7a-4735-9c93-6770345e2d1b'), 
        'nombre': 'Lana Del Rey', 
        'genero': 'Dream Pop'
    }
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
        'fecha': '2026-09-12'}, 
    UUID('0588de90-1cf9-40fa-8ac5-b28fd82d96cb'): {
        'id': UUID('0588de90-1cf9-40fa-8ac5-b28fd82d96cb'), 
        'lugar': 'Blue Note Jazz Club, Tokyo', 
        'artistaID': UUID('10b36124-4949-4d97-beed-c37ce5c9899f'), 
        'fecha': '2026-07-05'}, 
    UUID('8c2edc08-3a35-4962-9c8d-fe7865dbe60b'): {
        'id': UUID('8c2edc08-3a35-4962-9c8d-fe7865dbe60b'), 
        'lugar': 'Berghain, Berlin', 
        'artistaID': UUID('ec56665a-017b-4099-95d7-4e119e36a825'), 
        'fecha': '2026-10-31'}, 
    UUID('0ac350e6-b278-4085-832b-05805d0c3b9f'): {
        'id': UUID('0ac350e6-b278-4085-832b-05805d0c3b9f'), 
        'lugar': 'Wizink Center, Madrid', 
        'artistaID': UUID('ed439459-09bd-4d0b-abd4-130160788785'), 
        'fecha': '2026-12-01'}, 
    UUID('607f422b-bb65-4770-9507-667ecd6d79bf'): {
        'id': UUID('607f422b-bb65-4770-9507-667ecd6d79bf'), 
        'lugar': 'Glastonbury Festival, UK', 
        'artistaID': UUID('894888ab-646e-472a-af1d-7d839aaec1a7'), 
        'fecha': '2026-06-25'}, 
    UUID('949148a0-5c9d-4aa6-b189-cd7b3f163fdb'): {
        'id': UUID('949148a0-5c9d-4aa6-b189-cd7b3f163fdb'), 
        'lugar': 'The Forum, LA', 
        'artistaID': UUID('825b3f72-f465-4dee-9687-b1714c63f85b'), 
        'fecha': '2026-05-14'}, 
    UUID('bc32e3fd-7ee4-4fb9-b350-4929f7646393'): {
        'id': UUID('bc32e3fd-7ee4-4fb9-b350-4929f7646393'), 
        'lugar': 'Royal Albert Hall, London', 
        'artistaID': UUID('128298e7-b6a3-40a2-980f-877d6af4521e'), 
        'fecha': '2026-04-22'}, 
    UUID('f2138129-19ce-4243-936d-23ce128409e7'): {
        'id': UUID('f2138129-19ce-4243-936d-23ce128409e7'), 
        'lugar': 'Olympia, Paris', 
        'artistaID': UUID('c26212ab-0f7c-4a4f-ab68-3f7916e41e79'), 
        'fecha': '2026-03-10'}, 
    UUID('223d5044-5c21-447b-ab8f-7e0ad4148ff7'): {
        'id': UUID('223d5044-5c21-447b-ab8f-7e0ad4148ff7'), 
        'lugar': 'Hollywood Bowl, CA', 
        'artistaID': UUID('d34017d7-2410-409e-9470-4e3c924a9211'), 
        'fecha': '2026-08-28'}, 
    UUID('e784b18f-867d-40ad-9f7a-b1b28359e27d'): {
        'id': UUID('e784b18f-867d-40ad-9f7a-b1b28359e27d'), 
        'lugar': 'Sydney Opera House, Australia', 
        'artistaID': UUID('5f13dc6f-a30f-49a4-9f1f-a13c770cbfe7'), 
        'fecha': '2026-02-15'}, 
    UUID('42adbd9e-f2bb-4bd7-9965-3ebd179ec705'): {
        'id': UUID('42adbd9e-f2bb-4bd7-9965-3ebd179ec705'), 
        'lugar': 'Auditorio Nacional, Ciudad de México', 
        'artistaID': UUID('f61d01b8-0c99-4d42-83e6-21db52186026'), 
        'fecha': '2026-11-05'}, 
    UUID('d6919a6a-797d-44a1-944b-eab4f9ada1e5'): {
        'id': UUID('d6919a6a-797d-44a1-944b-eab4f9ada1e5'), 
        'lugar': 'Philharmonie de Paris', 
        'artistaID': UUID('3005b616-4c05-498a-978c-da796c92762c'), 
        'fecha': '2026-01-20'}, 
    UUID('13cd2643-7416-4d1f-858b-0ec5af57481e'): {
        'id': UUID('13cd2643-7416-4d1f-858b-0ec5af57481e'), 
        'lugar': 'Red Rocks Amphitheatre, Colorado', 
        'artistaID': UUID('81ec85f2-aa7a-4735-9c93-6770345e2d1b'), 
        'fecha': '2026-07-19'
        }
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

# GET - Obtener todos los concierto o buscar por lugar
@app.get("/conciertos", response_model=list[ConciertoResp])
async def obtener_conciertos(lugar: str | None = None):
    resultados = list(conciertos_db.values())

    if lugar:
        lugar_lower = lugar.lower()
        resultados = [
            s for s in resultados
            if lugar_lower in s["lugar"].lower()
        ]

    return resultados

# GET - Obtener lugar por id
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
        concierto["genero"] = nueva_fecha

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
        "genero": artista.genero
    }

    artistas_db[nuevo_id] = nuevo_artista
    return nuevo_artista

# GET - Obtener todos los artistas o buscar por nombre
@app.get("/artistas", response_model=list[ArtistaResp])
async def obtener_artistas(nombre: str | None = None):
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
