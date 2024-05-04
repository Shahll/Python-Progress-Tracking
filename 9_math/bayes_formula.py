def bayes_formula(P_A, P_B_given_A):
    P_not_A = 1 - P_A  # Probability of a randomly selected person not being a user of the drug | 95%
    P_B_given_not_A = 1 - P_B_given_A # Probability of a nonuser of the drug testing positive | 2 %

    P_B = (P_B_given_A * P_A) + (P_B_given_not_A * P_not_A) #  the probability that a person tests positive for the drug

    P_A_given_B = (P_B_given_A * P_A) / P_B # Probability that a person who tests positive for the drug is actually a user of the drug
    
    return P_A_given_B

def main():
    P_A = 0.05  # Probability of a randomly selected person being a user of the drug | 5%
    P_B_given_A = 0.98  # Probability of a user of the drug testing positive | 98%

    print(bayes_formula(P_A, P_B_given_A)) # 0.7205882352941175

main()
