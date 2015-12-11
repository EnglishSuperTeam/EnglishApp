__author__ = 'root'
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","csvt01.settings")
django.setup()
from blog.models import User,Publisher,Author,Book

# p=Publisher(name='a',address='b',city='c',state_province='d',country='e',website='f')
# p.save()
# a=Author(first_name='hsuan',last_name='chou',email='965202810@qq.com')
# a.save()
# a1=Author(first_name='jay',last_name='chou',email='965202810@360.com')
# a.save()

u=User(name='Tomy')
u.save()

