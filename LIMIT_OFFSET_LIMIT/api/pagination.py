from rest_framework.pagination import LimitOffsetPagination

class mypagination(LimitOffsetPagination):
    default_limit=5
    offset_query_param='off'
    limit_query_param='lim'
    max_limit=3
    