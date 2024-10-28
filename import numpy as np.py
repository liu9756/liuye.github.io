import numpy as np

P_b = 0.001  # P(b) as provided
P_e = 0.002  # P(e) as provided

# Conditional probabilities
P_a_given_B_T_E_T = 0.95
P_a_given_B_T_E_F = 0.94
P_a_given_B_F_E_T = 0.29
P_a_given_B_F_E_F = 0.001
P_j_given_A_T = 0.90
P_j_given_A_F = 0.05
P_m_given_A_T = 0.70
P_m_given_A_F = 0.01

# Case 1: E = True
P_a_not_b_e_true = P_a_given_B_F_E_T * P_e  # P(A | ~b, E=T) * P(E=T)

# Case 2: E = False
P_a_not_b_e_false = P_a_given_B_F_E_F * P_e  # P(A | ~b, E=F) * P(E=F)

# Sum over e terms to get P(A | ~b)
sum_e_terms = P_a_not_b_e_true + P_a_not_b_e_false  # Should represent P(A | ~b)
print(f"Sum e term = ", sum_e_terms)

sum_m_given_a_true = P_m_given_A_T  # Use 0.70 as expected

unnormalized_result_true = P_j_given_A_T * sum_m_given_a_true * sum_e_terms 
unnormalized_result_false = P_j_given_A_F * sum_m_given_a_true * sum_e_terms 
print(f"unnormalized_result_true = ",unnormalized_result_true)
print(f"unnormalized_result_false  = ",unnormalized_result_false )