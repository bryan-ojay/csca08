"""CSCA08 Assignment 2, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus.
 Name: Bryan Oladeji
 UtorID: oladejib
 Student Number: 1004112738
 Date: November 23, 2017
"""


class NucleotideError(Exception):
    '''An error to raise if a user tries to set a nucleotide pair with
    invalid nucleotides.'''


class PositionError(Exception):
    '''An error to raise if a user tries to access a pair or position that
    does not exist.'''


class InputError(Exception):
    '''An error to raise if a user gives a wrong input type.'''


class MarkerError(Exception):
    '''An error to raise if a user tries to access an unset marker.'''


class Chromosome():
    '''A class to represent a chromosome pair.'''
    # Global constants
    NUCLEOS = ('A', 'T', 'C', 'G')
    MEMORY_TIDES = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    MATERNAL = ('LM', 'RM')

    def __init__(self):
        '''(Chromosome) -> NoneType
        Creates a new Chromosome to function as a nested dictionary.
        '''
        # The _positions attribute will be a dictionary that maps
        # nucleotide pairs to position numbers
        self._positions = dict()

    def __repr__(self):
        '''(Chromosome) -> str
        Returns an output for a Chromosome stating the positions at which it
        has defined pairs.
        '''
        # Create an empty list to store all the set positions
        # Append all the set positions to the list
        set_positions = []
        for next_pos in self.get_all_pos():
            set_positions.append(next_pos)
        set_positions.sort()
        return ("Positions set: " + str(set_positions))

    def get_all_pos(self):
        '''(Chromosome) -> dict of {int:str}
        Returns the Chromosome's known nucleotides at specified positions.
        '''
        return self._positions

    def get_by_pos(self, position):
        '''(Chromosome, int) -> str
        Takes in a position in the chromosome, returns the nucleotide at
        the given position.
        Returns ?? if the nucleotide is unknown.
        Returns -- if an invalid input or a position less than 0 was given.
        REQ: position >= 0
        '''
        # Check if the position is not an integer or is less than 0
        if type(position) != int or position < 0:
            nucleotide = '--'

        # Check if the nucleotide at the given position is unknown
        elif position not in self.get_all_pos():
            nucleotide = '??'

        # Or if everything is valid, run the standard code
        else:
            nucleotide = self.get_all_pos()[position]

        return nucleotide

    def set_by_pos(self, position, nucleotide):
        '''(Chromosome, int, str) -> NoneType
        Takes in a position in the chromosome and a nucleotide pair, sets the
        current nucleotide pair at that position to the given nucleotide pair.
        If an invalid position or nucleotide is given, the nucleotide will not
        be set.
        RAISES InputError if position is not an integer
        RAISES PositionError if position is less than 0.
        RAISES NucleotideError if len(nucleotide) != 2
        RAISES NucleotideError if nucleotide is not in one of:
        - ('A', 'T', 'C', 'G'),
        - ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        - ('LM', 'RM')
        '''
        # failproof: convert the nucleotide input into a string
        nucleotide = str(nucleotide)

        # use try/except to check if the nucleotide pair and chromosome pair
        # and position are valid

        # Check first if the nucleotide has a length not equal to 2
        # If so, raise a NucleotideError
        if len(nucleotide) != 2:
            raise NucleotideError("Nucleotide is not a pair.")

        # Check if the nucleotide only contains ordinary nucleotides or
        # memory nucleotides, or a left/right maternal input
        # If not, raise NucleotideError
        for element in nucleotide:
            no_nucleotide = element not in self.NUCLEOS
            no_memory = element not in self.MEMORY_TIDES
            not_maternal = nucleotide not in self.MATERNAL
            if no_nucleotide and no_memory and not_maternal:
                raise NucleotideError("Invalid nucleotide pair.")

        # Check if the chromosome position was inputted correctly
        # If not, raise InputError
        if type(position) != int:
            raise InputError("Position should be an integer.")

        # Check if the position index is valid
        # If not, raise PositionError
        elif position < 0:
            raise PositionError("Position number must be at least 0.")

        # If everything is valid, run the standard code
        self.get_all_pos()[position] = nucleotide


class Animal():
    '''A class to represent an animal.'''
    # Global constants
    NUCLEOS = ('A', 'T', 'C', 'G')
    MEMORY_TIDES = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    SEXES = ('M', 'F')

    def __init__(self, animal_id='', sex=SEXES[0], chromosomes=23):
        '''(Animal[, str[, str[, int]]]) -> NoneType
        Creates a new Animal.
        Optional Parameters:
        - animal_id - To identify animals from each other. Defaulted to a blank
          string if no id is given.
        - sex - To identify whether the animal is male or female.
          Defaults to male if no valid sex is given.
        - chromosomes - To specify the number of chromosomes the animal has.
          Defaulted to 23 for humans as they are the primary animal.
        REQ: sex in ('M', 'F')
        REQ: chromosomes > 0
        '''
        # initialized variables: animal_id, sex, chromosomes, markers

        # If an animal id is given, type-cast the id to str in case a string
        # is not entered
        # If not, keep the id as a blank string
        if type(animal_id) == str:
            self._id = animal_id

        else:
            self._id = ''

        # if a valid animal sex is given, set the sex variable to the one given
        # if not, default the sex to Male
        if sex in self.SEXES:
            self._sex = sex

        else:
            self._sex = self.SEXES[0]

        # failsave: change chromosome number to default if the input given for
        # the chromosomes is less than 1 or not an integer.
        if chromosomes < 1 or (type(chromosomes) != int):
            chromosomes = 23

        # set the list of chromosomes in the animal to be an empty dictionary
        # Add Chromosomes to the dictionary, 'indexed' by integers starting
        # from 0
        self._chromosomes = dict()
        for next_chromosome in range(chromosomes):
            self._chromosomes[next_chromosome] = Chromosome()

        # create an empty tuple to store the markers (purposely made public for
        # geneticists to access)
        self._markers = dict()

    def __repr__(self):
        '''(Animal) -> str
        Returns an output for the animal stating its animal type, gender, id,
        and number of chromosomes.
        '''
        animal_type = type(self).__name__
        # Set variable to 'None' if get_id is blank, else sets variable to
        # the string id
        if self.get_id() == '':
            my_id = str(None)
        else:
            my_id = self.get_id()

        chromosomes = str(len(self.get_chromosomes()))
        sex = self.get_sex()

        statement = (animal_type + ", id: " + my_id + ", sex: " + sex + ", " +
                     chromosomes + " chromosomes")

        return statement

    def get_id(self):
        '''(Animal) -> str
        Returns the animal's id.
        '''
        return self._id

    def set_id(self, new_id=None):
        '''(Animal[, str or NoneType]) -> NoneType
        Sets the animal's id to a new id. Defaults to a blank string if no_id
        is given.
        '''
        if new_id is not None:
            self._id = str(new_id)
        else:
            self._id = ''

    def get_sex(self):
        '''(Animal) -> str
        Returns the animal's sex.
        '''
        return self._sex

    def get_chromosomes(self):
        '''(Animal) -> dict of Chromosome
        Returns all the chromosomes in the animal.
        '''
        return self._chromosomes

    def validate_nucleotide(self, nucleotide):
        '''(Animal, str) -> NoneType
        Checks if the given nucleotide pair is a valid input. Returns a boolean
        that determines whether the nucleotide is valid or not valid.
        RAISES Nucleotide Error if:
        - The nucleotide pair has a length not equal to 2,
        - The individual nucleotides in the pair are not in:
         - ('A', 'T', 'C', 'G')
         - ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0') given a Query,
         - ('LM', 'RM') given a Binder.
        '''
        # failproof: convert the nucleotide input into a string
        nucleotide = str(nucleotide)

        # Check first if the nucleotide length is a pair
        if len(nucleotide) != 2:
            raise NucleotideError("Nucleotide is not a pair.")

        # If the object is a Query, check if the nucleotide only contains
        # ordinary nucleotides or memory nucleotides
        if type(self) == Query:
            for element in nucleotide:
                is_nucleotide = element in self.NUCLEOS
                is_memory = element in self.MEMORY_TIDES
                if not (is_nucleotide or is_memory):
                    raise NucleotideError("Invalid nucleotide pair for Query.")

        # If the object is a Binder, check if the 'nucleotide' is either a
        # left-maternal label or right maternal label.
        # If not, raise NucleotideError
        elif type(self) == Binder:
            if nucleotide not in self.MATERNAL:
                raise NucleotideError("Invalid nucleotide pair for Binder.")

        # If the object is some other Animal class or subclass, check if
        # the nucleotide pair contains only ordinary nucleotides
        else:
            for element in nucleotide:
                if element not in self.NUCLEOS:
                    raise NucleotideError("Invalid nucleotide pair.")

    def validate_pair(self, pair):
        '''(Animal, int) -> NoneType
        Checks if the given pair index is valid and exists in the array
        of chromosomes. Returns a boolean that determines whether the pair
        index is valid or not valid.
        RAISES InputError if the pair index input is not an integer.
        RAISES PositionError if pair index does not exist in the array of
        chromosomes.
        '''
        # create a variable to reference the chromosomes in the Animal
        chromosomes = self.get_chromosomes()
        # check if the chromosome pair was inputted correctly
        if type(pair) != int:
            raise InputError("Pair input must be an integer.")

        # check if the chromosome pair exists
        if pair not in chromosomes:
            chromosome_len = str(len(self.get_chromosomes()) - 1)
            raise PositionError("Pair must be between 0 and " + chromosome_len)

    def validate_position(self, position):
        '''(Animal, int) -> NoneType
        Checks if the given position index is valid. Returns a boolean that
        determines whether the position index is valid or not valid.
        RAISES InputError if the position index input is not an integer.
        RAISES PositionError if the position index input is less than 0.
        '''
        # check if the chromosome position was inputted correctly
        if type(position) != int:
            raise InputError("Position input must be an integer.")

        # Check if the position index is greater than or equal to 0
        if position < 0:
            raise PositionError("Position number must be at least 0.")

    def get_by_pos(self, pair, position):
        '''(Animal, int, int) -> str
        Takes in a chromosome pair and position in that pair. Returns the
        nucleotide pair at the corresponding chromosome position and pair.
        Returns '??' if the nucleotide is unknown.
        Returns '--' if an invalid input is given.
        REQ: 0 <= pair < len(self.get_chromosomes())
        REQ: position >= 0
        '''
        # create a variable to reference the chromosomes in the Animal
        chromosomes = self.get_chromosomes()

        # check if the chromosome pair and position were inputted correctly
        if type(pair) != int or type(position) != int:
            nucleotide = '--'

        # check if the chromosome pair exists and position index is valid
        elif pair not in chromosomes or position < 0:
            nucleotide = '--'

        # check if the chromosome position has a known nucleotide
        elif position not in chromosomes[pair].get_all_pos():
            nucleotide = '??'

        # or if everything is valid, run the standard code
        else:
            nucleotide = chromosomes[pair].get_all_pos()[position]

        return nucleotide

    def set_by_pos(self, pair, position, nucleotide):
        '''(Animal, int, int, str) -> NoneType
        Takes in a valid chromosome pair, a position in that pair, and a
        nucleotide pair, sets the nucleotide pair at that position to the
        given nucleotide pair.
        If an invalid pair, position, or nucleotide is given, the nucleotide
        will not be set.
        RAISES InputError if the pair index input is not an integer.
        RAISES InputError if the position index input is not an integer.
        RAISES PositionError if pair index does not exist in the array of
        chromosomes.
        RAISES PositionError if the position index input is less than 0.
        RAISES Nucleotide Error if:
        - The nucleotide pair has a length not equal to 2,
        - The individual nucleotides in the pair are not in:
         - ('A', 'T', 'C', 'G')
         - ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0') given a Query,
         - ('LM', 'RM') given a Binder.
        '''
        # create a variable to reference the chromosomes in the Animal
        chromosomes = self.get_chromosomes()

        # use try/except to check if the nucleotide pair and chromosome pair
        # and position are valid

        # Check if all the parameters are valid using 'validate' methods
        # An error will be raised if one of the parameters is not valid
        self.validate_nucleotide(nucleotide)
        self.validate_pair(pair)
        self.validate_position(position)

        # If and only if everything is valid, run the standard code
        chromosomes[pair].set_by_pos(position, nucleotide)

    def get_chromosome(self, pair):
        '''(Animal, int) -> Chromosome
        Takes in the index of a chromosome pair, returns the chromosome at that
        index.
        Returns a blank chromosome if an invalid pair index is given.
        REQ: 0 <= pair < number of chromosomes
        '''
        # Create boolean cases for if the pair index given is an invalid type
        # or does not exist
        # If this is the case, set the return variable to a blank Chromosome
        invalid_input = type(pair) != int
        invalid_position = pair not in self.get_chromosomes()
        if invalid_input or invalid_position:
            chromosome = Chromosome()

        # if everything is valid, run the standard code
        else:
            chromosome = self.get_chromosomes()[pair]

        return chromosome

    def set_chromosome(self, pair, chromosome):
        '''(Animal, int, Chromosome) -> NoneType
        Takes in the index of an existing chromosome pair and a new chromosome
        pair, sets the chromosome pair at the given index to be the new
        chromosome pair.
        If an invalid pair or chromosome is given, the chromosome will not be
        set.
        RAISES InputError if the inputted chromosome is invalid.
        RAISES InputError if the pair index input is not an integer.
        RAISES PositionError if pair index does not exist in the array of
        chromosomes.
        '''
        # Check if the pair index and chromosome inputted are valid
        # If not, a corresponding error will be raised
        self.validate_pair(pair)

        if type(chromosome) != Chromosome:
            raise InputError("The chromosome entered was invalid.")

        # If the chromosome and pair are valid, run the standard code
        self.get_chromosomes()[pair] = chromosome

    def set_marker(self, marker, pair, position):
        '''(Animal, str, int, int) -> NoneType
        Takes in a marker, and the indices of a chromosome pair and position.
        Maps the marker to the nucleotide pair at the given pair and position.
        If an invalid pair or position is given, the marker will not be set.
        REQ: 0 <= pair < number of chromosomes
        REQ: position >= 0
        RAISES InputError if the pair index input is not an integer.
        RAISES InputError if the position index input is not an integer.
        RAISES PositionError if pair index does not exist in the array of
        chromosomes.
        RAISES PositionError if the position index input is less than 0.
        '''
        # Check if the pair index and position index inputted are valid
        # Either PositionError or InputError will be returned
        self.validate_pair(pair)
        self.validate_position(position)

        # Check if the marker is a valid input, if not return InputError
        if type(marker) != str:
            raise InputError('Marker must be a string')

        # If everything is valid, run the standard code
        # Store the marker in an empty dictionary
        # The marker is a key to a tuple containing the chromosome pair
        # and position of the nucleotide, and the nucleotide itself.
        self._markers[marker] = (pair, position)

    def get_by_marker(self, marker):
        '''(Animal, str) -> str
        Takes in a marker, returns the nucleotide pair that the marker refers
        to.
        Returns '??' if a marker refers to an unknown nucleotide.
        Returns '--' if the marker does not exist.
        REQ: marker in self._markers
        '''
        # Check if the marker is a valid input and exists.
        if marker not in self._markers or type(marker) != str:
            nucleotide = '--'

        # If everything is valid, run the standard code
        else:
            # Extract the pair and position from the marker tuple in the
            # dictionary
            pair = self._markers[marker][0]
            position = self._markers[marker][1]
            nucleotide = self.get_by_pos(pair, position)

        return nucleotide

    def set_by_marker(self, marker, nucleotide):
        '''(Animal, str, str) -> NoneType
        Takes a marker referring to a nucleotide pair in a chromosome pair,
        and a nucleotide pair. Changes the nucleotide pair that the marker
        references into the given nucleotide pair.
        REQ: marker in self._markers
        REQ: len(nucleotide) == 2
        RAISES MarkerError if the marker has not been set to a position.
        RAISES Nucleotide Error if:
        - The nucleotide pair has a length not equal to 2,
        - The individual nucleotides in the pair are not in:
         - ('A', 'T', 'C', 'G')
         - ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0') given a Query,
         - ('LM', 'RM') given a Binder.
        '''
        # Check if either the marker or nucleotide are invalid
        self.validate_nucleotide(nucleotide)

        if type(marker) != str:
            raise InputError('Marker must be a string')

        if marker not in self._markers:
            raise MarkerError("Marker has not been set to a position.")

        # If everything is valid, run the standard code
        # Extract the pair and position form the marker tuple
        # Set the nuclelotide at the position of the marker
        # Re-set the marker to the new nucleotide
        pair = self._markers[marker][0]
        position = self._markers[marker][1]
        self.set_by_pos(pair, position, nucleotide)

    def test(self, query, sex_chromosome=22):
        '''(Animal, Query[, int]) -> bool
        Takes in a query and an optional input for the sex chromosome
        to find matches of pairs in the animal's genetic sequences.
        Returns a boolean determining whether or not the query was
        accepted or rejected.
        Returns False (meaning the query is rejected) if:
        - The query cannot match its normal nucleotide pair with another
        nucleotide that is in the same position in the animal's genes
        - The query cannot match its memory nucleotide with 1 and only 1
        ordinary nucleotide in the animal's genes.
        - The query attempts to match with an unknown nucleotide in a male
        sex pair.
        '''
        # store the mapping of the memory nucleotides in an empty dictionary
        # set the boolean to check if the query matches
        memory_to_nucleo = dict()
        is_matched = True

        # Run a while loop through all the chromosomes in the animal being
        # tested and check if the query is still matched on every loop.
        pair = 0
        while is_matched and pair < len(self.get_chromosomes()):

            # set a variable to get all of query's set positions in this
            # particular chromosome
            query_positions = query.get_chromosome(pair).get_all_pos()

            # run a for loop through all the set positions
            for next_pos in query_positions:

                # Obtain the nucleotides set at the same position
                # for query and animal
                query_nucleos = query.get_by_pos(pair, next_pos)
                animal_nucleos = self.get_by_pos(pair, next_pos)
                nucleo_num = 0

                # Run a while loop for the 2 nucleotides to compare in each
                # nucleotide pair
                while is_matched and nucleo_num < 2:
                    query_tide = query_nucleos[nucleo_num]
                    animal_tide = animal_nucleos[nucleo_num]

                    # Set boolean cases for:
                    # 1. If the query nucleotide equals the animal nucleotide
                    # 2. If the query nucleotide is a memory nucleotide
                    # 3. If the query nucleotide is a memory nucleotide that is
                    #    mapped to a normal nucleotide in the aninal
                    # 4. If the animal nucleotide is unknown
                    # 5. If the animal nucleotide is (somehow) invalid
                    # 6. If the current animal chromosome being analyzed is the
                    #    sex chromosome
                    # 7. If the sex of the animal is male
                    is_equal = query_tide == animal_tide
                    in_memory = query_tide in self.MEMORY_TIDES
                    is_mapped = query_tide in memory_to_nucleo
                    is_unknown = animal_tide == '?'
                    is_invalid = animal_tide == '-'
                    is_sex_pair = pair == sex_chromosome
                    is_male = self.get_sex() == self.SEXES[0]

                    # All unmatched/ignored cases in order:
                    # - Query matched with an unknown pair in the male sex
                    #   chromosome (reject query)
                    #
                    # - Query matched with an unknown pair (ignore)
                    #
                    # - Query matched with an invalid pair (reject query)
                    #
                    # - Query nucleotide is a memory nucleotide:
                    #   -> Case 1: Memory nucleotide is already mapped to a
                    #      nucleotide; the query is rejected if the current
                    #      animal nucleotide is not the same as the nucleotide
                    #      that the memory nucleotide is mapped to.
                    #
                    #   -> Case 2: Memory nucleotide is not mapped but matched
                    #      with an unknown nucleotide, in this case, do not map
                    #      the memory nucleotide to the current nucleotide,
                    #      ignore the query
                    #
                    #   -> Case 3: Memory nucleotide is not mapped and matched
                    #      with a known nucleotide; if this is the case, map
                    #      the memory nucleotide to the current nucleotide,
                    #
                    # - The query nucleotide is not the same as the animal
                    #   nucleotide (given none of the above cases hold true).
                    #

                    if is_sex_pair and is_unknown and is_male:
                        is_matched = False

                    elif is_unknown:
                        pass

                    elif is_invalid:
                        is_matched = False

                    elif in_memory and is_mapped:
                        if memory_to_nucleo[query_tide] != animal_tide:
                            is_matched = False

                    elif in_memory and (not is_mapped) and is_unknown:
                        pass

                    elif in_memory and (not is_mapped) and (not is_unknown):
                        memory_to_nucleo[query_tide] = animal_tide

                    elif not is_equal:
                        is_matched = False

                    nucleo_num += 1

            pair += 1

        return is_matched


class Human(Animal):
    '''A class to represent a Human'''
    def __init__(self, human_id, sex=Animal.SEXES[0]):
        '''(Human, str[, str]) -> NoneType
        Creates a new Human with an id.
        Optional parameter:
        - sex: Used to define the sex of a human, defaulted to male if no sex
          or an invalid sex is given.
        '''
        Animal.__init__(self, human_id, sex)


class Male(Human):
    '''A class to represent a male human'''
    # Global constants
    def __init__(self, human_id):
        '''(Male, str) -> NoneType
        Creates a new male Human with an id.'''
        Human.__init__(self, human_id, Human.SEXES[0])


class Female(Human):
    ''' A class to represent a female human'''
    # Global constants
    def __init__(self, human_id):
        '''(Female, str) -> NoneType
        Creates a new female Human with an id.'''
        Human.__init__(self, human_id, Human.SEXES[1])

    def procreate(self, male, binder):
        '''(Female, Male, Binder) -> Male or Female
        Takes in a male human and a chromosome binder, returns a procreated
        human with binded chromosomes from the male and female humans.
        '''
        # Assign the child's id to be the first two characters in the father's
        # id plus the first two characters in the mother's id
        fused_id = male.get_id()[0:2] + self.get_id()[0:2]

        # Create a new human corresponding to the sex set by the binder.

        # Make the child male with the fused id if the binder has set sex to
        # male
        if binder.get_sex() == self.SEXES[0]:
            child = Male(fused_id)

        # Make the child female with the fused id if the binder has set sex to
        # female
        elif binder.get_sex() == self.SEXES[1]:
            child = Female(fused_id)

        # Run through all the chromosomes in the binder
        for pair in self.get_chromosomes():
            # Assign variables to the current chromosome pair for mother,
            # father and binder.
            mother_chromo = self.get_chromosome(pair)
            father_chromo = male.get_chromosome(pair)
            binder_chromo = binder.get_chromosome(pair)

            # Run through all the set positions in the binder's chromosome
            for next_pos in binder_chromo.get_all_pos():
                # Assign variables to get all the set positions in the
                # corresponding mother and father chromosomes
                mother_pos = mother_chromo.get_all_pos()
                father_pos = father_chromo.get_all_pos()

                # Check if the set position in the binder chromosome exists in
                # both the mother and father chromosome
                if next_pos in mother_pos and next_pos in father_pos:
                    # Assign variables to the mother and father's nucleotide
                    # pairs, and the binder's maternal setting at the
                    # current position
                    mother_tide = mother_chromo.get_by_pos(next_pos)
                    father_tide = father_chromo.get_by_pos(next_pos)
                    binder_maternal = binder_chromo.get_by_pos(next_pos)

                    # If the position is set to be left maternal, assign the
                    # child nucleotide to be the left side of the mother and
                    # the right side of the father
                    if binder_maternal == binder.MATERNAL[0]:
                        child_tide = mother_tide[0] + father_tide[1]

                    # If the position is set to be right maternal, assign the
                    # child nucleotide to be the left side of the father and
                    # the right side of the mother
                    elif binder_maternal == binder.MATERNAL[1]:
                        child_tide = father_tide[0] + mother_tide[1]

                    # Set the child nucleotide at the pair and position
                    # specified by the binder
                    child.set_by_pos(pair, next_pos, child_tide)

                # If only the mother has a set nucleotide at this position,
                # set the child nucleotide to equal the mother's nucleotide
                # (Purely a design choice)
                elif next_pos in mother_pos and next_pos not in father_pos:
                    child_tide = mother_chromo.get_by_pos(next_pos)
                    child.set_by_pos(pair, next_pos, child_tide)

                # Or if only the father has a set nucleotide at this position,
                # set the child nucleotide to equal the father's nucleotide
                # (also a design choice)
                elif next_pos in father_pos and next_pos not in mother_pos:
                    child_tide = father_chromo.get_by_pos(next_pos)
                    child.set_by_pos(pair, next_pos, child_tide)

        return child


class Binder(Animal):
    '''A class to represent a chromosome binder.'''
    # Global constants
    MATERNAL = ('LM', 'RM')

    def __init__(self, sex=Animal.SEXES[0]):
        '''(Binder[, str]) -> NoneType
        Creates a new Binder with the option to specify its sex. Defaults to
        Male if an invalid sex was given.'''
        Animal.__init__(self, '', sex)

    def get_sex(self):
        '''(Binder) -> str
        Returns the sex set by the binder.'''
        return self._sex

    def set_sex(self, sex):
        '''(Binder, str) -> NoneType
        Sets the sex of the binder to the given sex.
        RAISES InputError if sex is not male or female
        '''
        if sex in self.SEXES:
            self._sex = sex
        else:
            raise InputError("Sex must be male or female.")


class Query(Animal):
    '''A class to represent a chromosome query'''

    def __init__(self, chromosomes=23):
        '''(Query[, int]) -> NoneType
        Creates a new Query with an option to specify the number of chromosomes
        in the Query.'''
        Animal.__init__(self, '', None, chromosomes)

if(__name__ == "__main__"):
    # create a new Male client with ID 12345
    father = Male('12345')

    # create a new Female client with ID 67890
    mother = Female('67890')

    # set chromosome pair 12 position 45 to be AG
    father.set_by_pos(12, 45, 'AG')
    mother.set_by_pos(12, 45, 'CT')

    # set chromosome marker rs12345 to refer to chromosome
    # pair 3, position 97
    father.set_marker('rs12345', 3, 97)

    # set marker rs12345 to be GT
    father.set_by_marker('rs12345', 'GT')

    # this should return "AG"
    result_str = father.get_by_pos(12, 45)

    # this should return "GT"
    result_str2 = father.get_by_marker('rs12345')

    c = father.get_chromosome(3)

    # This will set father's pair 3-85 to be "TA"
    c.set_by_pos(85, 'TA')

    # Now mother and father share a chromosome pair, updating
    # one will update the other
    mother.set_chromosome(7, c)

    # create a new query object
    query = Query()
    query.set_by_pos(12, 45, 'AG')

    # this should return True since 12-45 in the query matches
    # with 12-45 in father
    result = father.test(query)
    query.set_by_pos(12, 45, 'A1')
    query.set_marker('rs12345', 3, 97)

    # now the query will only work if 12-45 is AX and 3-97 is XT for
    # some value of X
    query.set_by_marker('rs12345', '1T')
    result2 = father.test(query)

    # create a new binder object
    binder = Binder()

    # set chromosome pair position 45 to be left maternal
    # (this means that the offspring will have 12-45 equal to CG
    # e.g., gets the left C from mother and the right G from father)
    binder.set_by_pos(12, 45, 'LM')
    binder.set_by_pos(19, 82, 'RM')

    # this means any offspring created with this binder will be female
    binder.set_sex("F")
