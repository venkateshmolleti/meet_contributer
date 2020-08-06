from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

ORPHAN_CHOICES = [
    ("Sri Venkateswara Orphanage","Sri Venkateswara Orphanage"),
    ("Goldage Home hospital","Goldage Home hospital"),
    ("St Joseph's Orphanage","St Joseph's Orphanage"),
    ("Amma Nanna Charitable Trust", "Amma Nanna Charitable Trust"),
    ("LO Rural Development Society", "LO Rural Development Society"),
    ("C.H.I.L.D Orphanage", "C.H.I.L.D Orphanage"),
    ("Children of Faith Ministries", "Children of Faith Ministries"),
    ("All. Religions Orphan CH", "All. Religions Orphan CH"),
    ( "Amma Nanna Orphanage", "Amma Nanna Orphanage"),
    ("Induvadhanamma Child WOH", "Induvadhanamma Child WOH"),
    ("Amma Nanna Charitable Trust", "Amma Nanna Charitable Trust"),
    ("Meriba Child Care and CD", "Meriba Child Care and CD"),
    ("Mother Father Charitable Trust", "Mother Father Charitable Trust"),
    ("Amma Nanna Orphan OAH", "Amma Nanna Orphan OAH"),
    ( "Shantidhara Social SS", "Shantidhara Social SS"),
    ("ACT Children Home", "ACT Children Home"),
    ("Flying Kites Orphanage", "Flying Kites Orphanage"),
    ("Grace Children Ministries", "Grace Children Ministries"),
    ( "Goldage Home Hospital & HC", "Goldage Home Hospital & HC"),
    ("Sneha Sandhya Orphanage", "Sneha Sandhya Orphanage"),
    ("Bhavani Old Age Home", "Bhavani Old Age Home"),
    ("Desire Society", "Desire Society"),
    ("Aasra Old Age Home", "Aasra Old Age Home"),
    ("Desire Society", "Desire Society"),
    ("Prema Samajam", "Prema Samajam"),
    ("Seva Saraswati Sadhu", "Seva Saraswati Sadhu"),
    ( "C.H.I.L.D. Orphanage - Co...", "C.H.I.L.D. Orphanage - Co..."),
    ("Orphanage", "Orphanage"),
    ( "Avatar Mehar Baba", "Avatar Mehar Baba"),
    ("Sos Children`s Villages Of India", "Sos Children`s Villages Of India"),
    ("Goldage Hospital", "Goldage Hospital"),
    ("Sri Vasavi Oldage Home", "Sri Vasavi Oldage Home"),
    ( "Induvadhanamma Orphan Home", "Induvadhanamma Orphan Home"),
    ("shanti orphanage","shanti orphanage"),
    ("Act Old age home","Act Old age home")

]
print("fill form")

class Person(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    orpfield= models.CharField(max_length=100,choices=ORPHAN_CHOICES , default='',blank = True)
    quality = models.IntegerField()
    quantity=models.IntegerField()
    noofcloths= models.IntegerField()
    address = models.TextField()
    city=models.CharField(max_length=100, default='',blank = True)
    phoneno = models.IntegerField()
    pincode= models.IntegerField()
