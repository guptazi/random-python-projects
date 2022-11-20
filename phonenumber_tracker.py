import phonenumbers
from phonenumbers import geocoder

phone_number1=phonenumbers.parse("+9779800789876")
phone_number2=phonenumbers.parse("+9779805461979")
phone_number3=phonenumbers.parse("+12030405067")
phone_number4=phonenumbers.parse("+809078675467")

print(geocoder.description_for_number(phone_number2,"en"))