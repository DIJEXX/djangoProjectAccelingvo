from .models import Message


def isRequestPost(request):
    return request.method == 'POST'

def isUserExist(user):
    return user is not None

def createMessage(request, main):
    return (Message.objects.create(
            text=request.POST['messageField'], 
            main=main,
            author=request.user, 
            receiver=request.user
        )
    )


def serializeJson(request, object):
    created_at_datetime = object.created_at
    formatted_created_at = created_at_datetime.strftime('%B %d, %Y')
    return {
            'pk': object.pk,
            'fields': {
                'text': object.text,
                'created_at': formatted_created_at,
                'main': object.main.id,
                'author': object.author.id,
                'receiver': object.receiver.id,
                'author_name': request.user.username
            }
        }

def filtermainMessages(id_number):
    return Message.objects.filter(main__id=id_number)