def Bayes_Theorem(prior_a, prior_b,conditional_b_given_a ):
    conditional_a_given_b = (conditional_b_given_a * prior_a)/prior_b 
    return conditional_a_given_b


prior_a = float(input("Enter prior_a: "))
prior_b = float(input("Enter prior_b: "))
conditional_b_given_a = float(input("Enter conditional_b_given_a: "))
print(Bayes_Theorem(prior_a, prior_b,conditional_b_given_a ))