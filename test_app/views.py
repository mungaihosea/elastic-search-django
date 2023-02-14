from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogPostSearchSerializer, BlogPostModelSerializer
from drf_yasg.utils import swagger_auto_schema
from .documents import BlogPostDocument
from .models import BlogPost
from django.db.models import Q
from elasticsearch_dsl.query import MultiMatch


class BlogPostSearch(APIView):
    @swagger_auto_schema(tags = ['Search blog post'], query_serializer=BlogPostSearchSerializer)
    def get(self, request):
        serializer = BlogPostSearchSerializer(data = request.GET)

        if not serializer.is_valid():
            return Response(serializer.errors)
        
        q = serializer.data['query']

        query = MultiMatch(query=q, fields=['title', 'tax'], fuzziness='AUTO')

        filter_results = BlogPostDocument.search().query(query)
       

        data = []
        for hit in filter_results:
            invoice = {
                "amount": hit.invoice.amount,
                "tax": hit.invoice.tax
            }
            data.append(
                {
                    "title": hit.title,
                    "invoice": invoice
                }
            )

        return Response(data)
    

    @swagger_auto_schema(tags = ["Search blog post"], request_body=BlogPostModelSerializer)
    def post(self, request):
        serializer = BlogPostModelSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        blog_post = BlogPost.objects.create(**serializer.data)
        return Response("created")


