from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from .models import task
from .forms import TaskForm

#Home page/ first page of the web application

def homepage(request):  # This is name of the function. You can call it anything, independent of the url
                        # from where it is being triggered

    context = {'first_name':'John Dob'} # Defining a dictionary which will be passed in render() on next line
                                        # so that the template named "index.html" can print the values

    return render(request, 'crm/index.html', context)

# CRUD- Create a task

def create_task(request):

    form = TaskForm() # create a variable that contains our Model form's blank instance

    if request.method == 'POST': #This will be true only when the Form is submitted
                                # The control will not enter here when the blank form is displayed
                                # for the first time
                                 

        form = TaskForm(request.POST) # This creates an instance of TaskForm with only the relevant attributes
                                      # request.POST contains the relevant attributes that we need
                                      # the TaskForm instance is then assigned to a variable form.

        if form.is_valid(): # this checks whether the form values coming in the POST request are valid
            
            form.save() # this command will save the values in the 'form' variable to the db

            return redirect ('view-tasks') #this will redirect the flow to route name: view-tasks
        


    #Now render our ModelForm. This will be done just how we rendered other models 
    # we will create a dictionary

    context_3 = {'TaskForm': form} # you can give any key of your choice i.e. TaskForm

    return render (request, 'crm/create-task.html', context_3)

# CRUD- Read tasks

def tasks(request):

    queryDataAll = task.objects.all()

    context_2 = {'AllTasks': queryDataAll}

    return render(request, 'crm/view-tasks.html', context_2)


# CRUD - Update task

def update_task (request, pk): # pk is the primary key, passed on from view-task.html file 
                                #pk is used for dynamic urls
    # update_task() will be called in 2 different scenarios:
        #1. When someone clicks on the 'update task' link below a particular task on view-tasks page
        #   In this case, the http request that will go to server, will NOT be a POST request.    
        #   Remember, this code will be put on server, so here in this code, you can check the request type.
        #2. When user clicks the submit button on 'update-task' page - after updating the task details
        #   In this case, the http request that will go to server, will be a POST request 

    task_record = task.objects.get(id=pk) # get the object/record from 'task' table, where value of id is equale
                                    # to the value of pk passed on from the url
    
    form = TaskForm(instance = task_record) # create a variable named 'form' which will carry the filled up
                                    # instance of our Modelform "TaskForm". The instance will have
                                    # value of the particular task object, which was fetched in previous line
                                    # in short, the TaskForm that will be displayed on the screen, will have 
                                    # filled up values.
    if request.method == 'POST':  # We are checking whether the http request is a POST
                                  # this will be the case when user will click submit button on the
                                  # update-task page - after updating the task details there.

        form = TaskForm(request.POST, instance = task_record)  #Q. what are we trying to do here?

        if form.is_valid():    

            form.save()    

            return redirect('view-tasks') #view-tasks is the name of the url for 'view-task' page
                                          #Using this command, the flow will redirect to view-tasks url
                                          # urls.py will determine which function to call.
                                          # ultimately view-tasks.html page will be rendered.
        
    context = {'UpdateTask': form}

    return render(request, 'crm/update-task.html', context) # this command will be executed only when
                                                            # the http request is NOT a POST request
                                                            # In that case, update-task.html page will be rendered



# CRUD - Delete Task

def delete_task(request, pk):

    task_record = task.objects.get(id=pk)
    
    if request.method == 'POST':

        task_record.delete()

        return redirect('view-tasks')

    return render(request, 'crm/delete-task.html')


# Registration webpage

def register(request):

    ClientList = [

            {
                'id': '1',
                'name': 'John',
                'occupation': 'Engineer'
                
            },
                
            {
                'id': '2',
                'name': 'Kate',
                'occupation': 'Lawyer'
                
            },

    ]

    context_1 = {'MainClientList': ClientList}

    return render(request, 'crm/register.html', context_1)





