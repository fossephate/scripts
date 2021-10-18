#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#SingleInstance Force
#NoTrayIcon
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

~LWin::
    Send {Blind}{vkE8}
return
~LWin Up::
	If (A_PriorKey = "LWin") ;  if pressed alone
		Send ^+!r
return