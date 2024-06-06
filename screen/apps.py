from django.apps import AppConfig

from TrackMyPrice.Core.Application.Factory.Repository_builder import RepositoryBuilder


class ScreenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'screen'

    def ready(self) -> None:
        RepositoryBuilder.BuildRepositories()

    