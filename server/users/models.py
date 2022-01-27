from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    User
      First Name
      Last Name
      Email
      Phone Number
        Optional?
      Payment Method
        Google Pay
        Apple Pay
        PayPal
        Credit Card Number
      Arena
      Seat Number
      Is_Staff = False
      Previous Orders
    """
    username = None
    email = models.EmailField(_('Email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


"""
Runner
  First Name
  Last Name
  Payment Method
    Bank Number
    PayPal
    Venmo
    Cash App
  Is_Staff = True
  Email
  Current Order
  Rating

Arena
  Location
  Description
  Image
  Number of stores
  Type of event
    NFL
    NBA
    MLB

Merchant
  Merchant ID
  Merchant Name
  Image
  Description
  Arena
  Snacks
  Popular Items
  Delivery Time
  Order

Snack
  Image
  Title
  Description
  Price
  Availability
  Item ID
  Type of snack
  Merchant

Order
  Snacks
  Delivery Type
  Delivery
  Pickup at front of line
  Price
  Tip
  Estimated Time
  Time Requested
  Time Delivered
  Seat Number
  Customer Name
  Special Request
  Service Rating
"""
