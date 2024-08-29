// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Counter
unsigned int count = 0;

unsigned int hash_value;



// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Hash to find index
    hash_value = hash(word);
    // Pointer for the cursor
    node *cursor = table[hash_value];
    //Iterate thru the index given
    while (cursor != 0)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long total = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        total += tolower(word[i]);
    }
    return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open File
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }
    char buffer[LENGTH + 1];
    // Loop and use fscanf
    while (fscanf(file, "%s", buffer) != -1)
    {
        // Allocate memory for new node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        // Store to node
        strcpy(n->word, buffer);
        // Hash the first letter to find where to store the node
        hash_value = hash(n->word);
        n->next = table[hash_value];
        table[hash_value] = n;
        count++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (count > 0)
    {
        return count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != 0)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
        if (cursor == NULL)
        {
            return true;
        }
    }
    return false;
}
