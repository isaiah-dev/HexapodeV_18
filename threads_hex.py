import threading
import simulation
import robot
import reality

def start_thread(thread_id):
    simulation_thread = threading.Thread(target=simulation.__init__)
    reality_thread = threading.Thread(target=reality.__init__)
    test_thread = threading.Thread(target=robot.robot_action)

    match thread_id:
        case 1:
            try:
                reality_thread.start()   
            except Exception:
                print(f'ending thread {thread_id}')     
        case 2:
            try:
                simulation_thread.start()   
            except Exception:
                simulation_thread.join()
                print(f'ending thread {thread_id}')    
        case 3:
            test_thread.start()
