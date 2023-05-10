import logging
from fastapi import FastAPI
from uvicorn import Server, Config
from configuration.config import settings

from sources.apis.dialect_ident import dialect_id_route
from sources.apis.dialect_sent import dialect_sent_route


# Create APP
app = FastAPI(
    title=settings.APP_NAME,
    description="MY PROJECT",
    version="0.0.1",
    contact={
        "name": "Fethi BOUGARES"
    },
    docs_url="/api",
    redoc_url="/reapi/",
    servers=[
        {"url": "/"},
    ],
    openapi_url="/swagger.json")


# include routes
app.include_router(dialect_id_route, tags=['ArabicNLP'])
app.include_router(dialect_sent_route, tags= ['ArabicNLP'])

# The Run function
def run():
    logging.info('Starting the service ...')
    server = Server(Config(app=app, host=settings.SERVER_HOST, port=settings.PORT))
    server.run()


# Running Mira Models
if __name__ == '__main__':
    run()