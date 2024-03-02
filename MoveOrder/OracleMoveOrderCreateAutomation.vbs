Dim response
response = MsgBox("Are you Sure to Create Move Order?", vbYesNo, "Confirmation! Create Move Order")

If response = vbYes Then
    ' Execute the batch file
    Dim objShell
    Set objShell = WScript.CreateObject("WScript.Shell")
    objShell.Run """F:\Ripon\Oracle Automation\MoveOrder\OracleMoveOrderCreateAutomation.bat"""
    Set objShell = Nothing
    
    ' MsgBox "You clicked Yes! Preparing platform for crate Move Order."
Else
    ' MsgBox "You clicked No. Nothing will be done."
End If
