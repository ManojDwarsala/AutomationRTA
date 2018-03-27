import os,glob,sys #os: This package is used to retreive the latest log file; sys: to retreive the command line arguments; glob: for regular expression matching in python
global dicoferr    #dictionary to store fail test cases
def PassFail(lst,k,testn): #func to count pass and fail testcases
    global ln #to get the line no for maitaining main loop
    passed,failed = 0,0
    st = map(str,lst[k].split(' ')) 
    while ('PASS') not in st and 'FAIL' not in st and k < len(lst)-1: #checking for the line containing the word PASS or FAIL by storing each line in st
        k +=1
        st = map(str,lst[k].split(' '))
    ln = k
    if 'PASS' in st:
        passed = 1 #if pass found in st 1 is set in passed
    if 'FAIL' in st:
        failed = 1 #if fail found in st 1 is set in failed
        a = k-1
        err = lst[a]
        errl = map(str,lst[a].split(' '))
        while errl==['\n']:
            a -=1
            errl = map(str,lst[a].split(' '))
            err = lst[a]
        if testn not in dicoferr:
            dicoferr[testn] = err
    return passed,failed
dicoftests = { }
dicoferr = { }
r = sys.argv[1] #path containg the log file
newest = max(glob.iglob(r+'*.log'), key=os.path.getctime)#getting the latest created log file
fp = open(newest, "r")
Lines = fp.readlines() #getting the total number of lines in log file
i = 1 #pointing to first line of log file
while i < len(Lines):
    line_content = map(str,Lines[i].split(' ')) #storing the content of each line in line_content
    test_name =  line_content[len(line_content)-2] #Retreiving the test case name from th line_content
    if line_content[len(line_content)-1] == 'tests/sec)\n': #checking whether it reached the line containing tests/sec located at the end of log file 
        break
    if test_name not in dicoftests: #If test name is not in dictionary it will update it by adding it in dicoftests 
        dicoftests[test_name] = {'pass' : 0,'fail' : 0}
    if test_name in dicoftests: #If it already present then it will update its pass and fail count
        p,f = PassFail(Lines,i+1,test_name)
        dicoftests[test_name]['pass'] += p
        dicoftests[test_name]['fail'] += f
        i = ln+2
        continue
    else:
        break


#printing into a text file
with open(r+'Test_Report.txt', 'w') as f:   
    sys.stdout = f
    tf,tp = 0,0
    print "{:<25} {:<30} {:<35}".format('TestName','Fail','Pass'),"\n" 
    for k, v in dicoftests.iteritems():
        label,num = v
        tf +=  dicoftests[k][label]
        tp +=  dicoftests[k][num]
        print "{:<25} {:<30} {:<35}".format(k, dicoftests[k][label],  dicoftests[k][num])
    print "\n","{:<25} {:<30} {:<35}".format('TOTAL', tf, tp),"\n"
    if(i == len(Lines)+1):
        print "TEST is Abrupted","\n"
        perc = float(tp)/(tf+tp)
        pr = perc * 100
        print "Percentage of Test-Cases passed till this time =",pr,"%"
    else:
        while i <len(Lines):
            print Lines[i]
            i +=1

#new xml code generation
with open(r+'result.xml','w') as ne:
    sys.stdout = ne
    msg = ""
    tf,tp = 0,0
    for k, v in dicoftests.iteritems():
        label,num = v
        tf +=  dicoftests[k][label]
        tp +=  dicoftests[k][num]
    total = tf+tp
    print "<?xml version = \"1.0\" encoding = \"utf-8\"?>"
    print "<testsuites failures = \""+str(tf)+"\" tests = \""+str(total)+"\">"
    print "<testsuite failures = \""+str(tf)+"\" name =\"RegressionTest\" tests = \""+str(total)+ "\">"
    for a,b in dicoftests.iteritems():
        c,d = b
        f = dicoftests[a][c]
        p = dicoftests[a][d]
        for n,v in dicoferr.iteritems():
            if(a == n):
                msg = v
        for i in range(f):
            print "<testcase name = \""+a+"\">"
            print "<failure>"+msg+"</failure></testcase>"
        for i in range(p):
            print "<testcase name = \""+a+"\"/>"
    print "</testsuite>"
    print "</testsuites>"

#printing into a Junit xml file format for graphical view
with open(r+'resultperf.xml', 'w') as p:
    sys.stdout = p
    print "<?xml version = \"1.0\" encoding = \"utf-8\"?>"
    print "<report name=\"perf\" categ=\"perfcat\">"
    for a,b in dicoftests.iteritems():
        c,d = b
        f = dicoftests[a][c]
        p = dicoftests[a][d]
        for i in range(p):
            print "  <test name=\""+a+"\" executed=\"yes\">"
            print "    <result>"
            print "     <success passed=\"yes\" state=\"100\"/>"
            print "    </result>"
            print "  </test>"
        for i in range(f):
            print "  <test name=\""+a+"\" executed=\"yes\">"
            print "    <result>"
            print "     <success passed=\"no\" state=\"0\"/>"
            print "    </result>"
            print "  </test>"
    print "</report>"    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


                 
                 
                 
                 
                








                 
                 

    
