from django.shortcuts import render

from django.http import HttpResponse
from booktest.models import BookInfo #导入图书类
from django.template import loader,RequestContext


def my_render(request,template_path,context_dict={}):
    temp=loader.get_template(template_path)

    context=RequestContext(request,context_dict)

    res_html=temp.render(context)

    return HttpResponse(res_html)

# Create your views here.
#1定义视图函数，HTTPRequest
#2进行url配置，建立url地址和视图的对应关系

def index(request):

    return render(request,'booktest/index.html',{'content':'hello word','list':list(range(1,10))})
    #进行处理，和m,t进行交互
    # return HttpResponse("老铁没毛病")
    #使用模板文件
    #1 加载模板文件，模板对象
    #2 定义模板上下文；给模板文件传递数据
    #3 模板渲染：产生标准的html内容
    #4 返回给浏览器

def index2(request):
    return HttpResponse("hello python")


def show_books(request):
    """显示图书的信息"""
    #1 通过M查找图书表中的数据
    books=BookInfo.objects.all()
    #2 使用模板
    return render(request,'booktest/show_books.html',{'books':books})


def detail(request,bid):
    #1.根据bid查询图书信息
    book=BookInfo.objects.get(id=bid)
    #2.查询和book关联的英雄信息
    heros=book.heroinfo_set.all()
    #3.使用模板
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})


