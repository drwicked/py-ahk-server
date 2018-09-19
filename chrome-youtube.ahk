#Persistent
#NoEnv
#SingleInstance, Force
DetectHiddenWindows, On
SetWorkingDir %A_ScriptDir%
SetTitleMatchMode, 2
controlID 		:= 0
return

#IfWinNotActive, ahk_exe chrome.exe

; Play/pause
+!p::
	ControlGet, controlID, Hwnd,,Chrome_RenderWidgetHostHWND1, Google Chrome
	
	ControlFocus,,ahk_id %controlID%

	IfWinExist, YouTube
	{
		ControlSend, Chrome_RenderWidgetHostHWND1, k , Google Chrome
		return
	}
	Loop {
		IfWinExist, YouTube
			break

		ControlSend, , ^{PgUp} , Google Chrome
		sleep 150
	}
	ControlSend, , k , Google Chrome
return

; Next video in playlist
+!n::
	ControlGet, controlID, Hwnd,,Chrome_RenderWidgetHostHWND1, Google Chrome
	
	ControlFocus,,ahk_id %controlID%

	IfWinExist, YouTube
	{
		ControlSend, Chrome_RenderWidgetHostHWND1, +n , Google Chrome
		return
	}
	Loop {
		IfWinExist, YouTube
			break

		ControlSend, , ^{PgUp} , Google Chrome
		sleep 150
	}
	ControlSend, , +n , Google Chrome
return

; Previous video in playlist
+!b::
	ControlGet, controlID, Hwnd,,Chrome_RenderWidgetHostHWND1, Google Chrome
	
	ControlFocus,,ahk_id %controlID%

	IfWinExist, YouTube
	{
		ControlSend, Chrome_RenderWidgetHostHWND1, +p , Google Chrome
		return
	}
	Loop {
		IfWinExist, YouTube
			break

		ControlSend, , ^{PgUp} , Google Chrome
		sleep 150
	}
	ControlSend, , +p , Google Chrome
return

; Seek back
+!left::
	ControlGet, controlID, Hwnd,,Chrome_RenderWidgetHostHWND1, Google Chrome
	
	ControlFocus,,ahk_id %controlID%

	IfWinExist, YouTube
	{
		ControlSend, Chrome_RenderWidgetHostHWND1, j , Google Chrome
		return
	}
	Loop {
		IfWinExist, YouTube
			break

		ControlSend, , ^{PgUp} , Google Chrome
		sleep 150
	}
	ControlSend, , j , Google Chrome
return

; Seek forward
+!right::
	ControlGet, controlID, Hwnd,,Chrome_RenderWidgetHostHWND1, Google Chrome
	
	ControlFocus,,ahk_id %controlID%

	IfWinExist, YouTube
	{
		ControlSend, Chrome_RenderWidgetHostHWND1, l , Google Chrome
		return
	}
	Loop {
		IfWinExist, YouTube
			break

		ControlSend, , ^{PgUp} , Google Chrome
		sleep 150
	}
	ControlSend, , +l , Google Chrome
return

#IfWinNotActive