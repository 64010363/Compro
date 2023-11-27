import tkinter as tk
from tkinter.constants import END
import blackbox as bx
import data 
import search

func_page = 0
cons_page = 0
symb_page = 0
num_page = 0
list_page = 0
data_list = search.all_folder()
data_list += [['','','']]*(12-len(data_list)%12 if len(data_list)%12 != 0 else (0 if len(data_list) > 0 else 12))
max_page = len(data_list)//12
previous_answer = ''

# ปิดหน้าจอ help
def close_help() :
    help_pop.destroy()

# เปิดหน้าจอ help
def help_page() :
    global help_pop
    help_pop = tk.Toplevel(Window)
    help_pop.title("Help")
    help_pop.geometry("250x150+960+540")
    help_pop.resizable(width=False, height=False)
    
    txt = tk.StringVar()
    txt.set(search.open_pdf())
    help_pop_label = tk.Label(help_pop,textvariable=txt)
    help_pop_label.place(x=70,y=30)
    
    help_ok_button = tk.Button(help_pop,text="OK",command=close_help)
    help_ok_button.place(x=110,y=80)

# เเปลี่ยนหน้าช่อง data
def list_datapage(page) :
    number = int(page_number.get()) - 1
    number += page

    if number < 0:
        number = 0
    elif number > max_page-1:
        number = max_page-1
    
    page_number.set(str(number+1))
    setting = 12*number
    
    listbox1_data.set(f'{data_list[setting][0]}\n{data_list[setting][1]}\n{data_list[setting][2]}')
    listbox2_data.set(f'{data_list[setting+1][0]}\n{data_list[setting+1][1]}\n{data_list[setting+1][2]}')
    listbox3_data.set(f'{data_list[setting+2][0]}\n{data_list[setting+2][1]}\n{data_list[setting+2][2]}')
    listbox4_data.set(f'{data_list[setting+3][0]}\n{data_list[setting+3][1]}\n{data_list[setting+3][2]}')
    listbox5_data.set(f'{data_list[setting+4][0]}\n{data_list[setting+4][1]}\n{data_list[setting+4][2]}')
    listbox6_data.set(f'{data_list[setting+5][0]}\n{data_list[setting+5][1]}\n{data_list[setting+5][2]}')
    listbox7_data.set(f'{data_list[setting+6][0]}\n{data_list[setting+6][1]}\n{data_list[setting+6][2]}')
    listbox8_data.set(f'{data_list[setting+7][0]}\n{data_list[setting+7][1]}\n{data_list[setting+7][2]}')
    listbox9_data.set(f'{data_list[setting+8][0]}\n{data_list[setting+8][1]}\n{data_list[setting+8][2]}')
    listbox10_data.set(f'{data_list[setting+9][0]}\n{data_list[setting+9][1]}\n{data_list[setting+9][2]}')
    listbox11_data.set(f'{data_list[setting+10][0]}\n{data_list[setting+10][1]}\n{data_list[setting+10][2]}')
    listbox12_data.set(f'{data_list[setting+11][0]}\n{data_list[setting+11][1]}\n{data_list[setting+11][2]}')

# ไปหน้าแรก
def first_page() :
    page_number.set('1')
    listbox1_data.set(f'{data_list[0][0]}\n{data_list[0][1]}\n{data_list[0][2]}')
    listbox2_data.set(f'{data_list[1][0]}\n{data_list[1][1]}\n{data_list[1][2]}')
    listbox3_data.set(f'{data_list[2][0]}\n{data_list[2][1]}\n{data_list[2][2]}')
    listbox4_data.set(f'{data_list[3][0]}\n{data_list[3][1]}\n{data_list[3][2]}')
    listbox5_data.set(f'{data_list[4][0]}\n{data_list[4][1]}\n{data_list[4][2]}')
    listbox6_data.set(f'{data_list[5][0]}\n{data_list[5][1]}\n{data_list[5][2]}')
    listbox7_data.set(f'{data_list[6][0]}\n{data_list[6][1]}\n{data_list[6][2]}')
    listbox8_data.set(f'{data_list[7][0]}\n{data_list[7][1]}\n{data_list[7][2]}')
    listbox9_data.set(f'{data_list[8][0]}\n{data_list[8][1]}\n{data_list[8][2]}')
    listbox10_data.set(f'{data_list[9][0]}\n{data_list[9][1]}\n{data_list[9][2]}')
    listbox11_data.set(f'{data_list[10][0]}\n{data_list[10][1]}\n{data_list[10][2]}')
    listbox12_data.set(f'{data_list[11][0]}\n{data_list[11][1]}\n{data_list[11][2]}')

# ไปหน้าสุดท้าย
def last_page() :
    page_number.set(str(max_page))
    lastpage = 12*(max_page-1)
    listbox1_data.set(f'{data_list[lastpage][0]}\n{data_list[lastpage][1]}\n{data_list[lastpage][2]}')
    listbox2_data.set(f'{data_list[lastpage+1][0]}\n{data_list[lastpage+1][1]}\n{data_list[lastpage+1][2]}')
    listbox3_data.set(f'{data_list[lastpage+2][0]}\n{data_list[lastpage+2][1]}\n{data_list[lastpage+2][2]}')
    listbox4_data.set(f'{data_list[lastpage+3][0]}\n{data_list[lastpage+3][1]}\n{data_list[lastpage+3][2]}')
    listbox5_data.set(f'{data_list[lastpage+4][0]}\n{data_list[lastpage+4][1]}\n{data_list[lastpage+4][2]}')
    listbox6_data.set(f'{data_list[lastpage+5][0]}\n{data_list[lastpage+5][1]}\n{data_list[lastpage+5][2]}')
    listbox7_data.set(f'{data_list[lastpage+6][0]}\n{data_list[lastpage+6][1]}\n{data_list[lastpage+6][2]}')
    listbox8_data.set(f'{data_list[lastpage+7][0]}\n{data_list[lastpage+7][1]}\n{data_list[lastpage+7][2]}')
    listbox9_data.set(f'{data_list[lastpage+8][0]}\n{data_list[lastpage+8][1]}\n{data_list[lastpage+8][2]}')
    listbox10_data.set(f'{data_list[lastpage+9][0]}\n{data_list[lastpage+9][1]}\n{data_list[lastpage+9][2]}')
    listbox11_data.set(f'{data_list[lastpage+10][0]}\n{data_list[lastpage+10][1]}\n{data_list[lastpage+10][2]}')
    listbox12_data.set(f'{data_list[lastpage+11][0]}\n{data_list[lastpage+11][1]}\n{data_list[lastpage+11][2]}')

# เปลี่ยนหน้าฟังก์ชั่น
def function_page() :
    global func_page
    func_page = func_page+1 if func_page < 2 else 0
    function_set = ("Sqrt", "Nroot", "Log", "Ln", "Sign", "Exp","Sin", "Cos", "Tan", "Csc", "Sec", "Cot", "Arcsin",
                    "Arccos", "Arctan", "Arcsec", "Arccosec", "Arccot","Sinh", "Cosh", "Tanh", "Csch", "Coth", "Sech",
                    "Arcsinh", "Arccosh", "Arccoth", "Arcsech", "Arctanh", "Arccsch", "Mean", "Std", "P", "C","Min", "Max")
    
    changebutton = [function_set[i] for i in range(12*func_page,12*func_page+12)] 
    function_name1_1.set(changebutton[0])
    function_name1_2.set(changebutton[1])
    function_name1_3.set(changebutton[2])
    function_name1_4.set(changebutton[3]) 
    function_name1_5.set(changebutton[4]) 
    function_name1_6.set(changebutton[5])
    
    function_name2_1.set(changebutton[6])
    function_name2_2.set(changebutton[7])
    function_name2_3.set(changebutton[8])
    function_name2_4.set(changebutton[9]) 
    function_name2_5.set(changebutton[10]) 
    function_name2_6.set(changebutton[11])

# เปลี่ยนหน้าค่าคงที่
def constant_page() :
    global cons_page
    cons_page = cons_page+1 if cons_page < 1 else 0
    cons_set = ('\u03c0','e','g','G',"mol",'c',"atm",'h','R','K','\u03c1w','Hp')
    changebutton = [cons_set[i] for i in range(6*cons_page,6*cons_page+6)] 
    
    cons_name1_1.set(changebutton[0])
    cons_name1_2.set(changebutton[1])
    cons_name1_3.set(changebutton[2])
    cons_name1_4.set(changebutton[3]) 
    cons_name1_5.set(changebutton[4]) 
    cons_name1_6.set(changebutton[5])

# เปลี่ยนหน้าสัญลักษณ์
def symbol_page() :
    global symb_page
    symb_page = symb_page+1 if symb_page < 1 else 0
    symb_set = ('+', '-', '*', '/', '^', '%', '&', '=', '(', '[', '<', '!', ')', ']', '>', '|')
    
    changebutton = [symb_set[i] for i in range(8*symb_page,8*symb_page+8)]
    
    symbol_name1_1.set(changebutton[0])
    symbol_name1_2.set(changebutton[1])
    symbol_name1_3.set(changebutton[2])
    symbol_name1_4.set(changebutton[3])
    
    symbol_name2_1.set(changebutton[4])
    symbol_name2_2.set(changebutton[5])
    symbol_name2_3.set(changebutton[6])
    symbol_name2_4.set(changebutton[7])

# เปลี่ยนโหมด
def mode_choice() :
    if mode.get() == 'Pemdas':
        mode.set('Function')
    elif mode.get() == 'Function':
        mode.set('Constant')
    elif mode.get() == 'Constant':
        mode.set('Pemdas')

# เปลี่ยนหน้าช่องตัวเลข
def numpad_page() :
    global num_page
    num_page = num_page+1 if num_page < 3 else 0
    num_set = ('1', '2', '3', '4', '5', '6', '7', '8', '9', 
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
               'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '')
    
    changebutton = [num_set[i] for i in range(9*num_page,9*num_page+9)]
    num1_1.set(changebutton[6])
    num1_2.set(changebutton[7])
    num1_3.set(changebutton[8])
    
    num2_1.set(changebutton[3])
    num2_2.set(changebutton[4])
    num2_3.set(changebutton[5])
    
    num3_1.set(changebutton[0])
    num3_2.set(changebutton[1])
    num3_3.set(changebutton[2])

# ใส่คำลงในช่องสมการ
def display(txt) :
    mainentry.insert(END,txt)

# ใส่ฟังก์ชั่นลงในช่องสมการ
def displayfunc(txt) :
    txt = f'{txt}<'
    mainentry.insert(END,txt)

# เคลียร์ข้อมูลฝั่งซ้าย
def clear() :
    mainentry.delete(1.0,END)
    answerblock.delete(1.0,END)

# คำนวณสมการ
def compute() :
    global previous_answer
    txt = mainentry.get('1.0','end-1c')
    txt = txt.replace('\n','')
    txt = txt.replace(' ','')
    choice = mode.get()

    if previous_answer != '' :
        txt = txt.replace('ANS',f'{previous_answer}') if previous_answer >= 0 else txt.replace('ANS',f'[{previous_answer}]')
    else :
        if 'ANS' in txt :
            choice = 'None'
    if choice == 'Pemdas' :
        answer = bx.formula(txt,choice)
        answerblock.delete(1.0,END)
        answerblock.insert(1.0,answer[0])
        if answer[1] :
            data.write_history(txt,answer[0])
            previous_answer = answer[0]
    elif choice == 'Function' :
        resort = data.write_function(txt)
        answerblock.delete(1.0,END)
        answerblock.insert(1.0,resort)
    elif choice == 'Constant' :
        resort = data.write_constant(txt)
        answerblock.delete(1.0,END)
        answerblock.insert(1.0,resort)
    else :
        answerblock.delete(1.0,END)
        answerblock.insert(1.0,'ANS has no value,Calculate Something First')
    update_program()

# ใส่ค่าจากช่อง data
def insert_data(txt) :
    data_list = txt.split('\n')
    data_type = data_list[1][7:]
    if data_type != "History":
        mainentry.insert(END,data_list[0])
    else:
        history0 = data_list[2].split('=')
        history1 = history0[1]
        history1 = history1.strip()
        mainentry.delete(1.0,END)
        mainentry.insert(END,history1)

# ใส่ค่า ANS ในช่องสมการ
def answer_insert() :
    mainentry.insert(END,"ANS")

# เปลี่ยนหมวดหมู่ข้อมูล
def catalog_change(txt) :
    global data_list
    global max_page
    catalog_text.set(f'Catalog : {txt}')
    data_list = search.folder_list(txt) if txt != 'All' else search.all_folder()
    fraction = 12-len(data_list)%12 if len(data_list)%12 != 0 else (0 if len(data_list) > 0 else 12)
    
    for _ in range(fraction):
        data_list.append(['','',''])
    
    max_page = len(data_list)//12
    page_number.set('1')
    listbox1_data.set(f'{data_list[0][0]}\n{data_list[0][1]}\n{data_list[0][2]}')
    listbox2_data.set(f'{data_list[1][0]}\n{data_list[1][1]}\n{data_list[1][2]}')
    listbox3_data.set(f'{data_list[2][0]}\n{data_list[2][1]}\n{data_list[2][2]}')
    listbox4_data.set(f'{data_list[3][0]}\n{data_list[3][1]}\n{data_list[3][2]}')
    listbox5_data.set(f'{data_list[4][0]}\n{data_list[4][1]}\n{data_list[4][2]}')
    listbox6_data.set(f'{data_list[5][0]}\n{data_list[5][1]}\n{data_list[5][2]}')
    listbox7_data.set(f'{data_list[6][0]}\n{data_list[6][1]}\n{data_list[6][2]}')
    listbox8_data.set(f'{data_list[7][0]}\n{data_list[7][1]}\n{data_list[7][2]}')
    listbox9_data.set(f'{data_list[8][0]}\n{data_list[8][1]}\n{data_list[8][2]}')
    listbox10_data.set(f'{data_list[9][0]}\n{data_list[9][1]}\n{data_list[9][2]}')
    listbox11_data.set(f'{data_list[10][0]}\n{data_list[10][1]}\n{data_list[10][2]}')
    listbox12_data.set(f'{data_list[11][0]}\n{data_list[11][1]}\n{data_list[11][2]}')

# คำสั่งลบข้อมูล
def delete_data_command() :
    global data_list
    page = 12*(int(page_number.get())-1)
    if check1.get() and listbox1_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox1_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page][0] = update
        data_list[page][1] = ''
        data_list[page][2] = ''
        listbox1_data.set(update)
    if check2.get() and listbox2_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox2_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+1][0] = update
        data_list[page+1][1] = ''
        data_list[page+1][2] = ''
        listbox2_data.set(update)
    if check3.get() and listbox3_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox3_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+2][0] = update
        data_list[page+2][1] = ''
        data_list[page+2][2] = ''
        listbox3_data.set(update)
    if check4.get() and listbox4_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox4_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+3][0] = update
        data_list[page+3][1] = ''
        data_list[page+3][2] = ''
        listbox4_data.set(update)
    if check5.get() and listbox5_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox5_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+4][0] = update
        data_list[page+4][1] = ''
        data_list[page+4][2] = ''
        listbox5_data.set(update)
    if check6.get() and listbox6_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox6_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+5][0] = update
        data_list[page+5][1] = ''
        data_list[page+5][2] = ''
        listbox6_data.set(update)
    if check7.get() and listbox7_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox7_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+6][0] = update
        data_list[page+6][1] = ''
        data_list[page+6][2] = ''
        listbox7_data.set(update)
    if check8.get() and listbox8_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox8_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+7][0] = update
        data_list[page+7][1] = ''
        data_list[page+7][2] = ''
        listbox8_data.set(update)
    if check9.get() and listbox9_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox9_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+8][0] = update
        data_list[page+8][1] = ''
        data_list[page+8][2] = ''
        listbox9_data.set(update)
    if check10.get() and listbox10_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox10_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+9][0] = update
        data_list[page+9][1] = ''
        data_list[page+9][2] = ''
        listbox10_data.set(update)
    if check11.get() and listbox11_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox11_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+10][0] = update
        data_list[page+10][1] = ''
        data_list[page+10][2] = ''
        listbox11_data.set(update)
    if check12.get() and listbox12_data.get().split('\n')[0] not in ('Deleted !!!',''):
        name = listbox12_data.get().split('\n')
        location = name[1][7:]
        update = data.delete(name[0], location)
        data_list[page+11][0] = update
        data_list[page+11][1] = ''
        data_list[page+11][2] = ''
        listbox12_data.set(update)

# ค้นหาข้อมูล
def search_data() :
    data_name = catalog_text.get()[10:]
    keywords = search_box.get('1.0','end-1c')
    catalog_change(data_name)
    
    global data_list
    global max_page
    data_list = [datas for datas in data_list if keywords in datas[0]]
    fraction = 12-len(data_list)%12 if len(data_list)%12 != 0 else (0 if len(data_list) > 0 else 12)
    for _ in range(fraction):
        data_list.append(['','',''])
    
    page_number.set('1')
    max_page = len(data_list)//12
    listbox1_data.set(f'{data_list[0][0]}\n{data_list[0][1]}\n{data_list[0][2]}')
    listbox2_data.set(f'{data_list[1][0]}\n{data_list[1][1]}\n{data_list[1][2]}')
    listbox3_data.set(f'{data_list[2][0]}\n{data_list[2][1]}\n{data_list[2][2]}')
    listbox4_data.set(f'{data_list[3][0]}\n{data_list[3][1]}\n{data_list[3][2]}')
    listbox5_data.set(f'{data_list[4][0]}\n{data_list[4][1]}\n{data_list[4][2]}')
    listbox6_data.set(f'{data_list[5][0]}\n{data_list[5][1]}\n{data_list[5][2]}')
    listbox7_data.set(f'{data_list[6][0]}\n{data_list[6][1]}\n{data_list[6][2]}')
    listbox8_data.set(f'{data_list[7][0]}\n{data_list[7][1]}\n{data_list[7][2]}')
    listbox9_data.set(f'{data_list[8][0]}\n{data_list[8][1]}\n{data_list[8][2]}')
    listbox10_data.set(f'{data_list[9][0]}\n{data_list[9][1]}\n{data_list[9][2]}')
    listbox11_data.set(f'{data_list[10][0]}\n{data_list[10][1]}\n{data_list[10][2]}')
    listbox12_data.set(f'{data_list[11][0]}\n{data_list[11][1]}\n{data_list[11][2]}')

# เคลียร์ข้อมูลฝั่งขวา
def clear_data() :
    check1.set(False)
    check2.set(False)
    check3.set(False)
    check4.set(False)
    check5.set(False)
    check6.set(False)
    check7.set(False)
    check8.set(False)
    check9.set(False)
    check10.set(False)
    check11.set(False)
    check12.set(False)
    search_box.delete(1.0,END)

# ลบช่องข้อความลบข้อมูล
def deleted_exit_pop() :
    deleted_pop.destroy()

# คำสั่งลบช่องลบข้อมูล
def delete_pop_command(choice) :
    delete_pop.destroy()
    if choice:
        delete_data_command()
        global deleted_pop
        
        deleted_pop = tk.Toplevel(Window)
        deleted_pop.title("Deleted")
        deleted_pop.geometry("250x150+960+540")
        deleted_pop.resizable(width=False, height=False)
        
        deleted_pop_label = tk.Label(deleted_pop,text="Deleted")
        deleted_pop_label.place(x=100,y=30)
        
        ok_button = tk.Button(deleted_pop,text="OK",command=deleted_exit_pop)
        ok_button.place(x=110,y=80)
    update_program()

# กล่องข้อความลบข้อมูล
def delete_data() :
    global delete_pop
    
    delete_pop = tk.Toplevel(Window)
    delete_pop.title("Delete Files")
    delete_pop.geometry("250x150+960+540")
    delete_pop.resizable(width=False, height=False)
    
    delete_pop_label = tk.Label(delete_pop,text="Are you sure to delete some files?")
    delete_pop_label.place(x=50,y=30)
    
    delete_yes_button = tk.Button(delete_pop,text="Yes",command=lambda:delete_pop_command(True))
    delete_yes_button.place(x=80,y=80)

    delete_no_button = tk.Button(delete_pop,text="No",command=lambda:delete_pop_command(False))
    delete_no_button.place(x=145,y=80)

# ลบช่องข้อความลบข้อมูลทั้งหมด
def delete_all_exit_pop() :
    deleted_all_pop.destroy()

# คำสั่งลบช่องลบข้อมูลทั้งหมด
def delete_all_pop_command(choice) :
    delete_all_pop.destroy()
    if choice:
        global deleted_all_pop
        folder = catalog_text.get()[10:]
        deleted_all_pop_text = tk.StringVar()
        
        deleted_all_pop_text.set(search.delete_all(folder))
        
        deleted_all_pop = tk.Toplevel(Window)
        deleted_all_pop.title("Deleted")
        deleted_all_pop.geometry("250x150+960+540")
        deleted_all_pop.resizable(width=False, height=False)
        
        deleted_all_pop_label = tk.Label(deleted_all_pop,textvariable=deleted_all_pop_text)
        deleted_all_pop_label.place(x=100,y=30)
        ok_button = tk.Button(deleted_all_pop,text="OK",command=delete_all_exit_pop)
        ok_button.place(x=125,y=80)
    update_program()

# กล่องข้อความลบข้อมูลทั้งหมด
def delete_all_data() :
    global delete_all_pop
    delete_all_pop = tk.Toplevel(Window)
    delete_all_pop.title("Delete All Files")
    delete_all_pop.geometry("250x150+960+540")
    delete_all_pop.resizable(width=False, height=False)
    
    delete_all_pop_label = tk.Label(delete_all_pop,text="Are you sure to delete all files?")
    delete_all_pop_label.place(x=50,y=30)
    
    delete_all_yes_button = tk.Button(delete_all_pop,text="Yes",command=lambda:delete_all_pop_command(True))
    delete_all_yes_button.place(x=80,y=80)
    
    delete_all_no_button = tk.Button(delete_all_pop,text="No",command=lambda:delete_all_pop_command(False))
    delete_all_no_button.place(x=145,y=80)

# อัพเดทโปรแกรม
def update_program() :
    catalog = catalog_text.get()[10:]
    catalog_change(catalog)
    search_txt = search_box.get('1.0','end-1c')
    clear_data()
    search_box.insert(1.0,search_txt)

#Main Object
Window = tk.Tk()

#Window Setting Zone
Window.title("Calculator")
Window.geometry("1480x610")
Window.resizable(width=False, height=False)
Window.config(bg='#050505')
search.setup()

# คำถาม
mainentry = tk.Text(Window,height=5,width=65, font = ("Times New Roman", 16),bg='#333333',foreground='white',border=False)
mainentry.place(x=10,y=20)

# คำตอบ
answerblock= tk.Text(Window,height=2,width=65, font = ("Times New Roman", 16),bg='#333333',foreground='white',border=False)
answerblock.place(x=10,y=150)

# ปุ่มแถบเทาอ่อน
mode = tk.StringVar()
mode.set('Pemdas')
modebutton = tk.Button(Window, textvariable=mode, width=15, height=2, command=mode_choice,bg='#a5a5a5',border=False)
modebutton.place(x=10, y=210)

answerbutton = tk.Button(Window, text="ANS",width=15,height=2,command=answer_insert,bg='#a5a5a5',border=False)
answerbutton.place(x=130, y=210) 

clearbutton = tk.Button(Window, text="CLEAR",width=15,height=2,command=clear,bg='#a5a5a5',border=False)
clearbutton.place(x=250, y=210) 

pagefunction = tk.Button(Window, text="FUNC",width=15,height=2,command=function_page,bg='#a5a5a5',border=False)
pagefunction.place(x=370, y=210) 

pageconsbutton = tk.Button(Window, text="CONS",width=15,height=2,command=constant_page,bg='#a5a5a5',border=False)
pageconsbutton.place(x=490, y=210) 

helpbutton = tk.Button(Window, text="HELP",width=15,height=2,command=help_page,bg='#a5a5a5',border=False)
helpbutton.place(x=610, y=210) 

#function-1
function_name1_1 = tk.StringVar()
function_name1_2 = tk.StringVar()
function_name1_3 = tk.StringVar()
function_name1_4 = tk.StringVar()
function_name1_5 = tk.StringVar()
function_name1_6 = tk.StringVar()
function_name1_1.set("Sqrt")
function_name1_2.set("Nroot")
function_name1_3.set("Log")
function_name1_4.set("Ln") 
function_name1_5.set("Sign") 
function_name1_6.set("Exp")

functionbutton1_1 = tk.Button(Window, textvariable=function_name1_1 ,width=15,height=2,command=lambda:displayfunc(function_name1_1.get()),bg='#ff94c9',border=False)
functionbutton1_1.place(x=10, y=260)

functionbutton1_2 = tk.Button(Window, textvariable=function_name1_2,width=15,height=2,command=lambda:displayfunc(function_name1_2.get()),bg='#ff94c9',border=False)
functionbutton1_2.place(x=130, y=260)

functionbutton1_3 = tk.Button(Window, textvariable=function_name1_3,width=15,height=2,command=lambda:displayfunc(function_name1_3.get()),bg='#ff94c9',border=False)
functionbutton1_3.place(x=250, y=260)

functionbutton1_4 = tk.Button(Window, textvariable=function_name1_4,width=15,height=2,command=lambda:displayfunc(function_name1_4.get()),bg='#ff94c9',border=False)
functionbutton1_4.place(x=370, y=260)

functionbutton1_5 = tk.Button(Window, textvariable=function_name1_5,width=15,height=2,command=lambda:displayfunc(function_name1_5.get()),bg='#ff94c9',border=False)
functionbutton1_5.place(x=490, y=260)

functionbutton1_6 = tk.Button(Window, textvariable=function_name1_6,width=15,height=2,command=lambda:displayfunc(function_name1_6.get()),bg='#ff94c9',border=False)
functionbutton1_6.place(x=610, y=260)

# function-2
function_name2_1 = tk.StringVar()
function_name2_2 = tk.StringVar()
function_name2_3 = tk.StringVar()
function_name2_4 = tk.StringVar()
function_name2_5 = tk.StringVar()
function_name2_6 = tk.StringVar()
function_name2_1.set("Sin")
function_name2_2.set("Cos")
function_name2_3.set("Tan")
function_name2_4.set("Csc") 
function_name2_5.set("Sec") 
function_name2_6.set("Cot")

functionbutton2_1 = tk.Button(Window, textvariable=function_name2_1,width=15,height=2,command=lambda:displayfunc(function_name2_1.get()),bg='#ff94c9',border=False)
functionbutton2_1.place(x=10, y=310)

functionbutton2_2 = tk.Button(Window, textvariable=function_name2_2,width=15,height=2,command=lambda:displayfunc(function_name2_2.get()),bg='#ff94c9',border=False)
functionbutton2_2.place(x=130, y=310)

functionbutton2_3 = tk.Button(Window, textvariable=function_name2_3,width=15,height=2,command=lambda:displayfunc(function_name2_3.get()),bg='#ff94c9',border=False)
functionbutton2_3.place(x=250, y=310)

functionbutton2_4 = tk.Button(Window, textvariable=function_name2_4,width=15,height=2,command=lambda:displayfunc(function_name2_4.get()),bg='#ff94c9',border=False)
functionbutton2_4.place(x=370, y=310)

functionbutton2_5 = tk.Button(Window, textvariable=function_name2_5,width=15,height=2,command=lambda:displayfunc(function_name2_5.get()),bg='#ff94c9',border=False)
functionbutton2_5.place(x=490, y=310)

functionbutton2_6 = tk.Button(Window, textvariable=function_name2_6,width=15,height=2,command=lambda:displayfunc(function_name2_6.get()),bg='#ff94c9',border=False)
functionbutton2_6.place(x=610, y=310)

# constant
cons_name1_1 = tk.StringVar()
cons_name1_2 = tk.StringVar()
cons_name1_3 = tk.StringVar()
cons_name1_4 = tk.StringVar()
cons_name1_5 = tk.StringVar()
cons_name1_6 = tk.StringVar()
cons_name1_1.set('\u03c0')
cons_name1_2.set('e')
cons_name1_3.set('g')
cons_name1_4.set('G') 
cons_name1_5.set("mol") 
cons_name1_6.set('c')

constant1 = tk.Button(Window, textvariable=cons_name1_1,width=15,height=2,command=lambda:display(cons_name1_1.get()),bg='#d14d4d',border=False)
constant1.place(x=10, y=360)

constant2 = tk.Button(Window, textvariable=cons_name1_2,width=15,height=2,command=lambda:display(cons_name1_2.get()),bg='#d14d4d',border=False)
constant2.place(x=130, y=360)

constant3 = tk.Button(Window, textvariable=cons_name1_3,width=15,height=2,command=lambda:display(cons_name1_3.get()),bg='#d14d4d',border=False)
constant3.place(x=250, y=360)

constant4 = tk.Button(Window, textvariable=cons_name1_4,width=15,height=2,command=lambda:display(cons_name1_4.get()),bg='#d14d4d',border=False)
constant4.place(x=370, y=360)

constant5 = tk.Button(Window, textvariable=cons_name1_5,width=15,height=2,command=lambda:display(cons_name1_5.get()),bg='#d14d4d',border=False)
constant5.place(x=490, y=360)

constant6 = tk.Button(Window, textvariable=cons_name1_6,width=15,height=2,command=lambda:display(cons_name1_6.get()),bg='#d14d4d',border=False)
constant6.place(x=610, y=360)

# symbolแถว1
symbol_name1_1 = tk.StringVar()
symbol_name1_2 = tk.StringVar()
symbol_name1_3 = tk.StringVar()
symbol_name1_4 = tk.StringVar()
symbol_name1_1.set('+')
symbol_name1_2.set('-')
symbol_name1_3.set('*')
symbol_name1_4.set('/')

symbol1_1 = tk.Button(Window, textvariable=symbol_name1_1,width=15,height=2,command=lambda:display(symbol_name1_1.get()),bg='#f1a43c',border=False)
symbol1_1.place(x=10, y=410)

symbol1_2 = tk.Button(Window, textvariable=symbol_name1_2,width=15,height=2,command=lambda:display(symbol_name1_2.get()),bg='#f1a43c',border=False)
symbol1_2.place(x=10, y=460)

symbol1_3 = tk.Button(Window, textvariable=symbol_name1_3,width=15,height=2,command=lambda:display(symbol_name1_3.get()),bg='#f1a43c',border=False)
symbol1_3.place(x=10, y=510)

symbol1_4 = tk.Button(Window, textvariable=symbol_name1_4,width=15,height=2,command=lambda:display(symbol_name1_4.get()),bg='#f1a43c',border=False)
symbol1_4.place(x=10, y=560)

# symbolแถว2
symbol_name2_1 = tk.StringVar()
symbol_name2_2 = tk.StringVar()
symbol_name2_3 = tk.StringVar()
symbol_name2_4 = tk.StringVar()
symbol_name2_1.set('^')
symbol_name2_2.set('%')
symbol_name2_3.set('&')
symbol_name2_4.set('=')

symbol2_1 = tk.Button(Window, textvariable=symbol_name2_1,width=15,height=2,command=lambda:display(symbol_name2_1.get()),bg='#f1a43c',border=False)
symbol2_1.place(x=130, y=410)

symbol2_2 = tk.Button(Window, textvariable=symbol_name2_2,width=15,height=2,command=lambda:display(symbol_name2_2.get()),bg='#f1a43c',border=False)
symbol2_2.place(x=130, y=460)

symbol2_3 = tk.Button(Window, textvariable=symbol_name2_3,width=15,height=2,command=lambda:display(symbol_name2_3.get()),bg='#f1a43c',border=False)
symbol2_3.place(x=130, y=510)

symbol2_4 = tk.Button(Window, textvariable=symbol_name2_4,width=15,height=2,command=lambda:display(symbol_name2_4.get()),bg='#f1a43c',border=False)
symbol2_4.place(x=130, y=560)

#number row1
num1_1 = tk.StringVar()
num1_2 = tk.StringVar()
num1_3 = tk.StringVar()
num1_1.set('7')
num1_2.set('8')
num1_3.set('9')

number1_1= tk.Button(Window, textvariable=num1_1,width=15,height=2,command=lambda:display(num1_1.get()),bg='#333333',foreground='white',border=False)
number1_1.place(x=250, y=410)

number1_2= tk.Button(Window, textvariable=num1_2,width=15,height=2,command=lambda:display(num1_2.get()),bg='#333333',foreground='white',border=False)
number1_2.place(x=370, y=410)

number1_3= tk.Button(Window, textvariable=num1_3,width=15,height=2,command=lambda:display(num1_3.get()),bg='#333333',foreground='white',border=False)
number1_3.place(x=490, y=410)

#number row2
num2_1 = tk.StringVar()
num2_2 = tk.StringVar()
num2_3 = tk.StringVar()
num2_1.set('4')
num2_2.set('5')
num2_3.set('6')

number2_1= tk.Button(Window, textvariable=num2_1,width=15,height=2,command=lambda:display(num2_1.get()),bg='#333333',foreground='white',border=False)
number2_1.place(x=250, y=460)

number2_2= tk.Button(Window, textvariable=num2_2,width=15,height=2,command=lambda:display(num2_2.get()),bg='#333333',foreground='white',border=False)
number2_2.place(x=370, y=460)

number2_3= tk.Button(Window, textvariable=num2_3,width=15,height=2,command=lambda:display(num2_3.get()),bg='#333333',foreground='white',border=False)
number2_3.place(x=490, y=460)

#number row3
num3_1 = tk.StringVar()
num3_2 = tk.StringVar()
num3_3 = tk.StringVar()
num3_1.set('1')
num3_2.set('2')
num3_3.set('3')

number3_1= tk.Button(Window, textvariable=num3_1,width=15,height=2,command=lambda:display(num3_1.get()),bg='#333333',foreground='white',border=False)
number3_1.place(x=250, y=510)

number3_2= tk.Button(Window, textvariable=num3_2,width=15,height=2,command=lambda:display(num3_2.get()),bg='#333333',foreground='white',border=False)
number3_2.place(x=370, y=510)

number3_3= tk.Button(Window, textvariable=num3_3,width=15,height=2,command=lambda:display(num3_3.get()),bg='#333333',foreground='white',border=False)
number3_3.place(x=490, y=510)

#number row4
number4_1= tk.Button(Window, text='0',width=15,height=2,command=lambda:display('0'),bg='#333333',foreground='white',border=False)
number4_1.place(x=250, y=560)

number4_2= tk.Button(Window, text='\u00b0',width=15,height=2,command=lambda:display('\u00b0'),bg='#333333',foreground='white',border=False)
number4_2.place(x=370, y=560)

number4_3= tk.Button(Window, text='.',width=15,height=2,command=lambda:display('.'),bg='#333333',foreground='white',border=False)
number4_3.place(x=490, y=560)

#Numpad Command
numpad_command1= tk.Button(Window, text='Change Symbol',width=15,height=2, command=symbol_page,bg='#0000a8',foreground='white',border=False)
numpad_command1.place(x=610, y=410)

numpad_command2= tk.Button(Window, text='Change Numpad',width=15,height=2, command=numpad_page,bg='#0000a8',foreground='white',border=False)
numpad_command2.place(x=610, y=460)

numpad_command3= tk.Button(Window, text='Calculate',width=15,pady=34,command=compute,bg='#0000a8',foreground='white',border=False)
numpad_command3.place(x=610, y=510)

#catalog display
catalog_text = tk.StringVar()
catalog_text.set('Catalog : All')
catalog_label = tk.Label(Window,height=2,width=18,bd=2,relief='sunken',textvariable=catalog_text,font = ("Times New Roman", 16),bg='#a5a5a5',border=False)
catalog_label.place(x=760,y=20)

all_button = tk.Button(Window,padx=35,pady=7,text='All', font = ("Times New Roman", 16), command=lambda:catalog_change('All'),bg='#a5a5a5',border=False)
all_button.place(x=985,y=20)

history_button = tk.Button(Window,padx=21,pady=7,text='History', font = ("Times New Roman", 16), command=lambda:catalog_change('History'),bg='#a5a5a5',border=False)
history_button.place(x=1100,y=20)

functions_button = tk.Button(Window,padx=16,pady=7,text='Function', font = ("Times New Roman", 16), command=lambda:catalog_change('Function'),bg='#a5a5a5',border=False)
functions_button.place(x=1224,y=20)

constants_button = tk.Button(Window,padx=15,pady=7,text='Constant', font = ("Times New Roman", 16), command=lambda:catalog_change('Constant'),bg='#a5a5a5',border=False)
constants_button.place(x=1350,y=20)

# กล่องค้นหา
search_box = tk.Text(Window,height=1,width=53, font = ("Times New Roman", 16),border=False)
search_box.place(x=760,y=80)

delete_button = tk.Button(Window,padx=15,pady=4, text=f'{chr(0x1F5D1)}',command=delete_data,bg='#a5a5a5',border=False)
delete_button.place(x=1419,y=76)

search_button = tk.Button(Window,padx=15,pady=4, text=f'{chr(0x1F50D)}',command=search_data,bg='#a5a5a5',border=False)
search_button.place(x=1360,y=76)

# Set 1
# 1
check1 = tk.BooleanVar()
checkbox1 = tk.Checkbutton(Window, variable=check1,bg='#050505',border=False)
checkbox1.place(x=760,y=120)

listbox1_data = tk.StringVar()
listbox1_data.set(f'{data_list[0][0]}\n{data_list[0][1]}\n{data_list[0][2]}')

listbox1 = tk.Button(Window,height=3,width=45,textvariable=listbox1_data,command=lambda:insert_data(listbox1_data.get()),bg='#333333',foreground='white',border=False)
listbox1.place(x=785,y=120)

# 2
check2 = tk.BooleanVar()
checkbox2 = tk.Checkbutton(Window, variable=check2,bg='#050505',border=False)
checkbox2.place(x=760,y=185)

listbox2_data = tk.StringVar()
listbox2_data.set(f'{data_list[1][0]}\n{data_list[1][1]}\n{data_list[1][2]}')

listbox2 = tk.Button(Window,height=3,width=45,textvariable=listbox2_data,command=lambda:insert_data(listbox2_data.get()),bg='#333333',foreground='white',border=False)
listbox2.place(x=785,y=185)

# 3
check3 = tk.BooleanVar()
checkbox3 = tk.Checkbutton(Window, variable=check3,bg='#050505',border=False)
checkbox3.place(x=760,y=250)

listbox3_data = tk.StringVar()
listbox3_data.set(f'{data_list[2][0]}\n{data_list[2][1]}\n{data_list[2][2]}')

listbox3 = tk.Button(Window,height=3,width=45,textvariable=listbox3_data,command=lambda:insert_data(listbox3_data.get()),bg='#333333',foreground='white',border=False)
listbox3.place(x=785,y=250)

# 4
check4 = tk.BooleanVar()
checkbox4 = tk.Checkbutton(Window, variable=check4,bg='#050505',border=False)
checkbox4.place(x=760,y=315)

listbox4_data = tk.StringVar()
listbox4_data.set(f'{data_list[3][0]}\n{data_list[3][1]}\n{data_list[3][2]}')

listbox4 = tk.Button(Window,height=3,width=45,textvariable=listbox4_data,command=lambda:insert_data(listbox4_data.get()),bg='#333333',foreground='white',border=False)
listbox4.place(x=785,y=315)

# 5
check5 = tk.BooleanVar()
checkbox5 = tk.Checkbutton(Window, variable=check5,bg='#050505',border=False)
checkbox5.place(x=760,y=380)

listbox5_data = tk.StringVar()
listbox5_data.set(f'{data_list[4][0]}\n{data_list[4][1]}\n{data_list[4][2]}')

listbox5 = tk.Button(Window,height=3,width=45,textvariable=listbox5_data,command=lambda:insert_data(listbox5_data.get()),bg='#333333',foreground='white',border=False)
listbox5.place(x=785,y=380)

# 6
check6 = tk.BooleanVar()
checkbox6 = tk.Checkbutton(Window, variable=check6,bg='#050505',border=False)
checkbox6.place(x=760,y=445)

listbox6_data = tk.StringVar()
listbox6_data.set(f'{data_list[5][0]}\n{data_list[5][1]}\n{data_list[5][2]}')

listbox6 = tk.Button(Window,height=3,width=45,textvariable=listbox6_data,command=lambda:insert_data(listbox6_data.get()),bg='#333333',foreground='white',border=False)
listbox6.place(x=785,y=445)

# Set2
# 7
check7 = tk.BooleanVar()
checkbox7 = tk.Checkbutton(Window, variable=check7,bg='#050505',border=False)
checkbox7.place(x=1120,y=120)

listbox7_data = tk.StringVar()
listbox7_data.set(f'{data_list[6][0]}\n{data_list[6][1]}\n{data_list[6][2]}')

listbox7 = tk.Button(Window,height=3,width=45,textvariable=listbox7_data,command=lambda:insert_data(listbox7_data.get()),bg='#333333',foreground='white',border=False)
listbox7.place(x=1145,y=120)

# 8
check8 = tk.BooleanVar()
checkbox8 = tk.Checkbutton(Window, variable=check8,bg='#050505',border=False)
checkbox8.place(x=1120,y=185)

listbox8_data = tk.StringVar()
listbox8_data.set(f'{data_list[7][0]}\n{data_list[7][1]}\n{data_list[7][2]}')

listbox8 = tk.Button(Window,height=3,width=45,textvariable=listbox8_data,command=lambda:insert_data(listbox8_data.get()),bg='#333333',foreground='white',border=False)
listbox8.place(x=1145,y=185)

# 9
check9 = tk.BooleanVar()
checkbox9 = tk.Checkbutton(Window, variable=check9,bg='#050505',border=False)
checkbox9.place(x=1120,y=250)

listbox9_data = tk.StringVar()
listbox9_data.set(f'{data_list[8][0]}\n{data_list[8][1]}\n{data_list[8][2]}')

listbox9 = tk.Button(Window,height=3,width=45,textvariable=listbox9_data,command=lambda:insert_data(listbox9_data.get()),bg='#333333',foreground='white',border=False)
listbox9.place(x=1145,y=250)

# 10
check10 = tk.BooleanVar()
checkbox10 = tk.Checkbutton(Window, variable=check10,bg='#050505',border=False)
checkbox10.place(x=1120,y=315)

listbox10_data = tk.StringVar()
listbox10_data.set(f'{data_list[9][0]}\n{data_list[9][1]}\n{data_list[9][2]}')

listbox10 = tk.Button(Window,height=3,width=45,textvariable=listbox10_data,command=lambda:insert_data(listbox10_data.get()),bg='#333333',foreground='white',border=False)
listbox10.place(x=1145,y=315)

# 11
check11 = tk.BooleanVar()
checkbox11 = tk.Checkbutton(Window, variable=check11,bg='#050505',border=False)
checkbox11.place(x=1120,y=380)

listbox11_data = tk.StringVar()
listbox11_data.set(f'{data_list[10][0]}\n{data_list[10][1]}\n{data_list[10][2]}')

listbox11 = tk.Button(Window,height=3,width=45,textvariable=listbox11_data,command=lambda:insert_data(listbox11_data.get()),bg='#333333',foreground='white',border=False)
listbox11.place(x=1145,y=380)

# 12
check12 = tk.BooleanVar()
checkbox12 = tk.Checkbutton(Window, variable=check12,bg='#050505',border=False)
checkbox12.place(x=1120,y=445)

listbox12_data = tk.StringVar()
listbox12_data.set(f'{data_list[11][0]}\n{data_list[11][1]}\n{data_list[11][2]}')

listbox12 = tk.Button(Window,height=3,width=45,textvariable=listbox12_data,command=lambda:insert_data(listbox12_data.get()),bg='#333333',foreground='white',border=False)
listbox12.place(x=1145,y=445)

# ปุ่มหน้าแรกกับสุดท้าย
first_page_button = tk.Button(Window,height=3,width=9,text="<<",command=first_page,bg='#a5a5a5',border=False)
first_page_button.place(x=920,y=540)

previous_page_button = tk.Button(Window,height=3,width=9,text="<",command=lambda:list_datapage(-1),bg='#a5a5a5',border=False)
previous_page_button.place(x=1000,y=540)

# ปุ่มเลื่อนเพจ
page_number = tk.StringVar()
page_number.set('1')
page_number_label = tk.Label(Window,height=1,width=3,font = ("Times New Roman", 36),bg='#a5a5a5',textvariable=page_number,border=False)
page_number_label.place(x=1078,y=540)

forward_page_button = tk.Button(Window,height=3,width=9,text=">",command=lambda:list_datapage(1),bg='#a5a5a5',border=False)
forward_page_button.place(x=1170,y=540)

last_page_button = tk.Button(Window,height=3,width=9,text=">>",command=last_page,bg='#a5a5a5',border=False)
last_page_button.place(x=1250,y=540)

clear_data_button = tk.Button(Window,height=3,width=9,text="Clear",command=clear_data,bg='#a5a5a5',border=False)
clear_data_button.place(x=780,y=540)

delete_all_button = tk.Button(Window,height=3,width=9,text="Delete All",command=delete_all_data,bg='#a5a5a5',border=False)
delete_all_button.place(x=1395,y=540)

Window.mainloop()