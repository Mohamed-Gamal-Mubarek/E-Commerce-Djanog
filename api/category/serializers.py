# FIRST THIN IN SERIALIZERS FROM RESET_FRAMEWORK IMPORT SERIALIZERS
from rest_framework import serializers

# SECOND IMPORT THE MODEL YOU WANT TO SERIALIZE IT 
from .models import Category

class CategorySerializer(serializers):
    class Meta:
        model = Category
        field = ('name', 'description')
