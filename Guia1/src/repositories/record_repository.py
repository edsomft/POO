from src.repositories.abstract_repository import AbstractRepository
from src.models.record import Record
from src.utils.file_loader import FileLoader
from unidecode import unidecode

class RecordRepository(AbstractRepository):

    def __init__(self, file_path: str):
        self._file_path = file_path
        self._records = []

    def load_all(self):
        data = FileLoader.load_csv(self._file_path)
        for row in data:
            try:
                id = int(row['id'])
                if row['name'].strip() == '' or row['address'].strip() == '' or id < 0:
                    raise ValueError()
                else:
                    self._records.append(Record(id, row['name'], row['address']))
            except:
                print(f"Registro inválido ignorado {row}")    

        return self._records

    def search(self, term: str):
        terms = unidecode(term).lower().split()
        results = []

        for r in self._records:
            nome = unidecode(r.name).lower()
            add = unidecode(r.address).lower()
            if all(palavra in nome or palavra in add for palavra in terms):
                results.append(r)
        return results