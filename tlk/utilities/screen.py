import time, random, threading, curses

class RealTimeScreen:

    def __init__(self):
        self.exit_flag = threading.Event()  #Event to signal the end of the cycle
    #End_def


    def monitor_server(self, window):
        ''' '''
        window.addstr("===CPU===\n")

        while not self.exit_flag.is_set():
            # Get CPU values
            cpu_values = self.getCPUValues()

            # Clear the CPU values line
            window.move(1, 0)
            window.clrtoeol()

            # Print CPU values in a single line
            cpu_line = " ".join([f"{cpu}: {valor}%     " for cpu, valor in cpu_values.items()])
            window.addstr(1, 0, cpu_line)

            # Refresh the window
            window.refresh()

            # Wait for a time interval before the next update
            time.sleep(1)

        window.addstr("\nExiting...")
        window.refresh()
    #End_def


    def getCPUValues(self):
        ''' Get CPU values from hypervisor module '''
        cpu0 = random.randint(1, 100)
        cpu1 = random.randint(1, 100)
        cpu2 = random.randint(1, 100)
        cpu3 = random.randint(1, 100)
        cpu_values = {'cpu0': cpu0, 'cpu1': cpu1, 'cpu2': cpu2, 'cpu3': cpu3}

        return cpu_values
    #End_def


    def askForOutput(self, stdscr):
        ''' '''
        stdscr.addstr("\nPress ENTER to exit!", curses.A_BOLD)  # Add the A_BOLD atrribute for bold text
        stdscr.refresh()
        while True:
            opcion = stdscr.getch()
            if opcion == ord('\n'):  # Chek if Enter key was pressed
                self.exit_flag.set()  # Set the output signal
                break
    #End_def


    def screen(self, stdscr):
        ''' '''
        curses.curs_set(0)  # Hide the cursor

        # Create and execute the threads
        monitor_thread = threading.Thread(target=self.monitor_server, args=(stdscr,))
        preguntar_thread = threading.Thread(target=self.askForOutput, args=(stdscr,))

        monitor_thread.start()
        preguntar_thread.start()

        # Wait for both threads to finish
        monitor_thread.join()
        preguntar_thread.join()
    #End_def


    def cursesWrapper(self):
        ''' '''
        rts = RealTimeScreen()
        curses.wrapper(rts.screen)
    #End_def
