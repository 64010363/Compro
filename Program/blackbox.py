import functions as fx
import math as m

ERROR_TYPE = ""

# ฟังก์ชั่นดูประเภท error
def ERROR_CHECKER(ERROR_MSG):
    ERROR = True
    ERROR_SET = ("This equation is Incalculable", "Write Number Here", "Syntax Error", "time(s)")
    for item in ERROR_SET:
        if item in ERROR_MSG:
            ERROR = False
            break
    return ERROR

# ฟังก์ชั่นแฟคทอเรียล
def factorial(fact, base):
    global ERROR_TYPE
    if fact != "":
        if int(str(numbers(fact, base))[str(numbers(fact, base)).find('.')+1:]) == 0 and numbers(fact, base) >= 0:
            fact = numbers(fact, base)
            return 1 if fact in (0,1) else fact*factorial(fact-1, base)
        else:
            ERROR_TYPE = f"{fact} is Negative Factorial at " if numbers(fact, base) < 0 else f"{fact} is Float Factorial at "
            return int("ERROR_WRONG_FACT")
    else:
        ERROR_TYPE = "Write something in front of ! at "
        return int("ERROR_NO_FACT")

# ฟังก์ชั่นค่าสัมบูรณ์
def absulute(sqare, base):
    if sqare[-1] == '|':
        return abs(numbers(sqare[1:-1], base))
    else:
        global ERROR_TYPE
        ERROR_TYPE = f"{sqare} <-(Write:'|') at "

# ฟังก์ชั่นค่าลบ
def negative(neg, base):
    return -1*numbers(neg, base)

# ฟังก์ชั่นองศา
def degree(rad, base):
    return (numbers(rad, base)*m.pi)/180

# ฟังก์ชั่นแปลงตัวเลขหรืออักขระเป็นค่าเลขฐาน
def to_num(digit, base, number):
    global ERROR_TYPE
    if base > 0:
        base_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                     'u', 'v', 'w', 'x', 'y', 'z')
        if digit in base_list[0:base]:
            return int(digit) if ord(digit) in range(48,58) else ord(digit)-87
        else:
            ERROR_TYPE = f"([{number}]{base} -> Base:{base} doesn't has '{digit}') at "
    else:
        ERROR_TYPE = f"Base:{base} is Invalid Base at "

# ฟังก์ชั่นแปลงค่าตัวเลขที่เป็น string เป็น float
def numbers(number, base = 10):
    global ERROR_TYPE
    sums = 0
    end = len(str(number))-1
    number = str(number)
    if number[-1] == '!':
        return factorial(number[0:-1], base)
    if number[-1] == '\u00b0':
        return degree(number[0:-1], base)
    if number[0] == '-':
        return negative(number[1:], base)
    if number[0] == '|':
        return absulute(number, base)
    if number[0] == '[':
        position = 0
        for i in range(0,len(number)):
            if number[i] == '[':
                position += 1
            elif number[i] == ']':
                position -= 1
            if position == 0:
                end = i
                break
            if i == end and position != 0:
                ERROR_TYPE = f"{number}<-(Write ']':{position} more) at "
                return int("ERROR_SQR-bracket")
        return numbers(numbers(number[1:end], int(number[end+1:]) if number[end+1:] != '' else 10), base)
    if base == 10:
        return float(number)
    else:
        point = number.find('.')
        length = len(number)
        if point < 0:
            for i in range(0,length):
                sums += to_num(number[i], base, number)*(base**(length-1-i))
        elif point > 0 and point != length-1:
            for i in range(0,length):
                if i < point:
                    sums += to_num(number[i], base, number)*(base**(point-1-i))
                elif i > point:
                    sums += to_num(number[i], base, number)*(base**(point-i))
        else:
            ERROR_TYPE = f"{number}<-(Write some number here) at "
            return int("ERROR_POINT")
    return float("%.8f" %sums)
    
# ฟังก์ชั่นคิดเลขแบบไม่มีวงเล็บ
class Calculation:
    def __init__(self, equation, mode):
        global ERROR_TYPE
        ERROR_TYPE = "This equation is Incalculable"
        self.equation = equation
        self.number_list = []
        self.operator_list = []
        line = ""
        func_bracket = 0
        sqr_bracket = 0
        try:
            if equation[-1] not in ('+','-','*','/','^','%','&'):
                for i in range(0,len(equation)):
                    if equation[i] == '<':
                        func_bracket += 1
                    elif equation[i] == '>':
                        func_bracket -= 1
                    if equation[i] == '[':
                        sqr_bracket += 1
                    elif equation[i] == ']':
                        sqr_bracket -= 1
                    if equation[i] not in ('+','-','*','/','^','%','&') or func_bracket != 0 or sqr_bracket != 0:
                        line += equation[i]
                        if i == len(equation)-1:
                            if line.find('<') >= 0:
                                if line.find('<') == 0:
                                    ERROR_TYPE = f"Write Function name -> {line} at "
                                    return int("ERROR_NO_FUNC_NAME")
                                elif line[-1] != '>':
                                    ERROR_TYPE = f"{line} <- Delete This at " if line.find('>') > 0 else f"{line} <- Write '>' Here {func_bracket} time(s)"
                                    return int("TRASH_AT_BEHIDE_FUNC")
                                if func_bracket == 0:
                                    func = fx.function(line, mode)
                                    if func[1]:
                                        self.number_list.append(func[0])
                                    else:
                                        ERROR_TYPE = func[0]
                                        return int("ERROR_FUCNCTION")
                                else:
                                    if func_bracket > 0:
                                        ERROR_TYPE = f"{line} <- Write '>' Here {func_bracket} time(s)"
                                    else:
                                        ERROR_TYPE = f"{line} <- Delete '>' {abs(func_bracket)} time(s)"
                                    return int("ERROR_LACK_bracket")
                            elif line != "":
                                self.number_list.append(numbers(fx.constants(line)))
                    else:
                        self.operator_list.append(equation[i])
                        if line.find('<') >= 0:
                            if line.find('<') == 0:
                                ERROR_TYPE = f"Write Function name -> {line} at "
                                return int("ERROR_NO_FUNC_NAME")
                            elif line[-1] != '>':
                                ERROR_TYPE = f"{line} <- Delete This at " if line.find('>') > 0 else f"{line} <- Write '>' Here {func_bracket} time(s)"
                                return int("TRASH_AT_BEHIDE_FUNC")
                            func = fx.function(line, mode)
                            if func[1]:
                                self.number_list.append(func[0])
                            else:
                                ERROR_TYPE = func[0]
                                return int("ERROR_FUCNCTION")
                        elif line != "":
                            self.number_list.append(numbers(fx.constants(line)))
                        else:
                            ERROR_TYPE = f"{equation[0:i]} ?->{equation[i]}<-? {equation[i+1:]} : Syntax Error"
                            return int("ERROR_SYNTAX")
                        line = ""
                self.number_list.append(0)
                self.operator_list.append('+')
                self.length = len(self.number_list)
            else:
                ERROR_TYPE = f"{equation} <- Write Number Here"
                return int("SYNTAX_ERROR")
        except RecursionError:
            ERROR_TYPE = "Value of This Equation is Too Much"
            return int("ERROR_TOO_MUCH")
        except Exception:
            if ERROR_CHECKER(ERROR_TYPE):
                if "Function Error : " not in ERROR_TYPE:
                    ERROR_TYPE += equation
                else:
                    ERROR_TYPE = ERROR_TYPE.strip().replace("- Function Error : ", '-> ')
            return int("ERROR_EXTRACT")

    # ฟังก์ชั่น Pemdas
    def pemdas(self):
        try:
            number_list_pemdas = self.number_list
            operator_list_pemdas = self.operator_list
            # วนลูปทำยกกำลัง
            for i in range(0,self.length-1):
                if operator_list_pemdas[i] == '^':
                    number_list_pemdas[i+1] = number_list_pemdas[i]**number_list_pemdas[i+1]
                    number_list_pemdas[i] = 1
            # วนลูปทำคูณและหาร
            for i in range(0,self.length-1):
                if operator_list_pemdas[i] in ('*','/','^','%','&'):
                    if operator_list_pemdas[i] not in ('/','%','&'):
                        number_list_pemdas[i+1] = number_list_pemdas[i]*number_list_pemdas[i+1]
                        number_list_pemdas[i] = 0
                    else:
                        if operator_list_pemdas[i+1] == '^':
                            operator_list_pemdas[i+1] = operator_list_pemdas[i]
                        # วนลูปทำตัวหาร
                        if operator_list_pemdas[i] == '/':
                            number_list_pemdas[i+1] = number_list_pemdas[i]/number_list_pemdas[i+1]
                            number_list_pemdas[i] = 0
                        elif operator_list_pemdas[i] == '&':
                            number_list_pemdas[i+1] = number_list_pemdas[i]//number_list_pemdas[i+1]
                            number_list_pemdas[i] = 0
                        else:
                            number_list_pemdas[i+1] = number_list_pemdas[i]%number_list_pemdas[i+1]
                            number_list_pemdas[i] = 0
            # วนลูปทำบวกลบ
            for i in range(0,self.length-1):
                if operator_list_pemdas[i] != '-':
                    number_list_pemdas[i+1] = number_list_pemdas[i]+number_list_pemdas[i+1]
                else:
                    if operator_list_pemdas[i+1] != '+':
                        operator_list_pemdas[i+1] = '-'
                    number_list_pemdas[i+1] = number_list_pemdas[i]-number_list_pemdas[i+1]
            return "%.8f" %number_list_pemdas[-2] if number_list_pemdas[-2] >= 0 else "[%.8f]" %number_list_pemdas[-2]
        except ZeroDivisionError:
            global ERROR_TYPE
            ERROR_TYPE = f"Zerodivision at " + self.equation
            return None
        except:
            return None

# ฟังก์ชั่นคิดเลขแบบมีวงเล็บ
def formula(equation, mode):
    if equation == '':
        return ("Write Something", False)
    bracket_list = [equation]
    check_bracket = 0
    try:
        for i in range(0, len(equation)):
            if equation[i] == '(':
                bracket = 0
                temp = ""
                check_bracket += 1
                for j in range(i, len(equation)):
                    temp += equation[j]
                    if equation[j] == '(':
                        bracket += 1
                    elif equation[j] == ')':
                        bracket -= 1
                    if bracket == 0:
                        bracket_list.append(temp)
                        break
            elif equation[i] == ')':
                check_bracket -= 1
        if check_bracket > 0:
            ERROR_bracket = f"{equation} <- Write ')' or Delete '(' at Front {abs(check_bracket)} time(s)"
            return (ERROR_bracket,False)
        elif check_bracket < 0:
            ERROR_bracket = f"{equation[0:i+1]} <- Delete ')' or Write '(' at Front {abs(check_bracket)} time(s)"
            return (ERROR_bracket,False)
        bracket_list.reverse()
        for i in range(0, len(bracket_list)):
            for j in range(i+1, len(bracket_list)):
                if bracket_list[i] in bracket_list[j]:
                    A = Calculation(bracket_list[i][1:-1], mode) if bracket_list[i].find('(') == 0 and bracket_list[i].find(')') > 1 else Calculation(bracket_list[i], mode)
                    ans = {"Pemdas":A.pemdas()}
                    bracket_list[j] = bracket_list[j].replace(bracket_list[i], ans[mode])
        bracket_list.reverse()
        P = Calculation(bracket_list[0], mode)
        res = {"Pemdas":P.pemdas()}
        return (float(res[mode] if res[mode].find('[') < 0 else res[mode][1:-1]), True)
    except Exception:
        return (ERROR_TYPE, False)
