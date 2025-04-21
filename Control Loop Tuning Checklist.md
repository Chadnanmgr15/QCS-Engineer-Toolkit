# 🧰 Control Loop Tuning Checklist

This document outlines the key steps and best practices for tuning PID loops in process industries, especially in pulp & paper QCS/DCS environments.

---

## ✅ Pre-Tuning Checklist

- [ ] Identify loop purpose (e.g., level, flow, pressure, moisture)
- [ ] Check actuator health (no stiction, proper response)
- [ ] Verify sensor calibration and stability
- [ ] Review process dynamics (dead time, lag, gain)
- [ ] Ensure loop is in manual before tuning

---

## ⚙️ Recommended PID Tuning Methods

| Method           | When to Use                           | Notes |
|------------------|----------------------------------------|-------|
| Ziegler-Nichols | Fast processes, less noise              | Initial guess only |
| Lambda Tuning   | Slow processes, like level control      | Good for smooth control |
| Manual Trial & Error | Skilled-based tuning              | Use only if experienced |

---

## 📈 Tuning Template

| Parameter       | Value |
|----------------|-------|
| PV (Process Variable) | Moisture Sensor |
| SP (Setpoint)        | 45% |
| Controller Mode      | PID |
| P Gain (Kp)          | 1.2 |
| Integral (Ti)        | 180s |
| Derivative (Td)      | 20s |
| Final Control Element | Steam Valve |
| Notes                | Valve shows some deadband |

---

## 🛑 Post-Tuning Actions

- [ ] Put loop back in auto
- [ ] Monitor for 1–2 hours
- [ ] Document final settings
- [ ] Inform operations team
