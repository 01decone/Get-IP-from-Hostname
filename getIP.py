import socket
print(
'''
=========================================================
|                                                       |
|                                                       |
|         ██▓▒­░⡷⠂  GetIP by Vivek ⠐⢾░▒▓██          |
|                                                       |
|                                                       |
=========================================================
'''
    )
file1 = open('domainlist.txt', 'r')
#file2 = open('status.txt', 'w')

for x in file1:
 try: 
  x = x.strip()
  ip = socket.gethostbyname(x)
  print(x,ip)
 except:
   print("Not resolved: "+ x)
   pass
#file2.close()
