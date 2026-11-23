from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student


def student_list(request):  # READ
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def student_create(request):  # CREATE
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student added successfully.')
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Add Student'})


def student_update(request, pk):  # UPDATE
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated successfully.')
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Edit Student'})


def student_delete(request, pk):  # DELETE
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
