from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField('Категория', max_length=50, help_text='Введите категорию')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Tag(models.Model):
	name = models.CharField('Тэг', max_length=50, help_text='Введите тэг')

	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField('Заголовок', max_length=200, help_text='Введите заголовок статьи')
	description = models.TextField('Контент', max_length=2000, help_text='Введите контент статьи')
	pub_date = models.DateTimeField('Опубликовано', null=True, blank=True, help_text='Дата публикации')
	categories = models.ManyToManyField(Category, verbose_name='Категория', help_text='Выберите категорию')
	tags = models.ManyToManyField(Tag, verbose_name='Тэги', help_text='Выберите тэги')
	source_link = models.CharField('Ссылка', null=True, max_length=200, help_text='Введите ссылку на источник')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-pub_date']