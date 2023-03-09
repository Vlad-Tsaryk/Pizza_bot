import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the universe of discourse for temperature and fan speed
temp = np.arange(0, 101, 1)
fan_speed = np.arange(0, 101, 1)

# Define the fuzzy sets for temperature
temp_cold = fuzz.trimf(temp, [0, 0, 50])
temp_warm = fuzz.trimf(temp, [0, 50, 100])
temp_hot = fuzz.trimf(temp, [50, 100, 100])

# Define the fuzzy sets for fan speed
fan_low = fuzz.trimf(fan_speed, [0, 0, 50])
fan_medium = fuzz.trimf(fan_speed, [0, 50, 100])
fan_high = fuzz.trimf(fan_speed, [50, 100, 100])

# Define the antecedent and consequent variables
temp_antecedent = ctrl.Antecedent(temp, 'temperature')
fan_consequent = ctrl.Consequent(fan_speed, 'fan_speed')

# Add the fuzzy sets to the antecedent and consequent variables
temp_antecedent['cold'] = temp_cold
temp_antecedent['warm'] = temp_warm
temp_antecedent['hot'] = temp_hot
fan_consequent['low'] = fan_low
fan_consequent['medium'] = fan_medium
fan_consequent['high'] = fan_high

# Define the rules for fan speed based on temperature
rule1 = ctrl.Rule(temp_warm, fan_medium)
rule2 = ctrl.Rule(temp_hot, fan_high)
rule3 = ctrl.Rule(temp_cold, fan_low)

# Create the control system
fan_control_system = ctrl.ControlSystem([rule1, rule2, rule3])
fan_control = ctrl.ControlSystemSimulation(fan_control_system)

# Determine the fan speed for a temperature of 75 degrees
fan_control.input['temperature'] = 75
fan_control.compute()
fan_speed_value = fan_control.output['fan_speed']

print(fan_speed_value)
