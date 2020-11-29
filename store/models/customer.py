from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    # def get_customer_by_email(email):
    #     return Customer.objects.filter(email=email)
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False
