from django.core import serializers

class booking_serializer():
    def serializer(bookings):
        return serializers.serialize('json', bookings)


class menu_serializer():
    def serializer(menu):
        return serializers.serialize('json', menu)