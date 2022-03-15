# FIRST THIN IN SERIALIZERS FROM RESET_FRAMEWORK IMPORT SERIALIZERS
from rest_framework import serializers

# SECOND IMPORT THE MODEL YOU WANT TO SERIALIZE IT 
from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')
