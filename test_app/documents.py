from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import BlogPost
from elasticsearch_dsl import analyzer, tokenizer


autocomplete_analyzer = analyzer(
    'autocomplete_analyzer',
    tokenizer=tokenizer('trigram', 'nGram', min_gram=1, max_gram=20),
    filter=['lowercase']
)


@registry.register_document
class BlogPostDocument(Document):

    def generate_id(self, object_instance):
        return str(object_instance._id)

    #title: fields.TextField(analyzer=autocomplete_analyzer, search_analyzer='standard') # Here I'm trying to use the analyzer specified above <-- This was extremely incorrect, due to the colon in definition, I don't know how I missed it but I did...
    title = fields.TextField(required=True, analyzer=autocomplete_analyzer) # This is it....
    tax = fields.TextField(analyzer=autocomplete_analyzer)


    def prepare_tax(self, instance):
        # return instance.invoice['tax']
        # invoice_obj = instance.invoice['tax']
        return instance.invoice['tax']

    invoice = fields.ObjectField()
    # invoice = fields.ObjectField(
    #     properties = {
    #         "amount": fields.TextField(analyzer=autocomplete_analyzer),
    #         "tax": fields.TextField(analyzer=autocomplete_analyzer),
    #     }
    # )


    class Index:
        name = 'blogposts'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
            'max_ngram_diff': 20 # This seems to be important due to the constraint for max_ngram_diff beeing 1
        }

    class Django:
        model = BlogPost
        fields = [
            # 'title' <-- Notice, I removed this field, it would be redeclaration error
            # In reality here I have more fields

            'description',
            'content'
        ]
