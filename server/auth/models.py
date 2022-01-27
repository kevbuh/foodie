from django.db import models

# Create your models here.
"""
User
  First Name
  Last Name
  Phone Number
  Email
  Payment Method
    Google Pay
    Apple Pay
    PayPal
    Credit Card Number
  Arena
  Seat Number
  Is_Staff = False
  Previous Orders

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
