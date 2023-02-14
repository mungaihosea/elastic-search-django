from djongo import models as mongo_models
from uuid import uuid4
from bson import ObjectId
from drf_yasg.utils import swagger_auto_schema


class BlogPost(mongo_models.Model):
    # _id = mongo_models.CharField(default = ObjectId(), max_length = 200, primary_key=True)
    # _id = mongo_models.UUIDField(default = uuid4, primary_key=True)
    _id = mongo_models.ObjectIdField()
    title = mongo_models.CharField(max_length = 200)
    description = mongo_models.CharField(max_length = 200)
    content = mongo_models.CharField(max_length = 200)
    invoice = mongo_models.JSONField(default = dict)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        db_table = "blog post"