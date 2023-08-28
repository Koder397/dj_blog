from django.db import models

from category.models import Category


class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)

    post_name = models.CharField(max_length=255)

    post_content = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_name

    class Meta:
        db_table = 'post'
