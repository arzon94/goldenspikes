from django import forms
# from django.conf import settings
from django.http import HttpResponseRedirect
from homepage.models import *
from django_mako_plus import view_function
from formlib import Formless
# import re

@view_function
def process_request(request):
    form = SignupForm(request)
    if(form.is_valid()):
        form.commit()
        return HttpResponseRedirect('/homepage/thanks')

    context = {
        'form': form
    }
    return request.dmp.render('index.html', context)

DIVISION_1_CATEGORY_CHOICES =  (
    ('','-- --'),
    ('Institutional Programs', 'Institutional Programs'),
    ('Community Relations', 'Community Relations'),
    ('Public Service/Advocacy', 'Public Service/Advocacy'),
    ('Special Events', 'Special Events'),
    ('Crisis Management', 'Crisis Management'),
    ('Internal Relations', 'Internal Relations'),
    ('Social Media', 'Social Media'),
)
DIVISION_2_CATEGORY_CHOICES = (
    ('','-- --'),
    ('Publicity and Media Relations', 'Publicity and Media Relations'),
    ('Print Communications', 'Print Communications'),
    ('Press Kits/Media Kits', 'Press Kits/Media Kits'),
    ('Videos', 'Videos'),
    ('Writing', 'Writing'),
    ('Research', 'Research'),
    ('Interactive Communications', 'Interactive Communications'),
    ('Social Media', 'Social Media'),
    ('Photography and Illustrations', 'Photography and Illustrations'),
)

STATUS_CHOICES_1 =  (
    ('Profit', 'A. For Profit Companies'),
    ('Non-Profit', 'B. Government, nonprofit organizations and associations'),
)
STATUS_CHOICES_2 =  (
    ('Internal', 'A. Internal audiences primarily (e.g., employees, agents).'),
    ('External', 'B. External audiences primarily (e.g., consumers).'),
)
STATUS_CHOICES_3 =  (
    ('Photography', 'A. Photography'),
    ('Illustrations', 'B. Illustrations'),
)
STATUS_CHOICES_4 =  (
    ('News', 'A. News writing (brief factual, expository news articles), feature stories (longer articles), news releases and media advisories, speeches and presentations.'),
    ('Editorials', 'B. Editorials/op-ed columns/letters to the editor (opinion pieces), advertorials (paid advertising written as editorial matter).'),
)
DIVISION_CHOICES =  (
    ('','-- --'),
    ('d1', 'Division 1 - Campaigns'),
    ('d2', 'Division 2 - Tactics'),
)
class SignupForm(Formless):
    def init(self):
        self.fields['entryTitle'] = forms.CharField(label='Entry Title')
        self.fields['client'] = forms.CharField(label='Name of Organization')
        self.fields['division'] = forms.ChoiceField(choices=(DIVISION_CHOICES))
        self.fields['d1category'] = forms.ChoiceField(required=False, label='Division 1 Category',choices=(DIVISION_1_CATEGORY_CHOICES), widget=forms.Select(attrs={'class': 'category cat1'}))
        self.fields['d2category'] = forms.ChoiceField(required=False, label='Division 2 Category',choices=(DIVISION_2_CATEGORY_CHOICES), widget=forms.Select(attrs={'class': 'category cat2'}))
        self.fields['1status'] = forms.ChoiceField(label='Status', choices=(STATUS_CHOICES_1), widget=forms.Select(attrs={'class': 'status 1status'}))
        self.fields['2status'] = forms.ChoiceField(label='Status', choices=(STATUS_CHOICES_2), widget=forms.Select(attrs={'class': 'status 2status'}))
        self.fields['3status'] = forms.ChoiceField(label='Status', choices=(STATUS_CHOICES_3), widget=forms.Select(attrs={'class': 'status 3status'}))
        self.fields['4status'] = forms.ChoiceField(label='Status', choices=(STATUS_CHOICES_4), widget=forms.Select(attrs={'class': 'status 4status'}))
        self.fields['name'] = forms.CharField(label='Name of Person Submitting Entry')
        self.fields['email'] = forms.EmailField(label="Email of person submitting entry")
        self.fields['entryForm'] = forms.FileField( label='Please upload your completed entry form')
        self.fields['summary'] = forms.FileField( label='Please upload your summary (Two pages for Campaigns; One page for Tactics)')
        self.fields['file1'] = forms.FileField(required=False, label='(Additional supporting materials)')
        self.fields['file2'] = forms.FileField(required=False, label='(Additional supporting materials)')
        self.fields['file3'] = forms.FileField(required=False, label='(Additional supporting materials)')
        self.fields['link1'] = forms.URLField(required=False, label='Provide any link to videos, podcasts, websites, etc. to go with your entry.')
        self.fields['link2'] = forms.URLField(required=False, label='Additional Link')
        self.fields['link3'] = forms.URLField(required=False, label='Additional Link')

    def clean(self):
        if(self.cleaned_data.get('division') == 'd1'):
            if not self.cleaned_data.get('d1category'):
                raise forms.ValidationError('You must choose a category from the division you selected.')
        elif(self.cleaned_data.get('division') == 'd2'):
            if not self.cleaned_data.get('d2category'):
                raise forms.ValidationError('You must choose a category from the division you selected.')
        elif(self.cleaned_data.get('division') == '-- --'):
            raise forms.ValidationError('You must choose a division')
        if(self.cleaned_data.get('d1category') == '-- --'):
            raise forms.ValidationError('You must choose a division')
        if(self.cleaned_data.get('d2category') == '-- --'):
            raise forms.ValidationError('You must choose a division')

        return self.cleaned_data

    def commit(self):
        u = Submission()
        u.entryTitle = self.cleaned_data.get('entryTitle')
        u.client = self.cleaned_data.get('client')
        u.division = self.cleaned_data.get('division')
        if(self.cleaned_data.get('division') == 'd1'):
            u.category = self.cleaned_data.get('d1category')
            u.status = self.cleaned_data.get('1status')
        elif(self.cleaned_data.get('division') == 'd2'):
            u.category = self.cleaned_data.get('d2category')
            category = self.cleaned_data.get('d2category')
            if((category == 'Publicity and Media Relations') or (category == 'Print Communications') or (category =='Research') or (category=='Social Media')):
                u.status = self.cleaned_data.get('1status')
            elif(category=='Videos' or category == 'Interactive Communications'):
                u.status = self.cleaned_data.get('2status')
            elif(category=='Photography and Illustrations'):
                u.status = self.cleaned_data.get('3status')
            elif(category=='Writing'):
                u.status = self.cleaned_data.get('4status')
        u.name = self.cleaned_data.get('name')
        u.email = self.cleaned_data.get('email')
        u.entryForm = self.cleaned_data.get('entryForm')
        u.summary = self.cleaned_data.get('summary')
        if(self.cleaned_data.get('file1') is not None):
            u.file1 = self.cleaned_data.get('file1')
        if(self.cleaned_data.get('file2') is not None):
            u.file2 = self.cleaned_data.get('file2')
        if(self.cleaned_data.get('file3') is not None):
            u.file3 = self.cleaned_data.get('file3')
        if(self.cleaned_data.get('link1') is not None):
            u.link1 = self.cleaned_data.get('link1')
        if(self.cleaned_data.get('link2') is not None):
            u.link2 = self.cleaned_data.get('link2')
        if(self.cleaned_data.get('link3') is not None):
            u.link3 = self.cleaned_data.get('link3')
        u.save()
