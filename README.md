# CMS-django-
Content Management System with django ( user interface ) all the crud operations using class based views
Steps to get started

1 Step one :
```
git clone https://github.com/kusalkumar/CMS-django.git
```

Follow the tutorials to learn more

2 Step two :
```
virtualenv env
```

Now install all the dependencies
```
pip install -r requirements.txt
```

3 Step three : Change directory to dj_delery
```
cd project/
```

4 Step four : configure your db and redis configuration in settings.py
```
vim dj_celery/settings.py
```

5 Step five : Now you can run the server, celry and celery beat and flower (to monitor celery tasks)
```
python manage.py runserver
```

6 Step six : home page
 file:///home/its4ucharan/Pictures/homepagecrud.png![image](https://user-images.githubusercontent.com/17420868/116688617-956c5d80-a9d4-11eb-91a8-35fad7e2306a.png)

7 Step seven User can go to manage posts to perform all the CRUD operations

file:///home/its4ucharan/Pictures/crud-manageposts.png![image](https://user-images.githubusercontent.com/17420868/116688754-c187de80-a9d4-11eb-991f-2003dce59be9.png)

8 Create view:
file:///home/its4ucharan/Pictures/crud-create.png![image](https://user-images.githubusercontent.com/17420868/116688798-d49aae80-a9d4-11eb-9d6b-c21d65d3d0d1.png)

9 update view
file:///home/its4ucharan/Pictures/crud-edit.png![image](https://user-images.githubusercontent.com/17420868/116688840-e3816100-a9d4-11eb-81bf-3d6e4382aa33.png)

10 Delete the post
file:///home/its4ucharan/Pictures/crud-delete.png![image](https://user-images.githubusercontent.com/17420868/116688884-f7c55e00-a9d4-11eb-8245-94c087f0b224.png)

