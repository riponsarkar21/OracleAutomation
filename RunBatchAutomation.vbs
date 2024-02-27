Dim response
response = MsgBox("Are you open an Excel file?", vbYesNo, "Excel File Confirmation")

If response = vbYes Then
    ' Execute the batch file
    Dim objShell
    Set objShell = WScript.CreateObject("WScript.Shell")
    objShell.Run """F:\Ripon\Oracle Automation\BatchAutomation.bat"""
    Set objShell = Nothing
    
    MsgBox "You clicked Yes! Batch file executed."
Else
    ' MsgBox "You clicked No. Nothing will be done."
End If
