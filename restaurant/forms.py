from django import forms
from .models import Restaurant, Review

class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'location']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter restaurant name'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter restaurant location'
            }),
        }

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Rate between 1 and 5'
            }),
            'comment': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Write your comment'
            }),
        }