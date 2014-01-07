splitwatch is a python library that aims to make timing of code
- Easy to implement
- Switchable
- As automatic as possible

Usage:
The SplitWatch class must be imported.
    from splitwatch import SplitWatch
An instance is then created. SplitWatch takes 2 keywork arguments: mode and sorted. mode, when set to 'dev', sets the timer to collect data and print it when SplitWatch.dump() is called. If not included, it is set to '' and no data is collected. When in '' mode, all method calls result in pass statements with very low overhead. If sorted is set to True, the "splits" taken by SplitWatch are sorted from shortest to longest before display.

SplitWatch()
	Base object responsible for timing and storage of results.

	.split(desc = 'put a good description here')
		the split method is analogous to the split button on a stopwatch. The description argument refers to the following code

	.dump()
		the dump method prints the accumulated results of calls to the split method.