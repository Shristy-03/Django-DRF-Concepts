from rest_framework.pagination import PageNumberPagination

class mypagination(PageNumberPagination):
    page_size=5
    page_query_param='page_size'
    page_size_query_param='records'
    max_page_size=4
    last_page_strings='end'
