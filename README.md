# Smartness is relative 

So I made a way to scrape the comments from VG. 

Why? 

To read them loud from a Raspberry Pi.

Why?

I don't know. 

The project uses Python with Selenium to loop through VG and get all comments. Comments are put on a Kafka topic and with port forwadring to a Raspberry Pi it listens for events on the topics and plays them using Google TTS. 
