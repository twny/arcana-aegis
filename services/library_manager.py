import os
import hashlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.book import Book


class LibraryManager:
    def __init__(self, library_path, db_engine):
        self.library_path = library_path
        self.db_engine = db_engine
        self.Session = sessionmaker(bind=db_engine)

    def hash_file(self, file_path):
        # Hash file using SHA-256
        hasher = hashlib.sha256()

        with open(file_path, 'rb') as file:
            buf = file.read()
            hasher.update(buf)

        return hasher.hexdigest()

    def hash_and_store_files(self):
        session = self.Session()

        for root, dirs, files in os.walk(self.library_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_path = os.path.normpath(os.path.abspath(file_path))

                # Get file format (extension)
                _, file_format = os.path.splitext(file)

                # remove the dot at the beginning
                file_format = file_format.lstrip('.')

                # Get file size
                file_size = os.path.getsize(file_path)

                # Hash the file
                file_hash = self.hash_file(file_path)

                book = Book(
                    file_location=file_path,
                    file_format=file_format or "UNKNOWN",
                    file_size=file_size,
                    hash=file_hash,
                )

                session.add(book)

        session.commit()


if __name__ == "__main__":
    engine = create_engine('postgresql://localhost/arcana_aegis')

    library_path = "/Users/twny/Downloads/The Temple of Solomon the King"
    manager = LibraryManager(library_path, engine)
    manager.hash_and_store_files()
