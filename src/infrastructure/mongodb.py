import pymongo
from src.presentation.FastAPI.config.DbConfig import classifiyConfig

class DBImpelemnt():

    def __init__(self, LOCAL_HOSTE:str):

        self.local =str(LOCAL_HOSTE)



    def creat_db(self):

        myclient = pymongo.MongoClient(self.local)
        mydb = myclient[str(classifiyConfig.DATABASE_NAME)]
        mycollection = mydb[str(classifiyConfig.COLLECTION_NAME)]

        return mycollection