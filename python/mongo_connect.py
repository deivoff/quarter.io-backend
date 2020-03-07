from pymongo import MongoClient

class mongo_connect():
    connect = ''
    port = ''

    client = MongoClient(connect,port)
    db = client.sensor_readings

