import numpy as np

def get_matrix():
    r = int(input("Rows: "))
    c = int(input("Cols: "))
    print("Enter values:")
    return np.array([list(map(float, input().split())) for _ in range(r)])

while True:
    print("\n1.Add  \n2.Subtract  \n3.Multiply  \n4.Transpose  \n5.Determinant  \n6.Exit")
    choice = input("\nChoose: ")

    if choice == "1":
        print("Matrix A:")
        A = get_matrix()
        print("Matrix B:")
        B = get_matrix()
        print("Result:\n", A + B)

    elif choice == "2":
        print("Matrix A:")
        A = get_matrix()
        print("Matrix B:")
        B = get_matrix()
        print("Result:\n", A - B)

    elif choice == "3":
        print("Matrix A:")
        A = get_matrix()
        print("Matrix B:")
        B = get_matrix()
        print("Result:\n", A @ B)

    elif choice == "4":
        print("Matrix:")
        A = get_matrix()
        print("Transpose:\n", A.T)

    elif choice == "5":
        print("Matrix:")
        A = get_matrix()
        print("Determinant:", np.linalg.det(A))

    elif choice == "6":
        print("Bye!")
        break

    else:
        print("Invalid choice")
