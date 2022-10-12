from django.db import models

from shop.models import Product
from shop.models.customer import Customer


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь",
    )
    date_ordered = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата заказа",
    )
    complete = models.BooleanField(
        default=False,
        verbose_name="Завершено?",
    )
    transaction_id = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Транзакция",
    )

    def __str__(self):
        return f"{self.id}"

    @property
    def shipping(self):
        shipping = False
        order_items = self.orderitem_set.all()
        for i in order_items:
            if not i.product.digital:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Продукт",
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Пользователь",
    )
    quantity = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name="Количество",
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата заказа",
    )

    def __str__(self):
        return f"{self.pk}"

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    class Meta:
        verbose_name = 'Заказ товара'
        verbose_name_plural = 'Заказы товаров'
