import connect_n
if __name__ == '__main__': 
    ROW_COUNT = int(input("Enter row Count!\n"))
    if(ROW_COUNT<=0):
        ROW_COUNT=int(input("Enter correct row count!\n"))
    COLUMN_COUNT = int(input("Enter column Count!\n"))
    if(COLUMN_COUNT<=0):
        COLUMN_COUNT=int(input("Enter correct column count!\n"))
    PIECES_NO = int(input("Enter No of Pieces!\n"))
    if(PIECES_NO<=0 or PIECES_NO>max(ROW_COUNT,COLUMN_COUNT)):
        PIECES_NO=int(input("Enter Correct No of Pieces!\n"))
    while(connect_n.gamefun(ROW_COUNT,COLUMN_COUNT,PIECES_NO)=="Yes"):
        # connect_n.gamefun(ROW_COUNT,COLUMN_COUNT,PIECES_NO)
        pass