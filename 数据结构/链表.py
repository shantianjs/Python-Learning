class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if not self._head:
            raise LinkListUnderflow('in pop')
        tem = self._head.elem
        self._head = self._head.next
        return tem

    def pop_last(self):
	    if not self._head:
		    raise LinkListUnderflow('in pop_last')
	    p = self._head
	    if not p.next:
		    tem = p.elem
		    self._head = None
		    return tem
	    while p.next.next:
			p = p.next
		tem = p.next.elem
	    p.next = None
	    return tem
