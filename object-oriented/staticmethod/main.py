# Static method yang digunakan tanpa perlu self atau cls yang tidak perlu memerlukan 
# access permission jadi langsung

class Employer:

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def printJob(self):
        print(f"Nama nya adalah {self.name} dan jabatan nya {self.job}")

    @staticmethod
    def is_validation_job(job_title):
        job = ["Manager", "Supervisor", "Cashier"]
        return job_title in job

employe = Employer.is_validation_job("Chef")
employe1 = Employer("Tio", "Manager")



print(employe)
print(Employer.is_validation_job(employe1.job))
