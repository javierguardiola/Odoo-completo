# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api

# add base class
class Base(models.Model):
    _name = 'prueba.base'
    _description = 'Base class to be inherited'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         'El nombre debe ser único'),
    ]

# add a student models
class Student(models.Model):
    _name = 'prueba.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)

# add a teacher models
class Teacher(models.Model):
    _name = 'prueba.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)

# add a course models
class Course(models.Model):
    _name = 'prueba.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    teacher_id = fields.Many2one('prueba.teacher', string='Teacher')
    student_id = fields.Many2many('prueba.student', string='Students')

# add asignature models
class Asignature(models.Model):
    _name = 'prueba.asignature'
    _description = 'Asignature'

    name = fields.Char(string='Name', required=True)
    exam = fields.Date(string='Exam', required=True)
    course_id = fields.Many2one('prueba.course', string='Course')
    teacher_id = fields.Many2one('prueba.teacher', string='Teacher')
    student_id = fields.Many2many('prueba.student', string='Students')


