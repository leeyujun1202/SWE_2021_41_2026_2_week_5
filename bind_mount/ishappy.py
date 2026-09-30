def isHappy(n):
    curr_num = n
    num_seen = set()

    while True:
        if curr_num == 1:
            return True

        if curr_num in num_seen:
            return False

        num_seen.add(curr_num)

        sum = 0
        remain_num = curr_num

        while remain_num > 0:
            digit = remain_num % 10
            squared = digit * digit

            sum = sum + squared

            remain_num = remain_num // 10

        curr_num = sum


if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as file:
        file.write(f"19: {sample0_output}\n")
        file.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")
