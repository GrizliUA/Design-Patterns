class QualityAssurance:
    def __init__(self, id: int, first_name: str, last_name: str, address: str, phone_number: str, email: str, salary: float, rank: str, position: int):
        if isinstance (id,int) : self.id = id
        if isinstance (first_name,str) : self.first_name = first_name
        if isinstance (last_name,str) : self.last_name = last_name
        if isinstance (address,str) : self.address = address
        if isinstance (phone_number,str) : self.phone_number = phone_number
        if isinstance (email,str) : self.email = email
        if isinstance (salary,float) : self.salary = salary
        if isinstance (rank,str) : self.rank = rank 
        if isinstance (position,int) : self.position = position

