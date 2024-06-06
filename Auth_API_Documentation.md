# Auth API Documentation

API to create, login, reset the account is granted

## Sign-up

**Method:** `POST`

**URL:** `localhost:5000/auth/signup`

**Body:**

```json
{
  "name": "Aswin kumar",
  "email": "aswinrockz101@gmail.com",
  "password": "aswin"
}
```

**Response:**

```
User has been successfully created
```

## Login

**Method:** `POST`

**URL:** `localhost:5000/auth/login`

**Body:**

```json
{
  "email": "kumarsaswin10@gmail.com",
  "password": "aswin"
}
```

**Response:**

```
OTP is sent to Email kumarsaswin10@gmail.com
```

## Forgetpassword

**Method:** `POST`

**URL:** `localhost:5000/auth/forget-password`

**Body:**

```json
{
  "email": "nithya.anuki@gmail.com"
}
```

**Response:**

```
Reset link is successfully sent
```

## Reset

**Method:** `PUT`

**URL:** `localhost:5000/auth/reset`

**Body:**

```json
{
  "token": "7ca23c73-1224-482d-b022-a48a553c3259",
  "password": "aswin123"
}
```

**Response:**

```
Password has been updated. Try login
```

## Otp

**Method:** `POST`

**URL:** `localhost:5000/auth/otp`

**Body:**

```json
{
  "email": "kumarsaswin10@gmail.com",
  "otp": 3113
}
```

**Response:**

```json
{
  "jwtToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NzE3MTYyLCJleHAiOjE3MTc2NjM0OTEsIm5hbWUiOiJBc3dpbiBrdW1hciJ9.Uk0pbnyWmFDgItCpYz7JUm2sp81THqsEe4aZb6YfWtg",
  "role": "ADMIN",
  "userName": "Aswin kumar"
}
```
