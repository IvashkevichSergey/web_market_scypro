from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price')

    PROHIBITED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']

        for word in cleaned_data.split():
            if word.lower() in self.PROHIBITED_WORDS:
                raise forms.ValidationError(f'Недопустимое слово {word} в названии продукта')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in cleaned_data.split():
            if word.lower() in self.PROHIBITED_WORDS:
                raise forms.ValidationError(f'Недопустимое слово {word} в описании продукта')

        return cleaned_data


class VersionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_current':
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Version
        fields = '__all__'
