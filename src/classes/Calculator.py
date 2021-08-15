import math


class Calculator:

    def __init__(self) -> None:
        pass

    # HELPER

    def generate_distance_between_coordinates(self, coords1, coords2):
        x1, y1 = coords1
        x2, y2 = coords2
        return math.sqrt(
            math.pow((x2 - x1), 2) +
            math.pow((y2 - y1), 2)
        )

    # MOUSE MOVEMENTS

    def generate_mouse_movement_speed(self, events):
        speeds = []

        prev_x = 0
        prev_y = 0
        prev_timestamp = 0
        
        for i in range(len(events)):
            e = events[i]

            # IF FIRST MOUSE MOVEMENT
            if i == 0:
                speeds.append(0)
                prev_x = int(e['x'])
                prev_y = int(e['y'])
                prev_timestamp = int(e['timestamp'].replace('_', ''))
                continue

            coords1 = (prev_x, prev_y)
            coords2 = (int(e['x']), int(e['y']))

            # GENERATE SPEED ( pixels / millisecond)
            delta_time = (int(e['timestamp'].replace('_', '')) - prev_timestamp) / 1000
            delta_distance = self.generate_distance_between_coordinates(coords1, coords2)
            speeds.append(delta_distance / delta_time)

            # UPDATE PREV VALUES
            prev_timestamp = int(e['timestamp'].replace('_', ''))
            prev_x, prev_y = coords2

        return speeds

