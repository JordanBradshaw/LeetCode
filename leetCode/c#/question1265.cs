/*
1265. Print Immutable Linked List in Reverse

You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

    ImmutableListNode: An interface of immutable linked list, you are given the head of the list.

You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):

    ImmutableListNode.printValue(): Print value of the current node.
    ImmutableListNode.getNext(): Return the next node.

The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.


Runtime: 232 ms, faster than 83.75% of C# online submissions for Print Immutable Linked List in Reverse.
Memory Usage: 30.8 MB, less than 53.75% of C# online submissions for Print Immutable Linked List in Reverse.
*/


public class Solution
{
    public void PrintLinkedListInReverse(ImmutableListNode head)
    {
        Stack<ImmutableListNode> st = new Stack<ImmutableListNode>();
        while (head.GetNext() != null)
        {
            st.Push(head);
            head = head.GetNext();
        }
        st.Push(head);
        while (st.Count() != 0)
        {
            st.Pop().PrintValue();
        }
    }
}
