# Library Backend

# Auth
## Login
### POST call - /auth/login/ -> 
- Check email already exist
- validate password - hash map sha512
- Two step verification -> OTP to email(smtp) -> check whether the same user have the otp

### POST call - /auth/otp ->
- otp is valid for 2 hour  
- OTP also expire after 4 attempts
- Generate JWT token

## SignUp
### POST call - /auth/signup/ ->
- Validate the email address and also check if it exist in DB
- Generate the ID for the user - 6digit
- Hash the password and store in DB

## ForgetPassword
### POST call - /auth/forget-password
- get the email ID from user
- with uuid generete token
- store the token in DB and email to with resetURL to user

## Reset
### PUT call - /auth/reset
- Token which we sent to user and the new password
- validate the token and it is valid only for 2 hours
- Update the new password and delete the genereated toekn from DB

# Dashboard 
We will validate the JWT token at beforeRequest once it is valid the user is allowed to fetch the page

## GET call - /lib
- Fetch all the book from DB and bookCover image from the S3 bucket of AWS

## GET call - /lib/search
- Fetch all the book by book name from DB and bookCover image from the S3 bucket of AWS

## GET call - /lib/download
- Fetch the pdf url from the DB by using bookID
- Covert the file into binary
- Generate the public key using *HmacSHA256* which is a public key and the private key is shared between the FE and BE service as an secret environment variables
- allow download

## POST call - /lib/role
- Validate if the user has role admin
- change the role of the user as per payload
- Update the role change in the DB

## POST call - /lib/upload
- Validate if the user has role admin
- Covert the file into binary
- Upload the cover image and pdf into S3 bucket
- Generate a unique bookId and Insert the detail into database


## IMPROVE
- All key is in env which can be shifted to the sceret manager
- Clean up of expired OTP and Reset password rows
