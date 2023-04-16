import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()

# function to display text
def display(msg, row=1, col=0):
    mylcd.lcd_display_string(str(msg), row, col)
    
# function to clear text
def clear():
    mylcd.lcd_clear()