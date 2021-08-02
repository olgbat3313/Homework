#import pdb; pdb.set_trace()
def validation(function_date):
    def type_data(*args, **kwargs):
        type_of_data = number_of_type
        if type_of_data.isdigit():
            if i == 1:
                type_of_data = int(type_of_data)
            elif i == 2:
                type_of_data = float(type_of_data)
            elif i == 3:
                type_of_data = str(type_of_data)
            elif i == 4:
                type_of_data = tuple(type_of_data)
            elif i == 5:
                type_of_data = list(type_of_data)
            else:
                print('wrong number')
            #i = {1:int(type_of_data), 2:float(type_of_data), 3:str(type_of_data), 4:tuple(type_of_data), 5:list(type_of_data)}
           
        else:
            print('wrong number ')
        function_date(*args, **kwargs)     
        return type_data

number_of_type = input('enter type of data: 1-int, 2-float, 3-str, 4-tuple, 5-list ')

#import pdb; pdb.set_trace()
#@validation
#def function_date(d):