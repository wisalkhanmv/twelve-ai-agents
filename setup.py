from setuptools import setup, find_packages

setup(
    name='twelve-ai-agents',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'twelve-ai-agents=main:main'
        ]
    },
    author="Muhammad Wisal",
    author_email="muhammadwisalkhanmv@gmail.com",
    description="A library to convert text to Morse code and play it as audio.",
    url="https://github.com/wisalkhanmv/twelve-ai-agents",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",  # Corrected the license classifier
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'numpy',
        'python-dotenv',
        'websockets',
        'fastapi',
        'nltk',
        'tqdm',
        'beautifulsoup4'
    ],
    extras_require={
        'openai': ['openai'],
    },
)
