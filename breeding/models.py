from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Validators for breeding app


def validate_male(value):
    falcon = Falcon.objects.get(pk=value)
    if falcon.sex != "M":
        raise ValidationError(
            _("%(value)s is not a male falcon"),
            params={"value": falcon.name},
        )


def validate_female(value):
    falcon = Falcon.objects.get(pk=value)
    if falcon.sex != "F":
        raise ValidationError(
            _("%(value)s is not a female falcon"),
            params={"value": falcon.name},
        )


# Models for breeding app


class Falcon(models.Model):
    """ Model for a single falcon """

    SEX = [("M", "male"), ("F", "female")]

    name = models.CharField(max_length=30, null=True, blank=True)
    ring = models.CharField(max_length=30, null=True, blank=True)
    species = models.ForeignKey(
        "Species",
        on_delete=models.CASCADE,
        related_name="species",
        null=True,
        blank=True,
    )
    sex = models.CharField(max_length=1, choices=SEX, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    birth_cert = models.ForeignKey(
        "Birth_cert",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    CITES_num = models.CharField(max_length=30, null=True, blank=True)
    CITES_img = models.FileField(null=True, blank=True, upload_to="falcon_docs/")
    registration_img = models.FileField(null=True, blank=True, upload_to="falcon_docs/")
    RDOS_permission_img = models.FileField(
        null=True, blank=True, upload_to="falcon_docs/"
    )
    in_aviary = models.ForeignKey(
        "Aviary", on_delete=models.CASCADE, null=True, blank=True
    )
    father = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="falcon_father",
        null=True,
        blank=True,
    )
    mother = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="falcon_mother",
        null=True,
        blank=True,
    )
    width_young = models.PositiveSmallIntegerField(null=True, blank=True)
    length_young = models.PositiveSmallIntegerField(null=True, blank=True)
    weight_young = models.PositiveSmallIntegerField(null=True, blank=True)
    width_old = models.PositiveSmallIntegerField(null=True, blank=True)
    length_old = models.PositiveSmallIntegerField(null=True, blank=True)
    weight_old = models.PositiveSmallIntegerField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    additional_info = models.CharField(max_length=255, null=True, blank=True)

    def get_youngsters(self):
        return Falcon.objects.filter(Q(father=self) | Q(mother=self))

    def get_fields_for_template(self):
        """ Gets iterable for the loop in template """
        return [
            (field.name, field.verbose_name, field.value_to_string(self))
            for field in Falcon._meta.fields
            if field.name != "owner" and field.name != "id"
        ]

    def get_absolute_url(self):
        """ Returns the url to access a detail record for this falcon """
        return reverse("breeding:falcon-detail", args=[str(self.id)])

    def __str__(self):
        return "Falcon name: " + str(self.name) + ", ring: " + str(self.ring)


class Pair(models.Model):
    """ Model for a breeding pair """

    number = models.IntegerField()
    male = models.ForeignKey(
        Falcon,
        on_delete=models.PROTECT,
        related_name="male_pair",
        validators=[validate_male],
    )
    female = models.ForeignKey(
        Falcon,
        on_delete=models.PROTECT,
        related_name="female_pair",
        validators=[validate_female],
    )

    def get_youngsters(self):
        """ Gets iterable for the loop in template """
        return Falcon.objects.filter(father=self.male, mother=self.female)

    def get_absolute_url(self):
        """ Returns the url to access a detail record for this pair """
        return reverse("breeding:pair-detail", args=[str(self.id)])

    def __str__(self):
        return (
            "Pair:\nmale name: "
            + str(self.male.name)
            + ", ring: "
            + str(self.male.ring)
            + ";\n"
            + "female name: "
            + str(self.female.name)
            + ", ring: "
            + str(self.female.ring)
        )


class Aviary(models.Model):
    """ Model for a single aviary """

    number = models.IntegerField(default=0)
    last_cleaned = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_absolute_url(self):
        """ Returns the url to access a detail record for this aviary """
        return reverse("breeding:aviary-detail", args=[str(self.id)])

    def __str__(self):
        return "Aviary number: " + str(self.number)


class Photo(models.Model):
    """ Model to enable saving multiple photos per falcon """

    img = models.ImageField(null=True, blank=True, upload_to="falcon_imgs/")
    falcon = models.ForeignKey(Falcon, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "Falcon Photo"


class Species(models.Model):
    """ Model to enable using predefined species """

    name = models.CharField(max_length=30, null=True, blank=True)
    latin = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Office(models.Model):
    """ Model for data for office """

    TYPES = [
        ("PIW", "Powiatowy Inspektorat Weterynarii"),
        ("RDOS", "Regionalna Dyrekcja Ochrony Środowiska"),
        ("MIN", "Ministerstwo Środowiska"),
        ("POW", "Starostwo Powiatowe"),
    ]

    name = models.CharField(max_length=256)
    street = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=7)
    city = models.CharField(max_length=32)
    office_type = models.CharField(max_length=4, choices=TYPES)


class Birth_cert(models.Model):
    """ Model for birth certificates """

    signature = models.CharField(max_length=16)
    cert_file = models.FileField(null=True, blank=True, upload_to="falcon_docs/")
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("breeding:birth_cert-detail", args=[str(self.id)])
