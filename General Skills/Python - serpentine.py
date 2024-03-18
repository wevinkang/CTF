For this flag, we need to interpret the provided python script and fix it so that it gives us the flag. 

When you run the script at first, it gives you an error when you try to print the flag. To fix this, just needed to edit the python script so that we call on the defined print_flag function.

Change the following else if statement conditions to print_flag.

    elif choice == 'b':
      print_flag() 
