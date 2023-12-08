
def text_to_float_array(path):
    data: str = None
    array = []
    try:
        with open(path, 'r') as file:
            data = file.read()

        number = ''
        for item in data:
            if item.isdigit():
                number += item
            elif (number and item == '.') and (number[-1] != '-' and number[-1] != '.'):
                number += item
            elif not number and item == '-':
                number += item
            elif number and number != '-':
                array.append(float(number))
                number = ''
        
        if number and number != '-':
            print(number)
            array.append(float(number))
        
    except Exception as err:
        print(err)

    return array