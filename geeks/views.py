from django.shortcuts import render


def home_view(request):
    if request.method == 'POST':
        your_name = request.POST.get('your_name', '')
        print(f"Form submitted: {your_name}")
    else:
        print("This is a GET request. Probably just loading the page.")

    return render(request, 'geeks/home.html')
