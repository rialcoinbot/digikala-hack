import requests

data = {
  "otp_call": "false",
  "username": "09*********"
}

response = requests.post('https://api.digikala.com/v1/user/authenticate/', json=data)

print(response.status_code)
