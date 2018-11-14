from setuptools import setup, find_packages

setup(
    name='yafa',
    version="0.0.1",
    packages=find_packages(),
    url='https://github.com/treasureapp/yafa',
    author='Graham Crowell',
    author_email='graham.crowell@gmail.com',
    description='finance portfolio management app',
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # 'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
    ],
    install_requires=[
        "jupyter",
        "pandas",
        "quandl",
        "matplotlib",
        "numpy",
        "seaborn",
        "tox,"
        "pytest"
    ]
    # entry_points='''
    #     [console_scripts]
    #     dqf=dqf.main:main
    # '''
)