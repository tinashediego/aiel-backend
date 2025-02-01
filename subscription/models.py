from django.db import models

class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    email_address = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
        ordering = ['created_at']
    def __str__(self):
        return self.email_address