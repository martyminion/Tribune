from django.test import TestCase
from .models import Editor,tags,Article
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):
  #Set up Method

  def setUp(self):
    self.james = Editor(first_name = "James", last_name = "Muriuki", email = "james@gmail.com")
    self.marge = Editor(first_name = "Margaret", last_name = "Wamucii", email = "margie@gmail.com")

  #test an instance of the class
  def test_instance(self):
    self.assertTrue(isinstance(self.james,Editor))

  def test_save_method(self):
    self.james.save_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors)>0)

  def test_delete_editor(self):
    self.james.save_editor()
    self.james.delete_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors) == 0)

  def test_get_all_editors(self):
    self.james.save_editor()
    self.marge.save_editor()
    editors = Editor.get_all_editors()
    self.assertTrue(len(editors) == 2)


class ArticleTestClass(TestCase):

  def setUp(self):
    #creating a new editor and saving it
    self.james = Editor(first_name = "James", last_name = "Muriuki", email = "james@gmail.com")

    self.james.save_editor()

    #creating a new tag and saving it
    self.new_tag = tags(name = 'testing')
    self.new_tag.save()

    #creating a new article
    self.new_article = Article(title = "Test Article", post = "This is just a rnadom post", editor = self.james)
    self.new_article.save()

    self.new_article.tags.add(self.new_tag)

  def tearDown(self):
    Editor.objects.all().delete()
    tags.objects.all().delete()
    Article.objects.all().delete()

  def test_get_news_today(self):
    todays_news = Article.todays_news()
    self.assertTrue(len(todays_news)>0)

  def test_get_news_by_date(self):
    test_date = '2017-03-17'
    date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    news_by_date = Article.days_news(date)
    self.assertTrue(len(news_by_date)==0)