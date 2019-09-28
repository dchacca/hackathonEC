from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    edad = models.PositiveSmallIntegerField()
    sex=[('M','Masculino'),('F','Femenino')]
    sexo = models.CharField(max_length=1,choices=sex)

    def __str__(self):
        return '{} {}'.format(self.nombres,self.apellidos)

    class Meta:
        #Sdb_table = ''
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
class Denuncia(models.Model):
    dni = models.CharField(max_length=8)
    user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha= models.DateField()
    tipos= [('1','simple'),('2','Agravado')]
    tipo= models.CharField(max_length=1, choices=tipos)
    #objeto = models.CharField(max_length=50)
    descripcion= models.TextField()
    lat= models.DecimalField(max_digits=10, decimal_places=8)
    long= models.DecimalField(max_digits=10, decimal_places=8)
    estados=[('1','Pend. Verificacion'),('2','Aceptada'),('3','Rechazada')]
    estado= models.CharField(max_length=1,choices=estados)


    def __str__(self):
        return '{0}-{1}'.format(self.tipo,self.dni)
       

    class Meta:
        #db_table = ''
        managed = True
        verbose_name = 'Denuncia'
        verbose_name_plural = 'Denuncias'



class Comisaria(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True)
    long = models.DecimalField(max_digits=10, decimal_places=8, blank=True)
    
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        #db_table = ''
        managed = True
        verbose_name = 'Comisaria'
        verbose_name_plural = 'Comisarias'