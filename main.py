# from fastapi import FastAPI
from os import getenv as env
from json import loads
from dotenv import load_dotenv as envInit

from modules.firebase.connector import connect as firebase_connector

from modules.database.phRepository import PhRepository
from modules.database.bottomPressureRepository import BottomPressureRepository
from modules.database.backgroundHumidityRepository import BackgroundHumidityRepository
from modules.database.backgroundTempRepository import BackgroundTempRepository
from modules.database.waterDoRepository import WaterDoRepository
from modules.database.waterTDSRepository import WaterTDSRepository
from modules.database.waterTempRepository import WaterTempRepository
from modules.database.waterTurbidityRepository import WaterTurbidityRepository

envInit()


#mySqlite_connection = mySqlite_connector()
firebase_connection = firebase_connector(loads(env('FIREBASE_CONFIG')), env('DB_URL'))

ph_repository = PhRepository()
bottomPressure_repository = BottomPressureRepository()
background_humidity_repository = BackgroundHumidityRepository()
background_temp_repository = BackgroundTempRepository()
water_do_repository = WaterDoRepository()
water_tds_repository = WaterTDSRepository()
water_temp_repository = WaterTempRepository()
water_turbidity_repository = WaterTurbidityRepository()


reference = firebase_connection.reference("/Sensors/ph")

#(reference.get())
ph_sensor_data = (
    reference
    .order_by_child("timestamp")
    .start_at(1770294124)
    .end_at(1770336424)
    .get()
) or {}

for key, value in ph_sensor_data.items():
    print(f'key: {key} | value:{value}')
# app = FastAPI()

# # Root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "FastAPI is working!"}

# # Test endpoint with query parameter
# @app.get("/hello")
# def say_hello(name: str = "World"):
#     return {"message": f"Hello, {name}!"}
