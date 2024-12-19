from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class ReviewStatusType(models.IntegerChoices):
    pending = 1, "در انتظار تایید"
    accepted = 2, "تایید شده"
    rejected = 3, "رد شده"

class ReviewModel(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)
    description = models.TextField()
    rate = models.IntegerField(default=5, validators=[
                               MinValueValidator(0), MaxValueValidator(5)])
    status = models.IntegerField(
        choices=ReviewStatusType.choices, default=ReviewStatusType.pending.value)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]
    
    def __str__(self):
        return f"{self.user} - {self.service.id}"
    
    
    def get_status(self):
        return {
            "id":self.status,
            "title":ReviewStatusType(self.status).name,
            "label":ReviewStatusType(self.status).label,
        }
@receiver(post_save,sender=ReviewModel)
def calculate_avg_review(sender,instance,created,**kwargs):
    if instance.status == ReviewStatusType.accepted.value:
        blog = instance.blog
        average_rating = ReviewModel.objects.filter(blog=blog, status=ReviewStatusType.accepted).aggregate(Avg('rate'))['rate__avg']
        blog.avg_rate = round(average_rating,1)
        blog.save()