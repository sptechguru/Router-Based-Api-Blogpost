 
 # blog_api is applixation name
from blog_api.viewsets import MyPostViewset ,MycontactViewset
from rest_framework import routers
from rest_framework import viewsets


router = routers.DefaultRouter()

router .register('mypost/',MyPostViewset)
router .register('mycontact',MycontactViewset)
