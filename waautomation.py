import pywhatkit

print('''
 __          __                     _        
 \ \        / /\         /\        | |       
  \ \  /\  / /  \       /  \  _   _| |_ ___  
   \ \/  \/ / /\ \     / /\ \| | | | __/ _ \ 
    \  /\  / ____ \   / ____ \ |_| | || (_) |
     \/  \/_/    \_\ /_/    \_\__,_|\__\___/ 

Created by PythonX ~ ShahadathAkash                                             
''')

number = str(input('[~] Receiver Number (with country code)\nEx: +880179**2**0*\n>>> '))
message = str(input('[~] Type your message here\n>>> '))
time_hr = int(input('[~] Set time hr (24hr format)\nEx: 17\n>>> '))
time_min = int(input('[~] Set time min (59min format)\nEx: 05\n>>> '))
print("[0] Task added. Don't close the programme.")
pywhatkit.sendwhatmsg(number, message, time_hr, time_min)