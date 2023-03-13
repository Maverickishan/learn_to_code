def get_formatted_name(first_name,last_name):
    full_name= first_name+" "+last_name
    return full_name

while True:
    print("\n Please tell me your name:")
    print("(enter 'q' to exit any time.)")
    f_name=input()
    if f_name=='q':
        break
    l_name=input()
    if l_name=='q':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello," + formatted_name+"!")    