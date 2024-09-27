#!/usr/bin/env python

from setuptools import setup, find_packages

required = [
    'flax',
    'jax',
    'jaxlib',
    'matplotlib>=3.5.1',
    'numpy==1.24.2',
    'optax',
    'scipy',
    'wandb>=0.12.11',
    'termcolor>=1.1.0',
    'distrax==0.1.2',
    'tensorflow_probability',
    'gym',
    'argparse-dataclass>=0.2.1',
    'tqdm',
    'seaborn',
    'cloudpickle',
    'pandas',
    'jaxutils==0.0.8',
    'dm_control==1.0.10',
    'trajax @ git+https://github.com/lenarttreven/trajax.git',
    'jaxtyping~=0.2.28',
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
