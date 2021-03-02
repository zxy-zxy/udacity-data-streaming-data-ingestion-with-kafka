### Glossary of Key Terms for Stream Processing Fundamentals
* Join (Streams) - The process of combining one or more streams into an output stream, 
typically on some related key attribute.
* Filtering (Streams) - The process of removing certain events in a data stream based on a condition
* Aggregating (Streams) - The process of summing, reducing, or otherwise grouping 
data based on a key attribute
* Remapping (Streams) - The process of modifying the input stream data structure into a different output 
structure. This may include the addition or removal of fields on a given event.
* Windowing (Streams) - Defining a period of time from which data is analyzed. Once data falls outside of 
that period of time, it is no longer valid for streaming analysis.
* Tumbling Window (Streams) - The tumbling window defines a block of time which rolls over once the duration has elapsed. 
A tumbling window of one hour, started now, would collect all data for the next 60 minutes. 
Then, at the 60 minute mark, it would reset all of the data in the topic, and begin collecting a fresh set of data for the next 60 minutes.
* Hopping Window (Streams) - Hopping windows advance in defined increments of time. A hopping window 
consists of a window length, e.g. 30 minutes, and an increment time, e.g. 5 minutes. 
Every time the increment time expires, the window is advanced forward by the increment.
* Sliding Window (Streams) - Sliding Windows work identically to Hopping Windows, except the increment period is 
much smaller -- typically measured in seconds. Sliding windows are constantly updated and always represent the 
most up-to-date state of a given stream aggregation.
* Stream - Streams contain all events in a topic, immutable, and in order. As new events occur, they are 
simply appended to the end of the stream.
* Table - Tables are the result of aggregation operations in stream processing applications. 
They are a roll-up, point-in-time view of data.
* Stateful - Stateful operations must store the intermediate results of combining multiple events to represent the 
latest point-in-time value for a given key