from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Review

from .models import (
    Service,
    Booking
)


def home(request):

    city = request.GET.get('city')

    if city:
        services = Service.objects.filter(city=city)

    else:
        services = Service.objects.all()

    return render(
        request,
        'services.html',
        {'services': services}
    )


@login_required
def add_service(request):

    if request.method == 'POST':

        Service.objects.create(

            provider=request.user,

            category=request.POST['category'],

            name=request.POST['name'],

            description=request.POST['description'],

            price=request.POST['price'],

            city=request.POST['city'],

            address=request.POST['address'],

            phone=request.POST['phone'],

            whatsapp=request.POST['whatsapp'],

            email=request.POST['email'],

            image=request.FILES.get('image')
        )

        return redirect('/services/')

    return render(
        request,
        'add_service.html'
    )


@login_required
def book_service(request, id):

    service = Service.objects.get(id=id)

    if request.method == 'POST':

        Booking.objects.create(

            customer=request.user,

            service=service,

            booking_date=request.POST['date'],

            booking_time=request.POST['time']
        )

        return redirect('/services/')

    return render(
        request,
        'book_service.html',
        {'service': service}
    )
    


@login_required
def add_review(request, id):

    service = Service.objects.get(id=id)

    if request.method == 'POST':

        Review.objects.create(

            user=request.user,

            service=service,

            rating=request.POST['rating'],

            comment=request.POST['comment']
        )

        return redirect('/services/')
    
@login_required
def dashboard(request):

    services = Service.objects.filter(
        provider=request.user
    )

    bookings = Booking.objects.filter(
        service__provider=request.user
    )

    return render(
        request,
        'dashboard.html',
        {
            'services': services,
            'bookings': bookings
        }
    )

@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        customer=request.user
    )

    return render(
        request,
        'my_bookings.html',
        {'bookings': bookings}
    )