class User:
    def __init__(self, name, age, gender, weight, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height


class Activity:
    def __init__(self, exercise_type, calorie_burned, duration, date):
        self.exercise_type = exercise_type
        self.calorie_burned = calorie_burned
        self.duration = duration
        self.date = date


class Diet:
    def __init__(self, meal_type, food_item, calorie_intake, time):
        self.meal_type = meal_type
        self.food_item = food_item
        self.calorie_intake = calorie_intake
        self.time = time


class FitnessTracking:
    def __init__(self):
        self.users = []
        self.activities = []
        self.meals = []

    def add_user(self, name, age, gender, weight, height):
        user = User(name, age, gender, weight, height)
        self.users.append(user)
        print(f"{name} is added successfully!")

    def log_activities(self, exercise_type, calorie_burned, duration, date):
        activity = [exercise_type, calorie_burned, duration, date]
        if activity in self.activities:
            print("Activities Overlapped!")
        else:
            self.activities.append(activity)
            print(f"Activity for {activity.name} logged successfully.")

    def log_food_intake(self, meal_type, food_item, calorie_intake, time):
        type = ["Breakfast", "Lunch", "Snacks", "Dinner"]
        if meal_type in type:
            diet = Diet(meal_type, food_item, calorie_intake, time)
            self.meals.append(diet)
            print("Diet is logged.")
        else:
            print("Invalid Dietary inputs.")

    def generate_reports(self):
        pass


if __name__ == "__main__":
    fitness = FitnessTracking()

    fitness.add_user("John", 35, "Male", "58kg", )



