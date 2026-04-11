from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for creating/editing product reviews.
    """
    class Meta:
        model = Review
        fields = ('title', 'comment', 'rating')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Review title',
                'maxlength': '200'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Share your experience with this product...'
            }),
            'rating': forms.RadioSelect(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'title': 'Review Title',
            'comment': 'Your Review',
            'rating': 'Rating',
        }
