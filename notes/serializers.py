from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """ Сериализер основаный на модели Note """
    class Meta:
        model = Note
        read_only_fields = ('create_at',)
        fields = ('id', 'title', 'body', 'created_at')

