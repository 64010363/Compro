import os
import datetime as date

location = os.getcwd()

# อ่านบรรทัดสุดท้ายในไฟล์
def read_last(read):
    file = open(read, 'r', encoding='utf-8')
    words = file.readline()
    while words != '':
        line = file.readline()
        if line != '':
            words = line
        else:
            break
    return words

# แปลงชื่อไฟล์กลับไปเป็นเหมือนเดิม
def to_unicode(words):
    words = words[0:words.find('.txt')]
    names = words.split('')
    result = ''
    for name in names:
        if name[0] != '$':
            result += name
        else:
            result += chr(int(name[1:]))
    return result

# เรียงวันที่
def date_sort(day_list):
    pre_list = []
    for day in day_list:
        item1 = day[0:day.find('.txt')].split('_')
        date_list = [int(time) for time in item1]
        pre_list.append(date_list)
    pre_list = sorted(pre_list)
    pre_list.reverse()
    post_list = []
    for item in pre_list:
        months = f'0{item[1]}' if item[1] < 10 else f'{item[1]}'
        days = f'0{item[2]}' if item[2] < 10 else f'{item[2]}'
        text = f'{item[0]}_{months}_{days}_{item[3]}.txt'
        post_list.append(text)
    return post_list

# เรียกไฟล์ทั้งหมดในโฟล์เดอร์มาเก็บไว้ในลิสตื
def folder_list(folder_name):
    name_list = []
    try:
        folder_location = f"{location}\\{folder_name}"
        files_list = os.listdir(folder_location)
        if folder_name != 'History':
            files_list = sorted(files_list)
        else:
            files_list = date_sort(files_list)
        for files in files_list:
            detail = read_last(f'{folder_location}\\{files}')
            name = to_unicode(files)
            content = (name, f'Type : {folder_name}', f'Detail : {detail}')
            name_list.append(content)
        return name_list
    except:
        return name_list

# เรียกไฟล์ทั้งหมดมาเก็บไว้ในลิสต์
def all_folder():
    all_list = folder_list("Function")
    all_list += folder_list("Constant")
    all_list += folder_list("History")
    all_list = sorted(all_list)
    return all_list

# ค้นหาค่ำที่ตรงกันในไฟล์
def search_file(keyword, folder_list):
    
    search_list = [file for file in folder_list if keyword in file[0]]
    return search_list

# ลบไฟล์ทั้งหมด
def delete_all(folder_name):
    try:
        if folder_name != 'All':
            folder = f'{location}\\{folder_name}'
            file_list = os.listdir(folder)
            for file in file_list:
                name = f'{folder}\\{file}'
                os.remove(name)
        else:
            folder = f'{location}\\Function'
            file_list = os.listdir(folder)
            for file in file_list:
                name = f'{folder}\\{file}'
                os.remove(name)
            folder = f'{location}\\Constant'
            file_list = os.listdir(folder)
            for file in file_list:
                name = f'{folder}\\{file}'
                os.remove(name)
            folder = f'{location}\\History'
            file_list = os.listdir(folder)
            for file in file_list:
                name = f'{folder}\\{file}'
                os.remove(name)
        if folder_name == 'History' or folder_name == 'All':
            document = f'{location}\\Document\\history.txt'
            docs = open(document, 'w', encoding='utf-8')
            time = f'{date.date.today()}'
            docs.write(f'{time}\n')
            docs.write('0')
            docs.close()
        return "Deleted All !!!"
    except:
        return "Nothing To Delete"

# เปิดไฟล์ pdf
def open_pdf():
    try:
        pdf = f'{location}\\Document\\Tutorial.pdf'
        os.startfile(pdf)
        return 'Open Completed'
    except:
        return 'Tutorial Not Found'

# สร้างโฟล์เดอร์และสิ่งจำเป็นสำหรับโปรแกรม
def setup():
    folder = f'{location}\\Constant'
    if not os.path.exists(folder):
        os.makedirs(folder)
    folder = f'{location}\\Function'
    if not os.path.exists(folder):
        os.makedirs(folder)
    folder = f'{location}\\History'
    if not os.path.exists(folder):
        os.makedirs(folder)
    folder = f'{location}\\Document'
    if not os.path.exists(folder):
        os.makedirs(folder)
    history = f'{folder}\\history.txt'
    if not os.path.exists(history):
        hist = open(history, 'w', encoding='utf-8')
        time = f'{date.date.today()}'
        hist.write(f'{time}\n')
        hist.write('0')
        hist.close()
