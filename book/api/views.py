from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(["GET"])
def book(request):
    books = ["A Game of Thrones", "A Clash of Kings", "A Storm of Swords", "A Feast for Crows", "A Dance With Dragons", "The Winds of Winter", "A Dream of Spring"]
    return Response(status=status.HTTP_200_OK, data={"data": books})

