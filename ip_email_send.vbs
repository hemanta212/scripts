Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "F:\my_projects\script-dev\scripts\ip_email_sender.py" & Chr(34), 0
Set WinScriptHost = Nothing
