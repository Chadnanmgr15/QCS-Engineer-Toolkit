# Ziegler-Nichols PID Tuning Calculator
# Based on Ultimate Gain (Ku) and Ultimate Period (Pu)

def ziegler_nichols_tuning(ku, pu):
    print("Ziegler-Nichols Tuning Results (Classic):\n")

    # P Controller
    p_kp = 0.5 * ku

    # PI Controller
    pi_kp = 0.45 * ku
    pi_ti = pu / 1.2

    # PID Controller
    pid_kp = 0.6 * ku
    pid_ti = pu / 2
    pid_td = pu / 8

    print(f"P Controller:      Kp = {p_kp:.2f}")
    print(f"PI Controller:     Kp = {pi_kp:.2f}, Ti = {pi_ti:.2f}")
    print(f"PID Controller:    Kp = {pid_kp:.2f}, Ti = {pid_ti:.2f}, Td = {pid_td:.2f}")


# Example input
if __name__ == "__main__":
    ku = float(input("Enter Ultimate Gain (Ku): "))
    pu = float(input("Enter Ultimate Period (Pu): "))
    ziegler_nichols_tuning(ku, pu)
