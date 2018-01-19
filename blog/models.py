from django.db import models
from djrichtextfield.models import RichTextField
from django_fsm import FSMIntegerField, transition


__all__ = ['PostStates', 'POST_STATES', 'Post']


class PostStates:
    DRAFT =0
    PUBLISHED = 100

POST_STATES = (
    (PostStates.DRAFT, 'Draft', 'Post'),
    (PostStates.PUBLISHED, 'Published', 'Post'),
)


class Post(models.Model):
    title = models.CharField(max_length= 200)
    short_description = models.CharField(max_length=300)
    body = RichTextField()
    status= FSMIntegerField(state_choices=POST_STATES, default=PostStates.DRAFT, protected=False)
    published_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-published_on']

    @transition('status', source=PostStates.DRAFT, target=PostStates.PUBLISHED)
    def publish(self):
        pass

    @transition('status',
                source=PostStates.PUBLISHED,
                target=PostStates.DRAFT)
    def unpublish(self):
        pass