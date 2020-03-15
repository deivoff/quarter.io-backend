import mongoengine
import graphene_mongo

mongoengine.connect(
    "mongo-test", host="mongomock://localhost", alias="default"
)



