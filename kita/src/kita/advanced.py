
class integrals:
    def trapezoidal(f, a, b, n):
        h = float(b - a) / n
        s = 0.0
        s += f(a)/2.0
        for i in range(1, n):
            s += f(a + i*h)
        s += f(b)/2.0
        return s * h

class Matrix:

    def mul(A, B):
        # Check if matrices can be multiplied
        if len(A[0]) != len(B):
            print("These matrices cannot be multiplied")
            return None
        
        # Initialize result matrix with zeros
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        
        # Perform multiplication
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        
        return result
    
    def print(result):
        if result:
            for row in result:
                print(row)
