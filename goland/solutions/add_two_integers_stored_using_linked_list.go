package main

import (
	"fmt"
	"log"
)

/**
* Definition for singly-linked list.
* type ListNode struct {
*     Val int
*     Next *ListNode
* }
*/

type ListNode struct {
	Val int
	Next *ListNode
}

func addTwoNumbersHelp(multiply_by int, left_from int, l1 *ListNode, l2 *ListNode) int {
	var sum_of int

	if l1 == nil && l2 == nil {
		return 0
	} else if l1 == nil {
		return multiply_by * (left_from + l2.Val) + addTwoNumbersHelp(multiply_by * 10, 0, l1, l2.Next)
	} else if l2 == nil {
		return multiply_by * (left_from + l1.Val) + addTwoNumbersHelp(multiply_by * 10, 0, l1.Next, l2)
	}

	sum_of = l1.Val + l2.Val + left_from
	if sum_of > 10 {
		return multiply_by * (sum_of - 10) + addTwoNumbersHelp(multiply_by * 10, 1, l1.Next, l2.Next)
	}
	return multiply_by * sum_of + addTwoNumbersHelp(multiply_by * 10, 0, l1.Next, l2.Next)
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var node ListNode
	node.Val = addTwoNumbersHelp(1, 0, l1, l2)
	return &node
}

func test_add_two_integers_stored_using_linked_list(){
	var node1 *ListNode = &ListNode{
		0,
		&ListNode{
			1,
			&ListNode{
				2,
				&ListNode{},
			},
		},
	}
	var node2 *ListNode = &ListNode {
		0,
		&ListNode{},
	}

	fmt.Println(addTwoNumbers(node1, node2))

	var r *ListNode = addTwoNumbers(node1, node2)

	if r.Val != 210 {
		log.Fatal("r.Val != 210")
	} else if r.Next != nil {
		log.Fatal("r.Next != nil")
	}
	log.Println("Test Passed")
}

func main(){
	test_add_two_integers_stored_using_linked_list()
}
