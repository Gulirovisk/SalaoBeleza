from django.db import models


class Profissional (models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Profissional")
    especialidade = models.CharField(max_length=100, verbose_name="Especialidade")
    descricao = models.TextField(max_length=255, verbose_name="Descrição do Profissional", blank=True, null=True)
    telefone_whatsapp = models.CharField(max_length=16, verbose_name="WhatsApp", unique=True)
    foto = models.ImageField(upload_to='profissionais', verbose_name="Foto do Profissional", blank=True, null=True)

    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"

    def save(self, *args, **kwargs):
        self.telefone_whatsapp = self.telefone_whatsapp.replace("(", "")
        self.telefone_whatsapp = self.telefone_whatsapp.replace(")", "")
        self.telefone_whatsapp = self.telefone_whatsapp.replace("-", "")
        self.telefone_whatsapp = self.telefone_whatsapp.replace(" ", "")
        self.telefone_whatsapp = self.telefone_whatsapp.replace("+", "")
        super(Profissional, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.telefone_whatsapp}"
    
class Servico (models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Serviço")
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, verbose_name="Profissional")
    descricao = models.TextField(max_length=255, verbose_name="Descrição do Serviço", blank=True, null=True)
    horario_inicio = models.TimeField(max_length=100, verbose_name="Horário início de Atendimento", blank=True, null=True)
    horario_fim = models.TimeField(max_length=100, verbose_name="Horário término de Atendimento", blank=True, null=True)
    imagem = models.ImageField(upload_to='servicos', verbose_name="Imagem do Serviço", blank=True, null=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return f"{self.nome} - ({self.profissional.nome})"
    
class Galeria (models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Imagem", blank=True, null=True)
    imagem = models.ImageField(upload_to='galerias', verbose_name="Imagem da Galeria")

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"

    def __str__(self):
        return f"{self.nome}"