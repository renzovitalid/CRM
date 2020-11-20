from app.wsgi import *
from core.erp.models import *

#listar

print(Category.objects.all())

for i in Category.objects.filter():
    print (i)
