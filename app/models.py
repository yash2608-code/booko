from django.db import models

# Create your models here.


class Admin(models.Model):
    Role = models.CharField(max_length=100, default="Role")
    Email = models.EmailField(max_length=100, default="Email", unique=True)
    Password = models.CharField(max_length=100, default="passwd")
    Is_Created = models.DateTimeField(auto_now_add=True)
    Is_Verified = models.BooleanField(default=False)


class User(models.Model):
    Admin = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True)
    Firstname = models.CharField(max_length=100, default="fname")
    Lastname = models.CharField(max_length=100, default="lname")
    Gender = models.CharField(max_length=100, default="Gender")
    Profilepic = models.ImageField(upload_to="user-profile/", default="abc")


class Seller(models.Model):
    Admin = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True)
    Firstname = models.CharField(max_length=100, default="fname")
    Lastname = models.CharField(max_length=100, default="lname")
    Gender = models.CharField(max_length=100, default="Gender")
    Profilepic = models.ImageField(upload_to="seller-profile/", default="abc")


class Book(models.Model):
    Seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    Bookname = models.CharField(max_length=100, default="bname")
    Authorname = models.CharField(max_length=100, default="aname")
    Bookimage = models.ImageField(upload_to="book-image/", default="abc")
    Book = models.FileField(upload_to="Book-File/", default="abc")
    BookPrice = models.FloatField(default=0.0)
