from django.db import models
from django.db.models import UniqueConstraint

class DimStudents(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)

    def __str__(self):
        return self.student_id

class DimSubjects(models.Model):
    subject_id = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.subject_id

class FactScores(models.Model):
    score_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(DimStudents, on_delete=models.CASCADE)
    subject = models.ForeignKey(DimSubjects, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['student_id', 'subject_id'], name='unique_student_subject')
        ]

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.score}'
