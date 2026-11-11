from django.db import models

class questiondb(models.Model):
    question = models.CharField(max_length=100)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)

class AnswersubmissionDB(models.Model):
    
    student_name=models.CharField(max_length=100)
    question_id=models.ForeignKey(
        questiondb,
        on_delete=models.CASCADE,
        related_name='submission'
    )
    selected_answer=models.CharField(max_length=20)
    submitted_at=models.DateTimeField(auto_now_add=True)