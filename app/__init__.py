from flask import Flask
from flask_dance.contrib.google import make_google_blueprint, google
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key="CHANGETHISADD.envorSecrets.jsonORSOMETHING"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
db=SQLAlchemy(app)

google_bp=make_google_blueprint(client_id="YOURTOPSECRETCLIENTID",
                                client_secret="YOURTORPSECRETGOOGLECLIENTSECRET",
                                redirect_to='google_login')
app.register_blueprint(google_bp, url_prefix='/google')


#linked in and github and facebook will probably be similar but get this first part
#going first
# LinkedIn OAuth setup (similar structure as Google)
# from flask_dance.contrib.linkedin import make_linkedin_blueprint, linkedin
# linkedin_bp = make_linkedin_blueprint(client_id='YOUR_LINKEDIN_CLIENT_ID',
#                                       client_secret='YOUR_LINKEDIN_CLIENT_SECRET',
#                                       redirect_to='linkedin_login')
# app.register_blueprint(linkedin_bp, url_prefix='/linkein

if __name__=='__main__':
    app.run(debug=True)