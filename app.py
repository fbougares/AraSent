import logging
from fastapi import FastAPI
from uvicorn import Server, Config
from configuration.config import settings




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





# The Run function
def run():
    logging.info('Starting the service ...')
    server = Server(Config(app=app, host=settings.SERVER_HOST, port=settings.PORT))
    server.run()


# Running Mira Models
if __name__ == '__main__':
    run()