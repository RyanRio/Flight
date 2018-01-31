# Flight

Steps for setting up I2C on Raspberry Pi, as found on [this site](http://www.instructables.com/id/Raspberry-Pi-I2C-Python/)

1.  run the command  **sudo nano /etc/modprobe.d/raspi-blacklist.conf**  
  In this file there is a comment and two lines. Add a **#** before the "I2C" line to comment it out
1.  Original:
  
    ```
    # blacklist spi and i2c by default (many users don't need them)

    blacklist spi-bcm2708
    blacklist i2c-bcm2708
    ```
  
    End Result:
  
    ```
    # blacklist spi and i2c by default (many users don't need them)

    blacklist spi-bcm2708
    # blacklist i2c-bcm2708
    ```
1. asdf
