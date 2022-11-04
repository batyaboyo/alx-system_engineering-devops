# Postmortem

In this postmortem we will scrutinise a situation that I faced

## Issue Summary

I develop a website for local journalists. Their articles are about political topics and opinions. 8 months after I finished my work they contacted me again because something strange happened, when they published a new article the website got offline. All users were affected because no one can access and read the content, the reason was a DDoS attack.

## Timeline
**6 April 2021**

* 3:30 am: The traffic amount increased for no reason an the hour was very early in the morning

**7 April 2021**
* The issue was detected when users report that they can't visit the website.
* I was contacted by my client to check the issue.
* The action that I took was to review the access.log file, located in the server.

**8 April 2021**
* Cloud flare solution implemented to prevent DDoS attacks



## Root Cause and Resolution
While I was checking the logs I found an unusual amount of traffic in strange hours, I can think that someone was testing a botnet. In the log files we can see that two days later of those tests, a series of attacks against the web when the journalist published a new article started,, we can think that the motivation of this attack was sabotaging the website.

I also check that the website has enough bandwidth available, and everything is ok, the issue was that strange amount of traffic.

I implemented a solution with CloudFlare to handle this bad traffic and still online. 


## Correct and Preventative Measures

As I mentioned, the measures taken was use CloudFlare, a solution to prevent DDoS attacks, after implement this, the attacks continue a few days but without any impact.

## Misc

I used logstalgia software to visualize the first attack [video](https://www.youtube.com/watch?v=FLmF35Xs4bg)
