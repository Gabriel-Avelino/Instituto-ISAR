from django.contrib.auth.models import User
from django.db import models
import uuid 
from unicodedata import normalize

# Create your models here.
def uploadFotoImovel(instance, filename):
    return 'imoveis/{}-{}'.format(str(uuid.uuid4()), filename)

class Tipo_Doc(models.Model):
    name = models.CharField(max_length=256, unique=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tipos docs'

class Documento (models.Model):
    name_doc = models.CharField(max_length=255)
    tipo = models.ForeignKey(Tipo_Doc, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents')

    def __str__(self):
        return self.name_doc
    
    def save(self, *args, **kwargs):
        self.file.name = normalize('NFKD', self.file.name).encode('ascii', 'ignore').decode('ascii')
        existing_doc = Documento.objects.filter(name_doc=self.name_doc, tipo=self.tipo).first()
        
        if existing_doc:
            existing_doc.file.delete(save=False)  # Delete the old file from disk
            existing_doc.file = self.file  # Update the file with the new one
            existing_doc.tipo = self.tipo  # Update tipo if necessary
            super(Documento, existing_doc).save(*args, **kwargs)  # Save the existing document
        else:
            super(Documento, self).save(*args, **kwargs)

class Tipo(models.Model):
    name = models.CharField(max_length=256, unique=True)
    def __str__(self):
        return self.name
    
class Estado(models.Model):
    name = models.CharField(max_length=2, unique=True)
    def __str__(self):
        return self.name
    
class Cidade(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name
    
class Bairro(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Regiao(models.Model):
    name = models.CharField(max_length=256) 
    def __str__(self):
        return self.name
    
class Imovel(models.Model):
    name = models.CharField(max_length=256)
    foto = models.FileField(upload_to=uploadFotoImovel)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=512)
    numero = models.CharField(max_length=10)
    complemento = models.TextField(blank=True, null=True)
    largura = models.FloatField()
    comprimento = models.FloatField()
    area = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        # Calcula a área antes de salvar
        self.area = self.largura * self.comprimento
        super(Imovel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Imoveis'
    
class ImagemImovel(models.Model):
    file = models.FileField(upload_to= uploadFotoImovel)
    descricao = models.TextField()
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
    class Meta:
        verbose_name_plural = 'Imagens imoveis'