# 📚 Arcana Aegis

A Library of Rare Books

## Introduction

The Arcana Aegis is a project dedicated to organizing and preserving a digital
library of rare and unique media. The library, sourced from a collection
discovered on the internet, holds immense value for researchers, historians,
educators, and the general public. By making this collection accessible and
searchable, Arcana Aegis aims to support scholarly work and knowledge
dissemination.

### Scope

The outcome of this project is to create a digital library framework with a
running web application built using it. This web application aims to serve a
diverse audience including researchers, students, and the general public. The
backend server will use a RESTful API, GRPC, or GraphQL query interface for a
database that models disparate entities forming the library.

## Current State of the Collection

The library, in its current state, presents a few challenges:

* **Duplication of data**: There are multiple instances of the same items
  throughout the library.
* **Inconsistent curation**: File names across the library are inconsistent,
  and there are cases of missing metadata. Some of the media files are also in
  outdated or bespoke formats.
* **Scanned books with archaic scripts**: A significant portion of the books
  consists of scanned images packaged as PDFs. The text in these images is
  often handwritten, utilizing archaic scripts and pictographs, which makes
  Optical Character Recognition (OCR) impractical.
* **Uncertain copyright status**: The legalities surrounding the public
  distribution of the materials in the library are not well-defined.
  Determining the copyright status of these rare and old texts is a complex
  task, which raises concerns regarding the library's compliance with copyright
  laws and regulations.

## Future Goals

The primary goal for the Arcana Aegis project is to structure and categorize
the library in a way that makes it accessible and easy to navigate. To achieve
this, we are developing a robust data model that can accommodate the wide
variety of media types found in the library, which include:

* Books
* Periodicals
* Images
* Video files
* Audio files (MP3s)
* Series of books

Once the data model is in place and the library contents have been loaded into
it, an API and a user-friendly frontend will be added, allowing users to
"checkout" items from the library.

## What's Inside This Repository Now?

Currently, this repository contains a rudimentary data model, which was the
initial attempt to structure the library's contents. However, given the range
and diversity of media types in the library, it became clear that a more
sophisticated approach is required. 

The field of [Library
Science](https://en.wikipedia.org/wiki/Library_and_information_science) has
devoted significant effort to resolving these sorts of challenges. In
particular, The Library of Congress, the world's largest library with over 173
million items, has developed a wealth of practices and standards for managing
vast and diverse collections.

## Project Timeline

The Arcana Aegis project is currently in progress. Here's a breakdown of the
major tasks and their current status:

1. **Create a data model**: The new data model will be capable of referencing
   and categorizing the diverse contents of the library. *(In Progress)*
2. **Load the library into the data model**: This process will involve writing
   scripts to extract metadata from the library's contents and hash the
   contents to identify and remove duplicates. *(Upcoming)*
3. **Create a frontend to browse the library**: The frontend will provide a
   user-friendly interface for users to navigate and explore the library.
   *(Upcoming)*
4. **Deploy to the cloud**: This step will involve setting up a cloud-based
   database, blob store, and authentication system to support the library's
   online presence. *(Upcoming)*
5. **Provide access**: Once the above steps are complete, the library will be
   opened for public access. *(Upcoming)*

Stay tuned for updates on these tasks as the project progresses. We look
forward to sharing this incredible collection with the world!

## Data Modeling
We employ state-of-the-art practices in library science for data modeling. One
key component is BIBFRAME (Bibliographic Framework), which is a data model for
bibliographic description. BIBFRAME is aimed at replacing the MARC standards
and uses linked data principles to make bibliographic data more useful both
within and outside the library community. See:
[BIBFRAME](https://www.loc.gov/bibframe), [LOC
Standards](https://www.loc.gov/standards/standard.html), [Bibliographic
Metadata](https://www.loc.gov/standards/metadata.html)

**Categorization**
* [Cutter Table](https://www.loc.gov/aba/pcc/053/table.html)
* [LCC - Library of Congress Classification](https://en.wikipedia.org/wiki/Library_of_Congress_Classification)
* [LCSH - Library of Congress Subject Headings](https://www.loc.gov/aba/publications/FreeLCSH/freelcsh.html)

**Linked Data**
* [N-Triples](https://en.wikipedia.org/wiki/N-Triples)
* [RDF/XML](https://en.wikipedia.org/wiki/RDF/XML)
* [Turtle](https://en.wikipedia.org/wiki/Turtle_(syntax))
* [JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)

Linked data formats are critical for ensuring interoperability and for linking
our data with other libraries or external sources, thereby enhancing the
richness and context of the information.


### Challenges
**Bibliographic Metadata**
* Deep granularity and inconsistencies between resources, authors, media,
  classification, and more.

**Resource Types**
* Books, video, images, music, meeting notes, and more. Each of these have
  unique charactistics and thus metadata making a one-size-fits-all data model
  difficult.

**Authority**
* Consistently representing entities and their relationship to publisher,
  author, language, makes modeling hard.

**Multilingual & Scripts**
* A data model that supports many languages for the same text or rare scripts
  is critical and challenging. This includes dealing with issues such as
  character encoding, right-to-left scripts, and linguistic variations.

**Linked Data Formats**
* Creating URI to link between external datasets or interally and maintainig
  those linked relationships is non-trivial.

**Integrity & Provenance**
* Ensuring the integrity of the data and metadata, and maintaining a record of
the origin and any changes made to each item in the collection. This is crucial
for authenticity and reliability in a scholarly context.

#### Vocabulary Control and Thesauri
1. **Library of Congress Classification (LCC)** Ensuring notation used within
   LCC is consistent and unambiguous

1. **Cutter's Principles** A book number should be memorable, often involving
   an abbreviated form of the authors name or title.

1. **BIBFRAME with RDF/JSON-LD** URIs having consistent terms to denote entites
   and relationships.

1. **Thesauri** indexing around synonyms, hierarchical relationships (broader
   to narrower terms).

1. **External Authority Data**: Integration with external authority files like
   VIAF (Virtual International Authority File) for normalizing author names and
   other entities.

## What's Next?

Beyond the immediate goals, Arcana Aegis aims to foster a community around this
digital library. Future enhancements could include the integration of
user-generated content, development of a recommendation system, collaboration
with other libraries and archives for data exchange, and partnerships with
educational institutions or organizations dedicated to historical preservation.

## Contributing

Arcana Aegis welcomes contributions from the community. Whether you are a
developer, a librarian, or someone with a passion for preserving rare books,
there are many ways to get involved. Contributions needed include expertise in
cataloging, development, data cleaning, and more. Please refer to our
contribution guidelines for more information. (TODO)

## Stats on the collection:

NOTE: The following statistics were generated by a Python script
(`scripts/count_file_types.py`). Due to the library's lack of meticulous
curation and the presence of unusual file names, some of these statistics may
not be entirely accurate. They represent our best effort at comprehending the
wide variety of contents within the library. These statistics will be updated
as the library is further curated and organized.

```sh
Total files: 14777
pdf: 6103
htm: 4436
jpg: 1342
doc: 771
txt: 659
html: 502
gif: 496
bmp: 72
epub: 70
No extension: 66
rtf: 47
png: 34
mp3: 30
jpeg: 26
djvu: 18
mega: 14
docx: 13
mht: 10
mobi: 8
rar: 7
tif: 7
asc: 6
wmv: 5
cbz: 4
pma: 4
css: 3
crdownload: 2
chm: 2
zen: 2
rtx: 2
odt: 2
db: 2
mid: 2
wri: 2
pdb: 2
arj: 1
am: 1
js: 1
wpd: 1
```
