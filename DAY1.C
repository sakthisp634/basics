
// Linked list operations in C

#include <stdio.h>
#include <stdlib.h>

// Create a node
struct Node {
  int data;
  struct Node* next;
};

// Insert at the beginning
void insertAtBeginning(struct Node** head_ref, int new_data) {
  // Allocate memory to a node
  struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));

  // insert the data
  new_node->data = new_data;

  new_node->next = (*head_ref);

  // Move head to new node
  (*head_ref) = new_node;
}

// Insert a node after a node
void insertAfter(struct Node* prev_node, int new_data) {
 struct Node*new_node=(struct Node*)malloc(sizeof(struct Node));
  if (prev_node == NULL) {
  printf("the given previous node cannot be NULL");
  return;
  }

 // struct Node* new_node = (struct Node*)malloc(siz
  new_node->data = new_data;
  new_node->next = prev_node->next;
  prev_node->next = new_node;
}

// Insert the the end
void insertAtEnd(struct Node** head_ref, int new_data) {
  struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
  struct Node* last = *head_ref; /* used in step 5*/

  new_node->data = new_data;
  new_node->next = NULL;

  if (*head_ref == NULL) {
  *head_ref = new_node;
  return;
  }

  while (last->next != NULL) last = last->next;

  last->next = new_node;
  return;
}

// Delete a node
void deleteNode(struct Node** head_ref, int key) {
  struct Node *temp = *head_ref, *prev;

  if (temp != NULL && temp->data == key) {
  *head_ref = temp->next;
  free(temp);
  return;
  }
  // Find the key to be deleted
  while (temp != NULL && temp->data != key) {
  prev = temp;
  temp = temp->next;
  }

  // If the key is not present
  if (temp == NULL) return;

  // Remove the node
  prev->next = temp->next;

  free(temp);
}

// Search a node
int searchNode(struct Node** head_ref, int key) {
  struct Node* current = *head_ref;

  while (current != NULL) {
  if (current->data == key) return 1;
  current = current->next;
  }
  return 0;
}

// Sort the linked list
void sortLinkedList(struct Node** head_ref) {
  struct Node *current = *head_ref, *index = NULL;
  int temp;

  if (head_ref == NULL) {
  return;
  } else {
  while (current != NULL) {
    // index points to the node next to current
    index = current->next;

    while (index != NULL) {
    if (current->data > index->data) {
      temp = current->data;
      current->data = index->data;
      index->data = temp;
    }
    index = index->next;
    }
    current = current->next;
  }
  }
}

// Print the linked list
void printlist(struct Node* node) {
  while (node != NULL) {
  printf(" %d ", node->data);
  node = node->next;
  }
}
void swap(struct Node**first,struct Node**second)
{
struct Node*tmp=*first;
*first=*second;
*second=tmp;
}

void swapnodes(struct Node**headr,int key1,int key2)
{
struct Node**first=headr;
struct Node**second=headr;
if(key1==key2)
return;
//struct Node**first=headr;
while(*first&&(*first)->data!=key1)first=&(*first)->next;
if(*first==NULL)
return;
//struct Node **second=headr;
while(*second&&(*second)->data!=key2)second=&(*second)->next;
if(*second==NULL)
return;
swap(first,second);
swap(&(*first)->next,&(*second)->next);
}

int main() {
  struct Node* head = NULL;
  int item_to_find=3;
  clrscr();
  insertAtEnd(&head, 5);
  insertAtBeginning(&head, 6);
  insertAtBeginning(&head, 7);
  insertAtEnd(&head, 4);
  insertAfter(head->next, 1);

  printf("Linked list: ");
  printlist(head);

  printf("\nAfter deleting an element: ");
  deleteNode(&head, 3);
  printlist(head);

//  int item_to_find = 3;
  if (searchNode(&head, item_to_find)) {
  printf("\n%d is found", item_to_find);
  } else {
  printf("\n%d is not found", item_to_find);
  }

  sortLinkedList(&head);
  printf("\nSorted List: ");
  printlist(head);
  printf("\n Linked List before swapping");
  printlist(head);
  swapnodes(&head,5,7);
  printf("\nLinked list after swaping");
  printlist(head);
  getch();
  return 0;
}
