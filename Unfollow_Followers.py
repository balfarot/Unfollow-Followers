#Unfollow followers (use library instafollow)

from instapy import instapy

session = instapy(username="bre_nda_at"), passwd="$Mocha1154"
#you will need firefox mozilla explorer
seassion.login()
session.unfollow_users(amount=5, allFollowing=True, sleep_delay=60)
session.end()