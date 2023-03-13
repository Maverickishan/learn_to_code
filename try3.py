responses={}
polling_active=True #flag
while polling_active:
    name=input("\n what is your name:")
    response = input("which mountain could you like to climb someday?")
    responses[name]=response
    repeat= input("\nWould you like to lete another peroson respond? (yes/no)")
    if repeat == 'no':
        polling_active=False

print("\n --- poll Result ---")
for name,response in responses.items():
    print(name+ 'would like to climb' + response +".")