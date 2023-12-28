import logging.config
from fastapi import FastAPI

logging.config.fileConfig('config/logging.ini')
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_root():
    logger.info("Requête reçue pour /")
    return {"Hello": "World"}