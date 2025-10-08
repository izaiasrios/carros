from django import forms
from cars.models import Brand, Car
#from django.core.exceptions import ValidationError
#from django.utils.translation import gettext_lazy as _ # Para mensagens de erro

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


#def clean_value(self):
 #   value = self.cleaned_data.get('value')
 #   if value < 20000:
  #      self.add_error('value', 'Valor mínimo deve ser de R$ 20000')
  #      return value
    
#def clean_factory_year(self):
 #   factory_year = self.cleaned_data.get('factory_year')
 #   if factory_year < 1975:
 #       self.add_error('factory_year', 'Ano mínimo deve ser 1975')
 #       return factory_year