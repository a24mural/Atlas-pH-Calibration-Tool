from atlas_i2c import atlas_i2c
from time import sleep

print("Let's get this bread")

def calibration (probe_number):
    sensor_address= probe_number
    dev=atlas_i2c.AtlasI2C()
    dev.set_i2c_address(sensor_address)
    
    max_it=5 #redo calibration 5 times if needed
    i=0

    while i < max_it:
        sleep(5)
        print("Rinse probe and place it in the pH 7 solution. Type 'y' in the input box when completed.")
        
        for i in range(1000):
            a=input()
            if a =="y":
                dev.write("Cal,mid,7.00")
                break
            else:
                print("Incorrect input")
        
        sleep(5)
        print("Rinse probe and place it in the pH 4 solution. Type 'y' in the input when completed.")
        
        for i in range(1000):
            b=input()
            if b=="y":
                dev.write("Cal,low,4.00")
                break
            else:
                print("Incorrect input")
        
        sleep(5)
        print("Rinse probe and place it in the pH 10 solution. Type 'y' in the input when completed.")
        
        for i in range (1000):
            c=input()
            if c=="y":
                dev.write("Cal,high,10.00")
                break
            else:
                print ("Incorrect input")
        
        sleep(5)
        dev.write("R")
        sleep(5)
        reading= float(dev.read("Cal").data)
        sleep(5)
        print ("Let's check if probe is properly calibrated. The reading is currently:",reading)
        if reading>10.1 or reading<9.9:
            print('Reading is far off from 10. Redo calibration and check condition of the probe.')
            i+=1
            break
        else:
            i=max_it
            print ("Reading is close enough to 10. Calibration of probe",probe_number,"is now complete. Woohoo!")
            break


print("Type in the probe number that you are calibrating")
sensor_address=input()
calibration(int(sensor_address))
