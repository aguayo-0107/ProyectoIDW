from pydantic import BaseModel
from uuid import uuid4, UUID

class ArtistaDTO(BaseModel):
    nombre: str
    genero: str
    ranking: int

class ArtistaResp(BaseModel):
    id: UUID
    nombre: str
    genero: str
    ranking: int
    
class ConciertoDTO(BaseModel):
    lugar: str
    artistaID: str
    fecha: str
    
class ConciertoResp(BaseModel):
    id: UUID
    lugar: str
    artistaID: str
    fecha: str
    