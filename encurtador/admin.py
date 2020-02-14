from django.contrib import admin

from encurtador.models import Encurtador

class EncurtadorAdmin(admin.ModelAdmin):
    model = Encurtador
    list_display = ('url_curta', 'destino')

admin.site.register(Encurtador, EncurtadorAdmin)