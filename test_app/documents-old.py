from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import BlogPost


@registry.register_document
class BlogPostDocument(Document):

    def generate_id(self, object_instance):
        return str(object_instance._id)

    class Index:
        name = 'searchmodel'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = BlogPost
        fields = [
            'title',
            'description',
            'content'
        ]