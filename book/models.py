from django.db import models
from manageuser.models import User

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='publisher/',null=True,blank= True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author/', null=True,blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book/')
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete= models.CASCADE)
    genres = models.ForeignKey(Genre,on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    
 

class BookInstance(models.Model):
    book = models.ForeignKey(Book,on_delete=models.RESTRICT,null=True)
    due_back =models.DateField(null=True,blank=True)
    borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    LOAN_STATUS = (
        ('m','Maintanace'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability'

    )

    def __str__(self):
        return f'{self.id} ({self.book.title})'