# Postmortem

This postmortem is a scrutiny of a situation that I experienced

## Issue Summary

I develop a school management application for a local high school. The application handles all school activities student enrollment, student marks, teacher information and student payment details. 5 months after I finished  the app and deployed it, The school contacted me again after users were affected, teachers couldn't update student information and students couldn't access there marks due to a DDoS attack.

## Timeline
**Nov 22rd 2019**

* 5:50pm: The traffic amount increased for no reason in the evening hours

**Nov 24th 2019**    
* The issue was detected when teachers report that they can't update student marks on the application portal.
* I was contacted by the schoolto check the issue.
* The action that I took was to review the access.log file, located in the server.

**Nov 25th 2019**
* Cloud flare solution implemented to prevent DDoS attacks



## Root Cause and Resolution
While I was checking the logs I found an unusual amount of traffic in the evening hours, I can think a tech survy student launched a DDoS attack. We can think that the motivation of this attack was sabotaging the website and alter student marks.

I also check that the app has enough bandwidth available, and everything is ok, the issue was that strange amount of traffic.

I implemented a solution with CloudFlare to handle this bad traffic and still online. 


## Correct and Preventative Measures

Measure taken was use CloudFlare, a solution to prevent DDoS attacks, after implement this, the attacks continue a few days but without any impact.
