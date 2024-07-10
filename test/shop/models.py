from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import Media
from conf.settings import AUTH_USER_MODEL
from common.utils import validate_phone_number

class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    price = models.FloatField(_('price'), default=0)
    percentage = models.IntegerField(_('percentage'), default=0)
    tags = models.ManyToManyField('Tags', verbose_name=_('tags'))
    desc = models.TextField(_('description'))
    in_stock = models.BooleanField(_('in stock'), default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))

    @property
    def total_discount(self):
        return self.price * (self.percentage / 100)


class Reason(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Reason')
        verbose_name_plural = _('Reasons')

    def __str__(self):
        return self.title


class ToWhom(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('To Whom')
        verbose_name_plural = _('To Whom')

    def __str__(self):
        return self.title


class ProductReason(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'),
                                related_name='reason')
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, verbose_name=_('reason'))

    class Meta:
        verbose_name = _('Product Reason')
        verbose_name_plural = _('Product Reasons')


class ProductToWhom(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'),
                                related_name='to_whom')
    who = models.ForeignKey(ToWhom, on_delete=models.CASCADE, verbose_name=_('who'))

    class Meta:
        verbose_name = _('To whom product')
        verbose_name_plural = _('To whom product')


class ProductImage(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_('image'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))

    class Meta:
        verbose_name = _("Product image")
        verbose_name_plural = _('product images')


class Tags(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.title


class Feedback(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))
    feedback = models.TextField(_('feedback'))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __str__(self):
        return self.user


class Question(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))
    question = models.TextField(_('question'))

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return self.question


class Address(models.Model):
    address = models.CharField(max_length=120, verbose_name=_('address'))
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'))

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class Order(models.Model):
    class OrderDelivery(models.TextChoices):
        BY_COURIER = 'by courier', _('by courier')
        SELF_CALL = 'self-call', _('self-call')

    class OrderPaymentMethod(models.TextChoices):
        BY_CARD = 'by card', _('by card')
        CASH = 'cash', _('cash')

    phone_number = models.CharField(max_length=120, verbose_name=_('phone number'),
                                    validators=[validate_phone_number])
    full_name = models.CharField(_('full name'), max_length=120)
    last_name = models.CharField(_('last_name'), max_length=120)
    quantity = models.IntegerField(_('quantity'), default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))
    address = models.CharField(_('address'), max_length=120)
    obtaining_method = models.CharField(_('obtaining_method'), max_length=120,
                                        choices=OrderDelivery.choices,
                                        default=OrderDelivery.SELF_CALL)
    payment_method = models.CharField(_('payment method'), max_length=120,
                                      choices=OrderPaymentMethod.choices,
                                      default=OrderPaymentMethod.CASH)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity"), default=1)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")
        unique_together = ("order", "product")

    def __str__(self):
        return f"Id: {self.id}| Q: {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity


class OrderForPermanentBuyer(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))

    class Meta:
        verbose_name = _('OrderForPermanentBuyer')
        verbose_name_plural = _('OrderForPermanentBuyer')

    def __str__(self):
        return self.user.phone_number