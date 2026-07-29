from django.apps import AppConfig


class RasterConfig(AppConfig):
    """
    App configuration for django-raster.

    Pins the primary-key type for this app's models.

    Without this, the consuming project's ``DEFAULT_AUTO_FIELD`` applies to
    django-raster's models. Eight of them declare no explicit primary key, and
    their migrations create ``id`` as an ``AutoField`` -- so a project set to
    ``BigAutoField`` (which is what ``django-admin startproject`` has generated
    since Django 3.2, and therefore what most projects have) sees a permanent
    mismatch. ``makemigrations`` then tries to write an ``AlterField`` for
    every one of those models *into the installed package*, inside
    site-packages, where it will be lost on the next upgrade and cannot be
    applied by the project's own migration history.

    Declaring it here makes the app's primary keys independent of the project
    setting, which is what a reusable app should do. It changes nothing about
    the schema: ``AutoField`` is what the existing migrations already create.

    Projects that genuinely want 64-bit primary keys on these tables should
    subclass this config and migrate deliberately, rather than inheriting the
    change by accident from a project-wide default.
    """

    name = 'raster'
    verbose_name = 'Raster'

    # NOT BigAutoField -- see above. This must match what
    # raster/migrations/0001_initial.py already created.
    default_auto_field = 'django.db.models.AutoField'
