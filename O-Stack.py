








class Stack(object):

    def __init__(self):
        self.stack_data = []


    def push(self, data):
        self.stack_data.append(data)
    
    def pop(self):
        if self.depth() == 0:
            return None

        return self.stack_data.pop()


    def depth(self):
        return len(self.stack_data)


def add_to_stack():
    s = Stack()
    '''
    USER INPUTS A STRING INTO THE STACK.
    THE STACK RETURNS THE DEPTH.
    ASKS IF IT WANTS TO REMOVE THE LAST PIECE OF 
    DATA FROM THE STACK
    '''
    start = input('Start, Y/N : ')
    
    while start == 'Y':

        answer = input('Type \'yes\' to add name. Type \'re\' to remove last name. Type \'see\' to view amount : ')
        
        if answer == 'yes':
            s.push(input('Add name: '))
            while answer == 'yes':
                print(s.depth())
                break

        elif answer == 're':
            while answer == 're':
                print(s.depth())
                break
            print(s.pop()) # Maybe print

        elif answer == 'see':
            print(s.depth())
        else:
            print(s.depth())
            return None
        cont = input('Continue? Y/N : ')
        if cont == 'Y':
            continue
        else:
            break



def main():
    add_to_stack()

if __name__ == '__main__':
    main()




