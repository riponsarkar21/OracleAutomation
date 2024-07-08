Dim response
Dim password
Dim objShell, objExec, objWMIService, colProcessList

' Prompt the user for the password
password = InputBox("Please enter the password:", "Password")

If password = "1" Then
    ' Execute the batch file silently
    Set objShell = WScript.CreateObject("WScript.Shell")
    objShell.Run """F:\Ripon\python\OracleAutomation\OracleAutomation.bat""", 0

    ' Show the processing message
     objShell.Popup "Processing, please wait...", 4, "Processing", 64

'    objShell.Run "wscript.exe ""F:\Ripon\python\OracleAutomation\ShowMessage.vbs"" ' ""Processing, Please Wait..."" 1", 0, False
    
    ' Wait for the batch file to complete (replace the Sleep with appropriate wait logic if needed)
'    Do
'        WScript.Sleep 1000
'        Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")
'        Set colProcessList = objWMIService.ExecQuery("Select * from Win32_Process Where Name = 'cmd.exe'")
'        If colProcessList.Count = 0 Then Exit Do
'    Loop

    Set objShell = Nothing
Else
    MsgBox "Incorrect password. Access denied."
End If
