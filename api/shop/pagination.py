# pagination.py
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class OffsetLimitPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(data)
