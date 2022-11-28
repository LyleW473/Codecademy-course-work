class DriveBot():
    all_disabled = False
    latitude = -999999 
    longitude = -999999

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()

robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_2 = DriveBot(35, 75, 25)
print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

robot_3 = DriveBot(20, 60, 10)

DriveBot.longitude = 50.0
DriveBot.latitude = -50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.latitude)
print(robot_3.latitude)
print(robot_1.longitude)
print(robot_2.longitude)
print(robot_3.longitude)
print(robot_1.all_disabled)
print(robot_2.all_disabled)
print(robot_3.all_disabled)