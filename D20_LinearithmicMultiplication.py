'''
10 days ago I used Karatsuba to multiply two numbers. Another possibility is to use Fourier transform.

While convolution in time domain takes O(n²) operations, it can be done in O(n) operations as point-wise multiplication in frequency domain. Conversions between time and frequency take O(n.log(n)) operations which is also the final complexity.

The very same idea is successfully used in computer graphics when you need to apply large 2D kernels on large images.

https://en.wikipedia.org/wiki/Fourier_transform

Discrete Fourier Transform (numpy.fft)
Standard FFTs
fft(a[, n, axis, norm]) Compute the one-dimensional discrete Fourier Transform.
ifft(a[, n, axis, norm])    Compute the one-dimensional inverse discrete Fourier Transform.
fft2(a[, s, axes, norm])    Compute the 2-dimensional discrete Fourier Transform
ifft2(a[, s, axes, norm])   Compute the 2-dimensional inverse discrete Fourier Transform.
fftn(a[, s, axes, norm])    Compute the N-dimensional discrete Fourier Transform.
ifftn(a[, s, axes, norm])   Compute the N-dimensional inverse discrete Fourier Transform.

'''
import numpy as np

def mult(x, y):
    nx, ny = len(x), len(y)
    # auxiliary x
    fx = np.zeros(nx + ny, dtype=np.float64)
    fx[:nx] = list(map(int, reversed(x)))
    # auxiliary y
    fy = np.zeros(nx + ny, np.float64)
    fy[:ny] += list(map(int, reversed(y)))
    # convolution via FFT
    fx = np.fft.fft(fx)
    fy = np.fft.fft(fy)
    z = np.fft.ifft(fx * fy).real.round().astype(int)
    # carry over
    for i in range(nx + ny - 1):
        z[i + 1] += z[i] // 10
        z[i] %= 10
    return ''.join(map(str, reversed(z)))


print(mult('987324', '23487'))






