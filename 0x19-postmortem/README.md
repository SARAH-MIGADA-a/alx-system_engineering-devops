<img src="postmortem software.png" alt="postmortem" width="1000" height="500">

``` This report is based on 0x0D. Web stack debugging #0```
<br>
<h1>Incident Report: Apache Service Not Running in Docker Container</h1>
<h3><b>Incident Summary:</h3></b>
<p>On [27-9-2023:10.30am EAT], an incident occurred during a debugging task where the objective
was to set up an Apache web server to return a page containing "Hello Holberton"
when querying the root of the container. The incident was related to the Apache service
not running within the Docker container, causing a "curl: (52) Empty reply from server" error.<p>

<h3><b>Incident Timeline:</h3></b>
<ol>
<li>[27-9-2023:10.30am EAT]: The incident occurred while attempting to test the Apache web server setup by running a "curl" command to query the container at port 8080.</li>
<li>[27-9-2023:10.35am EAT]: The "curl" command returned an error: "curl: (52) Empty reply from server," indicating that no response was received</li>
<li>[27-9-2023:10.40am EAT]: A decision was made to investigate the issue by connecting to the specific Docker container to check the status of the Apache service.</li>
</ol>

<h3><b>Incident Analysis:</h3></b>
<p>Root Cause: The root cause of the incident was determined to be the Apache service not running within the Docker container.</p>

<h3><b>Resolution Steps:</h3></b>
<ol>
<li>[27-9-2023:10.40am EAT]: After accessing the Docker container using docker exec, it was confirmed that the Apache service was not running.</li>
<li>[27-9-2023:10.41am EAT]: The Apache service was started within the Docker container using the appropriate command.(sudo service apache2 start)</li>
<li>[27-9-2023:10.41am EAT]: After successfully starting the Apache service, the container was tested again by running the "curl" command.</li>
<li>[27-9-2023:10.42am EAT]: This time, the "curl" command returned the expected response, "Hello Holberton," indicating that the Apache web server was operational.</li>

<h3><b>Lessons Learned:</h3></b>
<p><em>Proper service monitoring and maintenance are crucial for ensuring the reliability of containerized applications. Regularly checking the status of essential services can help prevent issues related to service failures.</p></em>

<h3><b>Preventive Measures:</h3></b>
<p><em>Implement a monitoring solution to proactively detect service failures and automatically restart them when necessary.</p></em>
<p><em>Configure Apache and other essential services to start automatically when the Docker container is launched.</p></em>

<h3><b>Incident Closure:</h3></b>
<p>This postmortem summarizes the incident where the Apache service was not initially running within a Docker container.
The incident was successfully resolved, with the Apache service being started, and the container responding as expected.
Appropriate preventive measures will be taken to avoid similar incidents in the future.
</p>

<p><em>Date and Time of Closure: 27-9-2023 at 11am EAT</p></em>
