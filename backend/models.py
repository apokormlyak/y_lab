from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from django.db import models
from base import Base

app = FastAPI()


# @app.get('/')
# def read_root():
#     html_content = '<h2>Hello METANIT.COM!</h2>'
#     return HTMLResponse(content=html_content)


class Menu(Base, models.Model):
    submenu = models.CharField('Разделы меню', max_length=300, db_index=True)

    class Meta:
        verbose_name = 'Меню'


class Submenu(Base, models.Model):
    menu = models.ForeignKey(Menu.submenu, verbose_name='Подменю', on_delete=models.CASCADE)
    meal = models.CharField('Блюда', max_length=300, db_index=True)

    class Meta:
        verbose_name = 'Разделы меню'


class Meal(Base, models.Model):
    name = models.CharField('Блюдо', max_length=300, db_index=True)
    submenu = models.ForeignKey(Submenu.meal, verbose_name='Подменю', on_delete=models.CASCADE)
    price = models.DecimalField('Стоимость', null=True, blank=True)

    class Meta:
        verbose_name = 'Блюда'
