from django.db import models

class Post(models.Model):
    name = models.CharField('Nomi: ', max_length=255)
    content = models.TextField("Ma'lumot: ")
    use = models.CharField('Ism: ', max_length=20)
    categories = models.CharField(max_length=50)
    date = models.DateTimeField('Sana: ', auto_now_add=True)
    img1 = models.CharField('Rasm: ', max_length=255)
    img2 = models.CharField('Rasm: ', max_length=255)
    img3 = models.CharField('Rasm: ', max_length=255)
    def __str__(self):
        return self.name


class TopPost(models.Model):
    name = models.CharField('Turi: ', max_length=20)
    content = models.TextField("Ma'lumot: ")
    use = models.CharField('Nomi: ', max_length=20)
    categories = models.CharField(max_length=50)
    date = models.DateTimeField('Sana: ', auto_now_add=True)
    img = models.CharField('Rasm: ', max_length=255)
    def __str__(self):
        return self.use        


class MainPost(models.Model):
    name = models.CharField('Turi: ', max_length=255)
    content = models.TextField('Malumoti: ')
    use = models.CharField("Ismi: ", max_length=20)
    categories = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    img1 = models.CharField('Rasm: ', max_length=255)
    img2 = models.CharField('Rasm:', max_length=255)
    def __str__(self):
        return self.use

class CatePost(models.Model):
    turi1 = models.CharField(max_length=20)
    turi2 = models.CharField(max_length=20)        
    turi3 = models.CharField(max_length=20) 
    turi4 = models.CharField(max_length=20)        
    turi5 = models.CharField(max_length=20)
    soni1 = models.IntegerField(default=1)
    soni2 = models.IntegerField(default=1) 
    soni3 = models.IntegerField(default=1) 
    soni4 = models.IntegerField(default=1) 
    soni5 = models.IntegerField(default=1)  
    def __str__(self):
        return self.turi1   


class LatPost(models.Model):
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=255)
    def __str__(self):
        return self.content            
       
        


