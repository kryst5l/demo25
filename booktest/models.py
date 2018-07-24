from django.db import models

#ORM作用是通过类和对象就可以对数据表进行操作
#还有一个作用是根据类生成数据库中的表

# Create your models here.
class BookInfo(models.Model):
    """图书模型类"""
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateField()

    def __str__(self):
        #返回书名
        return self.btitle


class HeroInfo(models.Model):
    """英雄人物类"""
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField(default=False)
    hcomment=models.CharField(max_length=128)

    hbook=models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname
