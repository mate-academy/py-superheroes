# Superheroes

**Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before starting.

In this task, we will create superheroes using classes and inheritance.

## Superhero Class
The Superhero class represents a basic superhero. It has the following characteristics:

### Attributes:
- `name`: the name of the superhero;
- `power_level`: the power level of the superhero.
### Methods
- `use_power()`: prints a message indicating that the superhero is using their power;
- `calculate_power()`: calculates the power of the superhero based on their power level. Returns the calculated power multiplied by 2.

Example:
```python
super_man = Superhero("Superman", 25)
super_man.use_power()  # "Superman is using their power."
print(super_man.calculate_power())  # "50"
```

## FlyingSuperhero Class
The FlyingSuperhero class is a subclass of Superhero and represents a superhero with the ability to fly. 
It has the following additional characteristics:

### Attributes
- `flight_speed_multiplier`: a multiplier that determines the superhero's flight speed.
### Methods
- `fly()`: prints a message indicating that the superhero is flying;
- `calculate_power()`: overrides the calculate_power() method of the base class. 
Calculates the power of the superhero based on their power level and flight speed multiplier. Returns the calculated power.

Example:
```python
flying_superhero = FlyingSuperhero("FlyingSuperhero", 25, 3)
flying_superhero.use_power()  # "FlyingSuperhero is using their power. "
                              # "FlyingSuperhero is flying."
print(flying_superhero.calculate_power())  # "125"
flying_superhero.fly()  # "FlyingSuperhero is flying."
```

## StrengthSuperhero Class
The StrengthSuperhero class is another subclass of Superhero and represents a superhero with exceptional strength. 
It has the following additional characteristics:

### Attributes
- `lifting_capacity_multiplier`: a multiplier that determines the superhero's lifting capacity.
### Methods
- `lift_weight()`: prints a message indicating that the superhero is lifting a weight;
- `calculate_power()`: Overrides the calculate_power() method from the base class to include the lifting capacity multiplier in the power calculation. 
Returns the calculated power.

Example:
```python
strength_superhero = StrengthSuperhero("StrengthSuperhero", 25, 3)
strength_superhero.use_power()  # "StrengthSuperhero is using their power. "
                                # "StrengthSuperhero is lifting a weight."
print(strength_superhero.calculate_power())  # "3750"
strength_superhero.lift_weight()  # "StrengthSuperhero is lifting a weight."
```
