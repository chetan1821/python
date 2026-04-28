from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """
    Form to handle UserProfile creation and validation.
    """
    class Meta:
        # Link this form to the UserProfile model
        model = UserProfile
        # Specify which fields should appear in the form
        fields = ['username', 'age', 'is_public']
        # Add Bootstrap styling to the form fields
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_age(self):
        """
        Custom validation to ensure age is 13 or older.
        Django automatically calls methods named clean_<field_name>.
        """
        age = self.cleaned_data.get('age')
        if age < 13:
            # If age is too low, raise an error that will be shown on the form
            raise forms.ValidationError("Age must be at least 13.")
        # Always return the cleaned data
        return age
