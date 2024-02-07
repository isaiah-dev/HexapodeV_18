import constants
import simulation
import os
import robot


def clear_screen():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')
        
def print_behaviour_choice():
    print("Select Behaviour :")
    print("1. Move leg to position")
    print("2. Move robot center to position")
    print("3. Walk in a straight line")
    print("4. Rotate robot")
    print("5. Exit")
    behaviour_choice = input("Choice : ")
    
    return behaviour_choice


def main_menu():
    while(True):
        
        print("- Select Software Mode : -")
        print("1. Robot")
        print("2. Simulation")
        print("3. Exit")
        choice = input("Choice : ")
        clear_screen()

        match choice:
            case "1":
                print("- Robot Mode -")
                constants.set_constants(constants.SOFTMODE.PHANTOMX)
                while(True):
                    behaviour_choice = print_behaviour_choice()
                    if behaviour_choice == "5":
                        break
                    else:
                        r = robot.robot_physical()
                        robot.robot_action(r, behaviour_choice)
                        # raise NotImplementedError("Not handled yed.")
                clear_screen()
            case "2":
                print("- Simulation Mode -")
                constants.set_constants(constants.SOFTMODE.PHANTOMX_SIMULATION)
                while(True):
                    behaviour_choice = print_behaviour_choice()
                    if behaviour_choice == "5":
                        break
                    else:
                        r = robot.robot_simulation()
                        robot.robot_action(r, behaviour_choice)
                        # simulation.simulation_init(constants.BEHAVIOUR_MODE(int(behaviour_choice)).name)
                clear_screen()
            case _:
                print("Bye!")
                break