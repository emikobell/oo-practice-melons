############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name # Maybe put in a default for is_bestseller
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
            "musk",
            1998,
            "green",
            True,
            True,
            "Muskmelon",
            )
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType(
            "cas",
            2003,
            "orange",
            True,
            False,
            "Casaba",
            )
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType(
            "cren",
            1996,
            "green",
            True,
            False,
            "Crenshaw",
            )
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType(
                "yw",
                2013,
                "yellow",
                True,
                True,
                "Yellow Watermelon"
                )
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        pairings = melon.pairings
        print(f"\n{melon.name} pairs with")
        for pairing in pairings:
            print(f"- {pairing}")



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    
    melon_dict = {} 
    for melon in melon_types:
        melon_dict[melon.code] = melon
    return melon_dict
    

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, type, shape_rating, color_rating, field, harvester):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            self.sellability = True
        else:
            self.sellability = False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    
    melon_objects = []
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_objects.append(Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila'))
    melon_objects.append(Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila'))
    melon_objects.append(Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila'))
    melon_objects.append(Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila'))
    melon_objects.append(Melon(melons_by_id['cren'], 8, 9, 35, 'Michael'))
    melon_objects.append(Melon(melons_by_id['cren'], 8, 2, 35, 'Michael'))
    melon_objects.append(Melon(melons_by_id['cren'], 2, 3, 4, 'Michael'))
    melon_objects.append(Melon(melons_by_id['musk'], 6, 7, 4, 'Michael'))
    melon_objects.append(Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila'))
    
    return melon_objects


def make_melons_from_file(filepath):

    melon_objects = []
    melon_types = make_melon_types()
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_file = open(filepath)

    for melon in melon_file:
        melon_details = melon.split()
        melon_type = melon_details[5]
        shape = int(melon_details[1])
        color = int(melon_details[3])
        field = int(melon_details[-1])
        harvester = melon_details[-4]

        melon_objects.append(Melon(melons_by_id[melon_type], shape,
                                   color, field, harvester))
        
    return melon_objects


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        # store sellability by callng the method on the melon
        melon.is_sellable()
        if melon.sellability:
            # set sellable_text to (CAN BE SOLD) string
            sellable_text = "(CAN BE SOLD)"
        else:
            sellable_text = "(NOT SELLABLE)"
            # set sellable_text to (NOT SELLABLE)
        print(f"Harvested by {melon.harvester} from Field {melon.field} {sellable_text}")

    # sellable_text = "(CAN BE SOLD)" if melon.sellability else "(NOT SELLABLE)"
