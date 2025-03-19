import pygame as pg
import random
import time
from tkinter import *
from tkinter.messagebox import *

FPS = 24
game_chosen = None
font = ('DejaVu Sans Mono', 10)
font_b = ('DejaVu Sans Mono', 10, 'bold')
font_s = ('DejaVu Sans Mono', 6, 'bold')
G = open('Games/Games.txt', 'r', encoding='utf8')
games_list = []
games_list_short = []
games = []
images = []  # [<name>, <image>]
database = []  # [<length>, [<elements>]]
cells = []  # [<name>, [x0, y0, x1, y1], <image>, <image_name>]
controls = []  # [<button>, *<cell>, <name>]
events = []  # [<name>, [<code>]]
variables = []  # [<name>, <value>]
h, w = 0, 0  # height, width
cut = 0
err0r = ''
rec = 0  # record
rec_file = None
rec_filename = ''
rec_stop = 0


def coordinates():
    if pg.mouse.get_focused():
        return pg.mouse.get_pos()  # returns mouse position (x, y)
    else:
        return None


def downloader():
    global G, games_list, games
    for g in G:
        g2 = g.split('\n')[0].split(' - ')
        games_list.append(g2[0])
        games_list_short.append(g2[1].split('.')[0])
        games.append([])
        g3 = open(f'Games/{g2[1]}', 'r', encoding='utf8')
        line_ = 1
        for g4 in g3:
            games[-1] += [[g4.replace('\n', '').split(' '), line_]]
            line_ += 1


def record(cord):
    global rec_file, rec_filename
    rec_file = open(f'Reports/{rec_filename}.txt', 'r+', encoding='utf8')
    rec_file_length = len(rec_file.readlines())
    rec_file.close()
    rec_file = open(f'Reports/{rec_filename}.txt', 'a+')
    if type(cord) == str:
        rec_file.write(str(cord) + '\n')
        rec_file.close()
        return rec_file_length


def menu(error):
    global games_list, game_chosen, cut, rec
    if cut == 1:
        return
    sc = Tk()
    sc.title('     Menu')
    sc.geometry('400x300+50+50')
    sc.resizable(False, False)
    if error != '' and error is not None:
        if rec == 1:
            record('*' * 32)
            record(error)
        showerror(title='Error', message=error)
        error = ''

    def btn1_f():
        sc_n = 1
        otd = [lbl_, lbl0, lbl1, btn1, btn2, btn8, btn9, btn10]
        for o in otd:
            o.destroy()
        games_list_var = Variable(value=games_list)
        lbx1 = Listbox(listvariable=games_list_var, background='white',
                       font=font)
        lbx1.pack(anchor=NW, fill=X)
        lbl2 = Label(text='<No game>', font=font)
        lbl2.pack(anchor=N)

        def btn3_f():
            global game_chosen
            nonlocal lbl2
            if lbx1.curselection() != ():
                lbl2['text'] = lbx1.get(lbx1.curselection())
                game_chosen = lbx1.curselection()[0]

        btn3 = Button(text='Choose', font=font, command=btn3_f, width=10)
        btn3.pack(anchor=N)

        def btn4_f():
            global game_chosen, cut, rec, rec_file, rec_filename
            if game_chosen is not None:
                cut = 1
                if rec == 1:
                    tm = str(time.ctime())
                    rec_filename = f'{games_list_short[game_chosen]}_{tm[11:19].replace(":", "_")}' \
                                   f'_{tm[4:7]}_{tm[8:10].replace(" ", "0")}_{tm[-4:]}'
                    rec_file = open(f'Reports/{rec_filename}.txt', 'w+')
                    rec_file.close()
                sc.destroy()
            else:
                showwarning(title='Warning!', message='You have not chosen any game yet.')

        def btn11_f():
            nonlocal btn11
            global rec
            if rec == 0:
                btn11.destroy()
                btn11 = Button(text='Report: On ', font=font, command=btn11_f, width=10)
                btn11.place(relx=0.5, rely=0.8925, anchor=N)
                rec = 1
            elif rec == 1:
                btn11.destroy()
                btn11 = Button(text='Report: Off', font=font, command=btn11_f, width=10)
                btn11.place(relx=0.5, rely=0.8925, anchor=N)
                rec = 0

        def btn5_f():
            global game_chosen
            lbl2['text'] = '<No game>'
            game_chosen = None

        def btn6_f():
            otd = [lbl2, lbx1, btn3, btn4, btn11, btn5, btn6]
            for o in otd:
                o.destroy()
            sc.destroy()
            menu('')

        btn4 = Button(text='Run', font=font, command=btn4_f, width=10)
        btn4.pack(anchor=N)
        btn11 = Button(text='Report: Off', font=font, command=btn11_f, width=10)
        btn11.place(relx=0.5, rely=0.8925, anchor=N)
        btn5 = Button(text='Clear', font=font, command=btn5_f, width=5)
        btn5.pack(anchor=SW, side=LEFT)
        btn6 = Button(text='Back', font=font, command=btn6_f, width=5)
        btn6.pack(anchor=SE, side=RIGHT)

    def btn2_f():
        sc_n = 2
        otd = [lbl_, lbl0, lbl1, btn1, btn2, btn8, btn9, btn10]
        for o in otd:
            o.destroy()
        lbl3 = Label(text='Zakrevskiy Yuriy, 2025', font=font)
        lbl3.pack(anchor=CENTER, expand=True)

        def btn7_f():
            otd = [lbl3, btn7]
            for o in otd:
                o.destroy()
            sc.destroy()
            menu('')

        btn7 = Button(text='Back', font=font, command=btn7_f, width=5)
        btn7.pack(anchor=SE, side=RIGHT)

    lbl_ = Label(text="C.R.I.X.U.S.", font=font_b)
    lbl_.place(relx=0.5, rely=0.05, anchor=N)
    lbl0 = Label(text="Collection of Riddles for Intellectual eXperience, Unified Structurally",
                 font=font_s)
    lbl0.place(relx=0.5, rely=0.125, anchor=N)
    lbl1 = Label(text="You're welcome!", font=font)
    lbl1.place(relx=0.5, rely=0.225, anchor=N)
    btn1 = Button(text="Game list", font=font, command=btn1_f, width=10)
    btn1.place(relx=0.5, rely=0.325, anchor=N)
    btn8 = Button(text="Code editor", font=font, width=10)
    btn8.place(relx=0.5, rely=0.45, anchor=N)
    btn9 = Button(text="Manual", font=font, width=10)
    btn9.place(relx=0.5, rely=0.575, anchor=N)
    btn10 = Button(text="Settings", font=font, width=10)
    btn10.place(relx=0.5, rely=0.7, anchor=N)
    btn2 = Button(text="Credits", font=font, command=btn2_f, width=10)
    btn2.place(relx=0.5, rely=0.825, anchor=N)
    sc.mainloop()


def parser(code, evt):
    global images, database, cells, controls, events, variables, h, w
    flag = 'NOP'
    wls = []  # While start positions
    wle = []  # While end positions
    ifs = []  # If start positions
    ife = []  # If end positions
    ifv = []  # If values
    els = []  # Else start positions
    stm = 0
    stn = 0
    stl = 0
    brk = 0
    command = []
    ops = ['::', '+', '-', '*', '/', '^', '%',
           '+:', '-:', '*:', '/:', '^:', '%:']
    cps = ['&', '|', '~', '=', '<', '>', '~=', '<=', '>=']

    def er(ro, r):
        global images, cells, variables, cut
        ro_2 = 'Code " '
        for ri in ro:
            if ri[0] == 'v':
                ro_2 += f'v[{variables[int(ri[1:])][0]}]'
            elif ri[0] == 'c':
                ro_2 += f'c[{cells[int(ri[1:])][0]}]'
            elif ri[0] == 'i':
                ro_2 += f'i[{images[int(ri[1:])][0]}]'
            elif len(ri) >= 4 and ri[:2] == '"`' and ri[-2:] == '`"':
                ro_2 += f't[{ri[2:-2]}]'
            elif ri.isdigit():
                ro_2 += f'n[{ri}]'
            else:
                ro_2 += ri
            ro_2 += ' '
        ro_2 += f'" [line: {r}] causes an error.'
        return ro_2

    def interpreter(st):
        global images, database, cells, variables, h, w, rec, rec_stop
        nonlocal wls, wle, ifs, ife, ifv, els, stm, stn, stl, brk, line, evt
        if st[0][0] == 'v':
            st2 = []
            for j in st[2:]:
                if j[0] == 'v':
                    st2.append(str(variables[int(j[1:])][1]))
                elif j[0] == '-' and j[-1].isdigit():
                    st2.append(f'({j})')
                elif j == '/':
                    st2.append('//')
                elif j == '~':
                    st2.append(' not ')
                elif j == '&':
                    st2.append(' and ')
                elif j == '|':
                    st2.append(' or ')
                elif j == '=':
                    st2.append(' == ')
                elif j == '~=':
                    st2.append(' != ')
                else:
                    st2.append(j)
            var5 = eval(''.join(st2))
            if str(var5)[0] + str(var5)[-1] != '``':
                var5 = int(var5)
            else:
                var5 = '"' + str(var5) + '"'
            if st[1] == '::':
                variables[int(st[0][1:])][1] = var5
            elif st[1] == '+:':
                variables[int(st[0][1:])][1] += var5
            elif st[1] == '-:':
                variables[int(st[0][1:])][1] -= var5
            elif st[1] == '*:':
                variables[int(st[0][1:])][1] *= var5
            elif st[1] == '/:':
                variables[int(st[0][1:])][1] //= var5
            elif st[1] == '^:':
                variables[int(st[0][1:])][1] **= var5
            elif st[1] == '%:':
                variables[int(st[0][1:])][1] %= var5
        if len(st) == 3 and st[0][0] == 'c' and st[1] == '::' and st[2][0] == 'i':
            cells[int(st[0][1:])][2] = images[int(st[2][1:])][1]
            cells[int(st[0][1:])][3] = images[int(st[2][1:])][0]
        if len(st) == 3 and st[0][0] == 'c' and st[1] == '::' and st[2][0] == 'c':
            cells[int(st[0][1:])][2] = cells[int(st[2][1:])][2]
            cells[int(st[0][1:])][3] = cells[int(st[2][1:])][3]
        if st[0][0] == '@':
            st2 = []
            for j in st[1:]:
                if j[0] == 'v':
                    st2.append(str(variables[int(j[1:])][1]))
                elif j[0] == '-' and j[-1].isdigit():
                    st2.append(f'({j})')
                elif j == '/':
                    st2.append('//')
                elif j == '~':
                    st2.append(' not ')
                elif j == '&':
                    st2.append(' and ')
                elif j == '|':
                    st2.append(' or ')
                elif j == '=':
                    st2.append(' == ')
                elif j == '~=':
                    st2.append(' != ')
                else:
                    st2.append(j)
            var5 = eval(''.join(st2))
            if var5 == 0 or var5 is False:
                if wle[int(st[0][1:-1])] == -1:
                    stm = -1 * (int(st[0][1:-1]) + 1)
                    brk = 1
                else:
                    stm = wle[int(st[0][1:-1])]
        if st[0][0] == '#':
            ln2 = int(st[0][1:])
            for _ in range(1, len(wls)+1):
                if wle[len(wls)-_] == -1 and wls[len(wls) - _] < line:
                    stm = -1 * ((len(wls)-_) + 1)
                    brk = 1
                    break
                if wls[len(wls)-_] < ln2 < wle[len(wls)-_]:
                    stm = wle[len(wls)-_]
                    break
        if st[0][0] == '$':
            ln2 = int(st[0][1:])
            for _ in range(1,len(wls)+1):
                if wls[len(wls)-_] < ln2 < wle[len(wls)-_]:
                    stm = wls[len(wls)-_] - 1
        if st[0][0] == '?':
            st2 = []
            for j in st[1:]:
                if j[0] == 'v':
                    st2.append(str(variables[int(j[1:])][1]))
                elif j[0] == '-' and j[-1].isdigit():
                    st2.append(f'({j})')
                elif j == '/':
                    st2.append('//')
                elif j == '~':
                    st2.append(' not ')
                elif j == '&':
                    st2.append(' and ')
                elif j == '|':
                    st2.append(' or ')
                elif j == '=':
                    st2.append(' == ')
                elif j == '~=':
                    st2.append(' != ')
                else:
                    st2.append(j)
            var5 = eval(''.join(st2))
            if var5 == 0 or var5 is False:
                ifv[int(st[0][1:-1])] = False
            else:
                ifv[int(st[0][1:-1])] = True
            if var5 == 0 or var5 is False:
                if els[int(st[0][1:-1])] == -1:
                    stl = -1 * (int(st[0][1:-1]) + 1)
                else:
                    stl = els[int(st[0][1:-1])]
        if st[0][0] == '!' and ifv[int(st[0][1:-1])] is True:
            if ife[int(st[0][1:-1])] == -1:
                stn = -1 * (int(st[0][1:-1]) + 1)
            else:
                stn = ife[int(st[0][1:-1])]
        if rec == 1 and (rec_stop <= 5000 or evt == 1):
            rec_stop = record('=' * 32)
            if not (evt == 0 and rec_stop >= 5000):
                record(' '.join(st) + f' [line: {line}]')
                record('Variables:')
                for _ in variables:
                    record(f'{_[0]} = {_[1]}')
                record('Cells:')
                for _ in cells:
                    record(f'{_[0]} : {_[3]}')
                record('Conditions:')
                for _ in range(len(ifv)):
                    record(f'[Lines {ifs[_]}:{els[_]}] {str(ifv[_])}')
            else:
                record('.' * 32)
                record('.' * 32)
                record('.' * 32)

    line = 1
    while line < len(code):
        tokens = code[line - 1][0]
        if flag in ['MYN', 'EVT'] and tokens[-1] != '\\' and tokens[-1] != '***':
            tokens.append('***')
        if tokens[0][0] == '{':
            line += 1
            continue
        for token in tokens:
            if token == '<I>' and stm == 0 and stn == 0 and stl == 0:
                flag = 'IMG'
            elif token == '<D>' and stm == 0 and stn == 0 and stl == 0:
                flag = 'DTB'
            elif token == '<B>' and stm == 0 and stn == 0 and stl == 0:
                flag = 'BRD'
            elif token == '<M>' and stm == 0 and stn == 0 and stl == 0:
                flag = 'MYN'
            elif token == '<E>' and stm == 0 and stn == 0 and stl == 0:
                flag = 'EVT'
            elif token == '<C>' and stm == 0 and stn == 0 and stl == 0:
                flag = 'CTR'
            elif token.find('</') == 0 and stm == 0 and stn == 0 and stl == 0:
                flag = 'NOP'
                if token == '</M>' and len(command) > 0:
                    try:
                        interpreter(command)
                    except:
                        return er(command, line)
            else:
                if flag == 'IMG' and stm == 0 and stn == 0 and stl == 0:
                    if token.count(',') == 1:
                        try:
                            var1 = token.find(',')
                            images.append([token[:var1], pg.image.load(f'Images/{token[var1 + 1:]}')])
                        except:
                            return f'Code {token} [line: {line}] causes an error.'
                elif flag == 'DTB' and stm == 0 and stn == 0 and stl == 0:
                    try:
                        dtb = open(f'Database/{token}', 'r', encoding='utf8')
                        dtb_lines = dtb.readlines()
                        database = [len(dtb_lines), dtb_lines]
                    except:
                        return f'Code {token} [line: {line}] causes an error.'
                elif flag == 'BRD' and stm == 0 and stn == 0 and stl == 0:
                    if token.count(',') == 1:
                        try:
                            w, h = map(int, token.split(','))
                        except:
                            return f'Code {token} [line: {line}] causes an error.'
                    elif token.count(',') == 4:
                        try:
                            cells.append([])
                            var2 = token.split(',')
                            cells[-1].append(var2[0])
                            cells[-1].append([*map(int, var2[1:])])
                            cells[-1].append(None)
                            cells[-1].append(None)
                        except:
                            return f'Code {token} [line: {line}] causes an error.'
                elif flag == 'MYN' or evt == 1:
                    if evt == 1:
                        try:
                            t = token.replace('<X>', f'n[{coordinates()[0]}]')
                            t = token.replace('<Y>', f'n[{coordinates()[1]}]')
                        except:
                            t = token
                    try:
                        t = token.replace('<L>', database[0])
                    except:
                        t = token
                    pl = 0
                    pr = 0
                    lb = ''
                    rb = ''
                    tc = 0
                    while tc < len(token):
                        if t[tc] == '(':
                            pl += 1
                            lb += '('
                        elif t[tc] == '~':
                            pl += 1
                            lb += '~'
                        else:
                            break
                        tc += 1
                    tc = -1
                    while tc >= -len(token):
                        if t[tc] in '.,:;)':
                            pr += 1
                            if t[tc] == ')':
                                rb += ')'
                            if t[tc] == '.' and len(wls) + len(ifs) > 0:
                                wl_j = -1
                                if_j = -1
                                while True:
                                    if len(wls) > 0 and len(ifs) > 0:
                                        if wl_j >= -len(wls) and if_j >= -len(ifs):
                                            if wls[wl_j] > ifs[if_j]:
                                                if wle[wl_j] == -1 and line not in wle and line not in ife:
                                                    wle[wl_j] = line
                                                    break
                                                else:
                                                    wl_j -= 1
                                            elif wls[wl_j] <= ifs[if_j]:
                                                if ife[if_j] == -1 and line not in wle and line not in ife:
                                                    ife[if_j] = line
                                                    break
                                                else:
                                                    if_j -= 1
                                        elif wl_j >= -len(wls):
                                            if wle[wl_j] == -1 and line not in wle and line not in ife:
                                                wle[wl_j] = line
                                                break
                                            else:
                                                wl_j -= 1
                                        elif if_j >= -len(ifs):
                                            if ife[if_j] == -1 and line not in wle and line not in ife:
                                                ife[if_j] = line
                                                break
                                            else:
                                                if_j -= 1
                                        else:
                                            break
                                    elif len(wls) > 0 and wl_j >= -len(wls):
                                        if wle[wl_j] == -1 and line not in wle and line not in ife:
                                            wle[wl_j] = line
                                            break
                                        else:
                                            wl_j -= 1
                                    elif len(ifs) > 0 and if_j >= -len(ifs):
                                        if ife[if_j] == -1 and line not in wle and line not in ife:
                                            ife[if_j] = line
                                            break
                                        else:
                                            if_j -= 1
                                    else:
                                        break
                                if stm == 0:
                                    for _ in range(len(wls)):
                                        if wle[_] == line:
                                            line = wls[_] - 1
                                            break
                        else:
                            break
                        tc -= 1
                    if t[pl] == 'v' and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0 and (command[-1][-1].isdigit() or command[-1][-1] == '"'):
                                interpreter(command)
                                command = []
                            var_name = t[2 + pl:-1 - pr]
                            var4 = 0
                            for _ in variables:
                                if _[0] == var_name:
                                    for _ in lb:
                                        command.append(_)
                                    command.append(f'v{str(var4)}')
                                    for _ in rb:
                                        command.append(_)
                                    break
                                var4 += 1
                            if var4 == len(variables):
                                for _ in lb:
                                    command.append(_)
                                command.append(f'v{str(len(variables))}')
                                for _ in rb:
                                    command.append(_)
                                variables.append([var_name, None])
                        except:
                            return er(command, line)
                    elif t[pl] == 'n' and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0 and (command[-1][-1].isdigit() or command[-1][-1] == '"'):
                                interpreter(command)
                                command = []
                            for _ in lb:
                                command.append(_)
                            command.append(t[2 + pl:-1 - pr])
                            for _ in rb:
                                command.append(_)
                        except:
                            return er(command, line)
                    elif t[pl] == 'r' and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0 and (command[-1][-1].isdigit() or command[-1][-1] == '"'):
                                interpreter(command)
                                command = []
                            for _ in lb:
                                command.append(_)
                            command.append(str(random.randint(*map(int, t[2 + pl:-1 - pr].split(',')))))
                            for _ in rb:
                                command.append(_)
                        except:
                            return er(command, line)
                    elif t[pl] == 't' and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0 and (command[-1][-1].isdigit() or command[-1][-1] == '"'):
                                interpreter(command)
                                command = []
                            for _ in lb:
                                command.append(_)
                            command.append(f'"`{t[2 + pl:-1 - pr]}`"')
                            for _ in rb:
                                command.append(_)
                        except:
                            return er(command, line)
                    elif t in ops and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0 and not (command[-1][-1].isdigit() or
                                                         (command[-1] == ')' and command[-2][-1].isdigit())):
                                interpreter(command)
                                command = []
                            command.append(t)
                        except:
                            return er(command, line)
                    elif t in cps and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0 and not (command[-1][-1].isdigit() or
                                                         (command[-1] == ')' and command[-2][-1].isdigit())):
                                interpreter(command)
                                command = []
                            command.append(t)
                        except:
                            return er(command, line)
                    elif t == '@':
                        try:
                            if stm == 0 and stn == 0 and stl == 0 and len(command) > 0:
                                interpreter(command)
                                command = []
                            if line not in wls:
                                wls.append(line)
                                wle.append(-1)
                            if stm == 0 and stn == 0 and stl == 0:
                                st4 = 0
                                for _ in wls:
                                    if _ == line:
                                        command = [f'{t}{st4}:']
                                        break
                                    st4 += 1
                        except:
                            return er(command, line)
                    elif t[0] == '#':
                        try:
                            if stm == 0 and stn == 0 and stl == 0 and len(command) > 0:
                                interpreter(command)
                                command = []
                        except:
                            return er(command, line)
                        try:
                            if stm == 0 and stn == 0 and stl == 0:
                                command = [f'{t[0]}{line}']
                                interpreter(command)
                                command = []
                        except:
                            return er(command, line)
                    elif t[0] == '$':
                        try:
                            if stm == 0 and stn == 0 and stl == 0 and len(command) > 0:
                                interpreter(command)
                                command = []
                        except:
                            return er(command, line)
                        try:
                            if stm == 0 and stn == 0 and stl == 0:
                                command = [f'{t[0]}{line}']
                                interpreter(command)
                                command = []
                        except:
                            return er(command, line)
                    elif t == '?':
                        try:
                            if stm == 0 and stn == 0 and stl == 0 and len(command) > 0:
                                interpreter(command)
                                command = []
                            if line not in ifs:
                                ifs.append(line)
                                ife.append(-1)
                                els.append(-1)
                                ifv.append(None)
                            if stm == 0 and stn == 0 and stl == 0:
                                st4 = 0
                                for _ in ifs:
                                    if _ == line:
                                        command = [f'{t}{st4}:']
                                        break
                                    st4 += 1
                        except:
                            return er(command, line)
                    elif t == '!':
                        try:
                            if stm == 0 and stn == 0 and stl == 0 and len(command) > 0:
                                interpreter(command)
                                command = []
                            for _ in range(1, len(ifs) + 1):
                                if ife[len(ifs) - _] == -1 and ifs[len(ifs) - _] < line:
                                    els[len(ifs) - _] = line
                                    break
                                elif ifs[len(ifs) - _] < line < ife[len(ifs) - _]:
                                    els[len(ifs) - _] = line
                                    break
                            if stl < 0 and els[-1 * (stl + 1)] != -1:
                                stl = 0
                                command = []
                        except:
                            return er(command, line)
                        try:
                            if stm == 0 and stn == 0 and stl == 0:
                                st4 = 0
                                for _ in els:
                                    if _ == line:
                                        command = [f'{t}{st4}:']
                                        interpreter(command)
                                        command = []
                                        break
                                    st4 += 1
                        except:
                            return er(command, line)
                    elif t[pl] == 'e' and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0:
                                interpreter(command)
                                command = []
                            e_name = t[2 + pl:-1 - pr]
                            var6 = 0
                            for _ in cells:
                                if _[0] == e_name:
                                    cells[var6][2] = None
                                    break
                                var6 += 1
                            for _ in lb:
                                command.append(_)
                            for _ in rb:
                                command.append(_)
                        except:
                            return er(command, line)
                    elif t[pl] == 'c' and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0 and command[-1] != '::':
                                interpreter(command)
                                command = []
                            cell_name = t[2 + pl:-1 - pr]
                            var7 = 0
                            for _ in cells:
                                if _[0] == cell_name:
                                    for _ in lb:
                                        command.append(_)
                                    command.append(f'c{str(var7)}')
                                    for _ in rb:
                                        command.append(_)
                                    break
                                var7 += 1
                            if var7 == len(cells):
                                for _ in lb:
                                    command.append(_)
                                command.append(f'c{str(len(cells))}')
                                for _ in rb:
                                    command.append(_)
                                cells.append([cell_name, [0, 0, w-1, h-1], None])
                        except:
                            return er(command, line)
                    elif t[pl] == 'i' and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0 and command[-1] != '::':
                                interpreter(command)
                                command = []
                            img_name = t[2 + pl:-1 - pr]
                            var8 = 0
                            for _ in images:
                                if _[0] == img_name:
                                    for _ in lb:
                                        command.append(_)
                                    command.append(f'i{str(var8)}')
                                    for _ in rb:
                                        command.append(_)
                                    break
                                var8 += 1
                        except:
                            return er(command, line)
                    elif t[pl] == 'd' and len(database) > 0 and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if len(command) > 0 and (command[-1][-1].isdigit() or command[-1][-1] == '"'):
                                interpreter(command)
                                command = []
                            dbl = ['']
                            for q in t[2 + pl:-1 - pr]:
                                if q == ':':
                                    dbl.append('')
                                else:
                                    dbl[-1] += q
                            ln = f'database[1][{dbl[0]}][:-1][{dbl[1]}:{dbl[2]}:{dbl[3]}]'
                            for _ in lb:
                                command.append(_)
                            command.append(f'"`{eval(ln)}`"')
                            for _ in rb:
                                command.append(_)
                        except:
                            return er(command, line)
                    elif t[0] == 'w' and evt == 1 and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if stm == 0 and stn == 0 and stl == 0 and len(command) > 0:
                                interpreter(command)
                                command = []
                        except:
                            return er(command, line)
                        try:
                            print(int(t[2:-1]))
                            pg.time.wait(int(t[2:-1]))
                        except:
                            return f'Code {token} [line: {line}] causes an error.'
                    elif t == '***' and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if stm == 0 and stn == 0 and stl == 0 and len(command) > 0:
                                interpreter(command)
                                command = []
                        except:
                            return er(command, line)
                    elif len(t) >= 3 and t[pl:pl + 3] == '<Q>' and evt == 1 and stm == 0 and stn == 0 and stl == 0:
                        try:
                            if stm == 0 and stn == 0 and stl == 0 and len(command) > 0:
                                interpreter(command)
                                command = []
                        except:
                            return er(command, line)
                        if stm == 0 and stn == 0 and stl == 0:
                            return 'quit'
                    elif [stm, stn, stl] == [0, 0, 0] and t not in ['\\', '.']:
                        return f'Code {token} [line: {line}] causes an error.'
                elif flag == 'EVT' and stm == 0 and stn == 0 and stl == 0:
                    if len(token) > 4 and token[:3] == '>>>' and token[-1] == ':':
                        events.append([token[3:-1], []])
                        break
                    elif token != '<<<':
                        events[-1][1].append(code[line - 1])
                        break
                elif flag == 'CTR' and stm == 0 and stn == 0 and stl == 0:
                    if token.count(',') == 1:
                        try:
                            var3 = token.split(',')
                            controls.append([])
                            controls[-1].append(var3[0])
                            controls[-1].append(None)
                            controls[-1].append(var3[1])
                        except:
                            return f'Code {token} [line: {line}] causes an error.'
                    if token.count(',') == 2:
                        try:
                            var3 = token.split(',')
                            controls.append([])
                            controls[-1].append(var3[0])
                            controls[-1].append(var3[1])
                            controls[-1].append(var3[2])
                        except:
                            return f'Code {token} [line: {line}] causes an error.'
        if stm > 0:
            line = int(stm) + 1
            stm = 0
            command = []
        elif stm < 0 and wle[-1 * (stm + 1)] != -1:
            if brk == 1:
                line = wle[-1 * (stm + 1)] + 1
                brk = 0
            stm = 0
            command = []
        elif stn > 0:
            line = int(stn) + 1
            stn = 0
            command = []
        elif stn < 0 and ife[-1 * (stn + 1)] != -1:
            stn = 0
            command = []
            line += 1
        elif stl > 0:
            line = int(stl)
            stl = 0
            command = []
        elif stl < 0 and ife[-1 * (stl + 1)] != -1:
            line = ife[-1 * (stl + 1)] + 1
            stl = 0
            command = []
        else:
            line += 1


downloader()
while True:
    if game_chosen is None:
        menu(err0r)
    cut = 0
    if game_chosen is None:
        break
    err0r = parser(games[game_chosen], 0)
    if h != 0 and w != 0 and (err0r == '' or err0r is None):
        pg.init()
        clock = pg.time.Clock()
        sc2 = pg.display.set_mode((w, h))
        pg.display.set_caption(games_list[game_chosen])
        sc2.fill((0, 0, 0))
        cut2 = 0
    else:
        cut2 = 1
    while cut2 == 0:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                cut2 = 1
                pg.quit()
                break
            if i.type == pg.KEYUP:
                if i.key == pg.K_ESCAPE:
                    cut2 = 1
                    pg.quit()
                    break
                if 0 <= i.key <= 255:
                    for control in controls:
                        if control[0] == chr(i.key):
                            if control[1] is None:
                                for event_ in events:
                                    if event_[0] == control[2]:
                                        q = parser(event_[1], 1)
                                        if q == 'quit':
                                            cut2 = 1
                                            pg.quit()
                                            break
                            else:
                                for cell_ in cells:
                                    [x, y] = coordinates()
                                    [x1, y1, x2, y2] = cell_[1]
                                    if cell_[0] == control[1] and x1 <= x <= x2 and y1 <= y <= y2:
                                        for event_ in events:
                                            if event_[0] == control[2]:
                                                q = parser(event_[1], 1)
                                                if q == 'quit':
                                                    cut2 = 1
                                                    pg.quit()
                                                    break
            if i.type == pg.MOUSEBUTTONUP:
                if i.button == 1:
                    _k = '<'
                elif i.button == 2:
                    _k = '>'
                else:
                    continue
                for control in controls:
                    if control[0] == _k:
                        if control[1] is None:
                            for event_ in events:
                                if event_[0] == control[2]:
                                    q = parser(event_[1], 1)
                                    if q == 'quit':
                                        cut2 = 1
                                        pg.quit()
                                        break
                        else:
                            for cell_ in cells:
                                [x, y] = coordinates()
                                [x1, y1, x2, y2] = cell_[1]
                                if cell_[0] == control[1] and x1 <= x <= x2 and y1 <= y <= y2:
                                    for event_ in events:
                                        if event_[0] == control[2]:
                                            q = parser(event_[1], 1)
                                            if q == 'quit':
                                                cut2 = 1
                                                pg.quit()
                                                break

        if cut2 == 0:
            for cell in cells:
                if cell[2] is not None:
                    sc2.blit(cell[2], (cell[1][0], cell[1][1]))

            pg.display.update()
            clock.tick(FPS)
        else:
            break
    game_chosen = None
    images = []
    database = []
    cells = []
    controls = []
    events = []
    variables = []
    h, w = 0, 0
    cut = 0
    rec = 0
    rec_file = None
    rec_filename = ''
    rec_stop = 0
