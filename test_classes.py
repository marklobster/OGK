# Test Classes

class Test(object):        
    def __init__(self, message, next_event):
        self.message = message
        self.next_event = next_event
    
    def main(self):
        print(self.message)
        self.next_event.main()


class Test_3(Test):
    def main(self):
        choice = input(self.message).upper()
        while choice != "P" and choice != "Q":
            choice = input(self.message).upper()
            if choice == "P":
                self.next_event.main()

        
test3 = Test_3("Press Q to quit or P to play again.", None)
test2 = Test("This is also a test.", test3)
test1 = Test("This is a test", test2)






if __name__ == "__main__":
    print("This is a module for 'Oh Great Knight'")
    input("Press enter to exit.")
