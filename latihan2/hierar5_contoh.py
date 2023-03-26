class AkunBank:
    def _init_(self, nomor_akun, saldo):
        self.nomor_akun = nomor_akun
        self.saldo = saldo
    def get_nomor_akun(self):
        return self.nomor_akun
    def get_saldo(self):
        return self.saldo
class AkunTabungan(AkunBank):
    def _init_(self, nomor_akun, saldo, persentase_bunga):
        super()._init_(nomor_akun, saldo)
        self.persentase_bunga = persentase_bunga
    def get_persentase_bunga(self):
        return self.persentase_bunga
class CekAkun(AkunBank):
    def _init_(self, nomor_akun, saldo, overdraft_limit):
        super()._init_(nomor_akun, saldo)
        self.overdraft_limit = overdraft_limit
    def get_overdraft_limit(self):
        return self.overdraft_limit
# Hierarchical Inheritance
class JointAccount(AkunTabungan):
    def _init_(self, nomor_akun, saldo, persentase_bunga, owners):
        super()._init_(nomor_akun, saldo, persentase_bunga)
        self.owners = owners
    def get_owners(self):
        return self.owners