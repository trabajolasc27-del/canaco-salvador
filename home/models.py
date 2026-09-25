from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

    fk_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="categorias_creadas",
    )

    class Meta:
        db_table = "categoria"
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    nombre_temporal = models.CharField(
        max_length=255,
        blank=True,
    )
    ruta = models.FileField(upload_to="uploads/")
    tipo = models.CharField(
        max_length=100,
        blank=True,
    )
    tamano = models.PositiveIntegerField(default=0)

    fk_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="archivos_subidos",
    )

    createdat = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "archivo"
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    ESTADO_BORRADOR = "borrador"
    ESTADO_PUBLICADO = "publicado"

    ESTADOS = [
        (ESTADO_BORRADOR, "Borrador"),
        (ESTADO_PUBLICADO, "Publicado"),
    ]

    titulo = models.CharField(max_length=180)
    resumen = models.TextField()
    contenido = models.TextField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="publicaciones",
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="publicaciones",
    )

    imagen_portada = models.ForeignKey(
        Archivo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="portadas",
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default=ESTADO_BORRADOR,
    )

    visitas = models.PositiveIntegerField(default=0)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "publicacion"
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.titulo

    @property
    def publicada(self):
        return self.estado == self.ESTADO_PUBLICADO


class GaleriaPublicacion(models.Model):
    publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.CASCADE,
        related_name="galeria",
    )

    archivo = models.ForeignKey(
        Archivo,
        on_delete=models.CASCADE,
        related_name="galerias",
    )

    createdat = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "galeria_publicacion"
        verbose_name = "Imagen de galería"
        verbose_name_plural = "Galería de publicaciones"

    def __str__(self):
        return f"Imagen de {self.publicacion.titulo}"


class Comentario(models.Model):
    ESTADO_PENDIENTE = "pendiente"
    ESTADO_APROBADO = "aprobado"
    ESTADO_BLOQUEADO = "bloqueado"

    ESTADOS = [
        (ESTADO_PENDIENTE, "Pendiente"),
        (ESTADO_APROBADO, "Aprobado"),
        (ESTADO_BLOQUEADO, "Bloqueado"),
    ]

    publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.CASCADE,
        related_name="comentarios",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comentarios",
    )

    contenido = models.TextField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default=ESTADO_PENDIENTE,
    )

    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comentario"
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f"Comentario de {self.user.username}"


class Perfil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil",
    )

    foto_perfil = models.ForeignKey(
        Archivo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="perfiles",
    )

    apellido_paterno = models.CharField(
        max_length=80,
        blank=True,
    )

    apellido_materno = models.CharField(
        max_length=80,
        blank=True,
    )

    class Meta:
        db_table = "core_perfil"
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"Perfil de {self.user.username}"