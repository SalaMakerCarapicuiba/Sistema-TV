from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


class NoticesAdmin(admin.ModelAdmin):
    def imagem_notices(self, obj):
        if obj.imagem:
            return obj.imagem.url_for
        return "(Nenhuma imagem)"
    
    imagem_notices.short_description = 'Imagem'
    imagem_notices.allow_tags = True

class MateriaAdmin(admin.ModelAdmin):
    pass

class HorarioAdmin(admin.ModelAdmin):
    pass

class RecadosAdmin(admin.ModelAdmin):
    def imagem_recados(self, obj):
        if obj.imagem:
            return obj.imagem.url_for
        return "(Nenhuma imagem)"
    
    imagem_recados.short_description = 'Imagem'
    imagem_recados.allow_tags = True


admin.site.register(User, UserAdmin)
admin.site.register(Notices, NoticesAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Recados, RecadosAdmin)