# EDS-Linkage

EDS-Linkage is a record linkage library designed to:

- **Link records** from two different sources together.
- **Deduplicate records** from the same source.

Here is an overview of its main features:

- Developped in PySpark, so it is fully distributed and **can handle millions of records**.
- Uses a **string similarity score** on available patronyms to allow for fuzzy matching.
- Handles *test patients* in a dedicated preprocessing pipeline
- Automaticaly runs on **newly added** patients records to optimize performances
- Provides results in two forms:

    - As a set of **pairs of linked patients**
    - As a set of **components**, where each component contains **all patients that are linked to one another** (effectively extracting the *connected components* of the linkage  graph).

# Documentation

Check out the [documentation](https://equipedatascience-pages.eds.aphp.fr/eds-linkage/documentation)!
