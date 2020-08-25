from difflib import get_close_matches

import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)


def in_result():
    pass


# fetch result ma find word ko kam ani return garne result
def fetch_results(cursor, word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()
    if len(results) > 0:
        return results
    # maybe store the similar words results in list and search it
    elif find_similar_expression(word, results[0]):
        yn = input('Did you mean %s Y for yes and N for no:  ' % get_close_matches(word, results))
        if yn == 'y':
            for result in results:
                print('meaning: ' + result[1])
    else:
        return "No word found"


def find_word(word):
    cursor = con.cursor()
    results = fetch_results(cursor, word)

    query_expression = cursor.execute("SELECT Expression FROM Dictionary")
    expression_results = cursor.fetchall()
    i = 1
    for result in results:
        print(' * ' + str(i) + ' * ' + result[1])
        i += 1


def find_similar_expression(word, results2):
    print("find_similar_expression working")
    print(results2)
    if len(get_close_matches(word, results2)) > 0:
        print("Yay")
        return True
    else:
        print('nay')
        return False


def run():
    border = "----------------------------------------------------X---------------------------------------------------------"
    word = input("Enter the word : ")
    print(border + "\n")
    print("Word : %s" % word.capitalize() + "\n")
    find_word(word)
    print("\n" + border)
    print("\n")


while True:
    run()
