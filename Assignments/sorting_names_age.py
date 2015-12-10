

def function_name(s_name):
    return s_name['name']



def function_age (s_age):
    return s_age['age']
    


def main():
    records = [{"name":  " Pedro" , "age": 22} , {"name":  " Juan" , "age": 23}, {"name":  " Pepe" , "age": 24}] 

    print ("Choice: ")
    print("[1]  lambda sort by name")
    print("[2]  lambda sort by name")
    print("[3]  function sort by name")
    print("[4]  function sort by name")

    choice = input("Enter your choice: ")

    if choice == 1:
        print("lambda sort by name")

        for s_name in sorted(records, key=lambda k:k['name']):
            for k, v in s_name.items():
                 print "%s:%s" % (k, v) 

    elif choice == 2:
        print("lambda sort by age")
        
        for s_age in sorted(records, key=lambda k: k['age']):
            for k, v in s_age.items():
                    print "%s:%s" % (k, v) 

    elif choice == 3:
        print("Function sort by name")

        for s_name in sorted(records, key= function_name):
            for k, v in s_name.items():
                    print "%s:%s" % (k, v) 

    elif choice == 4:
        print("Function sort by age")

        for s_name in sorted(records, key= function_name):
            for k, v in s_name.items():
                    print "%s:%s" % (k, v) 
    else:
        print "Invalid Input"

        


if __name__ == '__main__':
  main()
