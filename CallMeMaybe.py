from twilio.rest import TwilioRestClient
 
# Your can find your AccountSID and AuthToken from http://twilio.com/user/account
account_sid = "YOUSHOULDPUTYOURSIDHERE"
auth_token = "YOUSHOULDPUTYOURAUTHTOKENHERE"
client = TwilioRestClient(account_sid, auth_token)
 
call = client.calls.create(to="+17078675309",
                           from_="+19006492568",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print call.sid