# pfchspring2020
Project Repository for PFCH, Spring 2020

This project uses Python to retrieve and filter object metadata for the collections of three different art museums in the United States: the Metropolitan Museum of Art in New York City; the Cleveland Museum of Art; and the Harvard Art Museums in Cambridge, MA. The aim of the project is to examine and compare collecting trends at each institution in the 21st century.

Each of the institutions had code written specifically for the manner and methods offered by that institution. As currently written, each Python script crawls the collection database to identify any object which was accessioned by that institution in the 21st century (2001 – present). It then retrieves select pieces of metadata and writes them out to a csv file.

The metadata fields selected for this project — in part, because they are fields with equivalent versions across all three institutions — were: Object ID, Accession Year, Creation Year, Culture, Division/Department, Classification/Type of Work. Also important for analysis of the resulting data is the fact that these fields have a limited number of possible values, each with a large number of works with that value (e.g., American culture). This is opposed to a field such as Artist, where there would likely be hundreds or thousands of values, each of which has only a handful of members.

It is also asserted (without argument) that the trends this project is intended to discover are broader trends, such as a rise over two decades in the collection of Dutch art, and not smaller patterns, such as a rise in one year of the purchase of Rembrandt works.

The three scripts are currently entirely static and can be run as is. Perhaps in the future, they might be edited to allow dynamic passing of arguments for particular bounding years or to filter other specified criteria. But to for the time being, a csv of all 21st-century accessions can be generated simply by running the script.

# Technical details

## Cleveland Museum of Art

CMA provides open access to their collection information via a downloadable json file available at their github (https://github.com/ClevelandMuseumArt/openaccess/blob/master/data.json). Though the accession date is not explicitly noted as its own metadata field, the script infers it from the accession number, and collects and writes the selected metadata for any work whose accession number indicates it was accessioned since 2001.

## Metropolitan Museum of Art

Similarly, the Metropolitan Museum of Art provides a downloadable csv file available at their github (https://github.com/metmuseum/openaccess/blob/master/MetObjects.csv). Since the accession date is explicitly noted in its own column, the script uses that column to identify 21st-century accessions, and collects and writes the selected metadata for any work with a date of 2001 or later.

## Harvard Art Museums

For the Harvard Art Museums, the script uses their online API (https://github.com/harvardartmuseums/api-docs). While both CMA and the Met have online APIs which could have been used for this project, neither API allows direct querying of metadata fields in respect to accession dates, so in a sense. Harvard's API, on the other hand, does allow for directy querying of any field. So the Python script does just that: it queries for each year since 2001 and pages through the result, collecting and writing the selected metadata for all works returned by each query.
