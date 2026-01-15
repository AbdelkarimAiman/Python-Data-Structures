class Stack:
    """
    Simple Stack Implementation using List.
    Strategy: LIFO (Last In, First Out).
    """
    def __init__(self):
        self.items = []

    def push(self, value):
        """Add item to the top. Complexity: O(1)"""
        self.items.append(value)

    def pop(self):
        """Remove and return the top item. Complexity: O(1)"""
        if self.is_empty():
            print("Stack Underflow (Empty)")
            return None
        else:
            return self.items.pop()

    def is_empty(self):
        """Check if stack is empty. Complexity: O(1)"""
        return len(self.items) == 0
        
    def top(self):
        """Get the top item without removing it. Complexity: O(1)"""
        if self.is_empty():
            return None
        return self.items[-1]

# --- Main Execution ---
if __name__ == "__main__":
    stack1 = Stack()
    
    elements = [10, 20, 30, 40, 50, 60]
    for el in elements:
        stack1.push(el)

    print(f"Top Element: {stack1.top()}") 

    print("\nPopping elements from Stack:")
    while not stack1.is_empty():
        print(stack1.pop())