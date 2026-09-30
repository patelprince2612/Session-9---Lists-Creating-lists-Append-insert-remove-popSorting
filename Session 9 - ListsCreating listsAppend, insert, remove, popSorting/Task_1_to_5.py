# 1. Create a Python list called my_fav_apps containing 5 apps you use daily and print the list.
my_fav_apps = ['Instagram', 'Zomato', 'Spotify', 'YouTube', 'Reddit']
print("Task 1:", my_fav_apps)

# 2. Use the append() method to add a new app to your my_fav_apps list, then print the updated list.
my_fav_apps.append('Notion')
print("Task 2:", my_fav_apps)

# 3. Insert 'WhatsApp' at the second position in your my_fav_apps list using the insert() method and print the result.
# Remember, list indices start from 0, so the second position is index 1.
my_fav_apps.insert(1, 'WhatsApp')
print("Task 3:", my_fav_apps)

# 4. Remove an app you no longer use from your my_fav_apps list using the remove() method, 
# then use the pop() method to remove the last app and print the list after each operation.
my_fav_apps.remove('Zomato')
print("Task 4 (After remove):", my_fav_apps)

my_fav_apps.pop()
print("Task 4 (After pop):", my_fav_apps)

# 5. Sort your my_fav_apps list in alphabetical order using the sort() method, 
# then reverse the order to show your least used app first and print both results.
# Constraint: Use only list methods, not built-in sorted().
my_fav_apps.sort()
print("Task 5 (Alphabetical sort):", my_fav_apps)

my_fav_apps.reverse()
print("Task 5 (Reversed order):", my_fav_apps)