file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

# recommended way to handle files
# most of the time 'with' syntax is used for file handling
with open('youtube.txt', 'w') as file:
    file.write('chai aur python')