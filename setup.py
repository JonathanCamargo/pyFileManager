from setuptools import setup, find_packages

setup(
    name='pyFileManager',
    version='0.1',
    packages=find_packages(where='src'),  # Specify the 'src' directory
    package_dir={'': 'src'},  # Specify the root package directory    
    author='Jonathan Camargo',
    author_email='jon-cama@uniandes.edu.co',
    description='A (python) file manager',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JonathanCamargo/pyFileManager',
    install_requires=[
        # Add your dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
)