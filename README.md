# POC_Parallel_Selenium
Distributed Testing with
Selenium Grid

Download the latest Selenium Server standalone JAR file from http://code.google.
com/p/selenium/downloads/list . For this recipe, selenium-server-standalone-2.25.0
version is used.

Setting up a Hub is a fairly simple job. Launch the Selenium Server using the
following command:
java -jar selenium-server-standalone-2.25.0.jar -port 4444 -role hub
-nodeTimeout 600


Creating and executing Selenium script in
parallel with Python
As we have seen in the previous recipe, TestNG provides a very powerful execution framework
for running tests in parallel for Java bindings.
However, if you are using Python or another binding to develop Selenium WebDriver tests, you
can also run tests in parallel for distributed testing.
In this recipe, we will create and execute tests in parallel with Python bindings using the
subprocess module. We will use the Hub and nodes configured in earlier recipes to run
these tests.

we will create two test scripts for testing the application with chrome
using the following steps. You can also create a single test

------------------------
Finally, we need to create a Python script, which will use the subprocess module to
run these tests concurrently on different nodes. Name this script as runner.py 
-------------------------
We need to place all three scripts in the same directory. When we execute runner.py , it
collects all the tests with names starting as test using the glob function. Then we create
a hash for processes and append each test using the Popen function from the subprocess
module. The Popen() function calls each test using Python as a subprocess of the main
process and waits for the script to complete.
---------------------------------------------------------------------
We can also use nose module for Python to run the tests in parallel. We need to install nose
by using the following command:

easy_install nose==0.11 multiprocessing

After nose is installed, you need to open the folder where all the tests are stored and use the
following command:

nosetests --processes=2

This will call the nosetests scripts, which will locate all the files with test prefix in the current
directory and start running tests concurrently. In this example, we are running two tests so
we need to specify the value for processes argumented as 2. nose module internally uses
multiprocessing module for concurrent execution.


