
from django.forms import ModelForm # importing ModelForm class from django.forms package
from .models import task #importing 'task' model from models.py file in our crm application.
                         #since this file i.e. forms.py is in same directory as models.py file, 
                         # we just need to put a '.' before models.

# Below we are importing Django's default i.e. inbuilt model forms as well as models (tables)
# The first one will provide us with a User creation form (model form)
# the second one will provide us with the User model (table) that we access from admin page
# Instead of using the inbuit ones, We can also go and create our own model form and Model from 
# the scratch -- just like what we did for our other model form i.e. TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Below is the class that we are creating for our Model form.
# Inherit the ModelForm base class inside the brackets of definition of the class.
class TaskForm(ModelForm):

    class Meta:
            model = task # the model(table) that we want to use for our form
            fields = '__all__' # utilize all the applicable fields of the model
            

class CreateUserForm(UserCreationForm):
      
      class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']

      