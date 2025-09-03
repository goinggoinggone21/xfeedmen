import requests
import datetime
import random
import requests, traceback, json, io, os, urllib.request, sys
#import moviepy
from moviepy.editor import VideoFileClip

#sys.stdout.reconfigure(encoding='utf-8')

def has_audio(filepath):
    """
    Checks if an MP4 file has an audio track.

    Args:
        filepath (str): The path to the MP4 file.

    Returns:
        bool: True if the file has an audio track, False otherwise.
              Returns None if the file is not found or an error occurs.
    """
    if not os.path.exists(filepath):
        print(f"helper.has_audio Error: File not found at '{filepath}'")
        return None

    try:
        # Load the video clip
        clip = VideoFileClip(filepath)

        # Check if the audio attribute is not None
        if clip.audio is not None:
            clip.close() # Close the clip to release resources
            return True
        else:
            clip.close() # Close the clip
            return False
    except Exception as e:
        print(f"helper.has_audio An error occurred while processing '{filepath}': {e}")
        return None


def get_redgifs_embedded_video_url(redgifs_url, output_fn):
	API_URL_REDGIFS = 'https://api.redgifs.com/v2/gifs/'
	r = requests.get('https://api.redgifs.com/v2/auth/temporary')
	token = r.json()['token']

	headers={"Authorization": "Bearer "+token}
	try:
		print("redgifs_url = {}".format(redgifs_url))

		#Get RedGifs video ID
		redgifs_ID = redgifs_url.split('/watch/', 1)
		redgifs_ID = redgifs_ID[1]
		print("redgifs_ID = {}".format(redgifs_ID))
		
		sess = requests.Session()
		
		#Get RedGifs Video Meta
		# request = requests.get(API_URL_REDGIFS + redgifs_ID)
		request = sess.get(API_URL_REDGIFS + redgifs_ID, headers=headers)
		print(request)
		
		if request is None:
			return
		else:
			rawData = request.json()
			#print(rawData)
			#print("rawData = {}".format(rawData))

			#Get HD video url
			hd_video_url = rawData['gif']['urls']['hd']
			#print("hd_video_url = {}".format(hd_video_url))
			
			with sess.get(hd_video_url, stream=True) as r:
				with open(output_fn, 'wb') as f:
					for chunk in r.iter_content(chunk_size=8192): 
						# If you have chunk encoded response uncomment 
						# if and set chunk_size parameter to None.
						# if chunk: 
						f.write(chunk)
			return hd_video_url
	except Exception:
		traceback.print_exc()
		return
def convert_hastag_to_at(tweet_title_):
	#if '#AngelWicky' in   tweet_title_:
	#	return  tweet_title_.replace('#AngelWicky','@Angel_Wicky_II')
	if '#SukiSin' in tweet_title_:
		return tweet_title_.replace('#SukiSin','@sukisinxx')
	elif '#liz_103' in tweet_title_:
		return tweet_title_.replace('#liz_103','@LilyLouOfficial')
	elif '#JosephineJackson' in tweet_title_:
		return tweet_title_.replace('#JosephineJackson','@josephinejxxx')
	elif '#SophiaLocke' in tweet_title_:
		return tweet_title_.replace('#SophiaLocke','@_SophiaLocke_')
	elif '#ArabelleRaphael' in tweet_title_:
		return tweet_title_.replace('#ArabelleRaphael','@MommyArabelle')
	elif '#VeronicaLeal' in tweet_title_:
		return tweet_title_.replace('#VeronicaLeal','@VeronicaLealoff')
	elif '#ValericaSteele' in tweet_title_:
		return tweet_title_.replace('#ValericaSteele','@VALERiCAx')
	elif '#AnnaDeVille' in tweet_title_:
		return tweet_title_.replace('#AnnaDeVille','@AnnadeVilleXXX')
	elif '#VioletMyers' in tweet_title_:
		return tweet_title_.replace('#VioletMyers','@violetsaucy')
	elif '#KiannaDior' in tweet_title_:
		return tweet_title_.replace('#KiannaDior','@Kianna_Dior')
	elif '#AvaDevine' in tweet_title_:
		return tweet_title_.replace('#AvaDevine','@1avadevine')
	elif '#RemyLaCroix' in tweet_title_:
		return tweet_title_.replace('#RemyLaCroix','@RemyLaCroixxxxx')
	#elif '#StephanieMichelle' in tweet_title_:
	#	return tweet_title_.replace('#StephanieMichelle','@omystephanie')
	elif '#MandyMuse' in tweet_title_:
		return tweet_title_.replace('#MandyMuse','@mandymusemedia')
	elif '#KendraLust' in tweet_title_:
		return tweet_title_.replace('#KendraLust','@KendraLust')
	elif '#SyrenDeMer' in tweet_title_:
		return tweet_title_.replace('#SyrenDeMer','@SyrenDeMerXXX')
	elif '#AshleyAdams' in tweet_title_:
		return tweet_title_.replace('#AshleyAdams','@xoxoashleyadams')
	elif '#KristyBlack' in tweet_title_:
		return tweet_title_.replace('#KristyBlack','@KristyBlack_new')
	elif '#ConniePerignon' in tweet_title_:
		return tweet_title_.replace('#ConniePerignon','@connperignon')
	elif '#MikeAdriano' in tweet_title_:
		return tweet_title_.replace('#MikeAdriano','@MikeAdrianoFeed')
	elif '#evaangelina' in tweet_title_:
		return tweet_title_.replace('#evaangelina','@onlyevaangelina')	
	elif '#NatashaNice' in tweet_title_:
		return tweet_title_.replace('#NatashaNice','@BeNiceNatasha')# \n \n https://onlyfans.com/benicenatasha')
	else:
		return tweet_title_

def convert_name_to_at(tweet_title_):
	if 'Valerica Steele' in tweet_title_:
		tweet_title_submit =  tweet_title_.replace('Valerica Steele','@VALERiCAx')
	if 'Kendra Lust' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Kendra Lust','@KendraLust')
	if 'Sage Hunter' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Sage Hunter','@sagexxxhunter')
	if 'Hailey Rose' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Hailey Rose','@HaileyRoseFucks')
	if 'Alexa Chains' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Alexa Chains','@ChainsAlexxxa')
	if 'Aria Sloane' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Aria Sloane','@theariasloane')
	if 'Raven Lane' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Raven Lane','@ravenlaneXX')
	if 'Rissa May' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Rissa May','@_RissaMay_XO')
	if 'Scarlett Rosewood' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Scarlett Rosewood','@ScarlettRose__2')
	if 'River Lynn' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('River Lynn','@riverlynnxxx')
	if 'Addison Vodka' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Addison Vodka','@addisonv0dka')
	if 'Scarlett Hampton' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Scarlett Hampton','@scarletthampt0n')
	if 'Dixie Lynn' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Dixie Lynn','@Xxxdixielynn')
	if 'Mia Kay' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Mia Kay','@MissMiaKayXXX')
	if 'Nicole Nichols' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Nicole Nichols','@NicoleNicholss')
	if 'Luna Lovely' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Luna Lovely','@lunalovelyx')
	if 'Jewelz Blu' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Jewelz Blu','@jewelz_blu')
	if 'Gia Derza' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Gia Derza','@giaderza69')
	if 'Sophia Burns' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Sophia Burns','@sophiaburnsx')
	if 'Rebel Rhyder' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Rebel Rhyder','@RebelRhyderXXX')
	if 'Jasmine Sherni' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Jasmine Sherni','@jasminesherni_')
	if 'Hazel Heart' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Hazel Heart','@HazelHeartxxx')
	if 'Brianna Arson' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Brianna Arson','@thebriannaarson')
	if 'Emily Jade' in tweet_title_:
		tweet_title_submit = tweet_title_.replace('Emily Jade','@xoemilyjade')
	
	if 'tweet_title_submit' not in locals():
		tweet_title_submit = tweet_title_
	if tweet_title_submit[0] == '@':
		tweet_title_submit = tweet_title_submit[-1] + ' ' + tweet_title_submit
	return tweet_title_submit

