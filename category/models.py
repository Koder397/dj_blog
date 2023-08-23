from django.db import models


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)

    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'category'
