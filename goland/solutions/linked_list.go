package main

import (
	"errors"
	"fmt"
)

type Node struct {
	Val int
	Next *Node
}

type LinkedList struct {
	head *Node
	tail *Node
	size int
}

func (linked *LinkedList) addNode(value int) {
	/*
		Case 1. linked list is empty
		Case 2. linked list has one or more nodes
	 */
	if linked.head == nil {
		linked.head = &Node{value, nil}
		linked.tail = linked.head
		linked.size++
	} else {
		linked.tail.Next = &Node{value, nil}
		linked.tail = linked.tail.Next
		linked.size++
	}
}

func (linked *LinkedList) removeFromFront() (int, error) {
	if linked.size == 0 {
		return 0, errors.New("List is empty")
	} else if linked.size == 1 {
		var value = linked.head.Val
		linked.head = nil
		linked.tail = nil
		linked.size = 0
		return value, nil
	}

	var value = linked.head.Val
	linked.head = linked.head.Next
	linked.size--
	return value, nil
}

func (linked *LinkedList) printList() error {
	if linked.size == 0 {
		fmt.Println("List is empty")
		return errors.New("List is empty")
	}

	fmt.Printf("Size: %v \n", linked.size)
	var temp = linked.head
	for temp != nil {
		fmt.Printf("[%v] -> ", temp.Val)
		temp = temp.Next
	}
	fmt.Println("nil")
	return nil
}

//func main(){
//	var linked = &LinkedList{}
//	linked.addNode(1)
//	linked.addNode(2)
//	linked.addNode(3)
//	value, err := linked.removeFromFront()
//	if err != nil {
//		log.Fatal(err)
//	}
//	fmt.Println("Removed:", value)
//	if err = linked.printList(); err != nil {
//		log.Fatal(err)
//	}
//}