from django.shortcuts import render, redirect
from gifti.models import Wish, BrandName, StoreName
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class WishList(LoginRequiredMixin, ListView):
    model = Wish
    template_name = "wishlist.html"
    context_object_name = "wishlist"

    def get_queryset(self):
        return Wish.objects.filter(nametag=self.request.user)


class CreateWish(LoginRequiredMixin, CreateView):
    model = Wish
    fields = [
        "item",
        "brand",
        "picture",
        "link",
        "store",
        "color",
        "style",
        "size",
        "notes",
    ]
    template_name = "create_wish.html"
    context_object_name = "createwish"
    success_url = reverse_lazy("wishlist")

    def form_valid(self, form):
        item = form.save(commit=False)
        item.user = self.request.user
        item.save()
        return redirect("wishdetail/<int:pk>", args=[self.objects.id])

class WishDetail(DetailView):
    model = Wish
    template_name = "wish_detail.html"
    context_object_name = "wishdetail"
    

class AddBrand(CreateView, LoginRequiredMixin):
    model = BrandName
    fields = ["brand_name"]
    template_name = "add_brand.html"
    context_object_name = "addbrandname"
    success_url = reverse_lazy("wishlist")


class AddStore(CreateView, LoginRequiredMixin):
    model = StoreName
    fields = ["store_name"]
    template_name = "add_store.html"
    context_object_name = "addstore"
    success_url = reverse_lazy("wishlist")

class HomepageView(TemplateView):
    template_name = "homepage.html"