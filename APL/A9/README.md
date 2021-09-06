# Spectra of Non-periodic Signals
For non-periodic Signals, using just the fft() function wouldn’t get us the desired
results. This is because the DFT Fourier analyses the replication of the -pi to
pi part, which is not the same as the original function. This results in discontinuity, resulting in undesired results. Using Hamming’s window, we correct this
discontinuity to some extent.
