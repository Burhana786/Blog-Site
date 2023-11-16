from django.urls import path,include
from .views import*

urlpatterns = [
    path('uhome/',UserHome.as_view(),name='uhome'),
    path('profile/',ViewProfile.as_view(),name='prof'),
    path('addbio/',UserProView.as_view(),name='addbio'),
    path('cpw/',ChangePasswordView.as_view(),name='change-psw'),
    path('update-bio/<int:user_id>',UpdateBioView.as_view(),name='update-bio'),
    path('addcmnt/<int:id>',add_comment,name='add-cmnt'),
    path('add-like/<int:bid>',add_like,name='add-like'),
    path('viewblog/',ViewBlog.as_view(),name='view-blog')
]