from dataclasses import fields
from schema import marshamllow


class ProductSchema(marshamllow.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')
