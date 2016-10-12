from test import *
import threading
if __name__=='__main__':
    print("装配线程")

    info("this is main")
    driver = run_service()

    # sel_server = threading.Thread(target=run_service)

    robot = threading.Thread(target=hello)
    # robot2 = threading.Thread(target=hello)

    # sel_server.start()
    time.sleep(3)

    robot.start()
    robot.join()

    driver.kill()
    # time.sleep(30)
    # robot2.start()