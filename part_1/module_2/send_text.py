from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfcfe000827bc74ba4839d0743a0f9823"
# Your Auth Token from twilio.com/console
auth_token  = "7b01fb3be0386e0270b26bc0c7ecdf08"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18099808868", 
    from_="+12075693729",
    body="Mi negra bella, tan buena que estas. Te amo!")

print(message.sid)