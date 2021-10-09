from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all_dojo(cls):
        query = "SELECT*FROM dojos"
        db_dojos = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []
        for i in db_dojos:
            dojos.append(Dojo(i))
        return dojos

    @classmethod
    def add(cls, data):
        query = "INSERT INTO dojos(name) VALUES(%(name)s)"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)

    @classmethod
    def all_ninja(cls, data):
        query = "SELECT*FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s"
        all_ninjas = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        dojoz = Dojo(all_ninjas[0])
        for i in all_ninjas:
            ninja_data = {
                "id": i["ninjas.id"],
                "first_name": i["first_name"],
                "last_name": i["last_name"],
                "age": i["age"], 
                "created_at": i["ninjas.created_at"],
                "updated_at": i["ninjas.updated_at"],
                "dojo_id": i["dojo_id"]
            }
            dojoz.ninjas.append(Ninja(i))
        return dojoz