
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["last_name"] = self.last_name
        if "id" not in member:
            member["id"] = self._generateId()
        member["lucky_numbers"] = list(member.get("lucky_numbers", set()))
        self._members.append(member)
        return member
    pass

    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                
                return None
        pass

    def get_member(self, id):
        for member in self._members:
            if member["id"] == int(id):
                return member
            
        return None
    pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
