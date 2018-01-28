from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.management import call_command

from files.models import File
from django.contrib.auth.decorators import login_required

from tasks.tasks import check_file
from tasks.models import Task

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, redirect
from collections import Counter

@login_required
def run_task(request):
    if request.method == 'GET':
        print(request.GET)
        if 'action' in request.GET:
            action = request.GET['action']
            file_id  = request.GET['file_id']

            file = File.get_object_or_404(pk=file_id)
            if action == "check":
                
                task_manifest = {}
                task_manifest['file'] = file.id
                task_manifest['action'] = action
                task = Task(user=request.user)
                
                task.manifest = task_manifest
                task.status = 'new'
                task.action = action
                task.user = request.user
                task.save()

                check_file.delay(task.id)

                file.status = 'scheduled'
                file.save()
            
    return redirect('files-index')


@login_required
def index(request):

    queries = []

    if request.method == 'POST':
        files = request.POST.getlist('files')
        action = request.POST['action']

        for file_id in files:

            # file = File.objects.get(pk=file_id)
            if request.user.is_staff:
                file = get_object_or_404(File, pk=file_id)
            else:
                file = get_object_or_404(File, pk=file_id, user=request.user)

            if action == "delete":
                file.delete()
            if action == "check":
                
                task_manifest = {}
                task_manifest['file'] = file.id
                task_manifest['action'] = action
                task = Task(user=request.user)
                
                task.manifest = task_manifest
                task.status = 'new'
                task.action = action
                task.user = request.user
                task.save()

                check_file.delay(task.id)

                file.status = 'scheduled'
                file.save()

        status = request.POST.getlist('status')
        
        if status:
            queries.append(Q(status=status))

        print('status', status)

    # Or the Q object with the ones remaining in the list
    
    
    if request.method == 'GET':
        print(request.GET)
        if 'orderby' in request.GET:
            orderby = request.GET['orderby'][0]
            order = request.GET['order'][0]
            if order == 'desc':
                order_string = '-{}'.format(orderby)
            else:
                order_string = orderby
        else:
            order_string = 'name'
    
    if request.user.is_staff:#status='scheduled' size=0
        files = File.objects.filter().order_by('size')
    else:
        files = File.objects.filter(user=request.user).order_by(order_string)

    files_summary = dict(Counter(files.values_list('status', flat=True)))

    context = {
        'files':files,
        'files_summary':files_summary
    }

    return render(request, 'files/index.html', context)

@login_required
def view(request, file_id):
    print('Hello')


@login_required
def import_files(request):
    print('Hello World')
    # call_command('import_files')
    return redirect('files-index')

class FileUpdate(LoginRequiredMixin, UpdateView):
    model = File
    fields = '__all__'

    def get_queryset(self):
        if not self.request.user.is_staff:
            return self.model.objects.filter(user=self.request.user)
        else:
            return self.model.objects

class FileDelete(LoginRequiredMixin, DeleteView):
    model = File
    success_url = reverse_lazy('files-index')
    def get_queryset(self):
        if not self.request.user.is_staff:
            return self.model.objects.filter(user=self.request.user)
        else:
            return self.model.objects

@login_required
def bulk_action(request):

    if request.method == 'POST':
        files = request.POST.getlist('files')
        action = request.POST['action']

        for file_id in files:


            # file = File.objects.get(pk=file_id)
            if request.user.is_staff:
                file = get_object_or_404(File, pk=file_id)
            else:
                file = get_object_or_404(File, pk=file_id, user=request.user)

            if action == "delete":
                file.delete()
            if action == "check":
                
                task_manifest = {}
                task_manifest['file'] = file.id
                task_manifest['action'] = action
                task = Task(user=request.user)
                
                task.manifest = task_manifest
                task.status = 'new'
                task.action = action
                task.user = request.user
                task.save()

                check_file.delay(task.id)

                file.status = 'scheduled'
                file.save()

    return redirect('files-index')
