import math

from django.shortcuts import render

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

    def get_context_data(self, page_number=1):
        context = super(ProductView, self).get_context_data()
        starting_page = (page_number - 1) * 2
        end_page = page_number * 2
        products = list(Product.objects.all()[starting_page:end_page])
        context['products'] = products
        variants = Variant.objects.all()
        context['variants'] = list(variants)
        product_variants = ProductVariant.objects.filter(product__in=products)
        context['product_variants'] = list(product_variants)
        product_variant_prices = ProductVariantPrice.objects.all()
        context['product_variant_prices'] = list(product_variant_prices)
        total_product = Product.objects.count()
        context['total_product'] = total_product
        context['product_from'] = page_number * 2 -1
        context['product_to'] = total_product if page_number * 2 > total_product else page_number * 2
        pagination = math.ceil(total_product / 2)
        page_list = []
        for num in range(1, pagination+1):
            page_list.append(num)
        context['pagination'] = page_list
        context['previous_page'] = page_number - 1
        context['next_page'] = page_number + 1 if page_number + 1 <= pagination else 0
        context['pagination_type'] = 'all_product_view'
        return context

class ProductFilterView(generic.TemplateView):
    template_name='products/list.html'

    def get_context_data(self, title='', price_from=0, price_to=0, date='', page_number=0, *args, **kwargs):
        context = super(ProductFilterView, self).get_context_data(*args, **kwargs)
        if page_number == 0:
            title = self.request.GET['title']
            price_from = self.request.GET['price_from']
            price_to = self.request.GET['price_to']
            date = self.request.GET['date']
            page_number = 1
        context['title'] = title
        context['price_from'] = price_from
        context['price_to'] = price_to
        context['date'] = date
        starting_page = (page_number - 1) * 2
        end_page = page_number * 2
        
        variants = Variant.objects.all()
        context['variants'] = list(variants)
        product_variants = ProductVariant.objects.all()
        context['product_variants'] = list(product_variants)
        
        products = Product.objects.filter(title=title)[starting_page:end_page]
        context['products'] = list(products)
        product_variant_prices = ProductVariantPrice.objects.filter(product__title=title, \
            price__gte=price_from, price__lte=price_to)
        context['product_variant_prices'] = list(product_variant_prices)

        total_product = Product.objects.filter(title=title).count()
        context['total_product'] = total_product
        context['product_from'] = page_number * 2 -1
        context['product_to'] = total_product if page_number * 2 > total_product else page_number * 2
        pagination = math.ceil(total_product / 2)
        page_list = []
        for num in range(1, pagination+1):
            page_list.append(num)
        context['pagination'] = page_list
        context['previous_page'] = page_number - 1
        context['next_page'] = page_number + 1 if page_number + 1 <= pagination else 0
        context['pagination_type'] = 'filtered_product_view'
        return context