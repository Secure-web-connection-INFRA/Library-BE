reset_email_template = """
<html>
<head>
    <title>Password Reset</title>
</head>
<body>
    <p>Hi,</p>
    <p>Click the link below to reset your password:</p>
    <p><a href="{{ reset_url }}">Reset Password</a>:{{reset_url}}</p>
</body>
</html>
"""

otp_email_template = """
<html>
<head>
    <title>Login OTP</title>
</head>
<body>
    <p>Hi {{name}},</p>
    <p>Please enter the OTP. It is valid for 5minutes</p>
    <p>OTP Code:<b>{{otp}}</b></p>
</body>
</html>
"""