# Lambda Tuning for Self-Regulating Process
# Requires Process Gain (K), Dead Time (θ), Time Constant (T), and Desired Closed-Loop Time Constant (Tc)

def lambda_tuning(K, T, theta, Tc):
    print("Lambda Tuning Results:\n")

    kp = (T / (K * (Tc + theta)))
    ti = T
    td = 0  # Often skipped in Lambda tuning

    print(f"Kp = {kp:.3f}")
    print(f"Ti = {ti:.3f} seconds")
    print(f"Td = {td:.3f} seconds (typically unused in Lambda Tuning)")


# Example input
if __name__ == "__main__":
    K = float(input("Enter Process Gain (K): "))
    T = float(input("Enter Time Constant (T): "))
    theta = float(input("Enter Dead Time (θ): "))
    Tc = float(input("Enter Desired Closed-Loop Time Constant (Tc): "))
    lambda_tuning(K, T, theta, Tc)
