# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, verbose_name='First Name', blank=True)),
                ('surname', models.CharField(max_length=200, null=True, verbose_name='Last Name', blank=True)),
                ('nickname', models.CharField(max_length=200, null=True, verbose_name='Nickname', blank=True)),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('assisted', models.BooleanField(default=False, verbose_name='Assisted')),
                ('is_going_to_install', models.BooleanField(default=False, help_text='Are you going to bring a PC for installing it?', verbose_name='Is going to install?')),
                ('additional_info', models.TextField(help_text='i.e. Wath kind of PC are you bringing', null=True, verbose_name='Additional Info', blank=True)),
            ],
            options={
                'verbose_name': 'Attendant',
                'verbose_name_plural': 'Attendants',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'ascii name', db_index=True)),
                ('slug', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('alt_names', models.ManyToManyField(to='cities.AlternativeName')),
            ],
            options={
                'verbose_name': 'Building',
                'verbose_name_plural': 'Buildings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('html', models.TextField()),
            ],
            options={
                'verbose_name': 'Event Info',
                'verbose_name_plural': 'Envent Info (s)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=200, verbose_name='Type', choices=[(b'MOB', 'Mobile'), (b'NOTE', 'Notebook'), (b'NET', 'Netbook'), (b'TAB', 'Tablet'), (b'DES', 'Desktop'), (b'OTH', 'Other')])),
                ('model', models.CharField(max_length=200, null=True, verbose_name='Model', blank=True)),
                ('serial', models.CharField(max_length=200, null=True, verbose_name='Serial', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HardwareManufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Name', blank=True)),
            ],
            options={
                'verbose_name': 'Hardware Manufacturer',
                'verbose_name_plural': 'Hardware Manufacturers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.TextField(help_text='Any information or trouble you found and consider relevant to document', null=True, verbose_name='Notes', blank=True)),
                ('attendant', models.ForeignKey(verbose_name='Attendant', to='manager.Attendant', help_text='The owner of the installed hardware')),
                ('hardware', models.ForeignKey(verbose_name='Hardware', blank=True, to='manager.Hardware', null=True)),
            ],
            options={
                'verbose_name': 'Installation',
                'verbose_name_plural': 'Installations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_coordinator', models.BooleanField(default=False, help_text='The user is the coordinator of the sede?', verbose_name='Is Coordinator')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='Phone', blank=True)),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Address', blank=True)),
                ('assignation', models.CharField(help_text='Assignations given to the user (i.e. Talks, Coffee...)', max_length=200, null=True, verbose_name='Assignation', blank=True)),
                ('additional_info', models.CharField(help_text='Any additional info you consider relevant', max_length=200, null=True, verbose_name='Additional Info', blank=True)),
                ('assisted', models.BooleanField(default=False, verbose_name='Assisted')),
                ('time_availability', models.CharField(help_text='Time gap in which you can help during the event. i.e. "All the event", "Morning", "Afternoon"...', max_length=200, null=True, verbose_name='Time Availability', blank=True)),
            ],
            options={
                'verbose_name': 'Organizer',
                'verbose_name_plural': 'Organizers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Installer',
            fields=[
                ('organizer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='manager.Organizer')),
                ('level', models.CharField(help_text='Linux Knowledge level for an installation', max_length=200, verbose_name='Level', choices=[(b'1', 'Beginner'), (b'2', 'Medium'), (b'3', 'Advanced'), (b'4', 'Super Hacker')])),
            ],
            options={
                'verbose_name': 'Installer',
                'verbose_name_plural': 'Installers',
            },
            bases=('manager.organizer',),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='i.e. Classroom 256', max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('date', models.DateField(help_text='Date of the event', verbose_name='Date')),
                ('city', models.ForeignKey(verbose_name='City', to='cities.City')),
                ('country', models.ForeignKey(verbose_name='Country', to='cities.Country')),
                ('district', models.ForeignKey(verbose_name='District', blank=True, to='cities.District', null=True)),
                ('place', models.ForeignKey(verbose_name='Place', to='manager.Building', help_text='Specific place (building) where the event is taking place')),
                ('state', models.ForeignKey(verbose_name='State', to='cities.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('version', models.CharField(max_length=200, verbose_name='Version')),
                ('type', models.CharField(max_length=200, verbose_name='Type', choices=[(b'OS', 'Operative System'), (b'AP', 'Application'), (b'SU', 'Support and Problem Fixing'), (b'OT', 'Other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TalkProposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=600, verbose_name='Title')),
                ('speakers_email', models.CharField(help_text="Comma separated speaker's emails", max_length=600, verbose_name='Speakers Emails')),
                ('labels', models.CharField(help_text='Comma separated tags. i.e. Linux, Free Software, Debian', max_length=200, verbose_name='Labels')),
                ('abstract', models.TextField(help_text='Short idea of the talk (Two or three sentences)', verbose_name='Abstract')),
                ('long_description', models.TextField(verbose_name='Long Description')),
                ('presentation', models.FileField(help_text='Any material you are going to use for the talk (optional, but recommended)', upload_to=b'talks', null=True, verbose_name='Presentation', blank=True)),
                ('home_image', image_cropping.fields.ImageCropField(help_text='Image that is going to appear in the home page of this web for promoting the talk (optional)', upload_to=b'talks_thumbnails', null=True, verbose_name='Home Page Image', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'home_image', '700x450', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text='The image must be 700x450 px. You can crop it here.', verbose_name='Cropping')),
                ('dummy_talk', models.BooleanField(default=False, verbose_name='Dummy Talk?')),
            ],
            options={
                'verbose_name': 'Talk Proposal',
                'verbose_name_plural': 'Talk Proposals',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('talkproposal_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='manager.TalkProposal')),
            ],
            options={
                'verbose_name': 'Talk',
                'verbose_name_plural': 'Talks',
            },
            bases=('manager.talkproposal',),
        ),
        migrations.CreateModel(
            name='TalkTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name='Start Date')),
                ('end_date', models.DateTimeField(verbose_name='End Date')),
                ('sede', models.ForeignKey(verbose_name=b'Sede', to='manager.Sede')),
            ],
            options={
                'verbose_name': 'Talk Time',
                'verbose_name_plural': 'Talk Times',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TalkType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Talk Type',
                'verbose_name_plural': 'Talk Types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='talktime',
            name='talk_type',
            field=models.ForeignKey(verbose_name='Talk Type', to='manager.TalkType', help_text='The type of talk the room is going to be used for.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talkproposal',
            name='sede',
            field=models.ForeignKey(verbose_name=b'Sede', to='manager.Sede', help_text='Sede you are proposing the talk to'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talkproposal',
            name='type',
            field=models.ForeignKey(verbose_name='Type', to='manager.TalkType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='hour',
            field=models.ForeignKey(verbose_name='Hour', to='manager.TalkTime'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='room',
            field=models.ForeignKey(verbose_name='Room', to='manager.Room'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(related_name='speakers', verbose_name='Speakers', to='manager.Organizer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='for_type',
            field=models.ForeignKey(verbose_name='For talk type', to='manager.TalkType', help_text='The type of talk the room is going to be used for.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room',
            name='sede',
            field=models.ForeignKey(verbose_name=b'Sede', to='manager.Sede'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizer',
            name='sede',
            field=models.ForeignKey(verbose_name=b'Sede', to='manager.Sede', help_text='Sede you are going to collaborate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizer',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='installer',
            name='software',
            field=models.ManyToManyField(help_text='Select all the software you can install. Hold Ctrl key to select many', to='manager.Software', null=True, verbose_name='Software', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='installation',
            name='installer',
            field=models.ForeignKey(related_name='installed_by', verbose_name='Installer', blank=True, to='manager.Installer', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='installation',
            name='software',
            field=models.ForeignKey(verbose_name='Software', blank=True, to='manager.Software', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hardware',
            name='manufacturer',
            field=models.ForeignKey(verbose_name='Manufacturer', blank=True, to='manager.HardwareManufacturer', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventinfo',
            name='sede',
            field=models.ForeignKey(verbose_name=b'Sede', to='manager.Sede'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendant',
            name='sede',
            field=models.ForeignKey(verbose_name=b'Sede', to='manager.Sede', help_text='Sede you are going to attend'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='attendant',
            unique_together=set([('email', 'sede')]),
        ),
    ]