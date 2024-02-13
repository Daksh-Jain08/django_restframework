from rest_framework import serializers
from base.models import Item
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(many=True, view_name='item-detail', queryset=Item.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'items']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Item
        fields = ['url', 'id', 'name', 'created', 'owner']