#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ Author: HeliantHuS
@ Codes are far away from bugs with the animal protecting
@ Time:  12/03/2020
@ FileName: urls.py
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Index),
    path("captcha", views.Captcha, name="Captcha"),  # 验证码API
    path("sendSMS", views.sendSMS, name="SMS"),       # 发送短信API
    path("download", views.downloadAPP, name="Download")  # 下载app页面 | 注册 写库
]

