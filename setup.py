#!/usr/bin/env python

from setuptools import setup, find_packages

required = [
    'flax',
    'jax',
    'jaxlib',
    'matplotlib',
    'numpy',
    'optax',
    'scipy',
    'wandb>=0.12.11',
    'termcolor',
    'distrax',
    'tensorflow_probability',
    'gym',
    'argparse-dataclass',
    'tqdm',
    'seaborn',
    'cloudpickle',
    'pandas',
    'jaxutils',
    'dm_control',
    'trajax @ git+https://github.com/lenarttreven/trajax.git',
    'jaxtyping',
    'moviepy'
]

extras = {'dev': ['seaborn', 'control>=0.9.2']}
setup(
    name='opax',
    version='0.0.1',
    packages=find_packages(),
    python_requires='>=3.10',
    include_package_data=True,
    install_requires=required,
    extras_require=extras
    )
