library(rvest)

# Read URLs from a text file (replace 'Scrapes.txt' with your file path)
urls <- readLines("D:/R_Code/Scrapes.txt", warn = FALSE)

# Specify the folder where you want to save the files (modify as needed)
output_folder <- "D:/R_Code"

# Create the output folder if it doesn't exist
if (!dir.exists(output_folder)) {
  dir.create(output_folder)
}

# Initialize an empty list to store scraped data
scraped_data_list <- list()

# Loop through the URLs and scrape data
for (url in urls) {
  # Skip empty lines (including incomplete final line)
  if (nchar(url) > 0) {
    # Read the HTML content of the current URL
    webpage <- read_html(url)
    
    # Use CSS selectors to scrape data (modify as needed)
    scraped_data <- html_text(html_nodes(webpage, 'p'))
    
    # Store the scraped data in the list with the URL as the identifier
    scraped_data_list[[url]] <- scraped_data
    
    # Define the file path, including the output folder
    file_name <- file.path(output_folder, paste0("scraped_data_", gsub("[^A-Za-z0-9]", "_", url), ".txt"))
    
    # Write the scraped data to the text file
    writeLines(scraped_data, con = file_name)
  }
}

# Display or process the scraped data as needed
