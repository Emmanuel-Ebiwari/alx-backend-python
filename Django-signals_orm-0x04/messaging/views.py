from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message
from django.contrib.auth.models import User
from .serializers import MessageSerializer


def serialize_message(message):
    return {
        'id': message.id,
        'sender': message.sender.username,
        'content': message.content,
        'timestamp': message.timestamp,
        'replies': [serialize_message(reply) for reply in message.replies.all()]
    }


@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({"detail": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def reply_message(request, message_id):
    try:
        message = Message.objects.get(id=message_id)
        content = request.data.get('content')
        if not content:
            return Response({"detail": "Content cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

        reply = Message.objects.create(
            sender=request.user,
            receiver=message.sender,
            content=content,
            parent_message=message
        )
        serializer = MessageSerializer(reply)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Message.DoesNotExist:
        return Response({"detail": "Message not found."}, status=status.HTTP_404_NOT_FOUND)
# utils.py or inline


@api_view(['GET'])
def get_threaded_conversations(request):
    top_level_messages = Message.objects.filter(parent_message__isnull=True) \
        .select_related('sender') \
        .prefetch_related('replies__sender', 'replies__replies__sender')

    data = [serialize_message(msg) for msg in top_level_messages]
    return Response(data)


@api_view(['GET'])
def get_unread_messages(request):
    unread_messages = Message.unread.unread_for_user(receiver=request.user) \
        .only('id', 'sender', 'content', 'timestamp') \
        .select_related('sender') \
        .values('id', 'sender__username', 'content', 'timestamp')

    return Response(list(unread_messages))
