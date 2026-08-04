from rest_framework.pagination import CursorPagination

class mypagination(CursorPagination):
    page_size=3
    ordering="-roll_no"
    cursor_query_param='cur'
    invalid_cursor_message="invalid"