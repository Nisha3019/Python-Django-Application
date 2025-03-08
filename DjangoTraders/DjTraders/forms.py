from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Reset #Div, HTML 

from .models import Product, Customer

# v2.1 Added Customer Form.
# A nice tutorial on Crispy Forms is at: https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html

#Customer Form
class CustomerForm(forms.ModelForm):
    
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Customer Name'}))
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contact Name'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'5 char postal code'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('customer_name', css_class='form-group col-md-6 mb-0'),
                Column('contact_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('postal_code', css_class='form-group col-md-6 mb-0'),
                Column('country', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
           
            Submit('submit','Add Customer',
                   css_class='btn btn-light mt-3',
            ),
            
            Reset('reset', 'Reset Search', css_class='btn btn-secondary')      
        )

    class Meta:
        model = Customer
        fields = '__all__'
        
    #validations for customer form
    
    def clean_customer_name(self):
        customer_name = self.cleaned_data['customer_name']
        if len(customer_name) > 100:
            raise ValidationError("Customer Name must not be more than 100 characters.")
        if customer_name.isnumeric():
            raise ValidationError("Customer name should not be numeric.")
        return customer_name
    
    def clean_contact_name(self):
        contact_name = self.cleaned_data['contact_name']
        if len(contact_name) > 100:
            raise ValidationError("Contact Name must not be more than 100 characters.")
        if contact_name.isnumeric():
            raise ValidationError("Contact name should not be numeric.")
        return contact_name
    
    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise ValidationError("Address cannot be empty.")
        if len(address) > 255:
            raise ValidationError("Address must not be more than 255 characters.")
        return address
    
    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city:
            raise ValidationError("City cannot be empty.")
        if len(city) > 100:
            raise ValidationError("City must not be more than 100 characters.")
        if city.isnumeric():
            raise ValidationError("City name should not be numeric.")
        return city
    
    def clean_country(self):
        country = self.cleaned_data.get('country')
        if not country:
            raise ValidationError("Country cannot be empty.")
        if len(country) > 100:
            raise ValidationError("Country must not be more than 100 characters.")
        if country.isnumeric():
            raise ValidationError("Country name should not be numeric.")
        return country
    
    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']
        if len(postal_code) != 5:
            raise ValidationError("Postal Code must be 5 characters long.")
        return postal_code


# Product form 
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            
            Reset('reset', 'Reset Search', css_class='btn btn-secondary')      
        )
        
    #validations for product form
    
    def clean_product_name(self):
        product_name = self.cleaned_data['product_name']
        if len(product_name) > 100:
            raise ValidationError("Product Name must not be more than 100 characters.")
        if product_name.isnumeric():
            raise ValidationError("Product name should not be numeric.")
        return product_name
    
    def clean_price(self):
        price = self.cleaned_data['price']

        if price == '':
            raise ValidationError("Product Price cannot be empty.")

        if price < 0:
            raise ValidationError("Product Price is never negative.")
    
        elif price > 100:
            raise ValidationError("Product Price is never more than $100.00.")
    
        return price
    
    def clean_unit(self):
        unit = self.cleaned_data['unit']
        if not unit:
            raise ValidationError("Unit cannot be empty.")
        return unit
    
   
   
            
    
  
