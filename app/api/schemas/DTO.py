from pydantic import BaseModel, Field
from datetime import date

#Usuario
class UsuarioDTOPeticion(BaseModel):
    nombre: str
    edad: int
    telefono: str
    correo: str
    contraseña: str
    fechaRegistro: date
    ciudad:str
    class Config:
        orm-mode=True

class UsuarioDTORespuesta(BaseModel):
    id: str
    nombre: str
    telefono: str
    ciudad: str
    class Config:
        orm-mode=True

#Gasto
class GastoDTOPeticion(BaseModel):
    monto: float 
    fecha: date
    descripcion: str
    nombre: str
    class Config:
        orm-mode=True

class GastoDTORespuesta(BaseModel):
    monto: float 
    fecha: date
    descripcion: str
    usuario_id: int
    nombre: str
    class Config:
        orm-mode=True

#Categoria
class CategoriaDTOPeticion(BaseModel):
    nombreCategoria: str
    descripcion: str
    fotoicono: str
    class Config:
        orm-mode=True

class CategoriaDTORespuesta(BaseModel):
    nombreCategoria: str
    descripcion: str
    fotoicono: str
    class Config:
        orm-mode=True
    
#Metodo de Pago
class MetodoPagoDTOPeticion(BaseModel):
    nombreMetodo: str
    descripcion: str
    class Config:
        orm-mode=True

class MetodoPagoDTORespuesta(BaseModel):
    nombreMetodo: str
    descripcion: str
    class Config:
        orm-mode=True