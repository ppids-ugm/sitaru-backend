from django.db import models

# Create your models here.
class Izin(models.Model):
    kode_izin = models.CharField(primary_key=True, max_length=5)
    keterangan_izin = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.kode_izin

    class Meta:
        managed = False
        db_table = 'izin'


class Kegiatan(models.Model):
    kode_tipekegiatan = models.ForeignKey('TipeKegiatan', models.DO_NOTHING, db_column='kode_tipekegiatan')
    id_kegiatan = models.IntegerField(primary_key=True)
    keterangan_kegiatan = models.CharField(max_length=50, blank=True, null=True)
	
    def __str__(self):
        return self.id_kegiatan    
    
    class Meta:
        managed = False
        db_table = 'kegiatan'
        unique_together = (('id_kegiatan', 'kode_tipekegiatan'),)


class PeraturanModel(models.Model):
    kode_tipekegiatan = models.OneToOneField(Kegiatan, models.DO_NOTHING, db_column='kode_tipekegiatan', primary_key=True)
    id_kegiatan = models.IntegerField()
    kode_subzona = models.ForeignKey('SubZona', models.DO_NOTHING, db_column='kode_subzona')
    kode_izin = models.ForeignKey(Izin, models.DO_NOTHING, db_column='kode_izin', blank=True, null=True)

    def __str__(self):
        return self.kode_tipekegiatan        

    class Meta:
        managed = False
        db_table = 'peraturan'
        unique_together = (('kode_tipekegiatan', 'id_kegiatan', 'kode_subzona'),)


class PetaPeraturan(models.Model):
    id = models.BigAutoField(primary_key=True)
    kode_tipekegiatan = models.CharField(max_length=5)
    kode_subzona = models.CharField(max_length=10)
    kode_izin = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'peta_peraturan'


class SubZona(models.Model):
    kode_subzona = models.CharField(primary_key=True, max_length=10)
    keterangan_subzona = models.CharField(max_length=60, blank=True, null=True)
    kode_zona = models.ForeignKey('Zona', models.DO_NOTHING, db_column='kode_zona', blank=True, null=True)

    def __str__(self):
        return self.kode_subzona  

    class Meta:
        managed = False
        db_table = 'sub_zona'


class TipeKegiatan(models.Model):
    kode_tipekegiatan = models.CharField(primary_key=True, max_length=5)
    keterangan_tipekegiatan = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.kode_tipekegiatan  

    class Meta:
        managed = False
        db_table = 'tipe_kegiatan'


class Zona(models.Model):
    kode_zona = models.CharField(primary_key=True, max_length=5)
    keterangan_zona = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.kode_zona  

    class Meta:
        managed = False
        db_table = 'zona'

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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'