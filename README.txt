This code looks at genetic information of different chromosomes. It tries to find specific patterns in the DNA that might indicate where the DNA starts to copy itself. It then prints out the positions where these patterns are found on each chromosome.


1. Set up the email address for Entrez (required for accessing NCBI databases).
2. Define a regular expression pattern that represents the ORI motif.
3. Specify a list of chromosome IDs to search for the ORI pattern.
4. Iterate over each chromosome ID:
   - Fetch the DNA sequence for the chromosome from the NCBI database.
   - Search for the ORI pattern within the DNA sequence.
   - Print the chromosome ID and positions of potential ORI sites.