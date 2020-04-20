# importing required modules
import time
import random
import sys

# defining difficulty levels
accepted=False
while not accepted:
    try:
        diff=int(input("Enter difficulty level:\
\n\t 1 for easy \n\t 2 for medium \n\t 3 for difficult \n"))
        if diff==1:
            no=11
            time_given=360       # Adding time limit to complete the game
            accepted=True
        elif diff==2:
            no=8
            time_given=540
            accepted=True
        elif diff==3:
            no=6
            time_given=780
            accepted=True
        else:
            raise Exception
    except Exception:
        print("Please enter only an integer between 1 and 3")

# giving instructions to the User
print("Now you will first have to enter the coordinates \
of the box where you want to enter a number")
print("Next you must enter the number to be inserted there")
time.sleep(6)
print('......You will get only',time_given-60,'seconds i.e', (time_given/60)-1,'minutes......')
print("Good luck!!")
time.sleep(4)
print("In case you want to quit the game anytime, just press 'q'")
time.sleep(2)
print("Okay..lets begin now!!")
time.sleep(2)

# initialising various lists and dictionary
solved_positions=[]
position_box=[]
value_box=[]
dict_ziplist={}   # A dictionary will increase the efficiency of the code

# entering the solved values of the sudoku puzzle
solved_values_1=[3,1,2,4,4,2,1,3,1,3,4,2,2,4,3,1]
solved_values_2=[1,2,3,4,4,3,2,1,2,1,4,3,3,4,1,2]
solved_values_3=[4,2,3,1,1,3,2,4,3,1,4,2,2,4,1,3]
solved_values_4=[1,3,4,2,4,2,1,3,3,4,2,1,2,1,3,4]
solved_values_5=[1,4,2,3,3,2,4,1,4,1,3,2,2,3,1,4]

# choosing any one of the above lists
select_list=[solved_values_1,solved_values_2,solved_values_3,solved_values_4,solved_values_5]
solved_values=random.choice(select_list)

temp_val=list(solved_values)  #assign to a temp variable be helpful in future 

# filling the solved_positions list with (1,1),(1,2),(1,3)...
for i in range(1,5):
    for j in range(1,5):
        solved_positions.append((i,j))

temp_pos=list(solved_positions) #assign to a temp variable be helpful in future

# randomly choosing the position and its corresponding value and
# appending them to lists position_box and value_box
while len(value_box)!= no:
    random_value=random.choice(solved_positions)
    index=solved_positions.index(random_value)
    solved_positions.remove(random_value)
    position_box.append(random_value)
    value_box.append(solved_values[index])
    solved_values.pop(index)

# generating the Sudoku Board along with the randomly generated positions
def BoardDisplay():
    print("_"*17)               # To get the horizontal line on the top
    for i in range(1,5):
        for j in range(1,5):
            k=1
            found=False
            while not found and k<=len(value_box):
                if i==position_box[k-1][1] and j==position_box[k-1][0]:
                    found=True
                k+=1
            if found==True:
                print("|"+'_'+str(value_box[k-2])+"_",end='')
            else:
                print("|"+'_'+' '+"_",end='')
        print("|")

# Starting the timer
start=time.perf_counter()

# Taking the input from the user
def UserInput():
    while len(value_box)!=16:
        try:
            end=time.perf_counter()
            if (end-start)>time_given:
                print("Oops time up")
                time.sleep(2)
                sys.exit()
            pos=input("Enter position comma separated: ")
            if pos=='q':
                time.sleep(2)
                sys.exit()  
            pos_i=int(pos.split(',')[0])
            pos_j=int(pos.split(',')[1])
            if (type(pos_i)!= int or type(pos_j)!=int): 
                raise AssertionError
            elif (pos_i<1 or pos_i>4 or pos_j<1 or pos_j>4):
                raise ValueError
            elif (pos_i,pos_j) in position_box:
                raise TypeError

        except AssertionError:
            print('Value should be integers only')
        except ValueError:
            print('Value should be integers between 1 and 4 only')
        except TypeError:
            print('Box already filled')
        else:
            pos_i=int(pos.split(',')[0])
            pos_j=int(pos.split(',')[1])
            try:
                choice=input("Enter number: ")
                if choice=='q':
                    time.sleep(2)
                    sys.exit()
                choice=int(choice)
                if type(choice)!=int:
                    raise AssertionError
                elif choice<1 or choice>4:
                    raise ValueError
            except AssertionError:
                print('Please enter an integer only')
            except ValueError:
                print('Please enter an integer between 1 and 4 only')
            else:
                position_box.append((pos_i,pos_j))
                value_box.append(choice)
        print()
        BoardDisplay()

#Checking according to the rules of the Sudoku
def SudokuLogic():
    row_list=list(zip(position_box,value_box))
    row_list.sort()

    column_1,column_2,column_3,column_4=set(),set(),set(),set()
    row_1,row_2,row_3,row_4=set(),set(),set(),set()
    box_1,box_2,box_3,box_4=set(),set(),set(),set()

    for i in range(1,len(row_list)+1):
        dict_ziplist[i]=row_list[i-1][-1]

    for i in range(1,5):
        row_1.add(dict_ziplist[i])
        row_2.add(dict_ziplist[i+4])
        row_3.add(dict_ziplist[i+8])
        row_4.add(dict_ziplist[i+12])

    for i in range(1,14,4):
        column_1.add(dict_ziplist[i])
        column_2.add(dict_ziplist[i+1])
        column_3.add(dict_ziplist[i+2])
        column_4.add(dict_ziplist[i+3])

    for i in range(1,13):
        if i==1 or i==2:
            box_1.add(dict_ziplist[i])
            box_1.add(dict_ziplist[i+4])
        elif i==3 or i==4:
            box_2.add(dict_ziplist[i])
            box_2.add(dict_ziplist[i+4])
        elif i==9 or i==10:
            box_3.add(dict_ziplist[i])
            box_3.add(dict_ziplist[i+4])
        elif i==11 or i==12:
            box_4.add(dict_ziplist[i])
            box_4.add(dict_ziplist[i+4])

    c1,c2,c3,c4=len(column_1),len(column_2),len(column_3),len(column_4)
    r1,r2,r3,r4=len(row_1),len(row_2),len(row_3),len(row_4)
    b1,b2,b3,b4=len(box_1),len(box_2),len(box_3),len(box_4)

    list_set_len=[c1,c2,c3,c4,r1,r2,r3,r4,b1,b2,b3,b4]

    for i in list_set_len:
        if i!=4:
            res='Loss'
            break
        else:
            res='Win'

    if res=='Loss':
        return False
    elif res=='Win':
        return True


# First displaying the board to the user
BoardDisplay()
print()

# Taking input from the user until all the boxes are filled...or 'q' is pressed
UserInput()
print()
time.sleep(1)
print("Okay...that was wonderful...Lets see how you performed.....")
time.sleep(2)

# Checking the User's solution
if SudokuLogic()==True:
    print('Congo! You got it right')
    end=time.perf_counter()
    print('You completed the game in',round((end-start),2),'seconds i.e',round((end-start)/60,2),'minutes')
    print()
    print("Thank you for playing...Hope you enjoyed")
    time.sleep(4)

elif SudokuLogic()==False:
    print('Sorry, try again')
    end=time.perf_counter()
    print('You completed the game in',round((end-start),2),'seconds')
    print()
    print("Thank you for playing...Hope you enjoyed")
    see_ans=input("Wait..You wanna see the answer?? Enter 'y' to see the answer: ")
    if see_ans=='y':
        position_box=temp_pos                     
        value_box=temp_val
        BoardDisplay()
        time.sleep(120)
    else:
        pass
#not reqiured
