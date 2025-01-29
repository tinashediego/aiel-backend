from django.db import models

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='board_images/images/')
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    #phone_number, email_address, linkedin_link
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    linkedin_url = models.CharField(max_length=255)
    x_url = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15)
    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Board"
        ordering = ['created_at']
    def __str__(self):
        return self.fullname

