class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char.isdigit():
                # If it's a digit, remove the closest non-digit to its left
                if stack:
                    stack.pop()
            else:
                # If it's a letter, keep it for now
                stack.append(char)
                
        # Combine the remaining letters back into a string
        return "".join(stack)

