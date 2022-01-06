from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView, ProductView, ProductFilterView
from product.views.variant import VariantView, VariantCreateView, VariantEditView

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/page<int:page_number>/', ProductView.as_view(), name='list.product'),
    path('list/', ProductView.as_view(), name='list.product'),
    path('list/filter/', ProductFilterView.as_view(), name='filter.product'),
    path('list/filter/<str:title>/<int:price_from>/<int:price_to>/<str:date>/<int:page_number>/', ProductFilterView.as_view(), name='filter.product'),
]
