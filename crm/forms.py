
from django.forms import ModelForm # importing ModelForm class from django.forms package
from .models import task #importing 'task' model from models.py file in our crm application.
                         #since this file i.e. forms.py is in same directory as models.py file, 
                         # we just need to put a '.' before models.


#Below is the class that we are creating for our Model form.
# Inherit the ModelForm base class inside the brackets of definition of the class.
class TaskForm(ModelForm):

    class Meta:
            model = task # the model(table) that we want to use for our form
            fields = '__all__' # utilize all the applicable fields of the model
            

            