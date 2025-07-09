from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField  # Для форматированного текста
from wagtail.admin.panels import FieldPanel

class HomePage(Page):  # Замените YourPage на имя вашей модели
    subtitle = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name="Подзаголовок"
    )
    # Или для форматированного текста:
    # subtitle = RichTextField(features=['bold', 'italic'], blank=True)
    rtfbody = RichTextField(
        features=[
            'h2', 'h3', 'h3', 'h4',        # Заголовки
            'bold', 'italic',   # Жирный/курсив
            'link',             # Ссылки
            'ol', 'ul',         # Списки
            'hr',               # Горизонтальная линия
            'document-link',    # Ссылки на документы
            'image',            # Изображения
            'code',             # Блоки кода
            'embed',            # Вставка контента (видео, карты, etc.)
            'blockquote',       # Цитаты

        ],
        blank=True,
        null=True,
        verbose_name="Тело страницы"
    )


    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),  # Добавляем поле в админ-панель
        FieldPanel('rtfbody'),  # Добавляем поле в админ-панель
      
    ]