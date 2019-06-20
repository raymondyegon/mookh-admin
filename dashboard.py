from controlcenter import Dashboard, widgets
from .models import *

class ModelItemList(widgets.ItemList):
    model = User
    list_display = ('pk', 'field')

class MyDashboard(Dashboard):
    widgets = (
        ModelItemList,
    )