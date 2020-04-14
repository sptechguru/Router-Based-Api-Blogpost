
from django.contrib import admin
from django.urls import path ,include

from.router import router


urlpatterns = [

    path('admin/', admin.site.urls),

    # router is include
    path('', include(router.urls)),

    # old apiview
    # path('', include('blog_api.urls'))

]
