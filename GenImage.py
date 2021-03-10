#!/usr/bin/env python
# coding: utf-8

# Copyright 2020 Brian Bodemann [brian underscore bodemann at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

from image_utils import ImageText
from bs4 import BeautifulSoup
import urllib.request
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Set a specific location on G-Drive to save your file 
gDriveId = ''
# browser link: http://drive.google.com/uc?export=view&id=<your GDrive File id>
# Use custom CSS in OBS to make it transparent: body { background-color: rgba(0,0,0,0)!important } 

# Grab the Race name & number from WTRL TTT-Event page
url = "https://www.wtrl.racing/ttt/TTT-Event.php"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
   the_page = response.read()

# Initate the Scraper:
soup = BeautifulSoup(the_page, 'lxml')

# Grab the body from the scraper
body = soup.body

# Initate a loop token to save the the element following Race Number:
saveValue = 0

# Find all the h2 and h4 tags in the page (I hope they use these consistently);
for tag in soup.find_all(['h2','h4']):

	# Check to see if this is the element following Race Number:
	if saveValue == 1:

		# Split the race name before the distance information:
		raceName = tag.contents[0].split(" -")[0]

		# Stop looking for Race Number / Race Name:
		break
	
	# Check to see if this is the Race Number:
	if 'WTRL Team Time Trial #' in tag.contents[0]:
		
		# Split off the Race number at the hashtag:
		raceNumber = tag.contents[0].split("Trial ")[1]
		
		# Set the loop token to save the next element (which should be the Race Course):
		saveValue = 1


# A table of courses, WORLDS for finding the raceWorld
courses = [("Time Trial Lap","BOLOGNA"),
("Bell Lap","CRIT CITY"),
("Downtown Dolphin","CRIT CITY"),
("Casse-Pattes","FRANCE"),
("Douce France","FRANCE"),
("La Reine","FRANCE"),
("Petit Boucle","FRANCE"),
("Route Grand Vitesse","FRANCE"),
("Roule Ma Poule","FRANCE"),
("Tire-Bouchon","FRANCE"),
("Ven-Top","FRANCE"),
("2018 UCI Worlds Course Short Lap","INNSBRUCK"),
("Achterbahn","INNSBRUCK"),
("Innsbruck KOM After Party","INNSBRUCK"),
("Innsbruckring","INNSBRUCK"),
("Lutscher CCW","INNSBRUCK"),
("Lutscher","INNSBRUCK"),
("Classique Reverse","LONDON"),
("Classique","LONDON"),
("Greater London 8","LONDON"),
("Greater London Flat","LONDON"),
("Greater London Loop Reverse","LONDON"),
("Greater London Loop","LONDON"),
("Greatest London Flat","LONDON"),
("Greatest London Loop Reverse","LONDON"),
("Greatest London Loop","LONDON"),
("Keith Hill After Party","LONDON"),
("Leith Hill After Party","LONDON"),
("London 8 Reverse","LONDON"),
("London 8","LONDON"),
("London Loop Reverse","LONDON"),
("London Loop with Box Hill Finish","LONDON"),
("London Loop","LONDON"),
("Surrey Hills","LONDON"),
("The London Pretzel","LONDON"),
("The PRL Full","LONDON"),
("The PRL Half","LONDON"),
("Triple Loops","LONDON"),
("Astoria Line 8","NEW YORK"),
("Couch to Sky K","NEW YORK"),
("Everything Bagel","NEW YORK"),
("Flat Irons","NEW YORK"),
("Gotham Grind Reverse","NEW YORK"),
("Gotham Grind","NEW YORK"),
("Grand Central Circuit Reverse","NEW YORK"),
("Grand Central Circuit","NEW YORK"),
("Hudson Roll","NEW YORK"),
("Knickerbocker Reverse","NEW YORK"),
("Knickerbocker","NEW YORK"),
("Lady Liberty","NEW YORK"),
("LaGuardia Loop Reverse","NEW YORK"),
("LaGuardia Loop","NEW YORK"),
("Mighty Metropolitan","NEW YORK"),
("NYC KOM After Party","NEW YORK"),
("Park Perimeter Loop","NEW YORK"),
("Park Perimeter Reverse","NEW YORK"),
("Park to Peak","NEW YORK"),
("Rising Empire","NEW YORK"),
("Shuman Trail Loop Reverse","NEW YORK"),
("Shuman Trail Loop","NEW YORK"),
("The 6 Train Reverse","NEW YORK"),
("The 6 Train","NEW YORK"),
("The Highline Reverse","NEW YORK"),
("The Highline","NEW YORK"),
("Champs-Élysées","PARIS"),
("Lutece Express","PARIS"),
("2015 UCI Worlds Course","RICHMOND"),
("Cobbled Climbs Reverse","RICHMOND"),
("Cobbled Climbs","RICHMOND"),
("Libby Hill After Party","RICHMOND"),
("Richmond Rollercoaster","RICHMOND"),
("Richmond UCI Reverse","RICHMOND"),
("The Fan Flats","RICHMOND"),
("11.1 Ocean Blvd","WATOPIA"),
("5K Loop","WATOPIA"),
("Bambino Fondo","WATOPIA"),
("Beach Island Loop","WATOPIA"),
("Big Foot Hills","WATOPIA"),
("Big Loop Reverse","WATOPIA"),
("Big Loop","WATOPIA"),
("Bigger Loop","WATOPIA"),
("Chili Pepper Reverse","WATOPIA"),
("Chili Pepper","WATOPIA"),
("Dust In the Wind","WATOPIA"),
("Figure 8 Reverse","WATOPIA"),
("Figure 8","WATOPIA"),
("Flat Route Reverse","WATOPIA"),
("Flat Route","WATOPIA"),
("Four Horsemen","WATOPIA"),
("Gran Fondo","WATOPIA"),
("Hilly Route Reverse","WATOPIA"),
("Hilly Route","WATOPIA"),
("Jon's Route","WATOPIA"),
("Jungle Circuit Reverse","WATOPIA"),
("Jungle Circuit","WATOPIA"),
("May Field","WATOPIA"),
("Medio Fondo","WATOPIA"),
("Mountain 8","WATOPIA"),
("Mountain Route","WATOPIA"),
("Muir and the Mountain","WATOPIA"),
("Ocean Lava Cliffside Loop","WATOPIA"),
("Out and Back Again","WATOPIA"),
("Quatch Quest","WATOPIA"),
("Road to Ruins Reverse","WATOPIA"),
("Road to Ruins","WATOPIA"),
("Road to Sky","WATOPIA"),
("Run Path Reverse","WATOPIA"),
("Sand and Sequoias","WATOPIA"),
("Seaside Sprint","WATOPIA"),
("Serpentine 8","WATOPIA"),
("Tempus Fugit","WATOPIA"),
("That's Amore Reverse","WATOPIA"),
("That's Amore","WATOPIA"),
("The Magnificent 8","WATOPIA"),
("The Mega Pretzel","WATOPIA"),
("The Pretzel","WATOPIA"),
("The Über Pretzel","WATOPIA"),
("Three Sisters Reverse","WATOPIA"),
("Three Sisters","WATOPIA"),
("Tick Tock","WATOPIA"),
("Tour of Fire and Ice","WATOPIA"),
("Two Bridges Loop","WATOPIA"),
("Volcano Circuit CCW","WATOPIA"),
("Volcano Circuit","WATOPIA"),
("Volcano Climb After Party","WATOPIA"),
("Volcano Climb","WATOPIA"),
("Volcano Flat Reverse","WATOPIA"),
("Volcano Flat","WATOPIA"),
("Watopia's Waistband","WATOPIA"),
("WBR Climbing Series","WATOPIA"),
("Whole Lotta Lava","WATOPIA"),
("2019 UCI Worlds Harrogate Circuit","YORKSHIRE"),
("Duchy Estate","YORKSHIRE"),
("Harrogate Circuit Reverse","YORKSHIRE"),
("Queen's Highway","YORKSHIRE"),
("Royal Pump Room 8","YORKSHIRE"),
("Tour of Tewit Well","YORKSHIRE")]

# Find the Course World, from the Race Name using the list above (this is a crappy solution):
for event in courses:
	if event[0]==raceName:
		raceWorld=event[1]
		print("Race World Found: "+raceWorld)

#Iniate some values for the imager, so it doesn't get angry:
raceNumber="$$"
raceName="Race in Zwift"
raceWorld="Zwift"

#Initate the WTRL Gold Color
color = (233, 179, 116)

# Iniate the WTRL font, (File must be present in working folder)
font = 'hanzel_condensed_italic.ttf'

# Open the Template iage with WTRL Logo, (File must be present in working folder):
img = ImageText('template.png', background=(255, 255, 255, 200)) # 200 = alpha

# Add the Race number to the image, grab its calculated Width and Height
raceNumberWidth,raceNumberHeight=img.write_text((190, 20),raceNumber, font_filename=font,
               font_size='fill', max_width=190, max_height=100, color=color)

# Add the Race World under the Number and set it to have the same width
img.write_text((190, 110),raceWorld, font_filename=font,
               font_size='fill', max_width=raceNumberWidth, max_height=50, color=color)

# Add the Race Course Name to the Image and place it along side the race (text will be wrapped) 
img.write_text_box((380, 0), raceName, box_width=220, font_filename=font,
                   font_size=40, color=color, place='center', position="middle")

# Save the image to a local file
img.save('TTT_Race_Label.png')


## The following code let's you upload to a specific file location on Google Drive
## You will need to setup your own API access token on 
# Initiate Google API Authenticator
gauth = GoogleAuth()

# Try to load saved client credentials
gauth.LoadCredentialsFile('mycreds.txt')

if gauth.credentials is None:
    # Authenticate if they're not there

    # Force a lasting credential set (so you only need to authenticate once):
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})

    gauth.LocalWebserverAuth()

elif gauth.access_token_expired:

    # Refresh them if expired

    gauth.Refresh()
else:

    # Initialize the saved creds

    gauth.Authorize()

# Save the current credentials to a file
gauth.SaveCredentialsFile('mycreds.txt')  

drive = GoogleDrive(gauth)

# Upload to My Google Drive
drive = GoogleDrive(gauth) 
upload_file = 'TTT_Race_Label.png'

# Upload the file to the same ID, so that it is accessible at the same browser-link:
gfile = drive.CreateFile({'id':gDriveId})
gfile.SetContentFile(upload_file)
gfile.Upload()
