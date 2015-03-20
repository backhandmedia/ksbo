#!/usr/bin/python
#imports for iTunes support
from Foundation import *
from ScriptingBridge import *
import hipchat
import urllib
import urllib2
import xml.etree.ElementTree as ET

HIPCHAT_TOKEN=''


#get the link from spotify
def getSpotifyId(artist):
	try:
		urlEncodedArtist = urllib.quote(artist.encode("utf-8"))
		spotifyUrl = 'http://ws.spotify.com/search/1/artist?q=' + urlEncodedArtist
		spotifyResponse = urllib2.urlopen(spotifyUrl)
		spotifyXml = spotifyResponse.read()
		root = ET.fromstring(spotifyXml)
		spotifyString = root[4].attrib['href']
		spotifyArtistID = spotifyString[15:]
		return spotifyArtistID
	except:
		return

#get current itunes song
def getSongInfo():
	iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
	currentArtist = iTunes.currentTrack().artist()
	track = iTunes.currentTrack().name()
	if getSpotifyId(currentArtist):
		spotifyLink = "http://open.spotify.com/artist/" + getSpotifyId(currentArtist)
	else:
		searchTerm = urllib.quote(currentArtist.encode("utf-8"))
		spotifyLink = "http://google.com/search?q=" + searchTerm
	nowPlayingInfo = track + " by <a href='" + spotifyLink + "'>" + currentArtist + "</a>"
	return nowPlayingInfo


	

#post to hipchat

hipster = hipchat.HipChat(token=HIPCHAT_TOKEN)

try:
	hipster.method('rooms/message', method='POST', parameters={'room_id': 217773, 'from': 'KSBO', 'message': 'Now Playing on KSBO: ' + getSongInfo(), 'message_format': 'html'})
except:
	pass


