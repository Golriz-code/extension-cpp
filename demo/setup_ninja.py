from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name='lltm_cuda',
    ext_modules=[
        CppExtension(
            'lltm_cuda',
            [
                'lltm_cuda.cpp',
            ],
            include_dirs=['/abs/path/to/includes'],
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
