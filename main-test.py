# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(10,22) == 30
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()
