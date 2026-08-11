

def notificaciones_no_leidas(request):
    try:
        # Solo calcular si el usuario es admin (rol = 1)
        if request.session.get('usuario_rol') == 1:
            from core.models import NotificacionProblema, NotificacionReporte
            
            # Contar problemas de entrega no leídos
            problemas_no_leidos = NotificacionProblema.objects.filter(leida=False).count()
            
            # Contar reportes no leídos (incluyendo mensajes de contacto)
            reportes_no_leidos = NotificacionReporte.objects.filter(leida=False).count()
            
            # Total de notificaciones no leídas
            total_notificaciones = problemas_no_leidos + reportes_no_leidos
            
            return {
                'total_notificaciones_no_leidas': total_notificaciones
            }
    except Exception:
        pass
    
    return {
        'total_notificaciones_no_leidas': 0
    }
