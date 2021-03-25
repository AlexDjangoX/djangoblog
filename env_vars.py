import os

email_host_user = os.environ.get('EMAIL_HOST_USER')
email_host_password = os.environ.get('EMAIL_HOST_PASSWORD')

print(email_host_user)
print(email_host_password)
