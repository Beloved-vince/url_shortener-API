from rest_framework import serializers
from .models import URLShortener, Click

class URLShortenerSerializer(serializers.ModelSerializer):
    shortened_url = serializers.SerializerMethodField()

    class Meta:
        model = URLShortener
        fields = ['id', 'original_url', 'short_url', 'shortened_url', 'clicks', 'created_at']
        
    def get_shortened_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.short_url)
        return obj.short_url

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ['id', 'url_shortener', 'clicked_at']
