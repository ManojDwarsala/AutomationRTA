# AutomationRTA
Automation of Regression Testing Analysis through Python Scripting and Visualizing through XML

Problem Description:-
The output generated by performing regression testing is very huge and it is difficult to make any analysis over it. For a typical person
it takes more than 24-48 hours to get an overview of what testcases have been failed and why they have been failed.
  Hence, the main goal of this automation, is to write a script that analyze the log file and generate a short and complete report of number
of test cases passed/failed for each tests, and to present the visual trent of pass/fail over past few tests that were ran. Also, the script 
should be called automatically whenever a log file has been generated without any kind of manual intervention.

Input:- Huge log file generated by performing Regression-Testing (around 80-100MB in size, more than 6Lakh lines)
Output:- 1-page summary reporting number of test cases failed/passed for each type of tests and also a Visual Representation of trend 
  over past tests.
  
Description of Solution:-
TestSummary.py:- script to analyze the input log file and generate a short summary report. Also, it produces XML file output used for 
displaying visual trend.

System Requirements:-
1. Jenkins- Automation tool, used to detect if a log file has been generated and call the python script to analyze.
2. Python- version 2.6 or above

Efficiency:-
1. It takes less than 2 min(far less than 24-48 hours) to analyze the log file.
2. Also, helps to visualize the pass/fail trend over past tests which has not been before.

Other scripts:-
1. reboot.py:- used to reboot the system from a remote desktop without actually going to the site.
2. timeconfig.py:- used to set the time of a system from a remote desktop.





