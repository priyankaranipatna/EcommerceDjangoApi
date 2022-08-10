from rest_framework import serializers
from .models import Product
class Productdata(serializers.ModelSerializer):
    id = serializers.IntegerField(default=False)
    pname = serializers.CharField(max_length=100, default=False)
    pdesc=serializers.CharField(max_length=100, default=False)
    pcat_id=serializers.CharField(default=False)
    pimages=serializers.CharField(max_length=100, default=False)
    class Meta:
        db_table = "products"
        model = Product
        fields = '__all__'