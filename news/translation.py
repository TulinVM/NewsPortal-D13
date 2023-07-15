from .models import Post, New, Author, Category, PostCategory, Comment, SubscribersCategory
from modeltranslation.translator import register, TranslationOptions  # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться


# регистрируем наши модели для перевода

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('datetime_post', 'header', 'content',)  # указываем, какие именно поля надо переводить в виде кортежа

@register(New)
class NewTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'category', 'data_pub',)

@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('user_name', 'user_rating',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name_category',)


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('post_comment', 'user_comment', 'text_comment', 'datetime_comment',)
