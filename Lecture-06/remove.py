fruits_with_duplicates = ["apple", "banana", "appie", "cherry", "apple", "kiwi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Fruits after remove: {fruits_with_duplicates}")