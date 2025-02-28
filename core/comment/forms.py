from django import forms
from .models import ReviewModel
from blog.models import Post

class SubmitReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['post','rate', 'description']
        error_messages = {
            'description': {
                'required': 'فیلد توضیحات اجباری است',
            },
        }

        def clean(self):
            cleaned_data = super().clean()
            post = cleaned_data.get('post')
            
            # Check if the post exists and is published
            try:
                Post.objects.get(id=post.id)
            except Post.DoesNotExist:
                raise forms.ValidationError("این قلم من وجود ندارد")

            return cleaned_data