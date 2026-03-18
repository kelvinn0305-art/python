import numpy as np

print("Welcome to the Numpy Analyzer!")
print("="*25)

class data_analytics:

    def array(self):
        num=input("\nEnter elements of 1D Array: ")
        num=list(map(int,num.split()))
        arr=np.array(num)
        print("\nArray created successfully:")
        print(arr,"\n")

    def array_2d(self):
        row=int(input("Enter the number of rows: "))
        col=int(input("Enter the number of columns: "))
        arr_l=input(f"Enter {row*col} elements for the array separated by space: ")
        arr_l=list(map(int,arr_l.split()))
        arr=np.array(arr_l).reshape(row,col)
        print("\nArray created successfully:")
        print(arr,"\n")
 
    def array_3d(self):
        block=int((input("Enter number of Blocks: ")))
        self.row=int(input("Enter number of Row: "))
        self.col=int(input("Enter number of columns: "))
        l1=input(f"Enter {block*row*col} elements separated by space: ")
        l1=list(map(int,l1.split()))
        arr=np.array(l1).reshape(block,row,col)
        print("\nArray created successfully:")
        print(arr,"\n")
    
    def indexing(self):
        try:
            ind_r=int(input("\nEnter a index for row: "))
            ind_c=int(input("Enter a index for colum: "))
            arr=np.array([[10,20,30],[40,50,60]])
            new=arr[ind_r][ind_c]
            print(f"\nSearch index is :{new}\n")
        except ValueError:
            print("\nInvalided Input!")

    def slicing(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            slice_r=input("Enter the row range (Start:End): ")
            slice_c=input("Enter the colume range (Start:End): ")
            slice_r=list(map(int,slice_r.split(":")))
            slice_c=list(map(int,slice_c.split(":")))
            new_arr=arr[slice_r[0]:slice_r[1],slice_c[0]:slice_c[1]]
            print("\nSliced Array:")
            print(new_arr,"\n")
        except ValueError:
            print("\nInvalided Input!")


    def add(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            add_arr=input("Enter the same-size array elements (6 elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(2,3)
            print("\nOriginal Array:")
            print(arr,"\n")
            print("Second Array:")
            print(sec_arr,"\n")
            result=arr+sec_arr
            print("Result of Addition:")
            print(result,"\n")
        except TypeError:
            print("\nInvalided Input!")

    def sub(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            add_arr=input("Enter the same-size array elements (6 elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(2,3)
            print("\nOriginal Array:")
            print(arr,"\n")
            print("Second Array:")
            print(sec_arr,"\n")
            result=arr-sec_arr
            print("Result of Addition:")
            print(result,"\n")
        except ValueError:
            print("\nInvalided Input!")

    def mul(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            add_arr=input(f"Enter the same-size array elements (6 elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(2,3)
            print("\nOriginal Array:")
            print(arr,"\n")
            print("Second Array:")
            print(sec_arr,"\n")
            result=arr*sec_arr
            print("Result of Addition:")
            print(result,"\n")
        except ValueError:
            print("\nInvalided Input!")

    def div(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            add_arr=input(f"Enter the same-size array elements (6 elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(2,3)
            print("\nOriginal Array:")
            print(arr,"\n")
            print("Second Array:")
            print(sec_arr,"\n")
            result=arr/sec_arr
            print("Result of Addition:")
            print(result,"\n")
        except ValueError:
            print("\nInvalided Input!")

    def combine(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            stack=input("Enter the array combine Vertically or Horizontally (V / H): ").upper()
            add_arr=input(f"Enter the element of another array to combine (6 elements separated by space): ")
            add_arr=list(map(int,add_arr.split()))
            sec_arr=np.array(add_arr).reshape(2,3)
            print("\nOriginal Array:")
            print(arr,"\n")
            print("Second Array:")
            print(sec_arr)
            if stack=="V":
                new_arr=np.vstack((arr,sec_arr))
                print("\nCombine Array (Vertically Stack):")
                print(new_arr,"\n")
            elif stack=="H":
                new_arr=np.hstack((arr,sec_arr))
                print("\nCombine Array (Horizontally Stack):")
                print(new_arr,"\n")
            else:
                print("\nInvalided Choice\n")
        except ValueError:
            print("\nInvalided Input!")

    def split(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            split=input("Enter the Split array Vertically or Horizontally (V / H): ").upper()
            print("\nOriginal Array:")
            print(arr)
            if split=="V":
                new_arr=np.vsplit(arr,2)
                print("\nSplit Array (Vertically Stack):")
                print(new_arr,"\n")
            elif split=="H":
                new_arr=np.hsplit(arr,3)
                print("\nSplit Array (Horizontally Stack):")
                print(new_arr,"\n")
            else:
                print("\nInvalided Choice\n")
        except ValueError:
            print("\nInvalided Input!")


    def search(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            search=int(input("Enter element for search: "))
            sea_arr=np.where(arr==search)
            print("\nSearchhing element successfully")
            print(sea_arr,"\n")
        except ValueError:
            print(f"\nThis {search} elemente is not match in this array\n")

    def sort(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            print("\nOriginal Array:")
            print(arr,"\n")
            sort_arr=np.sort(arr)
            print("Sorted Array:")
            print(sort_arr,"\n")
        except ValueError:
            print("\nInvalided Input!")

    def filter(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            elements = input("Enter 6 elements (True/False or 1/0): ").split()
            bool_list = [bool(int(i)) for i in elements]
            f_arr=np.array(bool_list).reshape(2,3)
            print("\nOriginal Array:")
            print(arr,"\n")
            print("Filter Array:")
            print(arr[f_arr],"\n")
        except ValueError:
            print("\nInvalided Input!")

    def sum(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            print("\nOriginal Array:")
            print(arr,"\n")
            sum=np.sum(arr)
            print(f"Sum of Array: {sum}\n")
        except ValueError:
            print("\nInvalided Input!")

    def mean(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            print("\nOriginal Array:")
            print(arr,"\n")
            mean=np.mean(arr)
            print(f"Mean of Array: {mean}\n")
        except ValueError:
            print("\nInvalided Input!")

    def median(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            print("\nOriginal Array:")
            print(arr,"\n")
            median=np.median(arr)
            print(f"Median of Array: {median}\n")
        except ValueError:
            print("\nInvalided Input!")

    def standard_deviation(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            print("\nOriginal Array:")
            print(arr,"\n")
            standard_deviation=np.std(arr)
            print(f"Standard Deviation of Array: {standard_deviation}\n")
        except ValueError:
            print("\nInvalided Input!")

    def variance(self):
        try:
            arr=np.array([[10,20,30],[40,50,60]])
            print("\nOriginal Array:")
            print(arr,"\n")
            variance=np.var(arr)
            print(f"Variance of Array: {variance}\n")
        except ValueError:
            print("\nInvalided Input!")

    def __del__(self):    
        pass

da=data_analytics()

while True:
    print("choose an option:")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Array")
    print("5. Compute Aggregates and Statistics")
    print("6. EXit\n")

    choice=int(input("Enter your choice: "))
    if choice==1:
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        achoice=int(input("Enter your choice: "))
        if achoice==1:
            da.array()
            while True:
                print("Choose an operation:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    da.indexing()
                elif choice==2:
                    da.slicing()
                elif choice==3:
                    print("\nReturning to Main Menu.\n")
                    break
                else:
                    print("\nInvalided Choice\n")
        elif achoice==2:
            da.array_2d()
            while True:
                print("Choose an operation:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    da.indexing()
                elif choice==2:
                    da.slicing()
                elif choice==3:
                    print("\nReturning to Main Menu.\n")
                    break
                else:
                    print("\nInvalided Choice\n")
        elif achoice==3:
            da.array_3d()
            while True:
                print("Choose an operation:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    da.indexing()
                elif choice==2:
                    da.slicing()
                elif choice==3:
                    print("\nReturning to Main Menu.\n")
                    break
                else:
                    print("\nInvalided Choice\n")
        else:
            print("\nInvalided Choice\n")
    elif choice==2:
        while True:
            print("Choose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Go Back\n")
            mchoice=int(input("Enter your choice: "))
            if mchoice==1:
                da.add()
            elif mchoice==2:
                da.sub()
            elif mchoice==3:
                da.mul()
            elif mchoice==4:
                da.div()
            elif mchoice==5:
                print("\nReturning to Main Menu.\n")
                break
            else:
                print("\nInvalided Choice\n")

    elif choice==3:
        while True:
            print("\nChoose an option:")
            print("1. Combine Array")
            print("2. Split Array")
            print("3. Go Back\n")
            choice=int(input("Enter your choice: "))
            if choice==1:
                da.combine()
            elif choice==2:
                da.split()
            elif choice==3:
                print("\nReturning to Main Menu.\n")
                break
            else:
                print("\nInvalided Choice\n")

    elif choice==4:
        while True:
            print("\nChoose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter value")
            print("4. Go Back\n")
            schoice=int(input("Enter your Choice: "))
            if schoice==1:
                da.search()
            elif schoice==2:
                da.sort()
            elif schoice==3:
                da.filter()
            elif schoice==4:
                print("\nReturning to Main Menu.\n")
                break
            else:
                print("\nInvalided Choice\n")

    elif choice==5:
        while True:
            print("Choose an aggregate/statistical operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Go Back\n")
            schoice=int(input("Enter your Choice: "))
            if schoice==1:
                da.sum()
            elif schoice==2:
                da.mean()
            elif schoice==3:
                da.median()
            elif schoice==4:
                da.standard_deviation()
            elif schoice==5:
                da.variance()
            elif schoice==6:
                print("\nReturning to Main Menu.\n")
                break
            else:
                print("\nInvalided Choice\n")

    elif choice==6:
        print("\nThank you for using the Numpy Analyzer! Goodbye!\n")
        break
    else:
        print("\nInvalided Choice\n") 