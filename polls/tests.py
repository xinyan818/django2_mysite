from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question
# Create your tests here.


class QuestionModelTests(TestCase):

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=23. minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True0)

	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_future_question(self):

		time = time.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.test_was_published_recently_with_future(), False)


def create_question(question_text, days)
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
	def test_no_questions(self):
		response = self.client.get(reverse('polls:index'))