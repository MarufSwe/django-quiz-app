import pandas as pd
from django.core.management.base import BaseCommand
from quiz.models import Question, Topic  # Replace 'your_app' with the actual app name


class Command(BaseCommand):
    help = 'Import questions from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.stdout.write(self.style.NOTICE(f'Reading data from {file_path}...'))

        # Read Excel file
        try:
            print('Reading Excel file...')
            data = pd.read_excel(file_path, header=None)
            print('Data read successfully:', data.head())  # Print first few rows of data
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading the Excel file: {e}'))
            return

        # Iterate through the rows and create Question objects
        for index, row in data.iterrows():
            try:
                # Assuming columns are in the following order: topic, question_text, option_a, option_b, option_c, option_d, correct_answer
                topic_name = row[0]
                question_text = row[1]
                option_a = row[2]
                option_b = row[3]
                option_c = row[4]
                option_d = row[5]
                correct_answer = row[6].strip().upper()  # Ensure correct_answer is in uppercase

                # Fetch or create the Topic object
                topic, created = Topic.objects.get_or_create(name=topic_name)

                # Create Question object
                question = Question.objects.create(
                    topic=topic,
                    question_text=question_text,
                    option_a=option_a,
                    option_b=option_b,
                    option_c=option_c,
                    option_d=option_d,
                    correct_answer=correct_answer
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully imported question: {question.question_text}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error importing row {index + 1}: {e}'))

        self.stdout.write(self.style.SUCCESS('Successfully imported all data'))

# For running the script
# python manage.py import_questions "D:\projects\quiz questions\python_questions.xlsx"
