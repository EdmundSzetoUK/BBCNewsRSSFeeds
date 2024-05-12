
# BBCNewsRSSFeeds
BBC News RSS feeds data analysis

##  1. Understanding the business problem
Here are a few business problems or challenges that might be relevant:
1. Content Categorization and Management
  - The data includes multiple levels of categorization, from general topics to specific categories. A primary business problem could be the development of a system to automatically categorize content to enhance searchability, manage content more efficiently, and improve user navigation on news platforms.
2. Trend Analysis and Reporting
  - With data on publication dates and times, along with detailed topics and keywords, there's an opportunity to analyze trends over time. Businesses could use this to understand shifts in news focus (like sudden spikes in articles about "Covid" or "Ukraine"), which can guide editorial decisions and resource allocation.
3. Audience Engagement
-  Understanding which topics or categories draw more attention could help in tailoring content to increase reader engagement. Analyzing the length of descriptions or the focus of articles could indicate what captures readers' interests, helping to strategize content creation.

## 2. Data understanding and collection
### Data source
[BBC News Self updating dataset - BBC News RSS Feeds](https://www.kaggle.com/datasets/gpreda/bbc-news)

### Context
Self updating dataset. It collects RSS Feeds from BBC News using a Kernel: https://www.kaggle.com/gpreda/bbc-news-rss-feeds. 
The Kernel is run with a fixed frequency and the dataset is updated using the output of the Notebook.
Content
 - BBC News RSS Feeds. The data contains the following columns:
    - title
    - pubDate
    - guid
    - link
    - description

## 3. Data Preparation

The Power Query code you provided is designed to import, transform, and refine data from a CSV file. Here's a step-by-step breakdown:

1. **Source Import**:
  - `Source`: Reads a CSV file from the specified path. It specifies the delimiter as a comma, sets the number of columns to 5, sets the encoding to UTF-8 (65001), and handles quotes in the data as literal text without special treatment.

2. **Header Promotion**:
  - `#"Promoted Headers"`: Transforms the first row of the data into column headers, treating all scalar values uniformly.

3. **Data Type Assignment**:
  - `#"Changed Type"`: Converts the data types of the columns: `title`, `pubDate`, `guid`, `link`, and `description` are set to text, datetime, text, text, and text, respectively.

4. **Column Duplication and Text Extraction**:
 - `#"Duplicated Column"`: Creates a duplicate of the `title` column.
 - `#"Extracted Text Before Delimiter"`: Extracts text from the duplicated `title` column before the colon (`:`) delimiter.
 - `#"Duplicated Column1"`: Duplicates the `title` column again for further extraction.
 - `#"Extracted Text After Delimiter"`: Extracts text from the newly duplicated column after the colon delimiter.

5. **Column Renaming and Cleanup**:
 - `#"Renamed Columns"`: Renames the extracted columns to more descriptive names, like "title Header" and "Subtitle".
 - `#"Removed Duplicates"`: Removes duplicate rows based on the `link` column to ensure each link is unique.

6. **Further Column Operations**:
 - `#"Duplicated Column2"`: Duplicates the `guid` column.
 - `#"Split Column by Delimiter"`: Splits the duplicated `guid` column into multiple parts based on the "/" delimiter.
 - `#"Changed Type1"`: Assigns data types to the newly created columns from the split operation.
 - `#"Removed Columns"`: Removes unnecessary columns created from the split.
 - `#"Renamed Columns1"`: Renames columns to more descriptive names.

7. **Text Trimming and Formatting**:
  - Various steps (`#"Trimmed Text"`, `#"Capitalized Each Word"`, `#"Trimmed Text1"` through `#"Capitalized Each Word5"`) involve duplicating columns, trimming whitespace, and capitalizing each word to standardize text data for consistency and readability.

8. **Final Column Removals and Splits**:
 - `#"Removed Columns1"`: Removes a duplicate column not needed for analysis.
 - `#"Split Column by Delimiter2"` and further: These steps involve splitting columns by different delimiters and changing their types, which is useful for segmenting information that is compounded into a single column.

9. **Final Renaming and Type Changing**:
 - `#"Changed Type4"`: Changes the type of date and time after splitting the `pubDate`.
 - `#"Renamed Columns2"`: Renames all processed columns to standardized, descriptive names.

10. **Capture Keywords**:
  - Capture the keyword form title column 
  - Exmple 'Ukraine': ` =IF(SUM(--(ISNUMBER(SEARCH({"Ukraine"},$A2 & " " & $F2)))) >= 1, "Ukraine", "")`

After processing raw data, it contains news articles, primarily focusing on several topics including Ukraine, Football, and COVID-19. Here's a summary of the data and its structure:

### Data Overview
- **Total Entries**: 29,845 rows.
- **Columns**: 19 columns including:
  - **Title**: The title of the news article.
  - **pub Date** and **pub Time**: Publication date and time.
  - **Description**: A brief description of the article.
  - **Description Length**: Length of the description.
  - **Title Keyword of Ukraine, Football, Covid, Transport**: Specific keywords extracted from the title.
  - **Title header**: Header derived from the title.
  - **Subtitle**: Subtitle of the news article.
  - **Topics**: General topic classification.
  - **Categories (1-6)**: Up to six categories for classifying the article in more detail.
  - **ID**: An identification number for each article.

### Key Points:
- The data includes focused keyword extractions indicating the presence of words like "Ukraine," "Football," and "Covid" in article titles.
- The articles are categorized under multiple categories which suggest a hierarchical classification system from general to specific.
- Publication timestamps suggest tracking of news output in real-time.

## 4. Data visualization
### Excel Dashboards 

![BBC News Excel Dashboard](image/BBC%20News%20Excel%20Dashboard.png)

### Power BI Dashboards

![BBC News Power BI 01](image/BBC%20News%20Power%20BI%2001.png)

![BBC News Power BI 02](image/BBC%20News%20Power%20BI%2002.png)

### Python Figures

![BBC News World - Title Header](image/BBC%20News%20World%20-%20Title%20Header.png)

BBC News - Title Header Figure

![BBC News Description Figure](image/BBC%20News%20Description%20Figure.png)

BBC News Description Figure

## 5. Data analysis

The dashboard images provided show various data visualizations related to BBC News topics and trends. 
The key information from each section:

### 1. Trends of All News
- **Timeline Trends**:
  - There are fluctuations in news topic counts over time with noticeable peaks and troughs, such as a sharp decline in January 2023 and peaks around July 2023 and January 2024.
  
- **Quarterly Trends**:
  - **Q4 2022 to Q1 2023**: A significant decrease in news coverage, with a notable drop from December to January.
  - **Q3 to Q4 2023**: A period of increase in topics.
  - **Q1 to Q2 2024**: There's a general downward trend across multiple categories.

### 2. Overview of BBC News Topics
- **Total Number of BBC News Topics**: 25.92K topics are categorized, with the majority under "news" (25.92K) and "sport" (6.64K).
- **News Topic Categories**:
  - **UK**: The most significant share of news topics falls under UK news, making up 38% of the coverage.
  - **World**: Following the UK, world news constitutes 33%.
  - Other categories like entertainment, business, and technology have smaller shares.
  
- **Trending Topics**:
  - The most frequently covered topic is the "Ukraine war", followed by general news updates such as "The Papers", "Watch", and "Cost of living".
  
- **Treemap of News Topics**:
  - The treemap confirms the dominance of UK news within the "news" category, with "England" and specific cities like "London" and "Manchester" being highlighted.

### Summary of Analysis:
- There is a clear focus on UK-centric news within BBC's coverage, with a substantial proportion of topics relating to domestic affairs.
- The news volume fluctuates seasonally with specific increases likely tied to significant world and local events.
- The trend data indicates variability in news topic coverage with periodic assessments likely showing correlation with ongoing events and news cycles at those times.
  
