from django.test import TestCase
from .models import Note, Category
from django.urls import reverse
from datetime import datetime
from django.utils import timezone

class NoteModelTest(TestCase):
    def test_string_repr(self):
        note = Note(title="Print documents")
        self.assertEqual(str(note), "Print documents")

    def test_note_content(self):
        note = Note(title="Print documents", text="Print documents regarding year report.", )

        self.assertEqual(note.title, "Print documents")
        self.assertEqual(note.text, "Print documents regarding year report.")

    def text_note_features(self):
        note = Note(reminder="2026-02-02 12:00:00", category="Work")
        self.assertEqual(note.reminder, "2026-02-02 12:00:00")
        self.assertEqual(note.category, "Work")

        note = Note(reminder="2026-02-02 12:00:00", category="Airport")
        self.assertNotEquals(note.category, "Airport")

class NoteViewTest(TestCase):
    def test_mainpage_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_if_template_correct(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'notes/my_notes.html')

class NoteActionsTest(TestCase):
    def test_adding(self):
        cat = Category.objects.create(title='Work')
        reminder_str = timezone.now().strftime('%Y-%m-%dT%H:%M')
        form_data = {
            'title': 'create a test',
            'text': 'create a test',
            'reminder': reminder_str,
            'category': cat.id
        }


        response = self.client.post(reverse('create_note'), data=form_data, follow=True)
        if response.status_code != 302:  # If it didn't redirect, it likely failed validation
            print('aaaaaaaa', response.context['form'].errors)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Note.objects.filter(title='create a test').exists())

    def test_updating(self):
        reminder_str = timezone.now().strftime('%Y-%m-%dT%H:%M')
        cat = Category.objects.create(title='Work')
        note = Note.objects.create(title='create a test', text='create a test',
                                   reminder=reminder_str, category=cat)


        updated_data = {
            'title': 'create 10 test',
            'text': 'create 10 tests for my django project',
            'reminder': reminder_str,
            'category': cat.id
        }

        update_url = reverse('update', args=[note.id])
        response = self.client.post(update_url, data=updated_data, follow=True)

        self.assertEqual(response.status_code, 200)

        note.refresh_from_db()
        self.assertEqual(note.title, updated_data['title'])
        self.assertEqual(note.text, updated_data['text'])

