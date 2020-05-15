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
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return '{0} por R$ {1}'.format(self.title, self.price)

    def save(self, *args, **kwargs):
        self.slug = self.slug_generator(self.title)
        super(Product, self).save(*args, **kwargs)

    def slug_generator(self, title: str) -> str:
        """Generate a slug based in the product title."""
        return slugify(title)

