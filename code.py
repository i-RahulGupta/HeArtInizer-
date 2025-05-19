import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Parameters for the simulation
np.random.seed(42)
time = np.arange(0, 24 * 60, 1)  # Simulate one day in minutes

# Adjust lengths to match the corresponding time intervals
sleeping_time = np.arange(0, 6 * 60, 1)  # 6 hours of sleep
running_time_morning = np.arange(6 * 60, 8 * 60, 1)  # 2 hours of running in the morning
walking_time = np.arange(8 * 60, 18 * 60, 1)  # 10 hours of walking
running_time_evening = np.arange(18 * 60, 22 * 60, 1)  # 4 hours of running in the evening
sleeping_time_evening = np.arange(22 * 60, 24 * 60, 1)  # 2 hours of sleep in the evening

# Generate heart rate data for each activity
sleeping_bpm = np.random.normal(60, 3, len(sleeping_time))  # Simulate sleeping heart rate
running_bpm_morning = np.random.normal(140, 10, len(running_time_morning))  # Morning running
walking_bpm = np.random.normal(90, 5, len(walking_time))  # Simulate walking heart rate
running_bpm_evening = np.random.normal(140, 10, len(running_time_evening))  # Evening running
sleeping_bpm_evening = np.random.normal(60, 3, len(sleeping_time_evening))  # Evening sleep

# Combine the heart rate data into one array
heart_rate = np.concatenate([
    sleeping_bpm,
    running_bpm_morning,
    walking_bpm,
    running_bpm_evening,
    sleeping_bpm_evening
])

# Create setpoints for the heart rate based on activities
setpoints = np.concatenate([
    np.full(len(sleeping_time), 60),  # Sleeping setpoint
    np.full(len(running_time_morning), 140),  # Running setpoint
    np.full(len(walking_time), 90),  # Walking setpoint
    np.full(len(running_time_evening), 140),  # Running setpoint
    np.full(len(sleeping_time_evening), 60)  # Sleeping setpoint
])


# PID Controller Class
class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.integral = 0
        self.prev_error = 0

    def update(self, measured_value):
        # Calculate error
        error = self.setpoint - measured_value

        # Update integral and derivative terms
        self.integral += error
        derivative = error - self.prev_error

        # Calculate PID output
        output = self.kp * error + self.ki * self.integral + self.kd * derivative

        # Update previous error
        self.prev_error = error

        return output


# Initialize PID controller
pid = PIDController(kp=0.1, ki=0.01, kd=0.05, setpoint=90)

# Apply the PID controller to the heart rate data
adjusted_heart_rate = []
for i in range(len(time)):
    # Update the setpoint for each time step
    pid.setpoint = setpoints[i]

    # Get the control signal to adjust the heart rate
    control_signal = pid.update(heart_rate[i])

    # Adjust heart rate and store the result
    adjusted_hr = heart_rate[i] + control_signal
    adjusted_heart_rate.append(adjusted_hr)

# Calculate the Mean Square Error (MSE)
mse = mean_squared_error(setpoints, adjusted_heart_rate)
print(f"Mean Square Error: {mse:.2f}")

# Plot the original vs adjusted heart rate
plt.figure(figsize=(12, 6))
plt.plot(time, heart_rate, label='Original Heart Rate')
plt.plot(time, adjusted_heart_rate, label='Adjusted Heart Rate')
plt.plot(time, setpoints, label='Setpoints', linestyle='dashed')
plt.title('Heart Rate Adjustment Using  Prophet PID Controller')
plt.xlabel('Time (minutes)')
plt.ylabel('Heart Rate (bpm)')
plt.legend()
plt.grid(True)
plt.show()



from sklearn.metrics import mean_squared_error

# Calculate the Mean Square Error (MSE) between the original heart rate and the setpoints
mse_original = mean_squared_error(setpoints, heart_rate)
print(f"Mean Square Error between setpoints and original heart rate: {mse_original:.2f}")

# Calculate the Mean Square Error (MSE) between the setpoints and the adjusted heart rate
mse_adjusted = mean_squared_error(setpoints, adjusted_heart_rate)
print(f"Mean Square Error between setpoints and adjusted heart rate: {mse_adjusted:.2f}")

