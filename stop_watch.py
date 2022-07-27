import time


def stop_watch():
    """
    This function used to calculate difference between start time and end time
    :return:
    """
    start_time = float
    is_bool = True
    try:
        while is_bool:
            input_text = int(input("Type 1 to start or 0 to stop "))
            if input_text == 1:
                start_time = time.time()
                print("Timer Started")
                print("Type stop to stop the Timer")
            if input_text == 0:
                print("Timer Stopped")
                end_time = time.time()
                time_elapsed = round(end_time - start_time, 2)
                print("Time Elapsed: ", time_elapsed, " secs")
                is_bool = False
    except KeyboardInterrupt:
        print("Timer Stopped")
        end_time = time.time()
        time_elapsed = round(end_time - start_time, 2)
        print("Time Elapsed: ", time_elapsed, " secs")


if __name__ == "__main__":
    stop_watch()
