from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='lltm_cuda',
    ext_modules=[
        CUDAExtension('lltm_cuda', [
            'lltm_cuda.cpp',
            'lltm_cuda_kernel.cu',
        ]),
    ],
    include_dirs=['includes'],
    cmdclass={
        'build_ext': BuildExtension.with_options(use_ninja=False)
    })
