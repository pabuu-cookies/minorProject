
import core.models
import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('usertype', models.CharField(max_length=20, validators=[core.models.validate_user_type])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu_images/')),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.customuser')),
            ],
            options={
                'db_table': 'user',
            },
            bases=('core.customuser',),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in-progress', 'In-Progress'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
                ('order_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.menuitem')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('rollNo', models.CharField(max_length=10)),
                ('batch', models.CharField(max_length=10)),
                ('semester', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.faculty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.customuser')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.student'),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('semester', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('faculty', models.ManyToManyField(to='core.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pass_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obtained_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('semester', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('exam_type', models.CharField(choices=[('regular', 'Regular'), ('back', 'Back')], max_length=10)),
                ('exam_date', models.DateField()),
                ('marks_updated_at', models.DateTimeField(auto_now_add=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.faculty')),
                ('marks_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.customuser')),
                ('student', models.ForeignKey(null='true', on_delete=django.db.models.deletion.SET_NULL, to='core.student')),
                ('subject', models.ForeignKey(null='true', on_delete=django.db.models.deletion.SET_NULL, to='core.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.customuser')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.teacher'),
        ),
    ]