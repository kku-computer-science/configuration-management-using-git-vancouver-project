# ============================
# TEAM SORTING PROGRAM
# ============================

# Input Handler  (Suphakrit)

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
    # Phisanuwat ทำการเติม Code ของ Quick Sort
    pass


# ----------------------------
# Main Program
# ----------------------------
def main():
    arr, algo = get_input()

    if algo == "bubble":
        result = bubble_sort(arr)
        print("Sorted (Bubble Sort):", result)

    elif algo == "quick":
        print("Quick sort not implemented yet ( teammate will add ).")

    else:
        print("Invalid algorithm choice!")

if __name__ == "__main__":
    main()
