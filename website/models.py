from django.db import models
from datetime import date
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image

# Create your models here.
class Pet(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ]

    STATUS_CHOICES = [
        ('available', 'Доступен для помощи'),
        ('adopted', 'Взят домой'),
        ('foster', 'Взят на передержку'),
    ]

    name = models.CharField("Имя", max_length=100, blank=False)
    gender = models.CharField("Гендер", max_length=10, choices=GENDER_CHOICES, blank=False)
    approximate_birth_date = models.DateField("Дата рождения (приблизительно)", default=date.today, blank=False)
    health_issues = models.BooleanField("Есть проблемы со здоровьем", default=False)

    description = models.TextField("Описание", blank=False)

    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, blank=False)

    video = models.CharField("Видео", max_length=255, blank=True)

    @property
    def age(self):
        today = date.today()
        if today.year - self.approximate_birth_date.year < 1:
            months = today.month - self.approximate_birth_date.month
            if months == 1:
                return "1 месяц"
            elif months in [2, 3, 4]:
                return str(months) + " месяца"
            return str(months) + " месяцев"
        years = today.year - self.approximate_birth_date.year
        if years == 1:
            return "1 год"
        elif years in [2, 3, 4]:
            return str(years) + " года"
        return str(years) + " лет"
    
    @property
    def age_category(self):
        today = date.today()
        months_diff = (today.year - self.approximate_birth_date.year) * 12 + (today.month - self.approximate_birth_date.month)
        if months_diff <= 12:
            return "little"
        elif months_diff <= 131:
            return "adult"
        else:
            return "elderly"

class PetPhoto(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField("Фото", upload_to='photos/')
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGBA")
            #img.thumbnail((1920, 1920))
            output = BytesIO()
            img.save(
                output,
                format="WEBP",
                quality=80,
                method=6
            )
            output.seek(0)
            filename = self.image.name.rsplit(".", 1)[0] + ".webp"
            self.image.save(
                filename,
                ContentFile(output.read()),
                save=False
            )
        super().save(*args, **kwargs)