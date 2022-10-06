#Complete the following pseudocode for a program that prompts the user to input a temperature reading and humidity reading. If the temperature is greater than 25 or humidity is greater than 50% and window is closed, then output a message “Open the window”. If the temperature is below 10, the humidity is below 50% and the window is not closed, output a message “Close the window”.

temp = input('Enter the temperature')
humidity = input('Enter the humidity')
if window == "closed":
  if temp > 25 or humidity > 50:
    print('Open the window')
elif window == "opened":
  if temp < 10 or humidity < 50:
    print('Open the window')
