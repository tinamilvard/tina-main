# class Notebook:
#     def __init__(self):
#         self.notes = []
#
#     def add_note(self):
#         note = input("napis poznamku: ")
#         self.notes.append(note)
#         print(f"pridana poznamka: '{note}'")
#
#     def delete_note(self):
#         try:
#             line_number = int(input("cislo posnamky pro smazani: "))
#             index = line_number - 1
#             if 0 <= index < len(self.notes):
#                 removed_note = self.notes.pop(index)
#                 print(f"smazano: '{removed_note}'")
#             else:
#                 print("zkus jeste jednou, prosim")
#         except ValueError:
#             print("введите корректное число")
#
#     def edit_note(self):
#         try:
#             line_number = int(input("cislo poznamky pro upraveni: "))
#             index = line_number - 1
#             if 0 <= index < len(self.notes):
#                 old_note = self.notes[index]
#                 new_note = input("napis novou poznamku: ")
#                 self.notes[index] = new_note
#                 print(f"poznamka zmenena '{old_note}' на '{new_note}'")
#             else:
#                 print("zkus jeste jednou, prosim")
#         except ValueError:
#             print("введите корректное число")
#
#     def display_notes(self):
#         if self.notes:
#             print("poznamkovy blok:")
#             for i, note in enumerate(self.notes, 1):
#                 print(f"{i}. {note}")
#         else:
#             print("poznamkovy blok je prrazdny")
#
#
# notebook = Notebook()
# notebook.add_note()
# notebook.add_note()
# notebook.add_note()
# notebook.add_note()
# notebook.add_note()
#
# notebook.display_notes()
# notebook.edit_note()
# notebook.display_notes()


import csv


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self):
        note = input("napis poznamku: ")
        self.notes.append(note)
        print(f"pridana poznamka: '{note}'")

    def delete_note(self):
        try:
            line_number = int(input("cislo posnamky pro smazani: "))
            index = line_number - 1
            if 0 <= index < len(self.notes):
                removed_note = self.notes.pop(index)
                print(f"smazano: '{removed_note}'")
            else:
                print("zkus jeste jednou, prosim")
        except ValueError:
            print("zadejte správné číslo")

    def edit_note(self):
        try:
            line_number = int(input("cislo poznamky pro upraveni: "))
            index = line_number - 1
            if 0 <= index < len(self.notes):
                old_note = self.notes[index]
                new_note = input("napis novou poznamku: ")
                self.notes[index] = new_note
                print(f"poznamka zmenena '{old_note}' на '{new_note}'")
            else:
                print("zkus jeste jednou, prosim")
        except ValueError:
            print("zadejte správné číslo")

    def display_notes(self):
        if self.notes:
            print("poznamkovy blok:")
            for i, note in enumerate(self.notes, 1):
                print(f"{i}. {note}")
        else:
            print("poznamkovy blok je prrazdny")

    def save_to_csv(self):
        filename = input("vumysli jmeno souboru (.csv): ")
        if not filename.endswith('.csv'):
            filename += '.csv'
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Notes"])
                for note in self.notes:
                    writer.writerow([note])
            print(f"zapis uspesne ulozen do souboru: {filename}")
        except Exception as e:
            print(f"Chyba pri ukladani: {e}")

    def load_from_csv(self):
        filename = input("napis jmeno souboru (.csv): ")
        if not filename.endswith('.csv'):
            filename += '.csv'
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                self.notes = [row[0] for row in reader]
            print(f"poznamky byly stahneni se souboru: {filename}")
        except FileNotFoundError:
            print("soubor neni najden")
        except Exception as e:
            print(f"chyba cteni: {e}")

if __name__ == "__main__":
    notebook = Notebook()
    while True:
        print("\nvyber akci:")
        print("1. pridat poznamku")
        print("2. smazat poznamku")
        print("3. upravit poznamku")
        print("4. zobrazit vse poznamky")
        print("5. ulozit poznamky do souboru")
        print("6. nacist poznamky ze souboru")
        print("7. konec")

        try:
            vyber = int(input("Vas vyber: "))
            if vyber == 1:
                notebook.add_note()
                notebook.add_note()
                notebook.add_note()
                notebook.add_note()
                notebook.add_note()
            elif vyber == 2:
                notebook.delete_note()
            elif vyber == 3:
                notebook.edit_note()
            elif vyber == 4:
                notebook.display_notes()
            elif vyber == 5:
                notebook.save_to_csv()
            elif vyber == 6:
                notebook.load_from_csv()
            elif vyber == 7:
                print("konec")
                break
            else:
                print("zkus to znovou")
        except ValueError:
            print("napis cislo")



