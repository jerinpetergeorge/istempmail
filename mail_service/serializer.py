from rest_framework import serializers


class DomainSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, name: str):
        return name.lower()
