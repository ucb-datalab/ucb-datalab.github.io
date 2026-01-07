---
title: Gaia & Astroquery
permalink: /resources/gaia/
published: true
layout: page
has_children: false
parent: Resources
nav_order: 1
---

# Using Gaia Data and `astroquery`
{:.no_toc}

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Using the Gaia Archive Interface

Before you write any code, you need to understand the environment where you will run it. The [**Gaia Archive**](https://gea.esac.esa.int/archive/) (hosted by ESA) is the primary portal for accessing Gaia data.

### Getting Set Up

While you can search the archive anonymously, creating an account is highly recommended.

* **Anonymous Users:** You are limited to smaller file downloads (typically ~20MB) and your query history is lost when you close the tab.
* **Registered Users:** You receive a permanent **User Space** (1GB+) to store results. You can also run **Async** (asynchronous) queries—jobs that take hours to run in the background—and share tables with collaborators. (Though hopefully none of your queries for this class should require such large data accesses.)

### Navigating the Interface

You can access data from the "SEARCH" page where you will want to navigate to the "Advanced (ADQL)" section. This page is divided into three main areas:

* **The ADQL Search Tab:** This is your command center. It contains the large text editor where you write your queries.
* **The Schema Browser (Metadata Tree):** Usually located on the right or left panel, this is your dictionary.
    * **Schemas:** Top-level folders (e.g., `gaiadr3`, `tmass`).
    * **Tables:** Datasets within a schema (e.g., `gaia_source`, `vari_rrlyrae`).
    * **Columns:** The specific data points (e.g., `ra`, `dec`, `parallax`).

    {: .note }
    Click on any table name in the tree to see a popup description of table including a link to documentation that includes all column names and descriptions. Similarly, click on any column name in the tree to see a popup description of the physics and units.
* **Results:** Located below the large text editor where you write your queries, this section is where you can see the results of your queries.

### Running Queries

1. **Type Code:** Enter your ADQL in the editor.
2. **Submit:** Once you submit your job you should see the dialogue: "Job launched..." and when your job is completed you will see an entry in the results section of the page.

### Downloading Data

Once a job finishes you can download it in multiple different formats depending on your use case:

* **VOTable:** The standard for Virtual Observatory tools (like TOPCAT).
* **FITS:** The professional standard for image and table data, ideal for `astropy`.
* **CSV:** Best for quick checks in Excel or Google Sheets or if you prefer to use `pandas`.

The download format can be selected in the dropdown menu at the bottom of the page.

### Debugging

Ideally you will see a check mark under the status of your query results, which means it ran successfully. However if you see an octogon with an X instead, click on the information icon (i in a square), then the "Error Summary" tab, and look for **"Encountered... at line X, column Y."** This is the most common error and usually is syntax related (e.g., a missed comma or incorrectly spelled column or keyword).

* **"Table not found":** Did you include the schema? (Use `gaiadr3.gaia_source`, not just `gaia_source`).
* **"Column not found":** Check for typos against the Schema Browser.
* **Timeouts:** If a Sync query fails, try running it as Async.

### Documentation & Useful Resources:

* **The Gaia Archive:** [ESA Gaia Archive Main Page](https://gea.esac.esa.int/archive/)
* **Data Model (Columns List):** [Gaia DR3 Datamodel](https://www.google.com/search?q=https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) (The most important reference for column names and units)
* **Data Release 3 Documentation:** [Gaia DR3 Documentation Home](https://www.google.com/search?q=https://gea.esac.esa.int/archive/documentation/GDR3/)
* **Gaia Cosmos:** [ESA Gaia Mission Portal](https://www.cosmos.esa.int/web/gaia/data-release-3) (News, caveats, and known issues with the data)
* **Geometric Distance Priors:** [Estimating Distances from Parallaxes](https://www.google.com/search?q=https://www.cosmos.esa.int/web/gaia/edr3-distances) (Critical context for using the `parallax` column correctly)


## ADQL Basics & Writing Queries

ADQL stands for **Astronomical Data Query Language**. It is a standard language used by virtual observatories to access astronomical datasets. If you have ever used SQL (Structured Query Language) for standard databases, ADQL will look very familiar. It is essentially a dialect of SQL with special features added specifically for astronomy, such as geometric functions (e.g., finding all stars within a certain circle on the sky).

The Basic Structure Every functional ADQL query requires at least two specific clauses (`SELECT` and `FROM`), but most useful queries will include a third (`WHERE`).

Think of a query as a sentence:
- `SELECT`: "I want these specific pieces of information..."
- `FROM`: "...taken from this specific catalog or table..."
- `WHERE`: "...but only for the objects that match these rules."

Here is a "Hello World" style query for ADQL. This query asks for the ID, Right Ascension (RA), and Declination (Dec) of all objects in the Gaia DR3 source table where the brightness (G-band mean magnitude) is brighter than magnitude 10.

```sql
SELECT source_id, ra, dec
FROM gaia_source
WHERE phot_g_mean_mag < 10
```

Key Concepts for Beginners:
- *Case Insensitivity:* generally, ADQL is case-insensitive. `SELECT`, `select`, and `Select` usually mean the same thing. However, keeping keywords in ALL CAPS is a standard convention that makes your code easier to read.
- *The Wildcard (`*`):* If you want to grab every column available in a table, you can use the asterisk.
    - **Example:** `SELECT * FROM gaia_source`
    - **Warning:** Astronomical tables often have hundreds of columns. Using `*` can make your query very slow and the result tables very large and difficult to work with. It is better practice to list only the columns you actually need.
- *Comments: *You can add notes to your code that the computer will ignore.
    - **Example:** `-- This is a single line comment`

### The `SELECT` Clause
The `SELECT` clause is your primary tool for defining the output of your query. It tells the database exactly which columns to retrieve and allows you to perform calculations on the fly before the data even reaches your computer.

#### Limiting Rows (`TOP`)
Astronomical catalogs (like Gaia or SDSS) often contain billions of rows. Downloading them all by accident is a common mistake that will time out your query. Use `TOP` when testing a new query to fetch just a sample.
- **Syntax:** `SELECT TOP [number] ...`
- **Example:** Get the first 10 rows to check what the data looks like.
```sql
SELECT TOP 10 source_id, ra, dec
FROM gaia_source
```
#### Aliasing (`AS`)
Table column names can sometimes be obscure (e.g., `phot_g_mean_mag`). You can rename them in your output to make them readable or shorter.
- **Syntax:** column_name AS new_name
- **Example:**
```sql
SELECT phot_g_mean_mag AS m_g
FROM gaia_source
```

{: .note }
Your new column name will now be different from the documentation, so be sure to keep track of which column names you change.

#### Mathematical Operations
You don't always have to download raw data and process it in Python. You can perform arithmetic directly in the query. This is commonly used to calculate color indices and to transform apparent magnitudes to absolute magnitudes.
- **Operators:** `+`, `-`, `*`, `/`
- **Example:** Calculate the BP-RP color.
```sql
SELECT source_id,
       (phot_bp_mean_mag - phot_rp_mean_mag) AS bp_rp
FROM gaia_source
```

#### Mathematical Functions
ADQL supports standard math functions.
- **Trigonometry:** `SIN(x)`, `COS(x)`, `TAN(x)`, `ASIN(x)`, `ACOS(x)`, `ATAN(x)`, `ATAN2(y, x)` (arguments usually in radians).
- **Degrees/Radians conversion:** `DEGREES(x)`, `RADIANS(x)`.
- **Other:** `SQRT(x)`, `LOG(x)` (natural log), `LOG10(x)`, `ABS(x)`, `POWER(x, y)`.

#### Aggregates
Sometimes you don't want the data itself, but statistics about the data.
- `COUNT(*)`: Counts the total number of rows.
- `AVG(column)`: Calculates the average value.
- `MIN(column)` / `MAX(column)`: Finds the minimum or maximum value.
- `SUM(column)`: Adds up the values.
- **Example:** Find the total number of stars and the average brightness in a table.
```sql
SELECT COUNT(*) AS total_stars,
       AVG(phot_g_mean_mag) AS average_brightness
FROM gaia_source
```

#### Unique Values (`DISTINCT`)
If you want to know what unique values exist in a column (e.g., seeing which specific surveys contribute to a merged catalog), use `DISTINCT`.

- **Example:**
```sql
SELECT DISTINCT filter_name
FROM observations
```

Here is the third section of your guide.

### The `FROM` and `JOIN` Clauses

The `FROM` clause defines your data source. While it can be as simple as naming a single table, it is also where you combine (join) multiple tables to gather different types of data—like combining position data from one table with astrophysical parameters from another.

#### The Basic `FROM`

In most astronomical databases, tables are organized into **schemas** (folders). To refer to a table, you often need to use the `schema.table` format.

* **Example:** `gaiadr3.gaia_source`
* `gaiadr3` is the schema (the specific data release).
* `gaia_source` is the specific table within that release.
```sql
SELECT *
FROM gaiadr3.gaia_source
```

#### The `JOIN` Clause

A `JOIN` allows you to combine rows from two different tables based on a related column.

* **`INNER JOIN` (Default):** Returns rows *only* when there is a match in **both** tables. If a star exists in Table A but not Table B, it is discarded.
* **`LEFT OUTER JOIN`:** Returns **all** rows from the left table (the first one mentioned), and adds matching data from the right table where available. If there is no match, the right side's columns will be empty (`NULL`).

#### Defining the Link (`ON` vs `USING`)

You must tell the database *how* to link the tables. Usually, you link them by a unique ID (like `source_id`).

* **`ON` (The flexible way):** Explicitly state which columns equal each other.
```sql
FROM table1 AS t1
JOIN table2 AS t2
ON t1.source_id = t2.source_id
```

* **`USING` (The shortcut):** If the column name is exactly the same in both tables, you can use this shorthand.
```sql
FROM table1
JOIN table2
USING (source_id)
```

#### Example: Joining Data

Imagine you want the position (RA, Dec) from the main Gaia source table, but you also want the temperature (`teff_gspphot`) which lives in a separate astrophysical parameters table.

```sql
SELECT src.source_id, src.ra, src.dec, astro.teff_gspphot
FROM gaiadr3.gaia_source AS src
JOIN gaiadr3.astrophysical_parameters AS astro
USING (source_id)
```

{: .note }
Standard `JOIN`s work perfectly when datasets share a common ID (like linking two tables within Gaia DR3). However, if you want to link two *different* surveys (e.g., Gaia vs. 2MASS) that don't share IDs, you cannot use a standard `JOIN`. You must perform a **Spatial Cross-Match** (matching by RA/Dec coordinates), which is usually handled in the `WHERE` clause using geometric functions.

Here is the fourth section of your guide. This is arguably the most important section for astronomers, as it covers both standard filtering and the special spatial functions that define ADQL.

### The `WHERE` Clause & Geometric Functions

The `WHERE` clause filters your data. Without it, you would download the entire sky. In ADQL, this section handles two jobs: **Standard Filtering** (values) and **Geometric Filtering** (positions).

#### Standard Filtering

These operators work exactly like standard SQL.

* **Comparison:** `=`, `<` (less than), `>` (greater than), `<=` (less/equal), `>=` (greater/equal), `<>` or `!=` (not equal).
* **Ranges (`BETWEEN`):** Selects values within a range (inclusive).
```sql
WHERE ra BETWEEN 45.0 AND 46.0
```

* **Lists (`IN`):** Checks if a value matches any item in a list.
```sql
WHERE source_id IN (12345, 67890, 11223)
```

* **Pattern Matching (`LIKE`):** Used for text. The `%` symbol is a wildcard.
```sql
WHERE object_name LIKE 'NGC%'  -- Starts with 'NGC'
```

* **Missing Data (`IS NULL`):** In astronomy, "0" is real data, but empty is unknown. Never use `= NULL`. Always use `IS NULL` or `IS NOT NULL`.
```sql
WHERE parallax IS NOT NULL
```

#### Logical Operators

You can combine multiple filters using `AND`, `OR`, and `NOT`.

* **Order of Operations:** `AND` is processed before `OR`. Use parentheses `()` to group logic explicitly.
```sql
WHERE (ra > 10 AND ra < 20) OR (dec > 0)
```

#### Geometric Functions (The "A" in ADQL)

This is what makes ADQL special. Instead of writing complex math to calculate distances on a sphere, you use built-in functions to find objects in specific regions of the sky.

**The "Cone Search" (Finding everything in a circle)**
The most common task is finding all objects within a certain radius of a central point. To do this, we use the `CONTAINS` predicate. **This will be super useful for Lab 0!**

* **Syntax:** `CONTAINS( geometry1, geometry2 ) = 1`
* This function asks: "Is geometry1 inside geometry2?"
* It returns `1` for True and `0` for False.

**Required Components:**
1. **`POINT('ICRS', ra, dec)`**: Defines a specific location.
* The first argument is the coordinate system. `'ICRS'` (International Celestial Reference System) is the standard modern default.

2. **`CIRCLE('ICRS', center_ra, center_dec, radius)`**: Defines the search area.
* **Radius must be in degrees.**

**Putting it together (Example):**
Find all stars within 0.1 degrees of the coordinates (RA=180, Dec=10).

```sql
SELECT *
FROM gaiadr3.gaia_source
WHERE 1 = CONTAINS(
          POINT('ICRS', ra, dec),
          CIRCLE('ICRS', 180.0, 10.0, 0.1)
      )
```

#### Other Geometric Shapes

* **`BOX('ICRS', center_ra, center_dec, width, height)`**: Useful for rectangular visual fields (like CCD footprints).
* **`POLYGON('ICRS', point1_ra, point1_dec, point2_ra, point2_dec, ...)`**: Used for complex, irregular survey footprints. You list the vertices in order.
 
Here is the fifth section of your guide. This section deals with organizing your output and generating statistics on groups of data.

### Sorting and Grouping

Once you have filtered your data with `WHERE`, you often need to organize the results (ranking stars by brightness) or summarize them (counting how many stars exist in different categories).

#### Sorting Results (`ORDER BY`)

By default, databases return rows in no guaranteed order. If you need a ranked list (e.g., the 10 closest stars), you must use `ORDER BY`.

* **Syntax:** `ORDER BY column_name [ASC | DESC]`
* **`ASC` (Ascending):** Smallest to largest (Default).
* **`DESC` (Descending):** Largest to smallest.

* **Multiple Sorts:** You can sort by primary and secondary columns.
* Example: `ORDER BY ra ASC, dec DESC` (Sorts by RA first; if RAs are equal, sorts those by Dec).


**Example: The 5 closest stars**
This query finds the stars with the largest parallax (closest distance) that are not errors.

```sql
SELECT TOP 5 source_id, parallax, phot_g_mean_mag
FROM gaiadr3.gaia_source
WHERE parallax IS NOT NULL
ORDER BY parallax DESC
```

#### Grouping Data (`GROUP BY`)

The `GROUP BY` clause is used when you want to collapse many rows into summary statistics based on shared values. It acts like a "pivot table" in Excel.

**The Golden Rule of Grouping:**
If you use `GROUP BY`, every column in your `SELECT` statement must be either:

1. Included in the `GROUP BY` clause.
2. Wrapped in an aggregate function (like `COUNT`, `AVG`, `SUM`).
*If you select a raw column that isn't grouped, the database won't know which row's value to display.*

**Example: Creating a Histogram**
A common use case is counting how many objects fall into specific bins. Here, we group stars by their integer magnitude (magnitude 10.1, 10.5, and 10.9 all become "10").

```sql
SELECT FLOOR(phot_g_mean_mag) AS mag_bin,
       COUNT(*) AS star_count
FROM gaiadr3.gaia_source
WHERE phot_g_mean_mag < 15
GROUP BY FLOOR(phot_g_mean_mag)
ORDER BY mag_bin
```

* **Result:** This returns a clean table showing how many stars are in magnitude bin 10, bin 11, bin 12, etc.

#### Filtering Groups (`HAVING`)

Sometimes you want to filter the *results* of a group, not the raw data. You cannot use `WHERE` for this because `WHERE` runs *before* the grouping happens. You must use `HAVING`.

* **`WHERE`:** Filters rows (e.g., "Only look at red stars").
* **`HAVING`:** Filters groups (e.g., "Only show me magnitude bins that have more than 100 stars").

**Example:**
```sql
SELECT FLOOR(phot_g_mean_mag) AS mag_bin,
       COUNT(*) AS star_count
FROM gaiadr3.gaia_source
GROUP BY FLOOR(phot_g_mean_mag)
HAVING COUNT(*) > 100
```

### Documentation & Useful Resources:

* **Gaia Archive ADQL Syntax:** [Gaia Archive Help - ADQL](https://www.google.com/search?q=https://gea.esac.esa.int/archive-help/adql/index.html) (The specific implementation used by ESA)
* **IVOA Standard:** [IVOA ADQL 2.0 Recommendation](https://www.ivoa.net/documents/ADQL/) (The technical standard definition)
* **GAVO ADQL Tutorial:** [GAVO ADQL Course](https://www.google.com/search?q=http://docs.g-vo.org/adql-course/html/) (Excellent step-by-step guide from the German Astrophysical Virtual Observatory)


## Accessing Astronomical Archives with `astroquery`

`astroquery` is an Astropy-affiliated package that provides a unified toolset for accessing online astronomical data services (e.g., SIMBAD, VizieR, **Gaia**, **SDSS**). It abstracts away complex HTTP requests and SQL handling, allowing you to query these services using Python commands.

### Caching Strategies (Vital for Gaia)

While many `astroquery` modules (like Vizier and SDSS) cache automatically, **`astroquery.gaia` does not cache async jobs by default.** Every time you run `launch_job_async`, it submits a new request to the ESA servers and re-downloads the data.

To avoid hitting quota limits or waiting for redundant downloads, you must use an external caching tool. **`joblib`** is the standard solution for this.

#### Persistent Caching with `joblib`

`joblib` caches the *output of a function* based on its input arguments. If you run your script again with the same query string, `joblib` intercepts the call and loads the data from your local disk immediately.

```python
from joblib import Memory
from astroquery.gaia import Gaia

# 1. Set up a local cache directory
memory = Memory(location='./cachedir', verbose=0)

# 2. Define a wrapper function decorated with @memory.cache
@memory.cache
def get_gaia_data(query_str):
    """
    Runs an async Gaia query. 
    If this query_str has been seen before, returns the cached Table immediately.
    """
    # Reset limit to ensure we get what we ask for
    Gaia.ROW_LIMIT = -1
    job = Gaia.launch_job_async(query_str)
    return job.get_results()

# 3. Use the function
# First run: Submits job to ESA -> Waits -> Downloads (Slow)
# Second run: Detects same query string -> Loads from ./cachedir (Instant)
query = "SELECT TOP 100 source_id, ra, dec, parallax FROM gaiadr3.gaia_source"
results = get_gaia_data(query)
```

### Accessing Gaia Data

The `astroquery.gaia` module is optimized for the ESA Gaia archive, handling large datasets and complex ADQL requests.

#### Synchronous vs. Asynchronous Queries

* **Avoid Synchronous (`launch_job`):** This keeps the connection open. If the query takes >60 seconds, it times out.
* **Use Asynchronous (`launch_job_async`):** This submits the job, closes the connection, and polls for completion. This is robust for science queries and should be the function you use in your labs.

{: .important }
A frequent point of confusion is the safety cap. `Gaia.ROW_LIMIT` defaults to **50 rows**. If you query a cluster and get exactly 50 stars, you have likely hit this limit. Always set `Gaia.ROW_LIMIT = -1` (unlimited) or use `TOP` in your ADQL as shown in the `joblib` example above. In cases, where you do not know how many sources you will end up (like star clusters) with it is best to use the former solution.

### Advanced: Gaia DataLink (RR Lyrae Light Curves)

Main tables (`gaia_source`) contain single values. Complex time-series data, like light curves, are stored as separate files. **Gaia DataLink** provides the bridge, allowing us to match sources to their datalink files. The most useful function to do this is `Gaia.load_data()`.

**Workflow: Retrieving Epoch Photometry**
In this example, we retrieve the `EPOCH_PHOTOMETRY` (light curve) for a known RR Lyrae star.

```python
from astroquery.gaia import Gaia
from astropy import table
import matplotlib.pyplot as plt

# 1. Define the source ID (Example RR Lyrae Star)
source_id = 4659713442253931776 

# 2. Query DataLink for the file URLs
data_release='Gaia DR3'
retrieval_type='EPOCH_PHOTOMETRY' # We ask for EPOCH_PHOTOMETRY to get the time series data
data_structure='INDIVIDUAL'
linking_parameter='SOURCE_ID'
file_format='fits'
datalink = Gaia.load_data(ids=[source_id],
                          data_release=data_release, 
                          retrieval_type=retrieval_type, 
                          data_structure=data_structure,
                          linking_parameter=linking_parameter,
                          format=file_format)

# Here we check the names of the datalink files we have accessed.
print(f'The following Datalink products have been downloaded:')
for dl_key in datalink.keys():
    print(f' * {dl_key}')

# 3. Extract and combine the timeseries data for the desired source.
source_filename = f'{retrieval_type}-{data_release} {source_id}.{file_format}'
data = table.vstack(datalink[source_filename])

# 4. Plotting the raw time series
plt.figure(figsize=(10,4))

time = data['g_transit_time']
g_band_mag = data['g_transit_mag']
plt.scatter(time, g_band_mag, s=10, color='green')
plt.gca().invert_yaxis() # Magnitudes are inverted!
plt.xlabel(f'Time [{time.unit}]')
plt.ylabel(f'G [{g_band_mag.unit}]')
plt.title(f"RR Lyrae Light Curve (Source {source_id})")
plt.show()
```

### Astropy Tables vs. Pandas DataFrames

`astroquery` returns data as an `astropy.table.Table`. While similar to a Pandas DataFrame, it is optimized for physics.

| Feature | Astropy Table (`astropy.table.Table`) | Pandas DataFrame (`pandas.DataFrame`) |
| --- | --- | --- |
| **Units** | **Native Support.** Columns can be `Quantity` objects (e.g., `5 * u.deg`), allowing for automatic unit conversions. | **No Native Support.** Values are raw numbers. You must track units manually. |
| **Coordinates** | **Native Support.** Can store `SkyCoord` objects directly in a single column. | **No Native Support.** Coordinates are usually split into separate `ra` and `dec` float columns. |
| **Missing Values** | Uses **Masked Arrays** (keeps the original value type but flags it as invalid). These can sometimes not play nice with numpy and matplotlib. | Uses **Sentinels** (like `NaN`), which often forces integer columns to become floats. |
| **Metadata** | **Rich Metadata.** Preserves detailed headers, descriptions, and UCDs from FITS/VOTable files. | **Limited.** Metadata is often lost or difficult to attach to specific columns. |

**Conversion:**
If you need to use Pandas-specific tools or just prefer them over Astropy tables, you can easily convert an Astropy table:

```python
# Convert Astropy Table to Pandas DataFrame
df = results.to_pandas()
```

{: .warning }
Units are stripped, Masked values become 'NaN's, and SkyCoords are often broken into component columns ('ra', 'dec').

### Other Data Sources

The same API patterns apply to other archives you may need for cross-matching:

* **SDSS (Sloan Digital Sky Survey):** `from astroquery.sdss import SDSS` - Useful for retriving data hosted by SDSS such as the APOGEE survey.
* **IPAC:** `from astroquery.ipac.irsa import Irsa` - For infrared data like WISE.

### Resources

* **Official Documentation:** [Astroquery ReadTheDocs](https://astroquery.readthedocs.io/en/latest/)
* **Gaia ADQL Cookbook:** [ESA Gaia Archive Writing Queries](https://www.cosmos.esa.int/web/gaia-users/archive/writing-queries)
* **Joblib Memory:** [Joblib Caching Documentation](https://joblib.readthedocs.io/en/latest/memory.html)