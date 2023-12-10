from text_to_array import textfile_to_farray
import numpy as np
import statistics


def central_tendency(data):
    result = {
        'N': len(data),
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': statistics.multimode(data)
    }
    return result


def percentile(data, p):
    if p < 0 and p > 100:
        raise Exception
    n = len(data)
    k = (n + 1) * (p / 100)
    i = int(k)
    d = k - float(i)
    if d == 0:
        return data[i - 1]
    else:
        r = (data[i] - data[i - 1]) * d
        return data[i - 1] + r


def measure_of_location(data, *args):
    data.sort()
    result = {
        'min': data[0],
        'max': data[-1],
        'Q1': percentile(data, 25),
        'Q2': percentile(data, 50),
        'Q3': percentile(data, 75)
    }
    for k in args:
        p = int(k[1:])
        if k[0].upper() == 'P':
            result[k] = percentile(data, p)
        elif k[0].upper() == 'D' and (p > 0 and p < 10):
            p *= 10
            result[k] = percentile(data, p)
        else:
            raise Exception
    return result


def measure_of_dispersion(data):
    data.sort()
    result = {
        'range': data[-1] - data[0],
        'IQR': percentile(data, 75) - percentile(data, 25),
        'sample variance': np.var(data, ddof=1),
        'population variance': np.var(data)
    }
    result['sample standard deviation'] = np.sqrt(result['sample variance'])
    result['population standard deviation'] = np.sqrt(
        result['population variance'])
    result['cofficient of variation'] = (
        result['sample standard deviation'] / np.mean(data)) * 100
    return result


def skew(data):
    result = {'sk1': {}}
    modes = statistics.multimode(data)
    stddev = np.sqrt(np.var(data, ddof=1))
    mean = np.mean(data)

    for mode in modes:
        result['sk1'][mode] = (mean - mode) / stddev

    result['sk2'] = (3 * (mean - np.median(data))) / stddev
    return result


def kurt(data):
    mean = np.mean(data)
    N = len(data)
    result = {}
    m2 = (N * np.sum(data ** 2) - np.sum(data) ** 2) / N ** 2
    m4 = (np.sum(data ** 4) / N) - 4 * mean * (np.sum(data ** 3) / N) + \
        6 * mean ** 2 * (np.sum(data ** 2) / N) - 3 * mean ** 4
    result['kurt1'] = m4 / m2 ** 2
    result['kurt2'] = (((N + 1) * (N - 1)) / ((N - 2) * (N - 3))) * \
        (result['kurt1'] - ((3 * (N - 1) / (N + 1))))
    return result


def population_moment(data):
    result = {}
    mean = np.mean(data)
    stddev = np.sqrt(np.var(data))
    N = len(data)
    sum2 = np.sum((data - mean) ** 2)
    sum3 = np.sum((data - mean) ** 3)
    sum4 = np.sum((data - mean) ** 4)

    result['raw'] = {
        'm1': mean,
        'm2': np.sum(data ** 2) / N,
        'm3': np.sum(data ** 3) / N,
        'm4': np.sum(data ** 4) / N
    }
    result['central'] = {
        'm2': sum2 / N,
        'm3': sum3 / N,
        'm4': sum4 / N
    }
    result['standard'] = {
        'm2': result['central']['m2'],
        'm3': (1 / N) * (sum3 / stddev ** 3),
        'm4': (1 / N) * (sum4 / stddev ** 4)
    }
    # (m2) Second standardised moment
    result['var'] = result['standard']['m2']
    # (m3) Third standardised moment
    result['skew'] = result['standard']['m3']
    # (m4) Fourth standardised moment
    result['kurt'] = result['standard']['m4']
    return result


def sample_moment(data):
    mean = np.mean(data)
    stddev = np.sqrt(np.var(data, ddof=1))
    N = len(data)
    result = population_moment(data)

    left = ((N * (N + 1)) / ((N - 1) * (N - 2) * (N - 3)))
    central = (np.sum((data - mean) ** 4) / stddev ** 4)
    right = (3 * (N - 1) ** 2) / ((N - 2) * (N - 3))

    result['standard'] = {
        'm2': np.sum(data ** 2 - mean) / (N - 1),
        'm3': (N / ((N - 1) * (N - 2))) * (np.sum((data - mean) ** 3) / stddev ** 3),
        'm4': left * central - right
    }
    # (m2) Second centralised moment
    result['var'] = result['standard']['m2']
    # (m3) Third standardised moment
    result['skew'] = result['standard']['m3']
    # (m4) Fourth standardised moment
    result['kurt'] = result['standard']['m4']
    return result
