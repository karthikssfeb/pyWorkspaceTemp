import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-karthick",
    version="0.0.5",
    license = 'MIT',
    author="Karthick Shanmuga Rao",
    author_email="karthikssfeb@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karthikssfeb/ExamplePackage",
    project_urls={
        "Bug Tracker": "https://github.com/karthikssfeb/ExamplePackage/issues",
    },
    download_url = 'https://github.com/karthikssfeb/ExamplePackage/archive/v_01.tar.gz',
    keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
    
    install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  
        'Topic :: Software Development :: Build Tools',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)