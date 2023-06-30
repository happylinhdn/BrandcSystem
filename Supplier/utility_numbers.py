import re

def detectNumber(input):
    detec_input = (input or '').replace('  ', '')
    nums2 = re.compile(r"[+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d)?[\s]?[kK]?[mM]?")
    match = nums2.search(detec_input)
    if match:
        output = match.group(0)
        return output
    return None

def convert_to_float_withoutException(text_input):
    correct_input = text_input or '-1'
    upper_input = correct_input.upper()#.replace(",",".")
    if upper_input.count(',') >= 2:
        upper_input = upper_input.replace(',','')
    if upper_input.count('.') >= 2:
        upper_input = upper_input.replace('.','')
        
    value = 0
    if 'K' in upper_input:
        upper_input = upper_input.replace(',', '.')
        tempK = upper_input.split("K")
        try:
            value = float(tempK[0]) * 1000
        except:
            print("Can not convert thousands of " + + str(upper_input))
            value = -1
            #raise Exception("The value of follower is not valid: " + str(text_input  or ''))

    elif 'M' in upper_input:
        upper_input = upper_input.replace(',', '.')
        tempK = upper_input.split("M")
        try:
            value = float(tempK[0]) * 1000000
        except:
            print("Can not convert million of " + str(upper_input))
            value = -1
            #raise Exception("The value of follower is not valid: " + str(text_input  or ''))
    else:
        try:
            print("start convert " + str(upper_input))
            value = float(upper_input)
        except:
            print("start convert " + str(upper_input) + ' face error step 1')
            try:
                upper_input = upper_input.replace('.','') #todo: consider In VN 1.000 -> 1000
                upper_input = upper_input.replace(',','') #todo: consider In VN 1,000 -> 1000
                value = float(upper_input)
            except:
                print("start convert " + str(upper_input) + ' face error step 2')
                try:
                    upper_input = detectNumber(upper_input)
                    value = float(upper_input)
                except:
                    print("start convert " + str(upper_input) + ' face error step 3')
                    value = 0
                #raise Exception("The value of follower is not valid: " + str(text_input or ''))
    return value

def convert_to_float(follower_input):
    follower = follower_input or '-1'
    upperFollower = follower.upper()#.replace(",",".")
    if upperFollower.count(',') >= 2:
        upperFollower = upperFollower.replace(',','')
    if upperFollower.count('.') >= 2:
        upperFollower = upperFollower.replace('.','')
        
    value = 0
    if 'K' in upperFollower:
        upperFollower = upperFollower.replace(',', '.')
        tempK = upperFollower.split("K")
        try:
            value = float(tempK[0]) * 1000
        except:
            print("Can not convert follower thousands")
            raise Exception("The value of follower is not valid: " + str(follower_input  or ''))

    elif 'M' in upperFollower:
        upperFollower = upperFollower.replace(',', '.')
        tempK = upperFollower.split("M")
        try:
            value = float(tempK[0]) * 1000000
        except:
            print("Can not convert follower million")
            raise Exception("The value of follower is not valid: " + str(follower_input  or ''))
    else:
        try:
            upperFollower = upperFollower.replace('.','') #todo: consider In VN 1.000 -> 1000
            upperFollower = upperFollower.replace(',','') #todo: consider In VN 1,000 -> 1000
            value = float(upperFollower)
        except:
            try:
                upperFollower = detectNumber(upperFollower)
                value = float(upperFollower)
            except:
                value = 0
                raise Exception("The value of follower is not valid: " + str(follower_input or ''))
    return value


def convert_to_string_number(number):
    if number >= 1000000:
        temp = number/1000000
        return "{0}M".format(round(temp, 2))
    
    if number >= 1000:
        temp = number/1000
        return "{0}K".format(round(temp, 2))
    return "{0}".format(round(number, 2))


