from controller import Robot, Motion
import time

class Nao(Robot):
    def __init__(self):
        Robot.__init__(self)
        self.motion = Motion('../../motions/FastKick.motion')  # Load Fast Kick motion
        self.motion.setLoop(False)  # Confirming motion doesn't loop
        self.timeStep = int(self.getBasicTimeStep())  # Get basic time step and convert to integer
        self.motion_playing = False  # Flag to track motion state

    def run(self):
    
        # Wait for a 1-second delay to stabilize
        start_time = time.time()
        while time.time() - start_time < 1:  # 1 seconds delay
            if self.step(self.timeStep) == -1:
                break

        # Using the Fast shooting motion
        self.motion.play()
        self.motion_playing = True

        # Wait until the kick motion finishes
        while self.motion_playing:
            if self.step(self.timeStep) == -1:
                break

        self.motion.stop()
        self.motion_playing = False  # Reset motion state

        # Return to the initial standing position
        self.standInit.play()
        while self.standInit.isRunning():
            if self.step(self.timeStep) == -1:
                break

# Creating Nao Robot instance to run main loop
robot = Nao()
robot.run()