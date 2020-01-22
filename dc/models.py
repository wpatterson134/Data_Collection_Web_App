from django.db import models
from django.contrib.auth.models import Permission, User
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid = models.IntegerField(default=0)

    def __str__(self):
        Accepted = str(self.user.media_set.filter(check='Accepted').count())
        Rejected = str(self.user.media_set.filter(check='Rejected').count())
        Not_Checked = str(self.user.media_set.filter(check='Not Checked').count())
        username = self.user.username
        Paid = str(self.paid)
        string = username + ' [ACCEPTED ' + Accepted + ' - REJECTED ' + Rejected + ' - NOT_CHECKED ' + Not_Checked + ' - PAID ' + Paid + ']'
        return string


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Media(models.Model):
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    NOT_CHECKED = 'Not Checked'
    CHECKS = (
        (NOT_CHECKED, 'Not Checked'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    video = models.FileField()
    check = models.CharField(max_length=15, choices=CHECKS, default=NOT_CHECKED)

    def video_tag(self):
        return mark_safe('<iframe src="%s" width="150" height="150"></iframe>' % (self.video.url))

    video_tag.short_description = 'Video'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.check + ' - ' + self.model)
