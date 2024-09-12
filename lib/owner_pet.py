class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner's name must be a string")
        self.name = name
        self._pets = []

    def pets(self):
        """Return owner's pets list."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner"""
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added.")
        if pet.owner is None:
            pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Return a sorted list of pets."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class")
            self.owner = owner
            owner.add_pet(self)
        
        Pet.all.append(self)
