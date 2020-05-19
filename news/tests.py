from django.test import TestCase
from .models import Editor,tags,Article
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
