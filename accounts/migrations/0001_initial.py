# Generated by Django 4.1.7 on 2023-03-12 16:00

import TechdaPlatform.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('type', models.CharField(choices=[('1', 'Administrator'), ('2', 'User'), ('3', 'Manager')], default='2', max_length=1, verbose_name='User Type')),
                ('imagePro', models.ImageField(default='profile/default.png', upload_to='profile/')),
                ('specialty', models.CharField(choices=[('MD', 'طبية'), ('ENG', 'هندسية'), ('SCI', 'العلوم'), ('FE', 'كلية التربية'), ('IN', 'معهد'), ('S', 'طالب اعدادية'), ('OTH', 'اخرى')], max_length=3, null=True)),
                ('education', models.CharField(choices=[('IS', 'متوسطة'), ('HS', 'اعدادية'), ('DIP', 'دبلوم'), ('BAC', 'بكلوريوس'), ('MD', 'ماجستير'), ('DOC', 'دكتوراه'), ('OTH', 'اخرى')], max_length=3, null=True)),
                ('phoneNo', models.CharField(help_text='077 or 078 or 075', max_length=11, null=True, validators=[TechdaPlatform.utils.validate_phone])),
                ('age', models.CharField(choices=[('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'), ('79', '79'), ('80', '80'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89')], max_length=2, null=True)),
                ('governorates', models.CharField(choices=[('AN', 'الانبار'), ('BB', 'بابل'), ('BG', 'بغداد'), ('BA', 'البصرة'), ('DQ', 'ذي قار'), ('QA', 'القادسية'), ('DI', 'ديالى'), ('DA', 'دهوك'), ('AR', 'اربيل'), ('KA', 'كربلاء'), ('KI', 'كركوك'), ('MA', 'ميسان'), ('MU', 'مثنى'), ('NA', 'النجف'), ('NI', 'نينوى'), ('SD', 'صلاح الدين'), ('SU', 'السليمانية'), ('WA', 'واسط')], max_length=2, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
