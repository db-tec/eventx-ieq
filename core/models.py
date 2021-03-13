from django.db import models
from stdimage import StdImageField

# Signals
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateTimeField('Data de Criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Evento(Base):    
    nome = models.CharField('Evento', max_length=100)
    descricao = models.TextField('Descrição do Evento', null=True, blank=True)
    data_inicial = models.DateTimeField('Entrada', auto_now_add=False)
    data_final = models.DateTimeField('Saída',auto_now_add=False, null=True)
    local = models.CharField('Endereço', max_length=100)
    quantidade = models.IntegerField('Quantidade')
    imagem = StdImageField('Imagem', upload_to='eventos', variations={'thumb': (600, 338)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    

    def __str__(self):
        return self.nome

class Inscricao(Base):
    nome = models.CharField('Nome',max_length=100 )
    sobrenome = models.CharField('Sobrenome', max_length=100)
    telefone = models.CharField('Telefone', max_length=16, null=True, blank=True)
    email = models.EmailField('Email', max_length=100, unique=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.sobrenome} - {self.telefone} - {self.email} - {self.evento}'

def evento_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(evento_pre_save, sender=Evento)