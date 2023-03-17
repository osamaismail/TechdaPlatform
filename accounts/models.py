from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from TechdaPlatform.utils import validate_phone
from datetime import datetime



def calculate_age(birthday):
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age


USER_TYPE = (
    ('1', 'Administrator'),
    ('2', 'User'),
    ('3', 'Manager'),
)

GENDER_LIST = (
                ('M', 'Male'),
                ('F', 'Female')
            )

GOVERNORATES_LIST = (
                ('AN', 'الانبار'),
                ('BB', 'بابل'),
                ('BG', 'بغداد'),
                ('BA', 'البصرة'),
                ('DQ', 'ذي قار'),
                ('QA', 'القادسية'),
                ('DI', 'ديالى'),
                ('DA', 'دهوك'),
                ('AR', 'اربيل'),
                ('KA', 'كربلاء'),
                ('KI', 'كركوك'),
                ('MA', 'ميسان'),
                ('MU', 'مثنى'),
                ('NA', 'النجف'),
                ('NI', 'نينوى'),
                ('SD', 'صلاح الدين'),
                ('SU', 'السليمانية'),
                ('WA', 'واسط')
            )

SPECIALTY_LIST = (
                ('MD', 'طبية'),
                ('ENG', 'هندسية'),
                ('SCI', 'العلوم'),
                ('FE', 'كلية التربية'),
                ('IN', 'معهد'),
                ('S', 'طالب اعدادية'),
                ('OTH', 'اخرى')
                )

EDUCATION_LIST = (
                ('IS', 'متوسطة'),
                ('HS', 'اعدادية'),
                ('DIP', 'دبلوم'),
                ('BAC', 'بكلوريوس'),
                ('MD', 'ماجستير'),
                ('DOC', 'دكتوراه'),
                ('OTH', 'اخرى'),
            )

AGE_LIST = tuple((str(age), str(age)) for age in range(10, 90))

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender = models.CharField(max_length=1, choices=GENDER_LIST, blank=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField('User Type', max_length=1, choices=USER_TYPE, default='2')
    imagePro = models.ImageField(upload_to='profile/', default='profile/default.png')
    specialty = models.CharField(max_length=3, choices=SPECIALTY_LIST, blank=False, null=True)
    education = models.CharField(max_length=3, choices=EDUCATION_LIST, blank=False, null=True)
    phoneNo = models.CharField(max_length=11, blank=False, null=True, validators=[validate_phone], help_text='077 or 078 or 075')
    birthday = models.DateField(null=True)
    age = models.CharField(max_length=2, blank=True, null=True)
    governorates = models.CharField(max_length=2, choices=GOVERNORATES_LIST, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=False)

    def __str__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        self.age = calculate_age(self.birthday)
        super(UserProfile, self).save(*args, **kwargs)



# Save created UserProfile with User
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)