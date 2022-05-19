from django.db import models


class VersionTypeHtml(models.TextChoices):
    allservers = "allservers"
    pcclassic = "pcclassic"
    pcmods = "pcmods"
    bedrock = "bedrock"
    newservers = "newservers"


class VersionMinecraft(models.Model):
    version = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.version)


class VersionDescriptionHtml(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    t_header = models.CharField(max_length=150)
    t_text = models.CharField(max_length=550)
    b_header = models.CharField(max_length=150)
    b_text = models.TextField()


class VersionDescription(models.Model):
    version = models.ForeignKey(VersionMinecraft, on_delete=models.CASCADE, verbose_name="minecraft version", )
    types = models.CharField(max_length=20, choices=VersionTypeHtml.choices)

    description = models.ForeignKey(VersionDescriptionHtml, on_delete=models.CASCADE, )

    def __str__(self):
        return "version: {}, type: {}".format(self.version, self.types)