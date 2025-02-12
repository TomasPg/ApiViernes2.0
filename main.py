from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosApp import Usuario, Base
from app.api.routes.rutas import rutas
from starlette.responses import RedirectResponse

#Activar el ORM
Base.metadata.create_all(bind = engine)


#Variable para administrar la aplicacion
app = FastAPI()

#Activo el API
@app.get('/')
def main():
    return RedirectResponse(url = '/docs')

app.include_router(rutas)