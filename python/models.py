from pydantic import BaseModel
from uuid import uuid4, UUID

class ArtistaDTO(BaseModel):
    nombre: str
    genero: str

class ArtistaResp(BaseModel):
    id: UUID
    nombre: str
    genero: str
    ranking: int
    
class ConciertoDTO(BaseModel):
    lugar: str
    artistaID: UUID
    fecha: str
    
class ConciertoResp(BaseModel):
    id: UUID
    lugar: str
    artistaID: UUID
    fecha: str
    