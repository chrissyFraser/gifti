from django.urls import path
from gifti.views import WishList, CreateWish, WishDetail, AddBrand, AddStore

urlpatterns = [
    path("", homepage, name="homepage")
    path("/wishlist", WishList.as_view(), name="wishlist")
    path("/createwish", CreateWish.as_view(), name="createwish")
    path("/wishdetail/<int:pk>", WishDetail.as_view(), name="wishdetail")
    path("/addbrand", AddBrand.as_view(), name="addbrand")
    path("/addstore", AddStore.as_view(), name="addstore")
]