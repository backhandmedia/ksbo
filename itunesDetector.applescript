global latest_song

property okflag : false

on run
	tell application "System Events"
		if not (exists process "iTunes") then return
	end tell
	
	set latest_song to ""
end run

on idle
	tell application "iTunes"
		if not (exists current track) then
			return
		else
			copy name of current track to current_tracks_name
			if current_tracks_name is not latest_song then
				copy current_tracks_name to latest_song
				do shell script "ksbo.py"
			end if
		end if
		return 10
	end tell
end idle