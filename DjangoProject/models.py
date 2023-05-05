# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airline(models.Model):
    airline_name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'airline'


class AirlineStaff(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    airline_name = models.ForeignKey(Airline, models.DO_NOTHING, db_column='airline_name')

    class Meta:
        managed = False
        db_table = 'airline_staff'


class Airplane(models.Model):
    airline_name = models.OneToOneField(Airline, models.DO_NOTHING, db_column='airline_name', primary_key=True)  # The composite primary key (airline_name, airplane_id) found, that is not supported. The first column is selected.
    airplane_id = models.IntegerField()
    seats = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'airplane'
        unique_together = (('airline_name', 'airplane_id'),)


class Airport(models.Model):
    airport_name = models.CharField(primary_key=True, max_length=50)
    airport_city = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'airport'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookingAgent(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    booking_agent_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'booking_agent'


class BookingAgentWorkFor(models.Model):
    email = models.OneToOneField(BookingAgent, models.DO_NOTHING, db_column='email', primary_key=True)  # The composite primary key (email, airline_name) found, that is not supported. The first column is selected.
    airline_name = models.ForeignKey(Airline, models.DO_NOTHING, db_column='airline_name')

    class Meta:
        managed = False
        db_table = 'booking_agent_work_for'
        unique_together = (('email', 'airline_name'),)


class Customer(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    building_number = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    passport_number = models.CharField(max_length=30)
    passport_expiration = models.DateField()
    passport_country = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Flight(models.Model):
    airline_name = models.OneToOneField(Airplane, models.DO_NOTHING, db_column='airline_name', primary_key=True)  # The composite primary key (airline_name, flight_num) found, that is not supported. The first column is selected.
    flight_num = models.IntegerField()
    departure_airport = models.ForeignKey(Airport, models.DO_NOTHING, db_column='departure_airport')
    departure_time = models.DateTimeField()
    arrival_airport = models.ForeignKey(Airport, models.DO_NOTHING, db_column='arrival_airport', related_name='flight_arrival_airport_set')
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=50)
    airplane = models.ForeignKey(Airplane, models.DO_NOTHING, to_field='airplane_id', related_name='flight_airplane_set')

    class Meta:
        managed = False
        db_table = 'flight'
        unique_together = (('airline_name', 'flight_num'),)


class Permission(models.Model):
    username = models.OneToOneField(AirlineStaff, models.DO_NOTHING, db_column='username', primary_key=True)  # The composite primary key (username, permission_type) found, that is not supported. The first column is selected.
    permission_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'permission'
        unique_together = (('username', 'permission_type'),)


class Purchases(models.Model):
    ticket = models.OneToOneField('Ticket', models.DO_NOTHING, primary_key=True)  # The composite primary key (ticket_id, customer_email) found, that is not supported. The first column is selected.
    customer_email = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer_email')
    booking_agent_id = models.IntegerField(blank=True, null=True)
    purchase_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'purchases'
        unique_together = (('ticket', 'customer_email'),)


class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    airline_name = models.ForeignKey(Flight, models.DO_NOTHING, db_column='airline_name')
    flight_num = models.ForeignKey(Flight, models.DO_NOTHING, db_column='flight_num', to_field='flight_num', related_name='ticket_flight_num_set')

    class Meta:
        managed = False
        db_table = 'ticket'
