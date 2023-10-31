#Juan Islas
#31/10/2023
#Prove that I can write a Python program and write and run test functions to help me find and fix mistakes in the program.
#Sources: CSE111 lessons


def ji_water_column_height(tower_height, tank_height):
   #calculates and returns the height of a column of water from a tower height and a tank wall height
    h = tower_height + (3 * tank_height) / 4

    return h

def ji_pressure_gain_from_water_height(height):
    #calculates and returns the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank
    p = (998.2 * 9.80665 * height)/1000

    return p

def ji_pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    #calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through
    p = (- friction_factor * pipe_length * 998.2 * fluid_velocity**2) /(2000 * pipe_diameter)

    return p

def ji_pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
     # calculates the water pressure lost because of fittings such as 45° and 90° bends that are in a pipeline

    p = (-0.04 * 998.2 * fluid_velocity **2 * quantity_fittings) / 2000

    return p

def ji_reynolds_number(hydraulic_diameter, fluid_velocity):
    #calculates and returns the Reynolds number for a pipe with water flowing through it
    r = 998.2 * hydraulic_diameter * fluid_velocity / 0.0010016

    return r

def ji_pressure_loss_from_pipe_reduction(larger_diameter,fluid_velocity, reynolds_number, smaller_diameter):
    #calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe with a smaller diameter
    k = (0.1 + (50/reynolds_number)) * ((larger_diameter/smaller_diameter)**4-1)

    p = (-k * 998.2 * fluid_velocity**2) / 2000

    return p

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = ji_water_column_height(tower_height, tank_height)
    pressure = ji_pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = ji_reynolds_number(diameter, velocity)
    loss = ji_pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = ji_pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = ji_pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = ji_pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()