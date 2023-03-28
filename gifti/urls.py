from django.urls import path
from gifti.views import WishList, CreateWish, WishDetail, AddBrand, AddStore, HomepageView, FaqView, FriendListView

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("wishlist/", WishList.as_view(), name="wishlist"),
    path("createwish/", CreateWish.as_view(), name="createwish"),
    path("wishlist/<int:pk>", WishDetail.as_view(), name="wishdetail"),
    path("addbrand/", AddBrand.as_view(), name="addbrand"),
    path("addstore/", AddStore.as_view(), name="addstore"),
    path("friendlists/", FriendListView.as_view(), name="friendlists"),
    path("faq&help/", FaqView.as_view(), name="faq")
]