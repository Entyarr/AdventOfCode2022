count = 0


for line in open("wha.txt", 'r').readlines():
    line = line.strip()
    elves = line.split(',')
    nums = []
    for elf in elves:
        nums.append(elf.split('-'))
    if((int(nums[0][0]) >= int(nums[1][0]) and int(nums[0][0]) <= int(nums[1][1])) or
       (int(nums[0][1]) >= int(nums[1][0]) and int(nums[0][1]) <= int(nums[1][1])) or
       (int(nums[1][0]) >= int(nums[0][0]) and int(nums[1][0]) <= int(nums[0][1])) or
       (int(nums[1][1]) >= int(nums[0][0]) and int(nums[1][1]) <= int(nums[0][1]))):
        print(nums)
        count += 1

print(count)
