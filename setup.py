import pathlib
import setuptools

ROOT = str(pathlib.Path(__file__).parent)
extras = {}

with open(ROOT + '/requirements.txt', encoding='utf-8') as fp:
    extras['install_requires'] = fp.read().splitlines()

with open(ROOT + '/README.md', encoding='utf-8') as fp:
    extras['long_description'] = fp.read().splitlines()


setuptools.setup(
    name='Laocr',
    version='0.1',
    description='An OCR library for manipulating lost ark',
    long_description=extras['long_description'],
    long_description_content_type='text/markdown',
    author='srounet',
    author_email='srounet@gmail.com',
    url='https://github.com/srounet/Laocr/',
    packages=['laocr'],
    license="mit",
    platforms=["windows"],
    keywords='lost ark windows ocr',
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'laocr': 'laocr'},
    include_package_data=True,
    python_requires=">=3, <4",
    install_requires=extras['install_requires'],
    zip_safe=False,
    classifiers=[
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Natural Language :: French',
        'OPERATING SYSTEM :: MICROSOFT :: WINDOWS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
    ],
    project_urls={
        'Documentation': 'https://github.com/srounet/Laocr',
        'Source': 'https://github.com/srounet/Laocr',
    },
)