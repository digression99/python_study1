def get_err_details():
    return 2, 'details'

errnum, errdet = get_err_details()

print(errnum, errdet)

errnum, errdet = errdet, errnum

print(errnum, errdet)