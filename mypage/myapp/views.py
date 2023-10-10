from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def factorial_result(request):
    if request.method == 'POST':
        number = int(request.POST['number'])
        result = calculate_factorial(number)
        return HttpResponse(f'Факторіал числа {number} дорівнює {result}')
    else:
        return HttpResponse('Неправильний метод запиту')


def calculate_factorial(n):
    if n < 0:
        return "невизначеному числу. Такі розрахунки неможливі."
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)