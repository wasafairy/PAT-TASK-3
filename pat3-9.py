def find_triplet(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if numbers[i] + numbers[j] + numbers[k] == target:
                    return (numbers[i], numbers[j], numbers[k])
    

if __name__ == "__main__":
    numbers = [10, 20, 30, 9]
    target_sum = 59
    triplet = find_triplet(numbers, target_sum)
    if triplet:
        print(f"Triplet found: {triplet}")
    else:
        print("No triplet found.")
