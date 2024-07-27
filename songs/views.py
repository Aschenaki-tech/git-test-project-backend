from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import  UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def by_language(self, request):
        language = request.query_params.get('language')
        songs = self.queryset.filter(language=language)
        serializer = self.get_serializer(songs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_genre(self, request):
        genre = request.query_params.get('genre')
        songs = self.queryset.filter(genre=genre)
        serializer = self.get_serializer(songs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_artist(self, request):
        artist = request.query_params.get('artist')
        songs = self.queryset.filter(artist=artist)
        serializer = self.get_serializer(songs, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def languages(self, request):
        languages = self.queryset.values_list('language', flat=True).distinct()
        return Response(languages)

    @action(detail=False, methods=['get'])
    def genres(self, request):
        genres = self.queryset.values_list('genre', flat=True).distinct()
        return Response(genres)

    @action(detail=False, methods=['get'])
    def artists(self, request):
        artists = self.queryset.values_list('artist', flat=True).distinct()
        return Response(artists)
      


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    # You can customize the token response here if needed
    pass