import setuptools 

# setup(name='helloworld',
#       version='0.1',
#       url='https://github.com/SnehSalesken/hello_world.git',
#       author='Sneh Shah',
#       author_email='sneh@salesken.ai',
#       license='MIT',
#       zip_safe=False)

setuptools.setup(
    name="hello_world",
    version="0.0.1",
    author="Sneh SHah",
    author_email="sneh@salesken.ai",
    description="A function that returns 'world'",
    long_description_content_type="text/markdown",
    url="https://github.com/SnehSalesken/hello_world.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)