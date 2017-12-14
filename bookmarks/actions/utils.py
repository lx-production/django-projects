from django.contrib.contenttypes.models import ContentType
from .models import actions
from django.utils import timezone
import datetime


def create_action(user, verb, target=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id,
                                            verb=verb,
                                            created__gte=last_minute)
    action.save()
