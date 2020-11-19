import tweepy
import csv

ckey ='...'
csecret ='...'
atoken = '...'
asecret = '...'

# Attributes of a twitter user profile (this header is already on my file)
twitter_datafile_attr = ['follow_request_sent', 'profile_use_background_image',       'contributors_enabled', 'id', 'verified', 
                       'profile_image_url_https', 'profile_sidebar_fill_color', 'profile_text_color', 'followers_count', 
                       'profile_sidebar_border_color', 'id_str', 'default_profile_image', 'listed_count' 'is_translation_enabled', 
                       'utc_offset', 'statuses_count', 'description', 'friends_count', 'location', 'profile_link_color', 
                       'profile_image_url', 'notifications', 'geo_enabled', 'profile_background_color', 'profile_banner_url', 
                       'profile_background_image_url', 
                       'screen_name', 'lang', 'following', 'profile_background_tile', 'favourites_count', 'name', 'url', 'created_at', 
                       'profile_background_image_url_https', 'time_zone', 'protected', 'default_profile', 'is_translator']

#Authencation
auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api=tweepy.API(auth)
# search for people who have both the words "hawaii and "water" anywhere in their bios
user=api.search('hawaii water')

Name = "Justine Braun"


