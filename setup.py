from setuptools import setup, find_packages

dev_requires = ['flake8', 'nose']
install_requires = ['requests>=2.2']

setup(
    author = "Grahame Bowland",
    author_email = "grahame@angrygoats.net",
    description = "Possible dates for an Australian federal election or by-election.",
    long_description = "Given a date, list all possible dates for an Australian federal election or by-election.",
    license = "GPL3",
    keywords = "aph auspol",
    url = "https://github.com/grahame/pollingdays",
    name = "pollingdays",
    version = "0.0.1",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    extras_require = {
        'dev': dev_requires
    },
    install_requires = install_requires,
    entry_points = {
        'console_scripts': [
            'pollingdays = pollingdays.cli:main',
        ],
    }
)
