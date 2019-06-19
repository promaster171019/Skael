

class Config(object):
    # configuration for docker container
    # SQLALCHEMY_DATABASE_URI = 'postgres://postgres:@172.18.0.3/postgres'

    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:otto123@localhost/postgres'
    SECRET_KEY = 'test'
    MAILGUN_ORIGIN_DOMAIN = 'sandbox5831985ac78942ab8a98db8f5914bd3f.mailgun.org'
    MAILGUN_ORIGIN_EMAIL = 'postmaster@sandbox5831985ac78942ab8a98db8f5914bd3f.mailgun.org'
    MAILGUN_API_KEY = 'key-523a461199a84acaaedafccf940dcf66'
    HOST = 'http://localhost:5000'
    JWT_MAX_EXPIRATION = 2592000
    VERIFY_EMAIL_CONTENT = """
<html>
<head>
    <title>Verify your account</title>
</head>
<body>
  Hello!

  <br>
  <br>
  Thanks for signing up, but first you need to verify your account.

  <br>
  <br>
  <form method="put" action="{0}">
    <button type="submit">Verify account</button>
  </form>

  <br>
  <br>
  Should the button above not work, copy the link below and paste it into your browser:

  <br>
  <br>
  <a href="{0}">{0}</a>

  <br>
  <br>
  You could use this password temporarily - "{1}".
</body>
</html>
"""
    RESET_EMAIL_CONTENT = """
<html>
<head>
    <title>Reset your Password</title>
</head>
<body>
  To reset your password, click the button below

  <br>
  <br>
  <form method="put" action="{0}">
    <button type="submit">Reset password</button>
  </form>

  <br>
  <br>
  Should the button above not work, copy the link below and paste it into your browser:

  <br>
  <br>
  <a href="{0}">{0}</a>
</body>
"""



