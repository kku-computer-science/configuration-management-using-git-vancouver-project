
def get_input():
    raw = input("Enter numbers separated by spaces: ")
    arr = list(map(int, raw.split()))

    algo = input("Choose algorithm (quick / bubble): ").strip().lower()
    return arr, algo

# Bubble Sort  (Suphakrit)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Quick Sort (Phisanuwat)

def quick_sort(arr):
    def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def main():
    arr, algo = get_input()

    if algo == "bubble":
        result = bubble_sort(arr)
        print("Sorted (Bubble Sort):", result)

    elif algo == "quick":
        result = quick_sort(arr)
        print("Sorted (Quick Sort):", result)

    else:
        print("Invalid algorithm choice!")

if __name__ == "__main__":
    main()
