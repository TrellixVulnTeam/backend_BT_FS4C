from django.urls import path
from monTiGMagasin import views
from django.urls import register_converter

class FloatConverter:
    regex = "[\d\.\d]+"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return "{}".format(value)


register_converter(FloatConverter, "float")

urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('putonsale/<int:tig_id>/<float:newpromo>/', views.PutOnSale.as_view()),
    path('removesale/<int:tig_id>/', views.RemoveOnSale.as_view()),
    path('incrementStock/<int:tig_id>/<int:number>/', views.IncrementStock.as_view()),
    path('decrementStock/<int:tig_id>/<int:number>/', views.DecrementStock.as_view()),
]