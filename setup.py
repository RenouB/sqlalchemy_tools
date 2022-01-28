from setuptools import setup

setup(
  name='sqlalchemy_tools',
  version='0.0.1',
  author='Renou Benteau',
  author_email='rebe01@dfki.de',
  packages=['sqlalchemy_tools'],
  description='simple tool to speed up connection to sqlalchemy session',
  install_requires=[
    "certifi==2021.10.8",
    "greenlet==1.1.2",
    "psycopg2-binary==2.9.3",
    "python-dotenv==0.19.2",
    "SQLAlchemy==1.4.31"
    ]
)