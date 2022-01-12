from setuptools import setup, find_packages

setup(
    name='department_app',
    version='1.0',
    author='Artur Ivanichyk',
    author_email='arturfole222@gmail.com',
    url='https://github.com/ArturIvanichyk/epam_winter2021_project',
    install_requires=[
        'Flask==2.0.0',
        'Flask-Migrate==3.0.0',
        'Flask-RESTful==0.3.8',
        'Flask-SQLAlchemy==2.5.1',
    ],
    include_package_data=True,
    zip_safe=False,
    packages=find_packages()
)