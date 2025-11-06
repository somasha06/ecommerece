from django.forms import ModelForm
from .models import Category,Product

class Categoryform(ModelForm): #Instead of writing form fields manually (like name, description, etc.), a ModelForm can generate those fields directly from your model.
    class Meta:
        model=Category
        fields = "__all__"


class Productform(ModelForm): #Instead of writing form fields manually (like name, description, etc.), a ModelForm can generate those fields directly from your model.
    class Meta:
        model=Product
        fields = "__all__"
