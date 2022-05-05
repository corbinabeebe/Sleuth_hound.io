
from http import HTTPStatus

from django.test import TestCase
from sleuthApp.forms import TaskForm
from sleuthApp.models import Project

# Create your tests here.
class TaskFormTests(TestCase):
    """Tests for tasks"""
    def test_subject_starting_lowercase(self):
        """Test to ensure title does not start with lowercase"""
        form = TaskForm(data={"task_subject": "a lowercase subject"})

        self.assertEqual(
            form.errors["task_subject"], ["Should start with an uppercase letter"]
        )
    def test_title_ending_in_full_stop(self):
        """tests to ensure title doesnt end with a period"""
        form = TaskForm(data={"task_subject": "A stopped subject."})

        self.assertEqual(
            form.errors["task_subject"], ["Should not end with a ."]
        )

    def test_title_with_ampersand(self):
        """Tests to ensure title doesnt have an ampersand"""
        form = TaskForm(data={"task_subject": "This is a task subject with an &"})

        self.assertEqual(
            form.errors["task_subject"], ["Use 'and' instead of '&'"]
        )

class TaskViewTests(TestCase):
    """Test the task view"""

    project = Project(id=1, title="Test project",
                      description="Test description")

    def test_get(self):
        '''Tests the creation of a task'''
        project = Project(id=1, title="Test project",
                          description="Test description")
        response = self.client.get(f'/project/{project.id}/create_task')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1>Task Form</h1>", html=True)

    def test_post_success(self):
        """Testing post success"""
        project = Project(id=1, title="Test project",
                          description="Test description")
        response = self.client.post(f'/project/{project.id}/create_task', data={""})

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], f"/sleuth/project/{project.id}")
    
    def test_post_error(self):
        """Test post error"""
        project = Project(id=1, title="Test project",
                          description="Test description")
        response = self.client.post(
            f'/project/{project.id}/create_task', data={"task_subject":"This is a test task subject & its great"})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Use 'and' instead of '&'", html=True)
