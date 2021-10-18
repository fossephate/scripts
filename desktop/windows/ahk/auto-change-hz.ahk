; Allows only 1 instance of the script to run
#SingleInstance Force
#NoTrayIcon



ChangeResolution( cD, sW, sH, rR ) {
    VarSetCapacity(dM,156,0), NumPut(156,2,&dM,36)
    DllCall( "EnumDisplaySettingsA", UInt,0, UInt,-1, UInt,&dM ),
    NumPut(0x5c0000,dM,40) NumPut(cD,dM,104), NumPut(sW,dM,108), NumPut(sH,dM,112), NumPut(rR,dM,120)
    Return DllCall( "ChangeDisplaySettingsA", UInt,&dM, UInt,0 )
}

getRefreshRate() {
	VarSetCapacity(dM,156,0), NumPut(156,2,&dM,36)
	DllCall( "EnumDisplaySettingsA", UInt,0, UInt,-1, UInt,&dM ),
	return NumGet(&dM, 120)
}

; run subroutine every 5s
SetTimer, refreshRateChecker, 5000
return

; Ctrl+Alt+Q is the kill switch for the script.
^!q::Exit

GetSystemPowerStatus(PowerStatus, PowerFlag, LifePct, LifeTime, FullLifeTime)
oldPS := PowerStatus




refreshRateChecker:
	; Get sys power info
	GetSystemPowerStatus(PowerStatus, PowerFlag, LifePct, LifeTime, FullLifeTime)
	ps		:= PowerStatus

    ; get the current refresh rate
    refreshRate	:= getRefreshRate()

    ; if laptop is on battery power and refresh rate is high
    ; change to 60hz
    if ((ps = 0) && (refreshRate > 60))
		ChangeResolution(32, 2560, 1440, 60)



    ; if laptop is plugged in and refresh rate is low
    ; change to 165hz
    if ((ps = 1) && (refreshRate = 60))
        ChangeResolution(32, 2560, 1440, 165)
	
return



/*
Author: OldMan (AHK forums)
Link: https://autohotkey.com/board/topic/112863-battery-level-triggers-action-or-ends-a-loop/#entry660619

Title: GetSystemPowerStatus

Introduction
------------

	Retrieves the power status of the system. The status indicates whether the system is
	running on AC or DC power, whether the battery is currently charging, and how much
	battery life remains.

ACLineStatus
------------
	The AC power status. This member can be one of the following values.

	0       Offline
	1       Online
	255 Unknown Status

BatteryFlag
-----------
	The battery charge status. This member can contain one or more of the following flags.

	1       High--the battery capacity is at more than 66 percent
	2       Low--the battery capacity is at less than 33 percent
	4       Critical--the battery capacity is at less than 5 percent
	8       Charging
	128 no system battery
	255 Unknown status--unable to read the battery flag information

	The value is zero if the battery is not being charged and the battery capacity is between
	low and high.

Reserved1
---------
	Reserved; must be zero.

BatteryLifeTime
---------------
   The number of seconds of battery life remaining, or –1 if remaining seconds are unknown.

BatteryFullLifeTime
-------------------
	The number of seconds of battery life when at full charge, or –1 if full battery lifetime
	is unknown.

BatteryLifePercent
------------------
	The percentage of full battery charge remaining. This member can be a value in the range
	0 to 100, or 255 if status is unknown.

Remarks
-------
	The system is only capable of estimating BatteryFullLifeTime based on calculations on
	BatteryLifeTime and BatteryLifePercent. Without smart battery subsystems, this value may
	not be accurate enough to be useful.
*/

GetSystemPowerStatus(ByRef _ACLineStatus=0
					,ByRef _BatteryFlag=0
					,ByRef _BatteryLifePercent=0
					,ByRef _BatteryLifeTime=0
					,ByRef _BatteryFullLifeTime=0){

	static System_Power_Status

	VarSetCapacity(System_Power_Status, 12, 0)

	if !DllCall("kernel32.dll\GetSystemPowerStatus", "Ptr", &System_Power_Status)
		return false

	_ACLineStatus        := NumGet(System_Power_Status, 0, "UChar")
	_BatteryFlag         := NumGet(System_Power_Status, 1, "UChar")
	_BatteryLifePercent  := NumGet(System_Power_Status, 2, "UChar")
	_BatteryLifeTime     := NumGet(System_Power_Status, 4, "Int")
	_BatteryFullLifeTime := NumGet(System_Power_Status, 8, "Int")
	return true
}