import random

class Zombie:

    # class variables
    max_speed = 5
    max_strength = 8
    horde = []
    plague_level = 10
    default_speed = 1
    default_strength = 3

    def __init__(self, speed, strength):
        """Initializes zombie's speed."""
        # instance variables
        # speed handling
        if speed > Zombie.max_speed:
          self.speed = Zombie.default_speed
        else:
          self.speed = speed

        # strength handling
        if strength > Zombie.max_strength:
            self.strength = Zombie.default_strength
        else:
            self.strength = strength

    def __str__(self):
        return "Speed: {} -- Strength: {}".format(self.speed, self.strength)

    # class methods
    @classmethod
    def spawn(cls):
        """Spawns a random number of new zombies, based on the plague level,
        adding each one to the horde.  Each zombie gets a random speed.
        For the purpose of testing (in test.py), add a minimum of 2 zombies to the horde."""
        new_zombies = random.randint(2, Zombie.plague_level)
        count = 0

        while count < new_zombies:
            speed = random.randint(1, Zombie.max_speed)
            strength = random.randint(1, Zombie.max_strength)
            Zombie.horde.append(Zombie(speed, strength))
            count += 1

    @classmethod
    def new_day(cls):
        """Represents the events of yet another day of the zombie apocalypse.
        Every day some zombies die off (phew!), some new ones show up, and the
        plague level increases (by any number from 0 to 2)."""
        Zombie.increase_plague_level()
        Zombie.spawn()
        Zombie.some_die_off()

    @classmethod
    def some_die_off(cls):
        """Removes a random number (between 0 and 10) of zombies from the horde.
        For the purpose of testing (in test.py), maintain a minimum of 2 zombies in the horde."""
        how_many_die = random.randint(0, 10)
        counter = 0
        while counter < how_many_die and len(Zombie.horde) > 2:
            random_zombie = random.randint(0,len(Zombie.horde) - 1)
            Zombie.horde.pop(random_zombie)
            counter += 1

    @classmethod
    def increase_plague_level(cls):
        """Increase the current plague level by a random number from 0 to 20% of the horde's size."""
        random_increase = random.randint(0,round(0.2 * len(Zombie.horde)))
        Zombie.plague_level += random_increase

    @classmethod
    def deadliest_zombie(cls):
        """Return the deadliest zombie in the horde, one with the highest combination of speed and strength."""
        max_zombie = None
        max_skill = 0
        for zombie in cls.horde:
            skill = zombie.speed + zombie.strength
            if skill > max_skill:
                max_skill = skill
                max_zombie = zombie
        return max_zombie

    # instance methods
    def encounter(self):
        """This instance method represents you coming across a zombie! This can end in three possible outcomes:
        1. You outrun the zombie and escape unscathed!
        2. You don't outrun the zombie, you fight and defeat it. While fighting you catch the zombie plague.
        As a result, you become a zombie and are added to the zombie horde.
        3. You don't outrun the zombie, you fight it and lose. It eats your brains and you die. :(
        Returns a summary of what happened."""
        outrun = self.chase()

        if outrun:
            return 'You escaped!'
        else:
            defeat = self.fight()
            if defeat:
                # add yourself to the horde as a new zombie
                # speed and strength are randomly generated
                speed = random.randint(1, Zombie.max_speed)
                strength = random.randint(1, Zombie.max_strength)
                Zombie.horde.append(Zombie(speed, strength))
                return 'You fought the zombie and caught the plague. You are now a zombie too. Raawwwrghh!'
            else:
                return 'You died.'

    def chase(self):
        """Represents you trying to outrun this particular zombie.
        Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run."""
        your_speed = random.randint(1, Zombie.max_speed)
        return your_speed > self.speed

    def fight(self):
        """Represents you trying to fight this particular zombie (self).
        Uses `Zombie.max_strength` to generate a random number that represents how strong you are."""
        your_strength = random.randint(1, Zombie.max_strength)
        return your_strength > self.strength
