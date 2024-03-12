from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URLShortener, Click
from .serializers import URLShortenerSerializer, ClickSerializer
from .models import URLShortener
import string
import random
from .forms import URLShortenerForm

def generate_short_url():
    ''' A Function to generate a random short URL '''
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url

class URLShortenerCreate(APIView):
    '''
        Check if the URL is already shortened
        Generate a new short URL
        Create and save the new URLShortener object
        Serialize the new object and return it
    '''
    def post(self, request):
        form = URLShortenerForm(request.data)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            existing_shortened_url = URLShortener.objects.filter(original_url=original_url).first()
            
            if existing_shortened_url:
                serializer = URLShortenerSerializer(existing_shortened_url, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)

            short_url = generate_short_url()
            new_url_shortener = URLShortener(original_url=original_url, short_url=short_url)
            new_url_shortener.save()
            serializer = URLShortenerSerializer(new_url_shortener, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
