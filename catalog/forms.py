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

    # def clean(self):
    #     self.forms = super().clean()
    #     active_list = [form.cleaned_data['is_current'] for form in self.forms if 'is_current' in form.cleaned_data]
    #     if active_list.count(True) > 1:
    #         raise forms.ValidationError('Возможна лишь одна активная версия. Пожалуйста, активируйте только 1 версию.')
    # def clean_is_current(self):
    #     product = self.cleaned_data['product']
    #     print(Version.objects.filter(product=product, is_current=True))
    #     if len(Version.objects.filter(product=product, is_current=True)) > 1:
    #         print('WE ARE HERE')
    #         raise forms.ValidationError('Возможна лишь одна активная версия. Пожалуйста, активируйте только 1 версию.')
    #     cleaned_data = self.cleaned_data
    #     print(self.cleaned_data)
        # all_current_versions = Version.objects.filter(product=product, is_current=True)

    #     cleaned_data = self.cleaned_data['is_current']
    #     # print(cleaned_data)
    #     check_is_current(cleaned_data)
    #     # product = cleaned_data.get('product')
    #     # is_current = cleaned_data.get('is_current')
    #     # print(is_current)
    #     # if all_current_versions and is_current:
    #     #     raise forms.ValidationError('!!!!!!!!!!!!!!!')
    #     return cleaned_data


