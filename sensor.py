class Sensor:
    def __init__(self):
        self.mailbox1 = False
        self.mailbox2 = False
        self.mailbox3 = False
        self.mailbox4 = False
        self.mailbox5 = False

    def check_movement(self):
        """Check de movement status"""
        self.mailbox1 = False
        self.mailbox2 = False
        self.mailbox3 = False
        self.mailbox4 = False
        self.mailbox5 = True

        mailboxes = [self.mailbox1, self.mailbox2, self.mailbox3, self.mailbox4, self.mailbox5]
        for i in mailboxes:
            if i == True:
                if i == self.mailbox1:
                    return 1
                if i == self.mailbox2:
                    return 2 
                if i == self.mailbox3:
                    return 3
                if i == self.mailbox4:
                    return 4
                if i == self.mailbox5:
                    return 5