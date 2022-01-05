from django.views import generic

from product.models import Variant, Product, ProductVariant, ProductVariantPrice


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class ProductView(generic.TemplateView):
    template_name='products/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = list(products)
        variants = Variant.objects.all()
        context['variants'] = list(variants)
        product_variants = ProductVariant.objects.all()
        context['product_variants'] = list(product_variants)
        product_variant_prices = ProductVariantPrice.objects.all()
        context['product_variant_prices'] = list(product_variant_prices)
        return context