from django.db import models


class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Төмен"),
        ("medium", "Орташа"),
        ("high", "Жоғары"),
    ]
    STATUS_CHOICES = [
        ("new", "Жаңа"),
        ("in_progress", "Орындалуда"),
        ("done", "Дайын"),
    ]

    title = models.CharField("Тақырып", max_length=200)
    description = models.TextField("Сипаттама")
    priority = models.CharField(
        "Басымдық", max_length=10, choices=PRIORITY_CHOICES, default="medium"
    )
    status = models.CharField(
        "Мәртебе", max_length=15, choices=STATUS_CHOICES, default="new"
    )
    created_at = models.DateTimeField("Құрылған уақыты", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Өтінім"
        verbose_name_plural = "Өтінімдер"

    def __str__(self):
        return self.title
