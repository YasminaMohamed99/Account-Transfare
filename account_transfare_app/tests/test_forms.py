from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from account_transfare_app.forms import UploadFileForm


class UploadFileFormTest(TestCase):
    def several_file_type(self, extension, content_type):
        file = SimpleUploadedFile(f"test_file.{extension}", b"file_content", content_type=content_type)
        form_data = {'file': file}
        form = UploadFileForm(files=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_valid(self):
        self.several_file_type("csv", "text/csv")
        self.several_file_type("tsv", "text/tab-separated-values")
        self.several_file_type("xls", "application/vnd.ms-excel")
        self.several_file_type("xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        self.several_file_type("json", "application/json")

    def test_form_with_invalid_file_type(self):
        file = SimpleUploadedFile("test_file.jpg", b"file_content", content_type="image/jpeg")
        form_data = {'file': file}
        form = UploadFileForm(files=form_data)
        self.assertFalse(form.is_valid())

    def test_form_with_no_file(self):
        form = UploadFileForm(files={})
        self.assertFalse(form.is_valid())
