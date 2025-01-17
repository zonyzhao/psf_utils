from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name = 'psf_utils',
    version = '0.4.0',
    description = 'Cadence PSF file utilities',
    long_description = readme,
    author = "Ken Kundert",
    author_email = 'psf_utils@nurdletech.com',
    url = 'https://psf_utils.readthedocs.io',
    download_url = 'https://github.com/kenkundert/psf_utils/tarball/master',
    license = 'GPLv3+',
    zip_safe = True,
    packages = 'psf_utils'.split(),
    entry_points = {'console_scripts': [
        'list-psf = psf_utils.list:list_signals',
        'plot-psf = psf_utils.plot:plot_signals',
    ]},
    install_requires = 'docopt inform>=1.19 matplotlib numpy ply quantiphy shlib'.split(),
    python_requires = '>=3.6',
    keywords = 'cadence spectre PSF simulation'.split(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering',
    ],
)
