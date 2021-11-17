# try:
#           Run this code
# except:
#           Execute this code when there is an exception
# else:
#           No exceptions? Run this code
# finally:
#           Always run this code.


# Trudny przykład

# import sys
# try:
#     f = open("plik.txt")
#     s = f.readline()
#     i = int(s.strip())  # Usuń spacje
#     print(i)
# except OSError as err:
#     print("Błąd systemu: {0}".format(err))
# except ValueError:
#     print("Nie można dokonać konwersji.")
# except:     # PEP 8: E722 nie używaj pustego 'except'
#     print("Nieoczekiwany wyjątek:", sys.exc_info()[0])
#     raise

# Easy przykład
#
# try:
#     print("Dzień dobry")
# except:
#     print("Coś poszło nie tak")
# else:
#     print("Nic nie poszło źle")
#
# # Inaczej to samo
#
# try:
#     print("Dzień dobry" + 0)
# except:
#     print("Coś poszło nie tak")
# else:
#     print("Nic nie poszło źle")


# Finally
# Finally zawsze się wykonuje

# try:
#     print("x")
# except:
#     print("Coś poszło nie tak")
# finally:
#     print("Klauzula „try except" jest zakończona")

# kolejny przykład

# x = -1
#
# if x < 0:
#     raise Exception("Przepraszamy, brak liczb poniżej zera")


# --------------------------------Cwiczenie 1-----------------------------------------
# Podczas pisania funkcji najlepiej jest przeprowadzić walidację liczb.
# Jeśli użytkownicy wprowadzą tekst, pojawi się błąd podczas próby konwersji na int.
# Napisz program, który poprosi użytkownika o podanie dwóch liczb.
# Dodaj i wydrukuj wynik.
# Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie.
# Dodatkowo zapętlamy program....

# while True:
#     a = input("Podal liczbe a: ")
#     b = input("Podal liczbe b: ")
#
#     try:
#         a = int(a)
#         b = int(b)
#
#         print(a + b)
#         break
#     except ValueError:
#         print("miały być liczby...")


# --------------------------------Cwiczenie 2-----------------------------------------
# Podziel przez siebie dwie liczby
# Umieść:
# wynik = "Nie możesz podzielić przez 0"
# we właściwym miejscu, aby program uniknął ZeroDivisionError
# Podpowiedź 1: Po prostu umieść przypisanie wartości dla wyniku po linii Except
# Podpowiedź 2: Zwróć uwagę na wcięcia

# a = 5
# b = 2
#
# try:
#     wynik = a / b
# except ZeroDivisionError:
#     wynik = "Nie możesz podzielić przez 0"
#
# print(wynik)


# --------------------------------Cwiczenie 3-----------------------------------------
# Napisz dowolny kod.
# Wychwyć w nim wyjątek, ale nic nie rób.

# try:
#     a = 0
#     b = 2
#     print(b/a)
# except ZeroDivisionError:
#     pass


# --------------------------------Cwiczenie 4-----------------------------------------
# Spróbuj dodać int do ciągu.
# Umieść:
# msg = "Nie możesz dodać int do string"
# aby program uniknął błędu BaseException.
# Możesz użyć wyjątku Exception, chociaż zwykle powinno się ostrożnie używać tak
# potężnych instrukcji wyjątków.

# l1 = int(input("Podaj liczbę 1: "))
# str1 = input("Podaj ciąg i: ")
# msg = "Nie możesz dodać int do string"
#
# try:
#     l1 + str1
# except TypeError:
#     print(msg)


# --------------------------------Cwiczenie 5-----------------------------------------
# Stwórz trójelementową listę.
# Spróbuj wydrukować piąty element.
# Umieść:
# msg = "Jesteś poza zakresem listy"
# aby uniknąć wyjątku IndexError.

# a = [1,2,3]
# try:
#     print(a[4])
# except IndexError as x:
#     print("Jesteś poza zakresem listy " + str(x))


# --------------------------------Cwiczenie 6-----------------------------------------
# Spróbuj otworzyć do czytania plik (podpowiedź: f = open(arg, "r")).
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy (podpowiedź: len(f.readlines()).
# Na koniec zamknij ten plik (podpowiedź: f.close()).

# arg = "czwiczenia5_cw6.txt"
#
# try:
#     f = open(arg, "r")
# except FileNotFoundError:
#     print("Nie mogę otworzyć pliku o nazwie: " + arg)
# else:
#     print("Plik o nazwie: " + arg + "Ma liczbę wierszy: " + str(len(f.readlines())))
#     f.close()


# --------------------------------Cwiczenie 7-----------------------------------------
# Użyj finally do zamykania obiektów i czyszczenia zasobów.
# Spróbuj otworzyć i zapisać (podpowiedź: write) w pliku, którego nie można zapisać.
# Zapewnij, aby program mógł kontynuować bez pozostawiania otwartego obiektu pliku.
# import io
#
# try:
#     f = open("cwiczenia_5_cw7.txt", "w")
#     f.write("Coś tam coś tam")
# except io.UnsupportedOperation:
#     print("Nie da się tego otworzyć! ")
# finally:
#     f.close()


# --------------------------------Cwiczenie 8-----------------------------------------
# Napisz funkcję dzielącą jej argument pierwszy przez drugi.
# Spróbuj wykonać działanie i zwrócić wynik.
# W przypadku błędu dzielenia przez zero, wypisz komunikat o błędzie.
# Wypisz komunikat, który zawsze się wypisze.
# Wywołaj funkcję z różnymi argumentami.

# def dzielenie(a, b):
#     try:
#         wynik = a / b
#         return wynik
#     except ZeroDivisionError as err:
#         print("Nie można dzielić przez 0! ")
#     finally:
#         print("Świetnie! Zawsze to zostanie wyświetlone ;] ")
#
#
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj pierwszą liczbę: "))
#
# print(dzielenie(a, b))


# --------------------------------Cwiczenie 9-----------------------------------------
# Użyj wszystkie 4 elementy struktury obsługi wyjątków przy otwieraniu plików.
# Spróbuj otworzyć do czytania plik.
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy.
# Na koniec zamknij ten plik.
# Jeżeli dany plik nie jest zamknięty (podpowiedź: f.closed), to go zamknij.

arg = "main.py"

try:
    f = open(arg)
except IOError as err: # as err nie musi być
    print("Nie można otowrzyć pliku :( " + arg + " " + str(err))
    # dlatego str(err) gdyż err nie zawsze jest stringiem
else:
    print(arg + str(len(f.readlines())))
finally:
    if not f.closed: # jeśli to jest if to nie daje ()
        f.close()













