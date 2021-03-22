from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from pages.models import Redirect
from django.core.cache import cache as memcache
from django.conf import settings
import memcache
import json

@require_http_methods(["GET"])
def index(request):

    redirects = Redirect.objects.all()

    context = {
        'redirects': redirects
    }
    return render(request, 'pages/index.html', context)


@require_http_methods(["GET"])
def get_key(request, key):

    memcached = settings.MEMCACHED_ENGINE_END_POINT
    engine_cache = False
    if memcached:
        try:
            engine_cache = memcache.Client(memcached)
        except Exception:
            print('No memcached client could be created')

    # Me fijo si existe en cache.
    result = engine_cache.get('redirect_cache')

    if result is not None:
        for x in result[0]:
            if x.key == key:
                response_data = {}
                response_data['key'] = x.key
                response_data['url'] = x.url
                return HttpResponse(json.dumps(response_data), content_type="application/json")

    # Si no existe en cache, se consulta a la base de datos.
    try:
        redirect_found = Redirect.objects.get(key=key)
        response_data = {}
        response_data['key'] = redirect_found.key
        response_data['url'] = redirect_found.url
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    except redirect_found.DoesNotExist:
        response_data = {}
        return HttpResponse(json.dumps(response_data), content_type="application/json")



