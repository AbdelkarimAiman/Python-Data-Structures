from typing import Any, Optional

class Queue:
    """
    Queue Implementation using Python List.
    Strategy: FIFO (First In, First Out).
    """
    def __init__(self) -> None:
        self.items = [] # Renamed 'q' to 'items' for clarity

    def enqueue(self, value: Any) -> None:
        """
        Add an item to the rear of the queue.
        Time Complexity: O(1)
        """
        self.items.append(value)

    def dequeue(self) -> Optional[Any]:
        """
        Remove and return the front item.
        Time Complexity: O(n) - Because popping from index 0 requires shifting elements.
        Note: For O(1) performance in production, use 'collections.deque'.
        """
        if self.is_empty():
            print("Queue Underflow (Empty)")
            return None
        return self.items.pop(0)
    
    def front(self) -> Optional[Any]:
        """Get the front item without removing it."""
        if self.is_empty():
            return None
        return self.items[0]
    
    def size(self) -> int:
        """Get the current number of elements."""
        return len(self.items)
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self.items) == 0

# --- Main Execution ---
if __name__ == "__main__":
    q = Queue()

    # Enqueue operations
    print("--- Enqueue Operations ---")
    elements = [10, 20, 5, 7, 2]
    for el in elements:
        q.enqueue(el)
        print(f"Enqueued: {el}")

    print("-" * 30)
    print(f"Front value before dequeue: {q.front()}")
    print("-" * 30)

    # Dequeue operations
    print("--- Dequeue Operations ---")
    
    removed_item = q.dequeue()
    print(f"Dequeue 1: Removed {removed_item}")
    print(f"New Front: {q.front()}")
    
    removed_item = q.dequeue()
    print(f"Dequeue 2: Removed {removed_item}")
    
    print("-" * 30)
    print(f"Final Front value: {q.front()}")
    print(f"Queue Size: {q.size()}")