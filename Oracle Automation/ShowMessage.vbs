Dim message, delay

' Get the message and delay time from the command line arguments
message = WScript.Arguments.Item(0)
delay = WScript.Arguments.Item(1)

' Show the message box
MsgBox message, vbInformation, "Processing"

' Wait for the specified time (in seconds)
WScript.Sleep delay * 5000

' Close the message box (since MsgBox is modal, it will automatically close after the script ends)
