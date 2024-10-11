from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Djiadji DIAW',
    author_email='diawdjiadji.94@gmail.com',
    install_required=['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
)