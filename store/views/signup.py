from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        firstname = postData.get('firstname')
        lastname = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        value = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'password': password
        }
        customer = Customer(firstname=firstname,
                            lastname=lastname,
                            email=email,
                            password=password)

        error_msg = self.ValidateCustomer(customer)

        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_msg,
                'values': value
            }
            return render(request, 'signup.html', data)

    def ValidateCustomer(self, customer):
        error_msg = None
        if not customer.firstname:
            error_msg = "First Name required !!"
        elif not customer.lastname:
            error_msg = "Last Name required !!"
        elif len(customer.password) < 6:
            error_msg = "Password must be 6 characters long"
        elif customer.isExists(customer):
            error_msg = "Email already registered..."

        return error_msg
