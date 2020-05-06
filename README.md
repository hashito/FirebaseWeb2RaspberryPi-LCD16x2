# FirebaseWeb2RaspberryPi-LCD16x2

# init
## firebase

** ruhru change**
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}
```
※this ruhru is dangerous...

## raspberry

** init command **

```
sudo raspi-config nonint do_i2c 0
sudo apt update
sudo apt install i2c-tools
sudo apt install python3 python3-pip
pip3 install smbus
wget http://osoyoo.com/driver/i2clcda.py
```

** hard **

### LCD→Pi
 GND→GND  
 VCC→5Vpin  
 SDA→SDA  
 SCL→SCL  


# start up
## firebase
use... 'firebase hosting'

## raspberry

```
python3 firebase2lcd.py
```
