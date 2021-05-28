from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view())
]



#get
#localhost:8000/products - case1 때문에 처음꺼 처럼 빈 스트링
#localhost:8000/products/kkk - case2 path('kkk',)

#as_view 는 http 리퀘스트가 get 인지 post인지 구분해서 보내줌