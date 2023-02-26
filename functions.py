from lists import days, times, notify, days_idx, courses

def mainFunc(day):
    for i in range(len(days)):
        if day == days[i]:
            courses_list = coursesFunc(days_idx[i])
            times_list = timesFunc(days_idx[i])
            notification_list = notificationFunc(days_idx[i])
    return courses_list, times_list, notification_list

def coursesFunc(idces):
    today_courses = []
    course_idx = idces[0]
    for i in course_idx:
        today_courses.append(courses[i])
    return today_courses

def timesFunc(idces):
    course_times = []
    times_idx = idces[1]
    for i in times_idx:
        course_times.append(times[i])
    return course_times

def notificationFunc(idces):
    notification_times = []
    times_idx = idces[1]
    for i in times_idx:
        notification_times.append(notify[i])
    return notification_times

