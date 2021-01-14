import configparser
config = configparser.ConfigParser()

config['Drivers'] = {'chrome': '../../chromedriver.exe'}
config['Pages'] = {'google': 'https://www.google.com',
                   'twitter': 'https://www.twitter.com',
                   'facebook': 'https://www.facebook.com'
                   }

with open('config.ini', 'w') as configfile:
    config.write(configfile)
