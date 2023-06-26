from django.db import models
from datetime import datetime
# Create your models here.

class AuthorModel(models.Model):
    name = models.CharField(max_length=65,default='')
    fname = models.CharField(max_length=65,default='')
    date_of_birth = models.DateField(default=datetime.now)
    country = models.CharField(max_length=15,default='')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'author'

class BookCategoryModel(models.Model):
    name = models.CharField(max_length=65,default='')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'book_category'

class BookModel(models.Model):
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=127,default='')
    category = models.ForeignKey(BookCategoryModel,on_delete=models.SET_NULL,null=True)
    page = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'book'
