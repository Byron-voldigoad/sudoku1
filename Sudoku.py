from tkinter import*
import random

nbr_list = [1,2,3,4,5,6,7,8,9]

row1 = []
row11 = []
row2 = []
row12 = []
row3 = []
row13 = []
r0 = 0
r1 = 0
r2 = 0
def table_clear():
    row1.clear()
    row11.clear()
    row2.clear()
    row12.clear()
    row3.clear()
    row13.clear()

def sudoku_start():
    global nbr_list,r0,r1,r2
    #***************************frame[1][0]*********************************************
    for row in range(3):
        for column in range(3):
            a = random.choice(nbr_list)
            b = random.choice(nbr_list)
            row1.append(a)
            num_remove = random.randint(1, 3)
            btn1[row][column]["text"] = a
            nbr_list.remove(a)
    for i in range(3):
        row11a = []
        for j in range(3):
            if row1:
                row11a.append(row1.pop(0))
        row11.append(row11a)

    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #***************************************************************
    #***************************frame[1][1]*********************************************
    for row in range(3):
        for column in range(3):
            b = random.choice(nbr_list)
            row2.append(b)
            nbr_list.remove(b)
    for i in range(3):
        row12a = []
        for j in range(3):
            if row2:
                row12a.append(row2.pop(0))
        row12.append(row12a)
    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # ***************************frame[1][2]*********************************************
    for row in range(3):
        for column in range(3):
            c = random.choice(nbr_list)
            row3.append(c)
            nbr_list.remove(c)
    for i in range(3):
        row13a = []
        for j in range(3):
            if row3:
                row13a.append(row3.pop(0))
        row13.append(row13a)

    def similaire_frame2():
#*********************  gere les repetitions ligne 1 frame 2************************************************************************
        for i in range(3):
            a = row12[0][i]
            if row12[0][i] == row11[0][0] or row12[i][i] == row11[i][i]:
                a = row12[0][i]
                if row12[1][i] == row11[0][0] or row12[1][i] == row11[0][1] or row12[1][i] == row11[0][2]: #verifie si l'une des valeurs des autre lignes nest pas deja presente sur cette ligne
                    row12[0][i] = row12[2][i]
                    row12[2][i] = a
                else:
                    row12[0][i] = row12[1][i]
                    row12[1][i] = a
            elif row12[0][i] == row11[0][1]:
                if row12[1][i] == row11[0][0] or row12[1][i] == row11[0][1] or row12[1][i] == row11[0][2]:
                    row12[0][i] = row12[2][i]
                    row12[2][i] = a
                else:
                    row12[0][i] = row12[1][i]
                    row12[1][i] = a
            elif row12[0][i] == row11[0][2]:
                if row12[1][i] == row11[0][0] or row12[1][i] == row11[0][1] or row12[1][i] == row11[0][2]:
                    row12[0][i] = row12[2][i]
                    row12[2][i] = a
                else:
                    row12[0][i] = row12[1][i]
                    row12[1][i] = a
            # *********************repetition ligne 2 frame 2************************************************************************
            for i in range(3):
                a = row12[1][i]
                if row12[1][i] == row11[1][0] or row12[i][i] == row11[i][i]:
                    if row12[0][i] == row11[1][0] or row12[0][i] == row11[1][1] or row12[0][i] == row11[1][2]:
                        row12[1][i] = row12[2][i]
                        row12[2][i] = a

                    else:
                        row12[1][i] = row12[0][i]
                        row12[0][i] = a
                elif row12[1][i] == row11[1][1]:
                    if row12[0][i] == row11[1][0] or row12[0][i] == row11[1][1] or row12[0][i] == row11[1][2]:
                        row12[1][i] = row12[2][i]
                        row12[2][i] = a

                    else:
                        row12[1][i] = row12[0][i]
                        row12[0][i] = a
                elif row12[1][i] == row11[1][2]:
                    if row12[0][i] == row11[1][0] or row12[0][i] == row11[1][1] or row12[0][i] == row11[1][2]:
                        row12[1][i] = row12[2][i]
                        row12[2][i] = a

                    else:
                        row12[1][i] = row12[0][i]
                        row12[0][i] = a

            # *********************repetition ligne 3 frame 2************************************************************************
            for i in range(3):
                a = row12[2][i]
                if row12[2][i] == row11[2][0] or row12[i][i] == row11[i][i]:
                    if row12[1][i] == row11[2][0] or row12[1][i] == row11[2][1] or row12[1][i] == row11[2][2]:
                        row12[2][i] = row12[0][i]
                        row12[0][i] = a

                    else:
                        row12[2][i] = row12[1][i]
                        row12[1][i] = a

                elif row12[2][i] == row11[2][1]:
                    if row12[1][i] == row11[2][0] or row12[1][i] == row11[2][1] or row12[1][i] == row11[2][2]:
                        row12[2][i] = row12[0][i]
                        row12[0][i] = a

                    else:
                        row12[2][i] = row12[1][i]
                        row12[1][i] = a

                elif row12[2][i] == row11[2][2]:
                    if row12[1][i] == row11[2][0] or row12[1][i] == row11[2][1] or row12[1][i] == row11[2][2] :
                        row12[2][i] = row12[0][i]
                        row12[0][i] = a

                    else:
                        row12[2][i] = row12[1][i]
                        row12[1][i] = a
    #*************************************************************************************************************
    def similaire_frame3():
    # ********************* fonction qui gere les repetitions ligne 1 frame 3************************************************************************
    #***********frame 1 et frame 3
         # *********************  gere les repetitions ligne 1 frame 3 avec ceux de la frame 1*****************************
         for i in range(3):
             b = row13[0][i]
             if row13[0][i] == row11[0][0] or  row13[i][i] == row11[i][i]:
                 b = row13[0][i]
                 if row13[1][i] == row11[0][0] or row13[1][i] == row11[0][1] or row13[1][i] == row11[0][2]:  # verifie si l'une des valeurs des autre lignes nest pas deja presente sur cette ligne
                     row13[0][i] = row13[2][i]
                     row13[2][i] = b
                 else:
                     row13[0][i] = row13[1][i]
                     row13[1][i] = b
             elif row13[0][i] == row11[0][1]:
                 if row13[1][i] == row11[0][0] or row13[1][i] == row11[0][1] or row13[1][i] == row11[0][2]:
                     row13[0][i] = row13[2][i]
                     row13[2][i] = b
                 else:
                     row13[0][i] = row13[1][i]
                     row13[1][i] = b
             elif row13[0][i] == row11[0][2]:
                 if row13[1][i] == row11[0][0] or row13[1][i] == row11[0][1] or row13[1][i] == row11[0][2]:
                     row13[0][i] = row13[2][i]
                     row13[2][i] = b
                 else:
                     row13[0][i] = row13[1][i]
                     row13[1][i] = b
         # *********************repetition ligne 2 frame 3 avec ceux de la frame 1***************************************
         for i in range(3):
             b = row13[1][i]
             if row13[1][i] == row11[1][0] or row13[i][i] == row11[i][i]:
                 b = row13[1][i]
                 if row13[0][i] == row11[1][0] or row13[0][i] == row11[1][1] or row13[0][i] == row11[1][2]:
                     row13[1][i] = row13[2][i]
                     row13[2][i] = b

                 else:
                     row13[1][i] = row13[0][i]
                     row13[0][i] = b
             elif row13[1][i] == row11[1][1]:
                 if row13[0][i] == row11[1][0] or row13[0][i] == row11[1][1] or row13[0][i] == row11[1][2]:
                                 row13[1][i] = row13[2][i]
                                 row13[2][i] = b

                 else:
                     row13[1][i] = row13[0][i]
                     row13[0][i] = b
             elif row13[1][i] == row11[1][2]:
                 if row13[0][i] == row11[1][0] or row13[0][i] == row11[1][1] or row13[0][i] == row11[1][2]:
                     row13[1][i] = row13[2][i]
                     row13[2][i] = b

                 else:
                     row13[1][i] = row13[0][i]
                     row13[0][i] = b
         # *********************repetition ligne 3 frame 3 avec ceux de la frame 1***************************************
         for i in range(3):
                     b = row13[2][i]
                     if row13[2][i] == row11[2][0] or row13[i][i] == row11[i][i]:
                         b = row13[2][i]
                         if row13[1][i] == row11[2][0] or row13[1][i] == row11[2][1] or row13[1][i] == row11[2][2]:
                             row13[2][i] = row13[0][i]
                             row13[0][i] = b

                         else:
                             row13[2][i] = row13[1][i]
                             row13[1][i] = b

                     elif row13[2][i] == row11[2][1]:
                         if row13[1][i] == row11[2][0] or row13[1][i] == row11[2][1] or row13[1][i] == row11[2][2]:
                             row13[2][i] = row13[0][i]
                             row13[0][i] = b

                         else:
                             row13[2][i] = row13[1][i]
                             row13[1][i] = b

                     elif row13[2][i] == row11[2][2]:
                         if row13[1][i] == row11[2][0] or row13[1][i] == row11[2][1] or row13[1][i] == row11[2][2]:
                             row13[2][i] = row13[0][i]
                             row13[0][i] = b

                         else:
                             row13[2][i] = row13[1][i]
                             row13[1][i] = b
    # ***********frame 2 et frame 3
        # *********************  gere les repetitions ligne 1 frame 3 avec ceux de la frame 1*****************************
    def similaire_frame3_2():
         for i in range(3):
                ab = row13[0][i]
                if row13[0][i] == row12[0][0] or row13[i][i] == row12[i][i]:
                    ab = row13[0][i]
                    if row13[1][i] == row12[0][0] or row13[1][i] == row12[0][1] or row13[1][i] == row12[0][2]:  # verifie si l'une des valeurs des autre lignes nest pas deja presente sur cette ligne
                        row13[0][i] = row13[2][i]
                        row13[2][i] = ab
                    else:
                        row13[0][i] = row13[1][i]
                        row13[1][i] = ab
                elif row13[0][i] == row12[0][1]:
                    if row13[1][i] == row12[0][0] or row13[1][i] == row12[0][1] or row13[1][i] == row12[0][2]:
                        row13[0][i] = row13[2][i]
                        row13[2][i] = ab
                    else:
                        row13[0][i] = row13[1][i]
                        row13[1][i] = ab
                elif row13[0][i] == row12[0][2]:
                    if row13[1][i] == row12[0][0] or row13[1][i] == row12[0][1] or row13[1][i] == row12[0][2]:
                        row13[0][i] = row13[2][i]
                        row13[2][i] = ab
                    else:
                        row13[0][i] = row13[1][i]
                        row13[1][i] = ab
                # *********************repetition ligne 2 frame 3 avec ceux de la frame 1***************************************
         for i in range(3):
                ab = row13[1][i]
                if row13[1][i] == row12[1][0] or row13[i][i] == row12[i][i]:
                    ab = row13[1][i]
                    if row13[0][i] == row12[1][0] or row13[0][i] == row12[1][1] or row13[0][i] == row12[1][2]:
                        row13[1][i] = row13[2][i]
                        row13[2][i] = ab

                    else:
                        row13[1][i] = row13[0][i]
                        row13[0][i] = ab
                elif row13[1][i] == row12[1][1]:
                    if row13[0][i] == row12[1][0] or row13[0][i] == row12[1][1] or row13[0][i] == row12[1][2]:
                        row13[1][i] = row13[2][i]
                        row13[2][i] = ab

                    else:
                        row13[1][i] = row13[0][i]
                        row13[0][i] = ab
                elif row13[1][i] == row12[1][2]:
                    if row13[0][i] == row12[1][0] or row13[0][i] == row12[1][1] or row13[0][i] == row12[1][2]:
                        row13[1][i] = row13[2][i]
                        row13[2][i] = ab

                    else:
                        row13[1][i] = row13[0][i]
                        row13[0][i] = ab
                # *********************repetition ligne 3 frame 3 avec ceux de la frame 1***************************************
         for i in range(3):
                ab = row13[2][i]
                if row13[2][i] == row12[2][0] or row13[i][i] == row12[i][i]:
                    ab = row13[2][i]
                    if row13[1][i] == row12[2][0] or row13[1][i] == row12[2][1] or row13[1][i] == row12[2][2]:
                        row13[2][i] = row13[0][i]
                        row13[0][i] = ab

                    else:
                        row13[2][i] = row13[1][i]
                        row13[1][i] = ab

                elif row13[2][i] == row12[2][1]:
                    if row13[1][i] == row12[2][0] or row13[1][i] == row12[2][1] or row13[1][i] == row12[2][2]:
                        row13[2][i] = row13[0][i]
                        row13[0][i] = ab

                    else:
                        row13[2][i] = row13[1][i]
                        row13[1][i] = ab

                elif row13[2][i] == row12[2][2]:
                    if row13[1][i] == row12[2][0] or row13[1][i] == row12[2][1] or row13[1][i] == row12[2][2]:
                        row13[2][i] = row13[0][i]
                        row13[0][i] = ab

                    else:
                        row13[2][i] = row13[1][i]
                        row13[1][i] = b
    print("Row1", row11[0])
    print("Row2", row12[0])
    similaire_frame2()
    similaire_frame3()
    similaire_frame3_2()

#*****************************************************************************************************
    for i in range(9):
        btn1_1[i//3][i%3]["text"] = row12[i//3][i%3]
        btn1_2[i // 3][i % 3]["text"] = row13[i // 3][i % 3]

    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #***************************************************************
    for i in range(9):
        if btn1_1[i//3][i % 3]["text"] == 1:
                btn1_1[i//3][i % 3]["bg"] = color[0][0]
        if btn1_1[i//3][i % 3]["text"] == 2:
            btn1_1[i//3][i % 3]["bg"] = color[0][1]
        if btn1_1[i//3][i % 3]["text"] == 3 :
            btn1_1[i//3][i % 3]["bg"] = color[0][2]
        if btn1_1[i//3][i % 3]["text"] == 4:
            btn1_1[i//3][i % 3]["bg"] = color[1][0]
        if btn1_1[i//3][i % 3]["text"] == 5:
            btn1_1[i//3][i % 3]["bg"] = color[1][1]
        if btn1_1[i//3][i % 3]["text"] == 6:
            btn1_1[i//3][i % 3]["bg"] = color[1][2]
        if btn1_1[i//3][i % 3]["text"] == 7:
            btn1_1[i//3][i % 3]["bg"] = color[2][0]
        if btn1_1[i//3][i % 3]["text"] == 8:
            btn1_1[i//3][i % 3]["bg"] = color[2][1]
        if btn1_1[i//3][i % 3]["text"] == 9:
            btn1_1[i//3][i % 3]["bg"] = color[2][2]
        if btn1[i//3][i % 3]["text"] == 1:
            btn1[i//3][i % 3]["bg"] = color[0][0]
        if btn1[i//3][i % 3]["text"] == 2:
            btn1[i//3][i % 3]["bg"] = color[0][1]
        if btn1[i // 3][i % 3]["text"] == 3:
            btn1[i // 3][i % 3]["bg"] = color[0][2]
        if btn1[i // 3][i % 3]["text"] == 4:
            btn1[i // 3][i % 3]["bg"] = color[1][0]
        if btn1[i // 3][i % 3]["text"] == 5:
            btn1[i // 3][i % 3]["bg"] = color[1][1]
        if btn1[i // 3][i % 3]["text"] == 6:
            btn1[i // 3][i % 3]["bg"] = color[1][2]
        if btn1[i // 3][i % 3]["text"] == 7:
            btn1[i // 3][i % 3]["bg"] = color[2][0]
        if btn1[i // 3][i % 3]["text"] == 8:
            btn1[i // 3][i % 3]["bg"] = color[2][1]
        if btn1[i // 3][i % 3]["text"] == 9:
            btn1[i // 3][i % 3]["bg"] = color[2][2]
        if btn1_2[i//3][i % 3]["text"] == 1:
            btn1_2[i//3][i % 3]["bg"] = color[0][0]
        if btn1_2[i//3][i % 3]["text"] == 2:
            btn1_2[i//3][i % 3]["bg"] = color[0][1]
        if btn1_2[i//3][i % 3]["text"] == 3 :
            btn1_2[i//3][i % 3]["bg"] = color[0][2]
        if btn1_2[i//3][i % 3]["text"] == 4:
            btn1_2[i//3][i % 3]["bg"] = color[1][0]
        if btn1_2[i//3][i % 3]["text"] == 5:
            btn1_2[i//3][i % 3]["bg"] = color[1][1]
        if btn1_2[i//3][i % 3]["text"] == 6:
            btn1_2[i//3][i % 3]["bg"] = color[1][2]
        if btn1_2[i//3][i % 3]["text"] == 7:
            btn1_2[i//3][i % 3]["bg"] = color[2][0]
        if btn1_2[i//3][i % 3]["text"] == 8:
            btn1_2[i//3][i % 3]["bg"] = color[2][1]
        if btn1_2[i//3][i % 3]["text"] == 9:
            btn1_2[i//3][i % 3]["bg"] = color[2][2]
    ii = 0
    ii1 = 0
    ii2 = 0


    table_clear()
    row12a.clear()
    row13a.clear()



    nbr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]



window = Tk()

window.geometry("516x700")
window.configure(background="orange")

color = [["green","red","yellow"],["gray","brown","pink"],["purple","blue","darkblue"]]

#*********** row 1 *****************************************************
btn1 = [[0,0,0],[0,0,0],[0,0,0]]
btn1_1 = [[0,0,0],[0,0,0],[0,0,0]]
btn1_2 = [[0,0,0],[0,0,0],[0,0,0]]
#*********** row 2 *****************************************************
btn2 = [[0,0,0],[0,0,0],[0,0,0]]
btn2_2 = [[0,0,0],[0,0,0],[0,0,0]]
btn2_1 = [[0,0,0],[0,0,0],[0,0,0]]
#*********** row 3 *****************************************************
btn3 = [[0,0,0],[0,0,0],[0,0,0]]
btn3_2 = [[0,0,0],[0,0,0],[0,0,0]]
btn3_1 = [[0,0,0],[0,0,0],[0,0,0]]

frame = Frame(window,width=150,height=150)
frame.grid(row=0,column=2)

btn_start = Button(window,text="Comencer",command=sudoku_start)
btn_start.place(x=12,y=12)

frame= [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

for row in range(1,4):
     for column in range(3):
        frame[row][column] = Frame(window,width=166.5,height=166.5,highlightbackground="black",highlightthickness=2)
        frame[row][column].grid(row=row,column=column)

#*********** row 1 *****************************************************
for row in range(3):
     for column in range(3):
        btn1 [row][column] = Button(frame[1][0],width=6,height=3)
        btn1[row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn1_1 [row][column] = Button(frame[1][1],width=6,height=3)
        btn1_1 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn1_2 [row][column] = Button(frame[1][2],width=6,height=3)
        btn1_2 [row][column].grid(row=row,column=column)
#*************************************************************************

#*********** row 2 ****************************************************
for row in range(3):
     for column in range(3):
        btn2 [row][column] = Button(frame[2][0],width=6,height=3)
        btn2 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn2_1 [row][column] = Button(frame[2][1],width=6,height=3)
        btn2_1 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn2_2 [row][column] = Button(frame[2][2],width=6,height=3)
        btn2_2 [row][column].grid(row=row,column=column)
#*************************************************************************

#*********** row 3 ********************************************************
for row in range(3):
     for column in range(3):
        btn3 [row][column] = Button(frame[3][0],width=6,height=3)
        btn3 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn3_1 [row][column] = Button(frame[3][1],width=6,height=3)
        btn3_1 [row][column].grid(row=row,column=column)
for row in range(3):
     for column in range(3):
        btn3_2 [row][column] = Button(frame[3][2],width=6,height=3)
        btn3_2 [row][column].grid(row=row,column=column)
#*************************************************************************


window.mainloop()