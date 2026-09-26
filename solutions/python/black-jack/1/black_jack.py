"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determina el valor de puntuación de una carta.

    Parámetros:
        card (str): La carta dada.

    Devuelve:
        int: El valor de la carta dada. Ver los valores a continuación:

        1. 'J', 'Q' o 'K' (figuras) = 10
        2. 'A' (As) = 1
        3. '2' - '10' = su valor numérico.
    """
    if card in ('J', 'K', 'Q'):
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

    


def higher_card(card_one, card_two):
    """Determina qué carta tiene un valor más alto en la mano.

    Parámetros:
        card_one (str): Primera carta repartida en la mano.
        card_two (str): Segunda carta repartida en la mano.

        1. 'J', 'Q' o 'K' (figuras) = 10
        2. 'A' (As) = 1
        3. '2' - '10' = su valor numérico.

    Devuelve:
        str o tuple: Devuelve la carta más alta. Si ambas cartas tienen el mismo valor,
        devuelve una tupla con ambas cartas.
    """
    v_card_one = value_of_card(card_one)
    v_card_two = value_of_card(card_two)

    if v_card_one > v_card_two:
        return  card_one
    elif v_card_one < v_card_two:
        return card_two
    else:
        return card_one, card_two
    


def value_of_ace(card_one, card_two):
    """Calcula el valor más ventajoso para un As que está por venir.

    Parámetros:
        card_one (str): Primera carta repartida en la mano.
        card_two (str): Segunda carta repartida en la mano.

        1. 'J', 'Q' o 'K' (figuras) = 10
        2. 'A' (As) = 11 (si ya está en la mano)
        3. '2' - '10' = su valor numérico.

    Devuelve:
        int: Ya sea 1 u 11, que será el valor del próximo As.
    """

    v_card_one = 11 if card_one == 'A' else value_of_card(card_one)
    v_card_two = 11 if card_two == 'A' else value_of_card(card_two)

    sum_card = v_card_one + v_card_two

    if sum_card + 11 <= 21:
        return 11
    else:
        return 1
    


def is_blackjack(card_one, card_two):
    """Determina si la mano es un 'Blackjack' o 'natural'.

    Parámetros:
        card_one (str): Primera carta repartida en la mano.
        card_two (str): Segunda carta repartida en la mano.

        1. 'J', 'Q' o 'K' (figuras) = 10
        2. 'A' (As) = 11 (si ya está en la mano)
        3. '2' - '10' = su valor numérico.

    Devuelve:
        bool: True si la mano es un blackjack (dos cartas que suman 21), False en caso contrario.
    """
    v_card_one = 11 if card_one == 'A' else value_of_card(card_one)
    v_card_two = 11 if card_two == 'A' else value_of_card(card_two)
    sum_card = v_card_one + v_card_two
    if sum_card == 21:
        return True
    else: 
        return False
    


def can_split_pairs(card_one, card_two):
    """Determina si un jugador puede dividir (split) su mano en dos manos.

    Parámetros:
        card_one (str): Primera carta en la mano.
        card_two (str): Segunda carta en la mano.

    Devuelve:
        bool: True si la mano se puede dividir (es decir, las cartas tienen el mismo valor).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determina si un jugador de blackjack puede realizar una apuesta de doblar (Double Down).

    Parámetros:
        card_one (str): Primera carta en la mano.
        card_two (str): Segunda carta en la mano.

    Devuelve:
        bool: True si la mano se puede doblar (es decir, el total suma 9, 10 u 11 puntos).
    """
    v_card_one = value_of_card(card_one)
    v_card_two = value_of_card(card_two)
    sum_card = v_card_one + v_card_two
    if sum_card in (9, 10, 11):
        return True
    else:
        return False
    
