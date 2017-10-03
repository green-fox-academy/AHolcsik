to_19= ['zero','one','two','three','four','five','six','seven','eight','nine',
        'ten', 'eleven', 'twelwe', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen','nineteen']
tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty','ninety']

def number_converter_to_float(number):
    if number < 20:
        for i in range(len(to_19)):
            if i == number:
                return to_19[i]
    elif number < 100:
        two_digit = ''
        for i in range(len(tens)):
            if i == int(str(number)[0]) - 2:
                two_digit += tens[i]
        for j in range(len(to_19)):
            if j == str(number)[1]:
                two_digit += to_19[j]
                print(two_digit)
        return two_digit

    # return str(float(num)) + "dollars"


print(number_converter_to_float(54))
 

