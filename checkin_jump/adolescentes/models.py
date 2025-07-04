from django.db import models

class PequenoGrupo(models.Model):
    nome = models.CharField(max_length=100)
    lider = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

class Imperio(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Adolescente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    data_nascimento = models.DateField()
    GENERO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True, null=False)
    pg = models.ForeignKey(PequenoGrupo, on_delete=models.SET_NULL, blank=True, null=True, related_name='adolescentes')
    imperio = models.ForeignKey(Imperio, on_delete=models.SET_NULL, null=True, blank=True)
    data_inicio = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
    def ultimas_presencas(self):
        return self.presenca_set.order_by('-dia__data')[:5]

class DiaEvento(models.Model):
    data = models.DateField(unique=True)

    def __str__(self):
        return self.data.strftime('%d/%m/%Y')

class Presenca(models.Model):
    adolescente = models.ForeignKey(Adolescente, on_delete=models.CASCADE)
    dia = models.ForeignKey(DiaEvento, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)
