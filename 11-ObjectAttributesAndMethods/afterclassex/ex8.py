class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_in_row(array):
        arrayend = []
        for i in array:
            i = str(i)
            arrayend.append(i)
        print(", ".join(arrayend))
            
my_array = [4,1,8,7,2]
my_array1 = [1,2,3,4,5,6,7,8,9]
Arrays.print_in_col(my_array)
print()
Arrays.print_in_col(my_array1)
Arrays.print_in_row(my_array)

