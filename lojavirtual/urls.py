from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('main.urls')),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('carrinho/', include('carrinho.urls', namespace='carrinho')),
    path('pedidos/', include('pedidos.urls', namespace='pedidos')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

