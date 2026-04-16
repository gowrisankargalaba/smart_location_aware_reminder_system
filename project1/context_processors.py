from django.conf import settings

def google_maps_api(request):
    """
    Makes the Google Maps API Key available in all templates.
    """
    return {
        'google_maps_key': getattr(settings, 'GOOGLE_MAPS_API_KEY', '')
    }
