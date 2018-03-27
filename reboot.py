import pycurl #pycurl is used to access and modify the web page content
import sys    #sys is used to retrieve the command line arguments
import cStringIO #This is used to create a buffer for storing the web page contents
import time#this is used to get the localtime 
c = pycurl.Curl() # creating the object for curl to access the web page
ip = sys.argv[1] #storing the ip address 
if(len(sys.argv)>2):
    passwd = sys.argv[2] #password is retrieved
else:
    passwd = "ex1048" #If password is not passed in command line then it will set the default password
buf = cStringIO.StringIO() #Buffer object to stroe the web page content
c.setopt(pycurl.URL,'http://'+ip+'/cgi-bin/reboot.cgi?') #Accessing the web page with the specified url
c.setopt(pycurl.COOKIE,'password='+passwd) #storing the passsword in the cookie
c.setopt(c.POSTFIELDS,'submitted=1&reboot=Reboot') #setting the values of the html form
c.setopt(c.VERBOSE, True) #verbose is set true to view any errors occurred
c.setopt(pycurl.WRITEFUNCTION, buf.write) #Updating the values of form using writefuntion
c.perform() #Performing the update operation
time.sleep(120) #Pausing the program for 120 sec, giving time for rebooting the instrument

