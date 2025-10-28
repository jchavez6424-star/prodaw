from django.contrib import admin
from .models import Cliente, TipoSeguro, Aseguradora, PolizaSeguro

admin.site.register(Cliente)
admin.site.register(TipoSeguro)
admin.site.register(Aseguradora)
admin.site.register(PolizaSeguro)
