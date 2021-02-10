from django.urls import path
from mainapp import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('writer/<slug>',views.writer_view,name="writer_info"),
    path('blog/<slug>',views.blog_view,name="blog_info"),
    path('create',views.create,name="createblog"),
    path('all_blogs',views.all_blogs,name="all_blog"),
    path('contact_us',views.about_us,name="contact_us"),
    path('search',views.search,name="search"),
    path('error',views.error404,name="error"),
    path('tags/<slug:tag_slug>',views.tag_search,name="post_by_tags")
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)