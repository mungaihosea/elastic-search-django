from rest_framework import serializers
from .models import BlogPost


class BlogPostSearchSerializer(serializers.Serializer):
    query = serializers.CharField(max_length = 200)


class BlogPostModelSerializer(serializers.ModelSerializer):

    # title = serializers.CharField(max_length = 200)
    # description = serializers.CharField(max_length = 200)
    # content = serializers.CharField(max_length = 200)
    invoice = serializers.JSONField()

    class Meta:
        model = BlogPost
        # fields = '__all__'
        fields = ('title', 'description', 'content', 'invoice')
    