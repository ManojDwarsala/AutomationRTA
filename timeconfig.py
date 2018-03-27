import pycurl#pycurl is used to access and modify the web page content                        
import sys    #sys is used to retrieve the command line arguments
import cStringIO #This is used to create a buffer for storing the web page contents
import time      #this is used to get the localtime
localtime =  time.localtime(time.time()) #storing the localtime in localtime variable
s = str(localtime) #converting that into a string
l = list(map(str,s.split(' '))) #using space as a delimiter storing each value in the list
par = []
for i in range(0,6):
    c = l[i][l[i].index('=')+1:l[i].index(',')] #then storing the values of day,month,year,hour,min and sec in par array
    par.append((c))
if(len(sys.argv) == 1):
    print("Pass IP Address")
    exit(-1)
ip = sys.argv[1] #storing the ip address
if(len(sys.argv)>2):
    passwd = sys.argv[2] #password is retrieved
else:
    passwd = "ex1048" #If password is not passed in command line then it will set the default password

buf = cStringIO.StringIO()#Buffer object to stroe the web page content
c = pycurl.Curl() #creating the object for curl to access the web page
c.setopt(pycurl.URL,'http://'+ip+'/cgi-bin/time.cgi?') #Accessing the web page with the specified url
c.setopt(pycurl.CONNECTTIMEOUT, 1000L)
c.setopt(pycurl.COOKIE,'password='+passwd) #storing the passsword in the cookie
c.setopt(c.POSTFIELDS, 'time_zone=None&time_source=Manual&set_time=do&month='+par[1]+'&day='+par[2]+'&year='+par[0]+'&hour='+par[3]+'&minute='+par[4]+'&second='+par[5]+'&submitted=1&submit_clicked=Submit')#setting the values of the html form
c.setopt(c.VERBOSE, True) #verbose is set true to view any errors occurred
c.setopt(pycurl.WRITEFUNCTION, buf.write) #Updating the values of form using writefuntion
c.perform() #Performing the update operation


