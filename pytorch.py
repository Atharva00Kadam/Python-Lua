import torch

print("Welcome to my required__ matrix calculator!")
print("Please enter required__**2 numbers separated by spaces (row-wise):")

# Read a single line of input and split into 25 numbers
input_str = input("➡️ ").strip().split()

if len(input_str) != required__**2:
    print("❌ You must enter exactly required__**2 numbers!")
else:
    try:
        numbers = [float(num) for num in input_str]
        matrix = torch.tensor(numbers).reshape(a, b)
        det = torch.linalg.det(matrix)
        print("\nYour matrix:")
        print(matrix)
        print(f"\n✅ Determinant: {det.item():.4f}")
    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")

