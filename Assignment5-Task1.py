print("Enter row and columns to recieve a checkered board with * and $.")
def checkered_board(rows,cols):
    
    for i in range(rows):
        for j in range(cols):
            if (i+j) %2 == 0:
                print("*",end="")
            else:
                print("$",end="")
        print()
num_rows = int(input("Enter the number of rows:"))
num_cols = int(input("Enter the number of columns:"))

checkered_board(num_rows,num_cols)
            