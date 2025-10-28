from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    identificacion = models.CharField(max_length=13, verbose_name='Cedula')
    direccion = models.TextField(verbose_name='Dirección')
    email = models.EmailField(max_length=150, verbose_name='Correo Electrónico')
    fecha_nacimiento = models.DateField(verbose_name='Fecha_de_Nacimiento')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    avatar = models.ImageField(upload_to='avatars', verbose_name='Foto', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae', verbose_name='Currículum Vitae', null=True, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']





class TipoSeguro(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Tipo_de_Seguro')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo_de_Seguro'
        verbose_name_plural = 'Tipos_de_Seguro'
        db_table = 'tipo_seguro'
        ordering = ['id']



class Aseguradora(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre_de_Aseguradora')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Aseguradora'
        verbose_name_plural = 'Aseguradoras'
        db_table = 'aseguradora'
        ordering = ['id']



class PolizaSeguro(models.Model):
    numero_poliza = models.CharField(max_length=50, verbose_name='Número_de_Poliza')
    fecha = models.DateField(verbose_name='Fecha_de_Registro')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    tipo_seguro = models.ForeignKey(TipoSeguro, on_delete=models.CASCADE, verbose_name='Tipo_de_Seguro')
    aseguradora = models.ForeignKey(Aseguradora, on_delete=models.CASCADE, verbose_name='Aseguradora')
    fecha_inicio = models.DateField(verbose_name='Fecha_de_Inicio')
    fecha_fin = models.DateField(verbose_name='Fecha_de_Fin')
    valor_seguro = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor_del_Seguro')
    valor_prima = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor_Prima')
    valor_adicional = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor_Adicional')

    def __str__(self):
        return f"Póliza {self.numero_poliza}"

    class Meta:
        verbose_name = 'Poliza_de_Seguro'
        verbose_name_plural = 'Polizas_de_Seguro'
        db_table = 'poliza_seguro'
        ordering = ['id']




