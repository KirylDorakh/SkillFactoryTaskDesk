from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

    # переопределить метод ready, чтобы при готовности нашего приложения
    # импортировался модуль со всеми функциями обработчиками
    def ready(self):
        import posts.signals
