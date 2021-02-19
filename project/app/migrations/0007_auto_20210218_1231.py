# Generated by Django 3.0.7 on 2021-02-18 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210218_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=100, verbose_name='Registration Number')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('middle_name', models.CharField(max_length=255, verbose_name='first name')),
                ('surname', models.CharField(max_length=255, verbose_name='first name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email Address')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_type', models.CharField(choices=[('P', 'Part Time'), ('R', 'Regular')], default=None, max_length=10)),
                ('accomodation', models.CharField(blank=True, choices=[('H', 'Hostels'), ('R', 'Rentals')], default=None, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=5)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('YOB', models.IntegerField(choices=[(1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)], default=2021, verbose_name='Year of Birth')),
                ('County', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.County')),
                ('course', models.ForeignKey(blank=True, help_text='COurse taken', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Course')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
                ('tribe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Tribe')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
