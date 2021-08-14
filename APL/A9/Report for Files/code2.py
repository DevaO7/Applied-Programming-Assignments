y = cos(0.86*t)**3
spectrum(y, 4, False, True, 4, 'Without Hamming Window')
spectrum(y, 4, True, True, 4,  'With Hamming Window')
