import a0

# these are just random example sequences and genes
# to use in order to test your functions. You may want
# to test with other strings as well.
SAMPLE_SEQUENCE = "A"
SAMPLE_GENE = "A"

# test that split_input returns a list containing 3 strings
split_input_result = a0.split_input(SAMPLE_SEQUENCE)
assert(isinstance(split_input_result, list))
assert(isinstance(split_input_result[0], str))
assert(isinstance(split_input_result[1], str))
assert(isinstance(split_input_result[2], str))

# test to see that get_gene returns a string
get_gene_result = a0.get_gene(SAMPLE_SEQUENCE)
assert(isinstance(get_gene_result, str))

# test to see that validate gene resturns a boolean
validate_gene_result = a0.validate_gene(SAMPLE_GENE)
assert(isinstance(validate_gene_result, bool))

# test to see that is_palindromic returns a boolean
is_palindromic_result = a0.is_palindromic(SAMPLE_GENE)
assert(isinstance(is_palindromic_result, bool))

# test to see that evaluate sequence returns a string
evaluate_sequence_result = a0.evaluate_sequence(SAMPLE_SEQUENCE)
assert(isinstance(evaluate_sequence_result, str))

print("Congratulations. If you are seeing this message (and no other errors)")
print("then you have correctly named functions which (at least in some instances")
print("return the correct types.")