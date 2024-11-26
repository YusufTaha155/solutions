
steps_nombers = input("Enter the numbers of steps (use spaces between evry value) : ")

steps_list = list(map(int, steps_nombers.split()))

bigest_value = max(steps_list)
print("the most steps are:", bigest_value)

smallest_value = min(steps_list)
print("the least steps are:", smallest_value)

average_steps = sum(steps_list) / len(steps_list)
print("Average steps =", average_steps)

sorted_list = sorted(steps_list, reverse=True)
print("Steps sorted in descending order :", sorted_list)