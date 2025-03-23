import marimo

__generated_with = "0.11.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Welcome to Data Analysis with Python! 🚀

        ## What is Data Analysis?
        Data analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information, draw conclusions, and support decision-making. It’s used in almost every industry, from finance and healthcare to marketing and sports.

        ## Why Learn Data Analysis?
        - **Make better decisions**: Use data to guide your choices.
        - **Solve problems**: Identify trends, patterns, and outliers.
        - **Tell stories**: Communicate insights through data visualizations.

        ## What Will You Learn?
        In this notebook, you’ll learn how to:

        - Use **Pandas** to work with data.
        - Clean and explore datasets.
        - Analyze and visualize data to uncover insights.

        Let’s get started!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Let's get familiar with our libaries""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Pandas": mo.md("**Pandas** is a data analyst's best friend! It’s used for working with tables and structured data, like spreadsheets or SQL tables. Analysts use it to clean, transform, and analyze data efficiently."),

            "Matplotlib": mo.md("**Matplotlib** is a go-to library for creating graphs and visualizations. Data analysts use it to turn raw data into insightful charts, helping them communicate findings effectively."),

            "NumPy": mo.md("**NumPy** is the backbone of numerical computing in Python. Data analysts use it for number crunching, performing complex math operations, and handling large datasets with ease.")
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        value=(
            """
            To install our libraries, we use `pip install {library_name}`
            The `as` keyword is used to create an alias for the library name, making it shorter and easier to type. For example, instead of typing `pandas` every time, we can use `pd` as a shorthand.
            """
        ),
        kind="info"
    )
    return


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.carousel([mo.md("## Meet Pandas: Your Data Analysis Tool 🐼"),
                mo.md("##Pandas has 3 core structures"), "##Series, Index and Dataframes",
                mo.md(   """
        ### What is Series?

        A Series is a one-dimensional array-like object that can hold any data type (e.g., integers, strings, floats).

        **Key Features:** 

        - It has an **index** (labels for each element).
        - Behaves like a combination of a **list** and a **dictionary**.

        **Example:**

        ```python
        data = [10, 20, 30]
        series = pd.Series(data, index=["a", "b", "c"]) 
        print(series)
        ```

        **Output:** 

        | Index | Value |
        |-------|-------|
        | a     | 10    |
        | b     | 20    |
        | c     | 30    |

        """),
        mo.md("""
        ### What is an Index?

        An Index is used to label rows or columns in a Series or DataFrame.

        **Key Features:**

        - Acts like an immutable **array** (cannot be changed after creation).
        - Can be numeric, string-based, or even datetime.

        **Example:**

        ```python
        index = pd.Index(["a", "b", "c"])
        print(index)
        ```

        **Output:**

        ```
        Index(['a', 'b', 'c'], dtype='object')
        ```
        """
        ),
        mo.md("""
        ### What is a DataFrame?

        A DataFrame is a two-dimensional table-like structure with rows and columns (like a spreadsheet or SQL table).

        **Key Features:**

        - Each column is a **Series**.
        - Can hold different data types in different columns.
        - Has both a **row index** and **column names**

        **Example:**

        ```python
        data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
        df = pd.DataFrame(data)
        print(df)
        ```

        **Output:**


        |   | Name  | Age |
        |---|-------|-----|
        | 0 | Alice | 25  |
        | 1 | Bob   | 30  |


        """)]
               )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Now since we have an understading of Pandas structures, let's get to cookin""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### Our Data as a Dictionary 📖

        Here’s our data stored as a Python dictionary:
        ```python
        population_dict = {'Muscat': 29393, 'Salalah': 2981, 'Sinaw': 38282, 'Sur': 298292, 'Sohar': 27271}
        ```

        Let’s convert this dictionary into a **Pandas Series** to make it easier to work with!
        """
    )
    return


@app.cell
def _(pd):
    population_dict = {'Muscat': 29393, 'Salalah': 2981, 'Sinaw': 38282, 'Sur': 298292,'Sohar': 27271}
    population = pd.Series(population_dict)
    return population, population_dict


@app.cell(hide_code=True)
def _(mo, population_dict):
    mo.ui.table(population_dict)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(value="Notice how we converted a dictionary into a Series? "
            "We used the `Pandas` library alias `pd` and called `Series` "
            "to specify how we wanted the data to be structured." ,kind= "info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Here's a challenge, i want to display the number of population in  Muscat only

        **Hint 1:** We notice that our `Series` data is stored in the variable **population**.

        **Hint 2:** Use the index of the `Series` to access the population of Muscat directly. For example, if the index is a city name, you can use `population["Muscat"]`.
        """
    )
    return


@app.cell
def _():
    ## Type here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        \"""
        ## Now, Let's Extract The Population of Salalah and Sur

        **Hint 1:** We start the same way as the previous challenge by using the `Series` data stored in the variable **population**.

        **Hint 2:** Use **label-based slicing** to extract data between two indices. For example, if the cities are ordered in the index, you can use `population["Salalah":"Sur"]`.  
        **Note:** Label-based slicing is **inclusive**, meaning it includes both the start and end indices.

        **Hint 3:** You can also use **positional slicing** (key numbers) to extract data. Remember, in programming, numbering starts from `0`. For example, if Salalah is at position `1` and Sur is at position `3`, you can use `population.iloc[1:4]` to get everything in between.  
        **Pro Tip:** For larger datasets or when working with DataFrames, use `.iloc` for **position-based indexing**. It’s faster and more efficient. For example:
        ```python
        population.iloc[1:4]  # Selects rows 1 to 3 (exclusive of 4)
        ```
        **Note:** Positional slicing is **exclusive**, meaning it includes the start index but excludes the end index.

        **Hint 4:** Ensure the indices (city names) are spelled correctly and match the ones in your `Series`.
        \"""
        """
    )
    return


@app.cell
def _():
    ### Type here
    return


@app.cell(hide_code=True)
def _(mo):
    test_test = mo.md(
        """
        Think Fast!, I am in a jam, and i need to show only 2 cities, Sinaw and  Sur how to do so?
        """
    )

    mo.callout(value=test_test,kind= "neutral")
    return (test_test,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Understanding Key Numbers in a Series

        Let’s take a look at our `population` Series with **key numbers** (positions) added for clarity:

        | Key Number | City    | Population |
        |------------|---------|------------|
        | 0          | Muscat  | 29393      |
        | 1          | Salalah | 2981       |
        | 2          | Sinaw   | 38282      |
        | 3          | Sur     | 298292     |
        | 4          | Sohar   | 27271      |

        **Key Points:**

        - Key numbers start from `0` (e.g., Muscat is at position `0`, Salalah is at position `1`, etc.).
        - You can use these key numbers for **positional slicing** (e.g., `population.iloc[1:4]`).
        - **Important Note:** Positional slicing is **exclusive**, meaning it includes the start index but excludes the end index. If you want to include the last value, you’ll need to add `+1` to the length of the Series.

        Let’s practice extracting data using both **label-based slicing** and **positional slicing**!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    sliced_set = ["1:2","2:4","3:4","0:3"]
    data_drop = mo.ui.dropdown(label="Represent only Two Cities, Sinaw and Sur using Key slicing", options=sliced_set)

    # Feedback
    def get_feedback(sliced_set):
        if sliced_set == "2:4":
            return mo.md("🎉 **Correct!** `[2:4]` is the right way to slice the data")
        else:
            return mo.md("❌ **Sorry!, please try again**")

    # Function to convert string slice to Python slice
    def string_to_slice(slice_str):
        if slice_str is None:
            return None
        start, stop = map(int, slice_str.split(":"))
        return slice(start, stop)
    return data_drop, get_feedback, sliced_set, string_to_slice


@app.cell(hide_code=True)
def _(data_drop, get_feedback, mo, population, string_to_slice):
    # Display the dropdown and feedback reactively

    mo.md(
        f"""

        {data_drop}

        **Sliced Data:**

            ```
            {population[string_to_slice(data_drop.value)] if data_drop.value else "No slice selected."}
            ```

        {get_feedback(data_drop.value)}
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    pandas_structure_test = mo.md(
        """
        Pop quiz! let's see if you know the differences between Series, Index and DataFrame
        """
    )

    mo.callout(value=pandas_structure_test,kind= "warn")
    return (pandas_structure_test,)


@app.cell(hide_code=True)
def _(mo, pd):
    dukan_stocks = {
        "products": ["chips_oman", "sun_top", "chips_sohar", "kinder_bueno","haribo_gummies"],
        "units_available": [1_540_241, 150_000, 240_901, 442_050, 107_403]
    }
    dukan_data = pd.DataFrame(dukan_stocks)

    # Display the DataFrame
    mo.md(
        f"""
        ### Dataset Preview:
        {mo.ui.table(dukan_data)}
        """
    )
    return dukan_data, dukan_stocks


@app.cell(hide_code=True)
def _(mo):
    # Challenge 1: Series vs DataFrame
    mo.md(
        """
        ### Challenge 1: Series vs DataFrame
        - **What is the difference between a Series and a DataFrame?**
        - Use `dukan_data["products"]` to create a Series and `dukan_data[["products"]]` to create a DataFrame. What do you notice?

        **Hint:** Delete the `None` value and type in your answer 
        """
    )
    return


@app.cell
def _(check_series):
    ## Type here
    dukan_data_series = None

    check_series(dukan_data_series)
    return (dukan_data_series,)


@app.cell
def _(check_dataframe):
    ## Type here
    dukan_data_dataframe = None

    check_dataframe(dukan_data_dataframe)
    return (dukan_data_dataframe,)


@app.cell(hide_code=True)
def _(mo, pd):
    def check_series(data):
        if data is None:
            return mo.md("👋 **Please type in your answer.**")
        elif isinstance(data, pd.Series):
            return mo.md("🎉 **Correct!** The data is a valid and non-empty Pandas Series.")
        else:
            return mo.md("❌ **Sorry! The input is not a Pandas Series.**")



    def check_dataframe(data):
        if data is None:
            return mo.md("👋 **Please type in your answer.**")
        elif isinstance(data, pd.DataFrame):
            return mo.md("🎉 **Correct!** The data is a valid and non-empty Pandas DataFrame.")
        else:
            return mo.md("❌ **Sorry! The input is not a Pandas DataFrame.**")
    return check_dataframe, check_series


@app.cell(hide_code=True)
def _(mo):
    # Challenge 2: Index
    mo.md(
        """
        ### Challenge 2: Index
        - **What is an Index in Pandas?**
        - Use `df.index` to see the Index of the DataFrame. What does it represent?
        - Try resetting the Index using `df.reset_index()`. How does the DataFrame change?
        """
    )
    return


@app.cell
def _():
    ## Type here
    return


@app.cell(hide_code=True)
def _():
    import kagglehub
    import os

    # Download latest version
    path = kagglehub.dataset_download("samithsachidanandan/most-popular-1000-youtube-videos")
    csv_file = os.path.join(path, "Most popular 1000 Youtube videos.csv")
    return csv_file, kagglehub, os, path


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## The Viral Detective: Uncover the Secrets of YouTube's Top 1000 Videos!

        **Description:**

        You’re a data detective tasked with analyzing the Top 1000 Most Popular YouTube Videos dataset. Your mission is to explore the data, uncover trends, and answer key questions:

        - What makes a video go viral?

        - Which categories have the most views, likes, or comments?

        - Are there any hidden patterns or outliers?

        Use your data analysis skills to clean, explore, and visualize the dataset. Can you crack the code behind YouTube’s most popular videos?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Step 1: Load our Data

        Pandas provides a powerful function called `read_{file_extension}` to load datasets into a DataFrame. The function you use depends on the file format of your dataset. For example:

        CSV Files: Use `pd.read_csv()`.

        Excel Files: `Use pd.read_excel()`.

        JSON Files: `Use pd.read_json()`.

        Since our dataset is in CSV format, we’ll use `pd.read_csv()`.

        **Hint:** `csv_file` is the path where our data is stored
        """
    )
    return


@app.cell
def _(check_data_loaded):
    # Load the dataset
    data_youtube = None

    check_data_loaded(data_youtube)
    return (data_youtube,)


@app.cell(hide_code=True)
def _(mo, pd):
    def check_data_loaded(data):
        if data is None:
            return mo.md("👋 **Please type in your answer.**")
        elif isinstance(data, pd.DataFrame):
            return mo.md("🎉 **Correct!** The data is a valid and non-empty Pandas Series.")
        else:
            return mo.md("❌ **Sorry! The input is not a Pandas Series.**")
    return (check_data_loaded,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        f"""
        ## Step 2: Explore the Dataset

        Now that we've loaded the dataset, let's explore it to understand its structure and contents. Here are some useful functions to get started:

        ### 1. **Get the Number of Rows**
        Use `len(data_youtube)` to find out how many rows are in the dataset:
        """)
    return


@app.cell
def _(check_length):
    # Type here
    data_youtube_check = None

    check_length(data_youtube_check)
    return (data_youtube_check,)


@app.cell(hide_code=True)
def _(data_youtube, mo):
    def check_length(data_length):
        try: 
            # Calculate the expected length of the dataset
            expected_length = len(data_youtube)
            if data_length is None:
                return mo.md("👋 **Please type in your answer.**")
            elif isinstance(data_length, int):  # Check if the input is an integer
                if data_length == expected_length:
                    return mo.md(f"🎉 **Correct!** The length of the dataset is {expected_length}.")
                else:
                    return mo.md(f"❌ **Incorrect!** The length of the dataset is {expected_length}, but you provided {data_length}.")
            else:
                return mo.md("❌ **Sorry! Try again. Hint: Use `len()` on the dataset.")
        except AttributeError as e:
            return mo.md(f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return mo.md(f"**An unexpected error occurred:** {e}")
    return (check_length,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### 2. **View Column Names**
        Use `data_youtube.columns` to see the names of all columns:
        ```python
        data_youtube.columns
        ```
        """
    )
    return


@app.cell
def _(check_columns):
    # Type here
    data_youtube_column = None

    check_columns(data_youtube_column)
    return (data_youtube_column,)


@app.cell(hide_code=True)
def _(data_youtube, mo, pd):
    def check_columns(user_describe):
        try :
            expected_columns = data_youtube.columns
            if user_describe is None:
                return mo.md("👋 **Please type in your answer.**")
            elif isinstance(user_describe, pd.Index):  # Check if the input is a pandas Index
                if user_describe.equals(expected_columns):  # Check if the columns match
                    return mo.md(f"🎉 **Correct!** The columns of the dataset are {list(expected_columns)}.")
                else:
                    return mo.md(f"❌ **Incorrect!** The columns of the dataset are {list(expected_columns)}, but you provided {list(user_describe)}.")
            else:
                return mo.md("❌ **Sorry! Try again. Hint: Use `data_youtube.columns` to get the columns.")
        except AttributeError as e:
            return mo.md(f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return mo.md(f"**An unexpected error occurred:** {e}")
    return (check_columns,)


@app.cell(hide_code=True)
def _(data_youtube, mo, pd):
    def check_data_describe(user_describe):
        try:
            # Ensure data_youtube is a valid DataFrame
            if data_youtube is None:
                raise ValueError("The dataset is not loaded. `data_youtube` is None.")

            # Calculate the expected result of data_youtube.describe()
            expected_describe = data_youtube.describe()

            if user_describe is None:
                return mo.md("👋 **Please type in your answer.**")
            elif isinstance(user_describe, pd.DataFrame):  # Check if the input is a pandas DataFrame
                if user_describe.equals(expected_describe):  # Check if the DataFrame matches the expected result
                    return mo.md("🎉 **Correct!** That's how you describe the dataset.")
                else:
                    return mo.md("❌ **Incorrect!** The result does not match the expected output.")
            else:
                return mo.md("❌ **Sorry! Try again. Hint: Use `data_youtube.describe()` to describe the dataset.")
        
        except AttributeError as e:
            return mo.md(f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return mo.md(f"**An unexpected error occurred:** {e}")
    return (check_data_describe,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### 3. **Summary Statistics**
        Use `data_youtube.describe()` to get summary statistics for numeric columns (e.g., mean, min, max):
        ```python
        data_youtube.describe()
        ```
        """
    )
    return


@app.cell
def _(check_data_describe):
    check_stats = None
    check_data_describe(check_stats)
    return (check_stats,)


@app.cell(hide_code=True)
def _(dataset_preview, mo):
    mo.md(
        f"""
        ### 4. **Preview the Dataset**
        - **`data_youtube`**: Displays the entire dataset. This is useful for small datasets but can be overwhelming for larger ones.

        **Output:**
        {dataset_preview}
        """
    )
    return


@app.cell(hide_code=True)
def _(data_youtube, mo):
    def display_dataset_preview(data):
        try:
            # Ensure data is a valid DataFrame
            if data is None:
                raise ValueError("The dataset is not loaded. `data_youtube` is None.")
            
            # Return the dataset as a table
            return mo.ui.table(data)
            
        
        except AttributeError as e:
            return (f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return (f"**An unexpected error occurred:** {e}")
    dataset_preview = display_dataset_preview(data_youtube)
    return dataset_preview, display_dataset_preview


@app.cell
def _(check_data_describe):
    # Type here
    check_data = None
    check_data_describe(check_data)
    return (check_data,)


@app.cell(hide_code=True)
def _(data_youtube, mo):
    def display_dataset_head(data):
        try:
            # Ensure data is a valid DataFrame
            if data is None:
                raise ValueError("The dataset is not loaded. `data_youtube` is None.")
            
            # Return the dataset as a table
            return mo.ui.table(data)
            
        
        except AttributeError as e:
            return (f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return (f"**An unexpected error occurred:** {e}")
    dataset_head = display_dataset_head(data_youtube)
    return dataset_head, display_dataset_head


@app.cell(hide_code=True)
def _(data_youtube, mo, pd):
    def check_data_head(user_describe):
        try:
            # Ensure data_youtube is a valid DataFrame
            if data_youtube is None:
                raise ValueError("The dataset is not loaded. `data_youtube` is None.")

            expected_describe = data_youtube.head()

            if user_describe is None:
                return mo.md("👋 **Please type in your answer.**")
            elif isinstance(user_describe, pd.DataFrame):  # Check if the input is a pandas DataFrame
                if user_describe.equals(expected_describe):  # Check if the DataFrame matches the expected result
                    return mo.md("🎉 **Correct!** That's how you check top dataset.")
                else:
                    return mo.md("❌ **Incorrect!** The result does not match the expected output.")
            else:
                return mo.md("❌ **Sorry! Try again. Hint: Use `data_youtube.head()` to view the top of the dataset")
        
        except AttributeError as e:
            return mo.md(f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return mo.md(f"**An unexpected error occurred:** {e}")
    return (check_data_head,)


@app.cell(hide_code=True)
def _(dataset_head, mo):
    mo.md(
        f"""
        - **`data_youtube.head()`**: Displays the first 5 rows. Great for a quick overview:
              ```python
              data_youtube.head()
              ```
              **Output:**
              {dataset_head}
        """
    )
    return


@app.cell
def _(check_data_head):
    check_head = None

    check_data_head(check_head)
    return (check_head,)


@app.cell(hide_code=True)
def _(data_youtube, mo):
    def display_dataset_tail(data):
        try:
            # Ensure data is a valid DataFrame
            if data is None:
                raise ValueError("The dataset is not loaded. `data_youtube` is None.")
            
            # Return the dataset as a table
            return mo.ui.table(data)
            
        
        except AttributeError as e:
            return (f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return (f"**An unexpected error occurred:** {e}")
    dataset_tail = display_dataset_tail(data_youtube)
    return dataset_tail, display_dataset_tail


@app.cell(hide_code=True)
def _(data_youtube, mo, pd):
    def check_data_tail(user_describe):
        try:
            # Ensure data_youtube is a valid DataFrame
            if data_youtube is None:
                raise ValueError("The dataset is not loaded. `data_youtube` is None.")

            expected_describe = data_youtube.tail()

            if user_describe is None:
                return mo.md("👋 **Please type in your answer.**")
            elif isinstance(user_describe, pd.DataFrame):  # Check if the input is a pandas DataFrame
                if user_describe.equals(expected_describe):  # Check if the DataFrame matches the expected result
                    return mo.md("🎉 **Correct!** That's how you check the bottom dataset.")
                else:
                    return mo.md("❌ **Incorrect!** The result does not match the expected output.")
            else:
                return mo.md("❌ **Sorry! Try again. Hint: Use `data_youtube.tail()` to view the bottom of the dataset")
        
        except AttributeError as e:
            return mo.md(f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return mo.md(f"**An unexpected error occurred:** {e}")
    return (check_data_tail,)


@app.cell(hide_code=True)
def _(dataset_tail, mo):
    mo.md(
        f"""
        - **`data_youtube.tail()`**: Displays the last 5 rows. Useful for checking the end of the dataset:
              ```python 
              data_youtube.tail()
              ```
              **Output:**
              {dataset_tail}
        """
    )
    return


@app.cell
def _(check_data_tail):
    check_tail = None
    check_data_tail(check_tail)
    return (check_tail,)


@app.cell(hide_code=True)
def _(data_youtube, mo):
    def display_dataset_sample(data):
        try:
            # Ensure data is a valid DataFrame
            if data is None:
                raise ValueError("The dataset is not loaded. `data_youtube` is None.")
            
            # Return the dataset as a table
            return mo.ui.table(data)
        
        except AttributeError as e:
            return (f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return (f"**An unexpected error occurred:** {e}")
    dataset_sample = display_dataset_sample(data_youtube)
    return dataset_sample, display_dataset_sample


@app.cell(hide_code=True)
def _(dataset_sample, mo):
    mo.md(
        f"""
        - **`data_youtube.sample()`**: Displays a random row. Helps you get a sense of the data distribution:
          ```python
          data_youtube.sample()
          ```
          **Output:**
          {dataset_sample}
        Use these functions to familiarize yourself with the dataset before diving into analysis!
        """)
    return


@app.cell
def _(display_dataset_sample):

    check_sample = None
    display_dataset_sample(check_sample)
    return (check_sample,)


@app.cell(hide_code=True)
def _(mo):
    text = mo.md(
        """
         Functions like `.head()`, `.tail()`, and `.sample()` have a default value of displaying 5 rows, but you can customize the number of rows to your liking.

            **Example:**
            ```python
            data_youtube.head(15)
            ```
            try it out!
        """
    )

    mo.callout(value=text,kind= "info")
    return (text,)


@app.cell
def _():
    # Type here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Before We Start: Check for Null Values
        Before diving into analysis, it's important to check for **null values** in the dataset. Null values represent missing or incomplete data, which can affect the accuracy of your analysis.

        ### How to Check for Null Values
        Pandas provides the `.isnull()` function, which returns a DataFrame of `True` (for null values) and `False` (for non-null values).

        Try it out on `data_youtube`, just like our previous example with `population["Muscat"]` we do the same but add `.isnull()`
        """
    )
    return


@app.cell
def _(check_data_null):
    # Type here
    data_null = None

    check_data_null(data_null)
    return (data_null,)


@app.cell(hide_code=True)
def _(data_youtube, mo, pd):
    def check_data_null(data):
        try:
            # Ensure data_youtube is a valid DataFrame
            if data_youtube is None:
                raise ValueError("The dataset is not loaded. `data_youtube` is None.")

            # Calculate the expected result of data_youtube.isnull()
            expected_isnull = data_youtube.isnull()

            if data is None:
                return mo.md("👋 **Please type in your answer.**")
            elif isinstance(data, pd.DataFrame):  # Check if the input is a pandas DataFrame
                if data.equals(expected_isnull):  # Check if the DataFrame matches the expected result
                    return mo.md("🎉 **Correct!** That's how you check for missing values.")
                else:
                    return mo.md("❌ **Incorrect!** The result does not match the expected output.")
            else:
                return mo.md("❌ **Sorry! Try again. Hint: Use `data_youtube.isnull()` to check for missing values.")

        except AttributeError as e:
            return mo.md(f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return mo.md(f"**An unexpected error occurred:** {e}")
    return (check_data_null,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now let's try it on the whole dataset.  

        To count the number of null values in each column, you can chain it with `.sum()`.

        **Hint:** Since we want to see the null values in every column, we

        **Fun Fact 🤔** the `.sum()` function simmilar to the **Excel** function
        """
    )
    return


@app.cell
def _(check_data_null_sum):
    # Type here
    data_na_sum = None

    check_data_null_sum(data_na_sum)
    return (data_na_sum,)


@app.cell(hide_code=True)
def _(mo, pd):
    def check_data_null_sum(data):
        if data is None:
            return mo.md("👋 **Please type in your answer.**")
        elif isinstance(data, pd.Series):  # Check if the input is a pandas Series
            return mo.md("🎉 **Correct!** That's how you check for null values.")
        else:
            return mo.md("❌ **Sorry! Try again. Hint: Add `.sum()` at the end.**")
    return (check_data_null_sum,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Let's ask questions about based on the dataset
        What are the most common catergory of videos types in the dataset?

        `value_counts()` will tell you how many times each unique value appears in the list

        **Hint: the get count in a category add the column name between the brackets like this `pd.[column_name"].value_counts()`
        """
    )
    return


@app.cell
def _(check_value_counts):
    ## Type here
    data_category = None

    check_value_counts(data_category)
    return (data_category,)


@app.cell(hide_code=True)
def _(data_youtube, mo, pd):
    def check_value_counts(data):
        try:
            expected_count = data_youtube['Category'].value_counts()
            if data is None:
                return mo.md("👋 **Please type in your answer.**")
            elif isinstance(data, pd.Series):  # Check if the input is a pandas Series
                if data.equals(expected_count):  # Check if the Series matches the expected result
                    return mo.md("🎉 **Correct!** That's how you check value counts for a column.")
                else:
                    return mo.md("❌ **Incorrect!** The result does not match the expected output.")
            else:
                return mo.md("❌ **Sorry! Try again. Hint: Use `data_youtube['Category'].value_counts()` to check value counts.")
        except AttributeError as e:
            return mo.md(f"**Error:** The dataset is not loaded please load the dataset")
        except Exception as e:
            return mo.md(f"**An unexpected error occurred:** {e}")
    return (check_value_counts,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Let's find the videos with the most `Views` and `Likes` ?

        `idxmax()` identifies the largest value in a single column
        """
    )
    return


@app.cell
def _():
    ## Type here
    data_max_view = None
    return (data_max_view,)


@app.cell(hide_code=True)
def _(check_max_view, mo, user_input):
    # Display the dataset and feedback

    mo.md(
        f"""
        ### Find the Video with the Maximum Views

        **Feedback:**
        {check_max_view(user_input.value)}

            **Your Input:**
        {user_input}
        """
    )
    return


@app.cell
def _():
    #Type here
    return


@app.cell(hide_code=True)
def _(data_youtube, mo):
    def check_max_view(user_input):
        if user_input == 0:
            return mo.md("👋 **Please type in your answer.**")
        elif user_input == data_youtube["Video views"].idxmax():
            return mo.md("🎉 **Correct!** You identified the video with the maximum views.")
        else:
            return mo.md("❌ **Sorry! That's not the correct number.**")

    # Interactive input for the user
    user_input = mo.ui.number(
        label="Enter the index of the video with the maximum views:",
        start=0,
        stop=10000000000000
    )
    return check_max_view, user_input


@app.cell(hide_code=True)
def _(check_max_likes, mo, user_input_like):
    # Display the dataset and feedback

    mo.md(
        f"""
        ### Find the Video with the Maximum Likes

        **Feedback:**
        {check_max_likes(user_input_like.value)}

        **Your Input:**
        {user_input_like}
        """


    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(data_youtube, mo):
    def check_max_likes(user_input):

        if user_input == 0:
            return mo.md("👋 **Please type in your answer.**")
        elif user_input == data_youtube["Likes"].idxmax():
            return mo.md("🎉 **Correct!** You identified the video with the maximum views.")
        else:
            return mo.md("❌ **Sorry! That's not the correct number.**")

    # Interactive input for the user
    user_input_like = mo.ui.number(
        label="Enter the index of the video with the maximum views:",
        start=0,
        stop= 100000000000000)
    return check_max_likes, user_input_like


@app.cell
def _():
    #Type here
    return


@app.cell(hide_code=True)
def _(mo):
    test_oldest_video = mo.md(
        """
        Think Fast!, I need to figure out the oldest video published in this dataset, help!
        """
    )

    mo.callout(value=test_oldest_video,kind= "neutral")
    return (test_oldest_video,)


@app.cell(hide_code=True)
def _(check_oldest_publised, mo, user_input_publised):
    # Display the dataset and feedback

    mo.md(
        f"""
        ### Find the oldest uploaded vidoe in this dataset

        **Feedback:**
        {check_oldest_publised(user_input_publised.value)}

            **Your Input:**
        {user_input_publised}
        """
    )
    return


@app.cell
def _():
    ## Type here
    data_oldest_publised = None
    return (data_oldest_publised,)


@app.cell(hide_code=True)
def _(data_youtube, mo):
    def check_oldest_publised(user_input):
        if user_input == 0:
            return mo.md("👋 **Please type in your answer.**")
        elif user_input == data_youtube["published"].min():
            return mo.md("🎉 **Correct!** You identified the oldest video.")
        else:
            return mo.md("❌ **Sorry! That's not the correct year.**")

    # Interactive input for the user
    user_input_publised = mo.ui.number(
        label="Enter the oldest video uploaded on this dataset:",
        start=0,
        stop= 5000
    )
    return check_oldest_publised, user_input_publised


if __name__ == "__main__":
    app.run()
