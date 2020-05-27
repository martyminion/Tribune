from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

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
  post = HTMLField()
  editor = models.ForeignKey(User,on_delete=models.CASCADE)
  tags = models.ManyToManyField(tags)
  pub_date = models.DateTimeField(auto_now_add=True)
  article_image = models.ImageField(upload_to='articles/',blank=True)

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

  @classmethod
  def todays_news(cls):
    today = dt.date.today()
    news = cls.objects.filter(pub_date__date = today)

    return news

  @classmethod
  def days_news(cls,date):
    news = cls.objects.filter(pub_date__date = date)
    return news

  @classmethod
  def search_by_title(cls,search_term):
    news = cls.objects.filter(title__icontains = search_term)
    return news

class NewsLetterRecipients(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()