from solution import *
from text_to_array import text_to_float_array

if __name__ == '__main__':
    data1 = text_to_float_array('./dataset1')

    print(*[f'{k}: {v}' for k, v in central_tendency(data1).items()], sep='\n')
    print(*[f'{k}: {v}' for k, v in measure_of_location(data1).items()], sep='\n')
    print(*[f'{k}: {v}' for k, v in measure_of_dispersion(data1).items()], sep='\n')
    smaple_m = sample_moment(data1)
    print("Skew:", smaple_m['skew'])
    print("Kurt:", smaple_m['kurt'])
