# from django_elasticsearch_dsl import Document, fields
# from django_elasticsearch_dsl.registries import registry
# from .models import Post, Connection
# from django.contrib.auth.models import User

# @registry.register_document
# class PostDocument(Document):
#     #ForeignKeyはfields内で設定不可のため以下のように記載
#     user = fields.ObjectField(properties={
#         'username': fields.TextField(),
#         'password': fields.TextField(),
#     })
#     class Index:
#         # Name of the Elasticsearch index
#         name = 'posts'
#         # See Elasticsearch Indices API reference for available settings
#         settings = {'number_of_shards': 1,
#                     'number_of_replicas': 0}

#     class Django:
#         model = Post # The model associated with this Document

#         # The fields of the model you want to be indexed in Elasticsearch
#         fields = [
#             'title',
#             'id',
#             'content',
#         ]

#         related_models = [User]
        