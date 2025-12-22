from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)

# Page Number Pagination
class UserPagination(PageNumberPagination):
    page_size = 5              # items per page
    page_size_query_param = 'page_size'
    max_page_size = 50

# Limit Offset Pagination
class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit=2
    max_limit=10


# Cursor Pagination
class UserCursorPagination(CursorPagination):
    page_size=2
    ordering='-created_a'
