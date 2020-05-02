from torch.utils.cpp_extension import load
lltm_cuda = load(
    'lltm_cuda', ['lltm_cuda.cpp', 'lltm_cuda_kernel.cu'],
    extra_include_paths=['includes'],
    verbose=True)
help(lltm_cuda)
