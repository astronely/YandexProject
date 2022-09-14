from rest_framework import serializers
from docs.models import Item

class ItemImportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'url', 'parentId', 'type', 'size', 'date')

class ItemUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('url', 'parentId', 'type', 'size', 'date')

	def update(self, instance, validated_data):
		instance.url = validated_data.get("url", instance.url)
		instance.parentId = validated_data.get("parentId", instance.parentId)
		instance.type = validated_data.get("type", instance.type)
		instance.size = validated_data.get("size", instance.size)
		instance.date = validated_data.get("dateTime", instance.date)
		instance.save()
		return instance
