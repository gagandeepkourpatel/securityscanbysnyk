import os

filename = input("Enter file name to view: ")
os.system(f"cat {filename}")  # Unsafe! Allows command chaining (e.g., file.txt; rm -rf /)
