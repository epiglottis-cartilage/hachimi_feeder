import time
import sight
import weight
import motor
import beep

# import hearing
from sight import HUMAN, CAT


if __name__ == "__main__":
    sight.init()
    # hearing.init()
    weight.init()
    motor.init()
    beep.init()
    try:
        while True:
            w = weight.read_avg()
            print(f"{w - 295}g remain...")
            if w - 295 < 40:
                beep.beep()
                time.sleep(3)

            step = 430 if w < 600 else 400

            # print(sight.can_see(), hearing.meow(), weight.read_avg())
            if sight.can_see([HUMAN, CAT]):
                print("I seeeee you, feeding...")
                motor.rotate(step)
                motor.rotate(-step)
                time.sleep(10)

            time.sleep(1)
    except KeyboardInterrupt:
        pass
    sight.close()
    # hearing.close()
    weight.close()
    motor.close()
    beep.close()
