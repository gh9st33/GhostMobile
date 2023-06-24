class JoystickDataPacketTranslator():
    #This is the left Joypad X axis(Primarily used for turning) -128 to 128
    l3x = None

    #This is the left Joypad Y axis(Probably not needed) -128 to 128
    l3y = None

    #This is the right Joypad X axis(Probably not needed) -128 to 128
    r3x = None

    #This is the right Joypad Y axis(Probably not needed) -128 to 128
    r3y = None

    #This is the the left trigger(Primarily used for brakes) 0-256
    l2 = None

    #This is the the right trigger(Primarily used as a gas pedal) 0-256
    r2 = None

    #This is R1, used for camera right
    r1 = None

    #This is L1, used for camera left
    l1 = None

    #This is Triangle, used to reset camera position
    triangle = None

    def createDataString(self, l3x, l3y, r3x, r3y, l2, r2, l1, r1):
        dataString = f"l3x:{l3x}"
        dataString += f" l3y:{l3y}"
        dataString += f" r3x:{r3x}"
        dataString += f" r3y:{r3y}"
        dataString += f" l2:{l2}"
        dataString += f" r2:{r2}"
        dataString += f" l1:{l1}"
        dataString += f" r1:{r1}"

        return dataString

    def interpretDataString(self, dataString):
        for dat in dataString.split():
            if dat.startswith("l3x"):
                self.l3x = float(dat.split(":")[1])
            if dat.startswith("l3y"):
                self.l3y = float(dat.split(":")[1])
            if dat.startswith("r3x"):
                self.r3x = float(dat.split(":")[1])
            if dat.startswith("r3y"):
                self.r3y = float(dat.split(":")[1])
            if dat.startswith("l2"):
                self.l2 = float(dat.split(":")[1])
            if dat.startswith("r2"):
                self.r2 = float(dat.split(":")[1])
            if dat.startswith("l1"):
                self.l1 = float(dat.split(":")[1])
            if dat.startswith("r1"):
                self.r1 = float(dat.split(":")[1])