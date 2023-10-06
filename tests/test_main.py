from fck_aws_sso.authorize_sso import authorize_sso

def test_authorize_sso():
    authorize_sso("https://device.sso.us-east-1.amazonaws.com/", "XXXX-XXXX")