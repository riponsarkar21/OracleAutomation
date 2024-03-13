Dim response
response = MsgBox("Are you Sure to Download On Hand Details?", vbYesNo, "Confirmation! Download On Hand Details")

If response = vbYes Then
    ' Execute the batch file
    Dim objShell
    Set objShell = WScript.CreateObject("WScript.Shell")
    objShell.Run """F:\Ripon\Oracle Automation\OnHandDetails\CheckOnHandDetails.bat"""
    Set objShell = Nothing
    
    ' MsgBox "You clicked Yes! Preparing platform for Download On Hand Details."
Else
    ' MsgBox "You clicked No. Nothing will be done."
End If
