"""Usage: pip install ."""

import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
if sys.version_info < (3, 5):
    raise 'must use Python version 3.5 or higher'

README = r"""Z2Pack is a tool that computes topological invariants and illustrates non-trivial features of Berry curvature. It works as a post-processing tool with all major first-principles codes (z2pack.fp), as well as with tight-binding models (z2pack.tb) and explicit Hamiltonian matrices -- such as the ones obtained from a k.p model (z2pack.hm).

It tracks the charge centers of hybrid Wannier functions - as described `here <http://journals.aps.org/prb/abstract/10.1103/PhysRevB.83.235401>`_ - to calculate these topological invariants.

The Wannier charge centers are computed from overlap matrices that are obtained either directly (for tb) or via the Wannier90 code package (fp).

- `Documentation <http://z2pack.ethz.ch/doc>`_
- `Online interface <http://z2pack.ethz.ch/online>`_ (tight-binding only)
"""

with open('./z2pack/__init__.py', 'r') as f:
    MATCH_EXPR = "__version__[^'\"]+(['\"])([^'\"]+)"
    VERSION = re.search(MATCH_EXPR, f.read()).group(2).strip()

EXTRAS = {
    'plot': ['matplotlib'],
    'tb': ['tbmodels>=1.1.1'],
    'doc': ['sphinx', 'sphinx_rtd_theme'],
    'dev': [
        'prospector==1.1.2',
        'pytest>=3.4',
        'pytest-cov',
        'yapf==0.24',
        'pre-commit==1.11.1',
        'pylint==2.1.1',
        'pyyaml',
    ],
}
EXTRAS['dev'] += EXTRAS['plot'] + EXTRAS['tb'] + EXTRAS['doc']

setup(
    name='z2pack',
    version=VERSION,
    url='http://z2pack.ethz.ch',
    author='Dominik Gresch',
    author_email='greschd@gmx.ch',
    description=
    'Automating the computation of topological numbers of band-structures',
    install_requires=[
        'numpy', 'scipy', 'decorator', 'blessings', 'sortedcontainers',
        'msgpack-python', 'fsc.locker', 'fsc.export', 'fsc.formatting',
        'fsc.iohelper'
    ],
    extras_require=EXTRAS,
    long_description=README,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English', 'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'Development Status :: 5 - Production/Stable'
    ],
    license='GPL',
    keywords=[
        'topology', 'topological', 'invariant', 'bandstructure', 'chern', 'z2',
        'solid-state', 'tight-binding'
    ],
    packages=[
        'z2pack', 'z2pack.io', 'z2pack.fp', 'z2pack.volume', 'z2pack.surface',
        'z2pack.line'
    ]
)
