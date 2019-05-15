class Vampires:

    coven = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = False
        self.drank_blood_today = False

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f"{self.name}, {self.age}, {self.in_coffin}, {self.drank_blood_today}"

    @classmethod
    def create(cls, name, age):
        vampire = Vampires(name, age)
        Vampires.coven.append(vampire)
        return vampire
    
    def drink_blood(self):
        self.drank_blood_today = True
    
    @classmethod
    def sunrise(cls):
        for vampire in cls.coven:
            starved = vampire.drank_blood_today is False
            sunburned = vampire.in_coffin is False
            if sunburned or starved:
                cls.coven.remove(vampire)
    
    @classmethod
    def sunset(cls):
        for vampire in Vampires.coven:
            vampire.in_coffin = False
            vampire.drank_blood_today = False
    
    def go_home(self):
        self.in_coffin = True
        return self

print("Initializing Coven")

cindy = Vampires.create('Cindy', 25)
Vampires.create('Sofia', 25)
liza = Vampires.create('Liza', 25)
Vampires.create('Chris', 25)

# print("Verify Coven")
print(Vampires.coven)

Vampires.coven[0].drink_blood()
print(Vampires.coven[0].drank_blood_today)

Vampires.coven[0].go_home()
print(Vampires.coven[0].in_coffin)

Vampires.sunset()
print("Verify Coven: after sunset")
print(Vampires.coven)

print("Verify Coven: Drank Blood and In Coffin values")
print(Vampires.coven[0].drank_blood_today)
print(Vampires.coven[0].in_coffin)
print(Vampires.coven[1].drank_blood_today)
print(Vampires.coven[1].in_coffin)
print(Vampires.coven[2].drank_blood_today)
print(Vampires.coven[2].in_coffin)
print(Vampires.coven[3].drank_blood_today)
print(Vampires.coven[3].in_coffin)

print("Verify Coven: after sunrise")
Vampires.sunrise()
print(Vampires.coven)
print(Vampires.coven[0].drank_blood_today)
print(Vampires.coven[0].in_coffin)
print(Vampires.coven[1].drank_blood_today)
print(Vampires.coven[1].in_coffin)
print(cindy.drank_blood_today)
print(cindy.in_coffin)
print(liza.drank_blood_today)
print(liza.in_coffin)

# Weird thing happening where two of my vampires are disappearing 