import numpy as np
from skfuzzy import membership
import skfuzzy as fuzz


def fuzzy_l(taste_val, price_val, cheese_val):
    # Define the taste variable
    taste = np.arange(0, 101, 1)
    taste_spicy = membership.trapmf(taste, [0, 20, 25, 34])
    taste_umami = membership.trapmf(taste, [40, 50, 55, 67])
    taste_sour_sweet = membership.trapmf(taste, [60, 70, 75, 100])
    taste_fit_spicy = fuzz.interp_membership(taste, taste_spicy, taste_val)
    taste_fit_umami = fuzz.interp_membership(taste, taste_umami, taste_val)
    taste_fit_sour_sweet = fuzz.interp_membership(taste, taste_sour_sweet, taste_val)

    # Define the cheese variable
    cheese = np.arange(0, 11, 1)
    cheese_low = fuzz.trimf(cheese, [0, 0, 5])
    cheese_mid = fuzz.trimf(cheese, [0, 5, 10])
    cheese_high = fuzz.trimf(cheese, [5, 10, 10])
    cheese_fit_low = fuzz.interp_membership(cheese, cheese_low, cheese_val)
    cheese_fit_mid = fuzz.interp_membership(cheese, cheese_mid, cheese_val)
    cheese_fit_high = fuzz.interp_membership(cheese, cheese_high, cheese_val)

    # Define the price variable
    price = np.arange(0, 101, 1)
    price_low = fuzz.trimf(price, [0, 0, 50])
    price_mid = fuzz.trimf(price, [0, 50, 100])
    price_high = fuzz.trimf(price, [50, 100, 100])
    price_fit_low = fuzz.interp_membership(price, price_low, price_val)
    price_fit_mid = fuzz.interp_membership(price, price_mid, price_val)
    price_fit_high = fuzz.interp_membership(price, price_high, price_val)

    pizza = np.arange(0, 1, 0.01)
    pizza_diablo = membership.trimf(pizza, [0, 0.15, 0.2])
    pizza_bbq = membership.trimf(pizza, [0.15, 0.25, 0.3])
    pizza_meat = membership.trimf(pizza, [0.25, 0.35, 0.4])
    pizza_peperoni = membership.trimf(pizza, [0.35, 0.5, 0.6])
    pizza_hawaii = membership.trimf(pizza, [0.55, 0.65, 0.7])
    pizza_pear = membership.trimf(pizza, [0.65, 0.75, 0.8])
    pizza_4cheeses = membership.trimf(pizza, [0.79, 0.9, 1])

    rule1 = np.fmin(np.fmin(np.fmin(taste_fit_spicy, cheese_fit_low), price_fit_mid), pizza_bbq)
    rule2 = np.fmin(np.fmin(np.fmin(taste_fit_spicy, cheese_fit_low), price_fit_high), pizza_bbq)
    rule3 = np.fmin(np.fmin(np.fmin(taste_fit_spicy, cheese_fit_low), price_fit_low), pizza_diablo)

    rule4 = np.fmin(np.fmin(np.fmin(taste_fit_spicy, cheese_fit_mid), price_fit_low), pizza_diablo)
    rule5 = np.fmin(np.fmin(np.fmin(taste_fit_spicy, cheese_fit_mid), price_fit_mid), pizza_bbq)
    rule6 = np.fmin(np.fmin(np.fmin(taste_fit_spicy, cheese_fit_mid), price_fit_high), pizza_bbq)

    rule7 = np.fmin(np.fmin(np.fmin(taste_fit_spicy, cheese_fit_high), price_fit_low), pizza_diablo)
    rule8 = np.fmin(np.fmin(np.fmin(taste_fit_spicy, cheese_fit_high), price_fit_mid), pizza_diablo)
    rule9 = np.fmin(np.fmin(np.fmin(taste_fit_spicy, cheese_fit_high), price_fit_high), pizza_bbq)

    rule10 = np.fmin(np.fmin(np.fmin(taste_fit_umami, cheese_fit_low), price_fit_low), pizza_peperoni)
    rule11 = np.fmin(np.fmin(np.fmin(taste_fit_umami, cheese_fit_low), price_fit_mid), pizza_meat)
    rule12 = np.fmin(np.fmin(np.fmin(taste_fit_umami, cheese_fit_low), price_fit_high), pizza_meat)

    rule13 = np.fmin(np.fmin(np.fmin(taste_fit_umami, cheese_fit_mid), price_fit_low), pizza_peperoni)
    rule14 = np.fmin(np.fmin(np.fmin(taste_fit_umami, cheese_fit_mid), price_fit_mid), pizza_peperoni)
    rule15 = np.fmin(np.fmin(np.fmin(taste_fit_umami, cheese_fit_mid), price_fit_high), pizza_meat)

    rule16 = np.fmin(np.fmin(np.fmin(taste_fit_umami, cheese_fit_high), price_fit_low), pizza_peperoni)
    rule17 = np.fmin(np.fmin(np.fmin(taste_fit_umami, cheese_fit_high), price_fit_mid), pizza_4cheeses)
    rule18 = np.fmin(np.fmin(np.fmin(taste_fit_umami, cheese_fit_high), price_fit_high), pizza_4cheeses)

    rule19 = np.fmin(np.fmin(np.fmin(taste_fit_sour_sweet, cheese_fit_low), price_fit_low), pizza_hawaii)
    rule20 = np.fmin(np.fmin(np.fmin(taste_fit_sour_sweet, cheese_fit_low), price_fit_mid), pizza_hawaii)
    rule21 = np.fmin(np.fmin(np.fmin(taste_fit_sour_sweet, cheese_fit_low), price_fit_high), pizza_hawaii)

    rule22 = np.fmin(np.fmin(np.fmin(taste_fit_sour_sweet, cheese_fit_mid), price_fit_low), pizza_hawaii)
    rule23 = np.fmin(np.fmin(np.fmin(taste_fit_sour_sweet, cheese_fit_mid), price_fit_mid), pizza_pear)
    rule24 = np.fmin(np.fmin(np.fmin(taste_fit_sour_sweet, cheese_fit_mid), price_fit_high), pizza_pear)

    rule25 = np.fmin(np.fmin(np.fmin(taste_fit_sour_sweet, cheese_fit_high), price_fit_low), pizza_pear)
    rule26 = np.fmin(np.fmin(np.fmin(taste_fit_sour_sweet, cheese_fit_high), price_fit_mid), pizza_pear)
    rule27 = np.fmin(np.fmin(np.fmin(taste_fit_sour_sweet, cheese_fit_high), price_fit_high), pizza_4cheeses)

    out_pizza_4cheeses = np.fmax(np.fmax(rule17, rule18), rule27)
    out_pizza_pear = np.fmax(np.fmax(np.fmax(rule23, rule24), rule25), rule26)
    out_pizza_hawaii = np.fmax(np.fmax(np.fmax(rule19, rule20), rule21), rule22)
    out_pizza_peperoni = np.fmax(np.fmax(np.fmax(rule10, rule13), rule14), rule16)
    out_pizza_meat = np.fmax(np.fmax(rule11, rule12), rule15)
    out_pizza_diablo = np.fmax(np.fmax(np.fmax(rule3, rule4), rule7), rule8)
    out_pizza_bbq = np.fmax(np.fmax(np.fmax(np.fmax(rule1, rule2), rule5), rule6), rule9)

    out_pizza = np.fmax(np.fmax(
        np.fmax(np.fmax(np.fmax(np.fmax(out_pizza_meat, out_pizza_peperoni), out_pizza_diablo), out_pizza_hawaii),
                out_pizza_pear), out_pizza_bbq), out_pizza_4cheeses)

    defuz = fuzz.defuzz(pizza, out_pizza, 'centroid')

    if 0 < defuz <= 0.2:
        return "Pizza Diablo"
    elif 0.2 < defuz <= 0.3:
        return "Pizza Bbq"
    elif 0.3 < defuz <= 0.4:
        return "Pizza Meat"
    elif 0.4 < defuz <= 0.6:
        return "Pizza Peperoni"
    elif 0.6 < defuz <= 0.7:
        return "Pizza Hawaii"
    elif 0.7 < defuz <= 0.8:
        return "Pizza Pear"
    elif 0.8 < defuz <= 1:
        return "Pizza 4 cheeses"
