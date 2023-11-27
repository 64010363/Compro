import math as m
import blackbox as bx
import data as dt

Pi = m.pi
eu = m.e

# คลาสฟังก์ชั่นในโปรแกรม
class f:
    def __init__(self, parameter):
        self.parameter = parameter
        self.length = len(parameter)
    # Sin -2
    def sin(self):
        try:
            return m.sin(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Cos -2
    def cos(self):
        try:
            return m.cos(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Tan -2
    def tan(self):
        try:
            if self.parameter[0] % (Pi/2) != 0:
                return m.tan(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
            else:
                return "Out of Domain"
        except:
            return "Out of Domain"
    # Csc -2
    def csc(self):
        try:
            return 1/m.sin(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Sec -2
    def sec(self):
        try:
            return 1/m.cos(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Cot -2
    def cot(self):
        try:
            if self.parameter[0] % (Pi) != 0:
                return 1/m.tan(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
            else:
                return "Out of Domain"
        except:
            return "Out of Domain"
    # Sqrt -1
    def sqrt(self):
        try:
            return m.sqrt(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Nroot -1
    def nroot(self):
        try:
            return self.parameter[0]**(1/self.parameter[1]) if self.length == 2 else "Insert only 2 parameter"
        except:
            return "Out of Domain"
    # Log -1
    def log(self):
        try:
            return m.log(self.parameter[0], self.parameter[1]) if self.length == 2 else "Insert only 2 parameter"
        except:
            return "Out of Domain"
    # ln -1
    def ln(self):
        try:
            return m.log(self.parameter[0], eu) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Sign -1
    def sign(self):
        try:
            return self.parameter[0]/abs(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # EXP -1
    def exp(self):
        try:
            return eu**self.parameter[0] if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arcsin -3
    def arcsin(self):
        try:
            return m.asin(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arccos -3
    def arccos(self):
        try:
            return m.acos(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arctan -3
    def arctan(self):
        try:
            return m.atan(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arccosec -3
    def arccsc(self):
        try:
            return m.asin(1/self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arcsec -3
    def arcsec(self):
        try:
            return m.acos(1/self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arccot -3
    def arccot(self):
        try:
            return m.acos(self.parameter[0]/m.sqrt(1+self.parameter[0]**2)) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Sinh -4
    def sinh(self):
        try:
            return m.sinh(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Cosh -4
    def cosh(self):
        try:
            return m.cosh(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Tanh -4
    def tanh(self):
        try:
            return m.tanh(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Csch -4
    def csch(self):
        try:
            return 1/m.sin(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Sech -4
    def sech(self):
        try:
            return 1/m.cosh(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Coth -4
    def coth(self):
        try:
            return 1/m.tanh(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arcsinh -5
    def arcsinh(self):
        try:
            return m.asinh(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arccosh -5
    def arccosh(self):
        try:
            return m.acosh(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arctanh -5
    def arctanh(self):
        try:
            return m.atanh(self.parameter[0]) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arccsch -5
    def arccsch(self):
        try:
            return m.log((1/self.parameter[0])+m.sqrt((1/self.parameter[0]**2)+1), eu) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arcsech -5
    def arcsech(self):
        try:
            return m.log((1/self.parameter[0])+m.sqrt((1/self.parameter[0]**2)-1), eu) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Arccoth -5
    def arccoth(self):
        try:
            return 0.5*m.log((self.parameter[0]+1)/(self.parameter[0]-1), eu) if self.length == 1 else "Insert only 1 parameter"
        except:
            return "Out of Domain"
    # Mean -6
    def mean(self):
        try:
            return sum(self.parameter)/self.length if self.length > 0 else "Out of Domain"
        except:
            return "Out of Domain"
    # S.D. -6
    def std(self):
        try:
            std = [(self.parameter[i] - (sum(self.parameter)/self.length))**2 for i in range(0, self.length)]
            return m.sqrt(sum(std)/self.length) if self.length > 0 else "Out of Domain"
        except:
            return "Out of Domain"
    # P -6
    def p(self):
        try:
            n = int(self.parameter[0])
            r = int(self.parameter[1])
            return m.factorial(n)/m.factorial(n-r) if self.length == 2 else "Insert only 2 parameter"
        except:
            return "Out of Domain"
    # C -6
    def c(self):
        try:
            n = int(self.parameter[0])
            r = int(self.parameter[1])
            return m.factorial(n)/(m.factorial(n-r)*m.factorial(r)) if self.length == 2 else "Insert only 2 parameter"
        except:
            return "Out of Domain"
    # Mins -6
    def mins(self):
        return min(self.parameter)
    # Max -6
    def maxs(self):
        return max(self.parameter)

# ฟังก์ชั่นเรียกค่าคงที่
def constants(constants):
    cons_set = {'\u03c0':Pi, 'e':eu, 'g':9.81, 'G':6.67*10**-11, "mol":6.022*10**23,'c':3*10**8, "atm":1.0103*10**5, 'h':6.626*10**-34, 'R':8.314}
    try:
        return cons_set[constants]
    except KeyError:
        try:
            return bx.formula(dt.read_constant(constants), "Pemdas")[0]
        except:
            return constants

# ฟังก์ชั่นเรียกฟังก์ชั่น
def function(functions, mode):
    body = functions[0:functions.find('<')].title()
    parameter_pre = functions[functions.find('<')+1:-1]
    if parameter_pre[0] == ',':
        return (f"Function Error : {functions} - Write Number -> {functions} ", False)
    elif parameter_pre[-1] == ',':
        return (f"Function Error : {functions} - {functions} <- Write Number ", False)
    elif ",," in parameter_pre:
        functions_error = functions[0:functions.find(',,')+1]
        return (f"Function Error : {functions} - {functions_error} <- Write Number ", False)
    func_bracket = 1
    parameter_str = ''
    parameter_list = []
    for i in range(0, len(parameter_pre)):
        if parameter_pre[i] == '<':
            func_bracket += 1
        elif parameter_pre[i] == '>':
            func_bracket -= 1
        if parameter_pre[i] != ',' or func_bracket != 1:
            parameter_str += parameter_pre[i]
            if i == len(parameter_pre)-1:
                parameter_ans = bx.formula(parameter_str, mode)
                
                if parameter_ans[1]:
                    parameter_list.append(parameter_ans[0])
                else:
                    return (f"Function Error : {functions} - {parameter_ans[0]} ", False)
        else:
            parameter_ans = bx.formula(parameter_str, mode)
            
            if parameter_ans[1]:
                parameter_list.append(parameter_ans[0])
            else:
                return (f"Function Error : {functions} - {parameter_ans[0]} ", False)
            parameter_str = ""
    try:
        F = f(parameter_list)
        func_dict = {"Sqrt":F.sqrt(), "Nroot":F.nroot(), "Log":F.log(), "Ln":F.ln(), "Sign":F.sign(), "Exp":F.exp(),
                    "Sin":F.sin(), "Cos":F.cos(), "Tan":F.tan(), "Csc":F.csc(), "Sec":F.sec(), "Cot":F.cot(), "Arcsin":F.arcsin(),
                    "Arccos":F.arccos(), "Arctan":F.arctan(), "Arcsec":F.arcsec(), "Arccosec":F.arccsc(), "Arccot":F.arccot(),
                    "Sinh":F.sinh(), "Cosh":F.cosh(), "Tanh":F.tanh(), "Csch":F.csch(), "Coth":F.coth(), "Sech":F.sech(),
                    "Arcsinh":F.arcsinh(), "Arccosh":F.arccosh(), "Arccoth":F.arccoth(), "Arcsech":F.arcsech(), 
                    "Arctanh":F.arctanh(), "Arccsch":F.arccsch(), "Mean":F.mean(), "Std":F.std(), "P":F.p(), 
                    "C":F.c(), "Min":F.mins(), "Max":F.maxs()}
        
        if "Insert only" not in str(func_dict[body]) and "Out of Domain" not in str(func_dict[body]):
            return (float("%.6f" %(func_dict[body])), True)
        else:
            return (f"Function Error : {functions} - {func_dict[body]} ", False)
    except KeyError:
        try:
            value1 = dt.read_function(body, parameter_list)
            if value1[1]:
                value2 = bx.formula(value1[0], mode)
                if value2[1]:
                    return (value2[0], True)
                else:
                    return (f"Function Error : {functions} - {value2[0]} ", False)
            else:
                return (f"Function Error : {functions} - {value1[0]} ", False)
        except:
            return (f"Function Error : {functions} - Not Found ", False)