from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from . import utils
import io
import json
import time
import random


# Create your views here.

def Index(request):
    """
    主页
    """
    return render(request, "loan/register.html")


def Captcha(request):
    """
    验证码
    """
    if request.method == "GET":
        buf = io.BytesIO()
        img, code = utils.create_validate_code()
        img.save(buf, "PNG")

        # 将字符串形式的验证码放在Session中
        request.session["captchaCode"] = code.lower()
        response = HttpResponse(buf.getvalue(), content_type="image/png")
        return response


def sendSMS(request):
    """
    发送短信
    """
    if request.method == "POST":

        # 防止频繁请求
        now_time = int(time.time())
        sess_time = request.session.get("time", "")
        if sess_time:
            if now_time < request.session["time"]:
                return JsonResponse({
                    "code": 3,
                    "error": "你请求的太快了. 稍等1分钟再试吧"
                })

        # 解析body
        body = json.loads(request.body)

        # 检查参数是否合法
        phoneNumber = body.get("phone", "")
        captchaCode = body.get("captcha", "")
        if utils.checkPhone(phoneNumber) != True:
            return JsonResponse({
                "code": 1,
                "error": "手机号码不合法"
            })

        if captchaCode != request.session["captchaCode"]:
            return JsonResponse({
                "code": 2,
                "error": "验证码输入错误"
            })

        # 全部通过 进行限制60秒请求
        request.session["time"] = int(time.time()) + 50


        # 发送短信
        ...
        ...
        ...

        # 发送成功
        request.session["access"] = True

        return JsonResponse({
            "code": 0,
        })


def downloadAPP(request):
    """
    下载APP | POST就写库
    """
    if request.method == "POST":
        # 如果需要判断是否是从注册页面注册成功
        flag = request.session.get("access", False)
        if flag != True:
            return redirect("/")
        # 验证手机验证码输入是否正确

        # 给Session

        # 给后台发注册成功的手机号

        # 给后台发是由谁来邀请的

    # 跳转APP下载页面
    return render(request, "loan/downloadPage.html")
