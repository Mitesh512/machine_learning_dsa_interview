from collections import deque, defaultdict

class FirstUniqueChar:
    def __init__(self):
        # Dictionary to store the frequency of characters
        self.char_count = defaultdict(int)
        # Queue to store the characters in the order they appear
        self.queue = deque()

    def add(self, char: str) -> str:
        """
        This function is called each time a new character is added to the stream.
        It updates the frequency of the character and the queue of potential unique characters.
        """
        # Increment the character count
        self.char_count[char] += 1
        
        # If the character is appearing for the first time, add it to the queue
        if self.char_count[char] == 1:
            self.queue.append(char)
        
        # Remove characters from the front of the queue that are no longer unique
        while self.queue and self.char_count[self.queue[0]] > 1:
            self.queue.popleft()

        # Return the first unique character if the queue is not empty
        return self.queue[0] if self.queue else None


# Example Usage
stream_processor = FirstUniqueChar()

# {g:2,e:4,k:2,s:2,f:1,o:1,r:1}
# [f,o,r]
# Stream of characters: we simulate this as a list of chars for demonstration.
stream = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]

# Process the stream one character at a time
for char in stream:
    result = stream_processor.add(char)
    print(f"After adding '{char}', first unique character: {result}")
