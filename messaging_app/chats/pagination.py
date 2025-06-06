from rest_framework import pagination


class MessagePagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'  # Optional: allows client to override
    max_page_size = 100  # Optional: limits max override
