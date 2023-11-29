def study_schedule(permanence_period, target_time):
    students_per_target_time = 0
    if target_time is None:
        return None

    for comein, comeout in permanence_period:
        if (comein is None or not type(comein) is int) or (
            comeout is None or not type(comeout) is int
        ):
            return None

        if comeout >= target_time >= comein:
            students_per_target_time += 1

    return students_per_target_time
