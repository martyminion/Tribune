from django.db import models

# Create your models here.
class Editor(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()
  phone_number = models.CharField(max_length=10,blank=True)

  def __str__(self):
    return self.first_name

  def save_editor(self):
    self.save()

  def delete_editor(self):
    self.delete()

  def get_all_editors():
    all_editors = Editor.objects.all()
    return all_editors

class tags(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  def save_tags(self):
    self.save()

  def get_all_tags():
    all_tags = tags.objects.all()
    return all_tags

class Article(models.Model):
  title = models.CharField(max_length=60)
  post = models.TextField()
  editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
  tags = models.ManyToManyField(tags)
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  def save_article(self):
    self.save()

  @classmethod
  def delete_article(cls,id):
    Article.objects.filter(id = id).delete()

  def get_all_articles():
    all_articles = Article.objects.all()
    return all_articles