# GenLabelWtrlTTT
This tool allows you to generate a weekly label to place on your OBS Studio (or other streaming tool) with the WTRL logo, Race number & world, and Race course. The script will create a transparent overlay file.

# Notes on usage:
Most people have a gmail, so google drive might be a good option for you to host your file in a way that you or others can access it on OBS.

## Get image_utils:
Make a sub-directory 'image_utils' in your python site-packages directory and place this file there:

https://gist.githubusercontent.com/pojda/8bf989a0556845aaf4662cd34f21d269/raw/48278b2f2efae00b8c797c3fc378503ce758b71c/image_utils.py

Project Info:

https://gist.github.com/pojda/8bf989a0556845aaf4662cd34f21d269#file-image_utils-py

## Setup a Google Drive API access token:
https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf

## Final Google Drive steps:
Click share and choose 'get link' and 'anyone on the internet' can access your file on Google Drive.
Copy the link and paste to a text editor. The 'ID' is the long string of characters between '/file/d/' and 'view?usp=sharing'.
Update the GenImage.py script file to set the gDriveId as this 'ID'.

## To use in OBs (or other):
Add your ID to this link to get a browser source link you can use in OBS (or other):

```http://drive.google.com/uc?export=view&id=```

Use custom CSS in OBS to make it transparent:

```body { background-color: rgba(0,0,0,0)!important }```
