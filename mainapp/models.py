from django.db import models

# Create your models here.

class Registered(models.Model):
    phoneNumber = models.IntegerField(max_length=11)  # 手机号
    time = models.DateTimeField(auto_now_add=True)    # 注册时间
