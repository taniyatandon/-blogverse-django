from django import forms
from .models import BlogPost, Profile, AppUser

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'content']  # Fields shown in the form


class ProfileForm(forms.ModelForm):
    # AppUser fields
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=AppUser.GENDER_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    birthdate = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    address = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    phone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['profile_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-populate AppUser fields from the related user object
        if self.instance and self.instance.user:
            self.fields['name'].initial = self.instance.user.name
            self.fields['email'].initial = self.instance.user.email
            self.fields['gender'].initial = self.instance.user.gender
            self.fields['birthdate'].initial = self.instance.user.birthdate
            self.fields['address'].initial = self.instance.user.address
            self.fields['phone'].initial = self.instance.user.phone

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        
        # Update AppUser fields
        user.name = self.cleaned_data.get('name', user.name)
        user.email = self.cleaned_data.get('email', user.email)
        user.gender = self.cleaned_data.get('gender', user.gender)
        user.birthdate = self.cleaned_data.get('birthdate', user.birthdate)
        user.address = self.cleaned_data.get('address', user.address)
        user.phone = self.cleaned_data.get('phone', user.phone)
        
        if commit:
            user.save()
            profile.save()
        return profile