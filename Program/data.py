import os
import blackbox as bx
import datetime as date

function_set = ("Sqrt", "Nroot", "Log", "Ln", "Sign", "Exp","Sin", "Cos", "Tan", "Csc", "Sec", "Cot", "Arcsin",
                "Arccos", "Arctan", "Arcsec", "Arccosec", "Arccot","Sinh", "Cosh", "Tanh", "Csch", "Coth", "Sech",
                "Arcsinh", "Arccosh", "Arccoth", "Arcsech", "Arctanh", "Arccsch", "Mean", "Std", "P", "C", "Min", "Max")
constant_set = ('\u03c0','e','g','G',"mol",'c',"atm",'h','R','K','\u03c1w','Hp','ANS')

# เปลี่ยนตัวอักษรต้องห้ามให้ระบบไฟล์อ่านได้
def to_eng(words):
    if words == '':
        return ('', False)
    words = words.strip()
    translate = ""
    forbid = ('"',',',':',';','<','=','>','?','[',']','|')
    extra_forbid = ('*','+','-','/','%','^',"\\",'', '&','$')
    for word in words:
        if word in extra_forbid:
            return ('', False)
        elif word in forbid or ord(word) > 127:
            translate += '' + '$' + str(ord(word)) + ''
        else:
            translate += word
    if translate[-1] == '':
        translate = translate[0:-1]
    return (translate, True)

# อ่านค่าคงที่ในระบบไฟล์
def read_constant(constants):
    constants = to_eng(constants)[0] + '.txt'
    file = open(f"{os.getcwd()}\\Constant\\{constants}", 'r', encoding='utf-8')
    value = file.readline()
    file.close()
    return value

# อ่านฟังก์ชั่นในระบบไฟล์
def read_function(functions, input_parameter):
    functions = to_eng(functions)[0].title() + '.txt'
    file = open(f"{os.getcwd()}\\Function\\{functions}", 'r', encoding='utf-8')
    length = int(file.readline()[0:-1])
    if length == len(input_parameter):
        input_parameter = [f'({item})' if item >= 0 else f'([{item}])' for item in input_parameter]
        func_parameter = file.readline()[0:-1].split(',')
        equation = file.readline()
        for i in range(0,length):
            equation = equation.replace(func_parameter[i],input_parameter[i])
        file.close()
        return (equation, True)
    else:
        return (f"Insert only {length} parameter", False)

# เขียนค่าคงที่ในไฟล์
def write_constant(constants):
    if constants.find('=') > 0:
        constant_list = constants.split('=')
        if len(constant_list) == 2:
            if to_eng(constant_list[0])[1]:
                body = to_eng(constant_list[0])[0] + '.txt'
                value = constant_list[1].replace(' ', '')
                if value == "":
                    return f"{constants} <- Write Something"
                elif value in constant_set:
                    return f"This Constant is Built-In One"
                elif bx.formula(value, "Pemdas")[1]:
                    file = open(f"{os.getcwd()}\\Constant\\{body}", 'w', encoding='utf-8')
                    file.write(value)
                    file.close()
                    return "Write Complete !!!"
                else:
                    read_error = bx.formula(value, "Pemdas")[0]
                    return f"Function Write Error -> {read_error}"
            else:
                return "Contain special charactor(s)"
        else:
            return "Must Insert '=' only one"
    elif constants.find('=') == 0:
        return f"Write Something -> {constants}"
    else:
        return "Insert '=' at least one"

# เขียนฟังก์ชั่นในไฟล์
def write_function(functions):
    if functions.find('=') > 0 and functions[-1] != '=':
        function_list = functions.split('=')
        if len(function_list) == 2:
            if to_eng(function_list[0])[1]:
                value = function_list[1]
                body = function_list[0]
                if body.find('<') > 0 and body[-1] == '>':
                    main = to_eng(body[0:body.find('<')])[0].title()
                    if main not in function_set:
                        parameter = body[body.find('<')+1:-1].lower()
                        parameter_length = len(parameter.split(','))
                        for item in parameter.split(','):
                            try:
                                check = float(item)
                                return f"Don't write number({check}) as parameter"
                            except:
                                if item not in value:
                                    return "Please Write Variable that exist in Function"
                        main += '.txt'
                        file = open(f"{os.getcwd()}\\Function\\{main}", 'w', encoding='utf-8')
                        file.write(f"{parameter_length}\n")
                        file.write(f"{parameter}\n")
                        file.write(value)
                        file.close()
                        return "Write Complete !!!"
                    else:
                        return "This Function is Built-In one"
                else:
                    return "Wrong Writing"
            else:
                return "Contain special charactor(s) -> (*, +, -, /, %, ^, \, , &, $)"
        else:
            return "Must Insert '=' only one"
    elif functions.find('=') == len(functions)-1:
        return f"{functions} <- Write Something"
    elif functions.find('=') == 0:
        return f"Write Something -> {functions}"
    else:
        return "Insert '=' at least one"

# ดูไฟล์ history.txt
def history_check(today):
    try:
        reads = open(f'{os.getcwd()}\\Document\\history.txt', 'r', encoding='utf-8')
    except:
        fix = writes = open(f'{os.getcwd()}\\Document\\history.txt', 'w', encoding='utf-8')
        fix.write(f'{today}\n')
        fix.write('0')
        fix.close()
        reads = open(f'{os.getcwd()}\\Document\\history.txt', 'r', encoding='utf-8')
    day = reads.readline()[0:-1]
    if day == today:
        number = int(reads.readline()) + 1
        number = str(number)
        reads.close()
        writes = open(f'{os.getcwd()}\\Document\\history.txt', 'w', encoding='utf-8')
        writes.write(f'{today}\n')
        writes.write(number)
        writes.close()
        return number
    else:
        reads.close()
        writes = open(f'{os.getcwd()}\\Document\\history.txt', 'w', encoding='utf-8')
        writes.write(f'{today}\n')
        writes.write('1')
        writes.close()
        return '1'

# เขียนประวัติการคำนวณ
def write_history(equation, answer):
    name = date.date.today()
    name = str(name).replace('-', '_')
    number = history_check(name)
    name += f'_{number}.txt'
    file = open(f'{os.getcwd()}\\History\\{name}', 'w', encoding='utf-8')
    file.write(f'{answer}\n')
    file.write(f'{answer} = {equation}')
    file.close()

# ลบไฟล์
def delete(filename, location):
    if to_eng(filename)[1]:
        filename = to_eng(filename)[0] + '.txt'
        position = f'{os.getcwd()}\\{location}\\{filename}'
        os.remove(position)
        return 'Deleted !!!'
    else:
        return ''