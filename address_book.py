from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data.update({str(record.name).lower(): record})

    def find(self, name):
        for record in self.data:
            if str(record).lower() == str(name).lower():
                return self.data[record]
        return None

    def delete(self, name):
        name_lower = str(name).lower()
        for record in self.data:
            if str(record).lower() == name_lower:
                return self.data.pop(name_lower)

    # Тут можна перевизначити str щоб при виведенні в консоль book виглядав так
        # {'john': Contact name: John, phones: 1112223333; 5555555555}
    # def __str__(self):
    #     return '{' + ', '.join(f"'{name}': {str(record)}" for name, record in self.data.items()) + '}'

    # def __repr__(self):
    #     return self.__str__()
