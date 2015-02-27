from django.db import models
from django.core.exceptions import ValidationError


# validators with Django are confusing. This will only be called automatically if ModelForm is used
def validate_not_none(value):
    if value is None:
        raise ValidationError(u'The value can not be none')


class Person(models.Model):
    name = models.CharField(max_length=200, validators=[validate_not_none])
    email = models.CharField(max_length=200, validators=[validate_not_none])
    age = models.IntegerField(default=0, validators=[validate_not_none])

    def adult(self):
        if(self.age >= 18):
            return True
        else:
            return False

    def age_str(self):
        return str(self.age)
