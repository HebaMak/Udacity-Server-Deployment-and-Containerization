# set variables TOKEN & LOG_LEVEL to my terminal
# $env:JWT_SECRET = 'myjwtsecret'
# $env:LOG_LEVEL = 'DEBUG'

# # To verify
# echo $env:JWT_SECRET
# echo $env:LOG_LEVEL

#--------------------------------------

# instead of using bash # A secret text string to be used to creating a JWT export JWT_SECRET='myjwtsecret' export LOG_LEVEL=DEBUG # Verify echo $JWT_SECRET echo $LOG_LEVEL
# Invoke-WebRequest -Uri http://127.0.0.1:8080 -Method GET
# Invoke-RestMethod -Uri http://127.0.0.1:8080 -Method GET


#---------------------------------------

# instead of 
'''
export TOKEN=`curl --data '{"email":"abc@xyz.com","password":"mypwd"}' --header "Content-Type: application/json" -X POST localhost:8080/auth  | jq -r '.token'`
'''

#run this 
'''
$TOKEN = (Invoke-WebRequest -Uri "http://localhost:8080/auth" -Method Post -ContentType "application/json" -Body '{"email":"abc@xyz.com","password":"mypwd"}' | Select-Object -ExpandProperty Content | 
ConvertFrom-Json).token
'''

#----------------------------------------------

# instead of using this 
'''
curl --request GET 'http://localhost:8080/contents' -H "Authorization: Bearer ${TOKEN}" | jq .
'''
#run this
'''
Invoke-WebRequest -Uri 'http://localhost:8080/contents' -Method GET -Headers @{Authorization = "Bearer $TOKEN"} | ConvertFrom-Json

'''


#---------------------------------------
# instead of using
'''
curl --request GET 'http://localhost:80/'
'''

#use this 
'''
Invoke-WebRequest -Uri 'http://localhost:80/'
''' 

#------------------------------------------------------
#instead of using these
'''
# Calls the endpoint 'localhost:80/auth' with the email/password as the message body. 
# The return JWT token assigned to the environment variable 'TOKEN' 
export TOKEN=`curl --data '{"email":"abc@xyz.com","password":"WindowsPwd"}' --header "Content-Type: application/json" -X POST localhost:80/auth  | jq -r '.token'`
echo $TOKEN

# Decrypt the token and returns its content
curl --request GET 'http://localhost:80/contents' -H "Authorization: Bearer ${TOKEN}" | jq .
'''

# use these
# Calls the endpoint 'localhost:80/auth' with the email/password as the message body.
# The return JWT token assigned to the environment variable 'TOKEN'

''' 
$TOKEN = (Invoke-RestMethod -Uri 'http://localhost:80/auth' -Method Post -ContentType "application/json" -Body '{"email":"abc@xyz.com","password":"WindowsPwd"}').token
Write-Host $TOKEN

# Decrypt the token and return its content
Invoke-RestMethod -Uri 'http://localhost:80/contents' -Method Get -Headers @{Authorization = "Bearer $TOKEN"} | ConvertTo-Json
'''

#------------------------------------------

