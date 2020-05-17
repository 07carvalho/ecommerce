from datetime import datetime
from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    """Product instance."""
    title = models.CharField(max_length=60, blank=False, null=False, unique=True)
    description = models.CharField(max_length=600, blank=False, null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=False, null=False)
    discount_price = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        app_label = 'products'
        db_table = 'api_product'

    def __str__(self):
        return '{0} por R$ {1}'.format(self.title, self.price)

    def save(self, *args, **kwargs):
        self.slug = self.slug_generator()
        super(Product, self).save(*args, **kwargs)

    def update(self, instance, **data):
        instance.title = data.title
        instance.description = data.description
        instance.price = data.price
        instance.discount_price = data.discount_price
        instance.image = data.image
        instance.slug = self.slug_generator()
        instance.visible = data.visible
        instance.update = datetime.now()
        instance.save()

    def slug_generator(self):
        """Generate a slug based in the product title."""
        return slugify(self.title)

    def order_queryset(self, queryset, order_by):
        """Order the posts list queryset."""
        if order_by is not None:
            return queryset.order_by(order_by)
        return queryset.order_by('-created_at')
