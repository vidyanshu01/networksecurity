import sys
import os 
import certifi
ca=certifi.where()

from dotenv import load_dotenv
load_dotenv()
mongo_db_url=os.getenv("MONGO_DB_URL")
print(mongo_db_url)

import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.pipeline.training_pipeline import TraningPipeline
from networksecurity.utils.ml_utils.model.estimator import NetworkModel

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,File,UploadFile,Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd
import asyncio

from networksecurity.utils.main_utils.utils import load_object

client=pymongo.MongoClient(mongo_db_url)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database=client[DATA_INGESTION_DATABASE_NAME]
collection=client[DATA_INGESTION_COLLECTION_NAME]

app=FastAPI()
origins=["*"]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

@app.get("/",tags=["authentication"])
async def index():
        return RedirectResponse(url='/docs')
@app.get("/train")
async def train_route():
        try:    
                logging.info("Starting training Route")
                train_pipeline=TraningPipeline()
                train_pipeline.run_pipeline()
                return Response("Training is SuccessFully")
        except Exception as e:
                raise NetworkSecurityException(e,sys)

@app.post("/predict") 

# Use @app.post() instead  -> Correct way to handle file upload.
# Using @app.get() with file upload (UploadFile)-> Invalid (GET can’t send a body)

async def predict_route(request: Request,file:UploadFile=File(...)):
    try:
        logging.info("Starting Prediction route for the New Data")
        logging.info("Step 1: Reading CSV...")
        print("Step 1: Reading CSV...")
        # df = pd.read_csv("valid_data/test.csv")
        df = pd.read_csv(file.file)

        print("CSV loaded successfully:", df.shape)
        logging.info("CSV loaded successfully")
        print("Step 2: Loading preprocessor and model...")
        preprocessor = load_object("final_model/preprocessor.pkl")
        model = load_object("final_model/model.pkl")
        print("Files loaded successfully")
        logging.info("Files loaded successfully")

        network_model = NetworkModel(preprocessor=preprocessor, model=model)
        print("Step 3: Predicting...")

        y_pred = network_model.predict(df)
        print("Prediction complete:", y_pred[:5])

        df["predicted_column"] = y_pred
        df.to_csv("Prediction_output/output.csv", index=False)
        print("Output saved successfully")
        logging.info("Output saved successfully")
        table_html = df.to_html(classes="table table-striped", index=False)
        return templates.TemplateResponse("table.html", {"request": request, "table": table_html})

    except Exception as e:
        import traceback
        print("Error occurred in /predict route:")
        traceback.print_exc()
        raise NetworkSecurityException(e, sys)

if __name__=="__main__":
        # app_run(app,host="0.0.0.0",port=8000)
        app_run(app,host="0.0.0.0",port=8080)




