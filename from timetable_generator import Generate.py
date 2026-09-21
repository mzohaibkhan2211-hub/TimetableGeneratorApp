from timetable_generator import GenerateTimeTable

scheduler = GenerateTimeTable()
timetable = scheduler.run()
scheduler.pretty_print()