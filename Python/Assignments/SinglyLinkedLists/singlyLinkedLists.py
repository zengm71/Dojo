class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self) -> None:
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
    def add_to_back(self, val):
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front(self):
        self.head = self.head.next
        return self
    def remove_from_back(self):
        runner = self.head
        runner_next = runner.next
        runner_next2 = runner_next.next
        while (runner_next2 != None):
            runner = runner.next
            runner_next = runner.next
            runner_next2 = runner_next.next
        runner.next = None
        return self
    def remove_val(self, val):
        current_node = self.head
        if current_node.value == val:
            self.head = current_node.next
        else:
            previous_node = self.head
            while current_node.value != val:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = current_node.next
        return self
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
        else:
            i = 1
            previous_node = self.head
            current_node = previous_node.next
            while i != n and current_node.next != None:
                i = i + 1
                previous_node = current_node
                current_node = current_node.next
            if i == n:
                new_node = SLNode(val)
                previous_node.next = new_node
                new_node.next = current_node
            if current_node.next == None:
                if i < n-1:
                    print('n is too big')
                else:
                    self.add_to_back(val)
            
        return self
            


my_list = SList()
my_list.add_to_front("are").add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.remove_val('fun!').print_values()
my_list.insert_at(val = 'lol', n = 4).print_values()
# my_list.remove_from_front().print_values()
# my_list.print_values()
# my_list.remove_from_back().print_values()
